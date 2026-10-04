import asyncio
import json
import os
import re
import time
from collections import defaultdict, deque
from pathlib import Path

import numpy as np
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastembed import TextEmbedding
from huggingface_hub import AsyncInferenceClient
from pydantic import BaseModel, Field
from rank_bm25 import BM25Okapi

# ---------- config ----------
LLM_MODEL = os.getenv("LLM_MODEL", "meta-llama/Llama-3.1-8B-Instruct")
EMBED_MODEL = "BAAI/bge-small-en-v1.5"
CACHE = os.getenv("FASTEMBED_CACHE_PATH") or None
ORIGINS = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "*").split(",")]
RATE_LIMIT = int(os.getenv("RATE_LIMIT_PER_MIN", "8"))
TOP_K = 5

app = FastAPI(title="Portfolio RAG API")
app.add_middleware(
    CORSMiddleware, allow_origins=ORIGINS, allow_methods=["*"], allow_headers=["*"]
)

llm = AsyncInferenceClient(model=LLM_MODEL, token=os.getenv("HF_TOKEN"))
embedder = TextEmbedding(EMBED_MODEL, cache_dir=CACHE)


# ---------- load + chunk knowledge base ----------
def load_chunks():
    chunks = []
    for f in sorted(Path("data").glob("*.md")):
        for block in re.split(r"\n(?=## )", f.read_text(encoding="utf-8")):
            block = block.strip()
            if len(block) < 30:
                continue
            title = block.splitlines()[0].lstrip("# ").strip()
            chunks.append({"id": len(chunks), "source": f.stem, "title": title, "text": block})
    return chunks


def tokenize(t: str):
    return re.findall(r"\w+", t.lower())


CHUNKS = load_chunks()
VECS = np.array(list(embedder.embed([c["text"] for c in CHUNKS])), dtype="float32")
VECS /= np.linalg.norm(VECS, axis=1, keepdims=True)
BM25 = BM25Okapi([tokenize(c["title"] + " " + c["text"]) for c in CHUNKS])


# ---------- retrieval ----------
def view(i, score):
    c = CHUNKS[i]
    return {"id": c["id"], "source": c["source"], "title": c["title"],
            "text": c["text"][:400], "score": round(float(score), 4)}


def embed_query(q: str):
    t = time.perf_counter()
    v = np.array(list(embedder.query_embed(q))[0], dtype="float32")
    v /= np.linalg.norm(v)
    return v, (time.perf_counter() - t) * 1000


def vector_search(v):
    t = time.perf_counter()
    sims = VECS @ v
    idx = np.argsort(-sims)[:TOP_K]
    return [view(i, sims[i]) for i in idx], (time.perf_counter() - t) * 1000


def keyword_search(q: str):
    t = time.perf_counter()
    scores = BM25.get_scores(tokenize(q))
    idx = [i for i in np.argsort(-scores)[:TOP_K] if scores[i] > 0]
    return [view(i, scores[i]) for i in idx], (time.perf_counter() - t) * 1000


def rrf(lists, k=60):
    fused = defaultdict(float)
    for hits in lists:
        for rank, h in enumerate(hits):
            fused[h["id"]] += 1 / (k + rank + 1)
    top = sorted(fused.items(), key=lambda x: -x[1])[:TOP_K]
    return [view(i, s) for i, s in top]


# ---------- rate limiting ----------
HITS: dict[str, deque] = defaultdict(deque)


def limited(ip: str) -> bool:
    now, q = time.time(), HITS[ip]
    while q and now - q[0] > 60:
        q.popleft()
    if len(q) >= RATE_LIMIT:
        return True
    q.append(now)
    return False


# ---------- API ----------
class Query(BaseModel):
    question: str = Field(min_length=2, max_length=300)


def evt(name: str, data: dict) -> str:
    return f"data: {json.dumps({'event': name, **data})}\n\n"


SYSTEM = (
    "You answer questions about the portfolio owner for hiring managers. "
    "Use ONLY the provided context. Cite sources like [1], [2]. "
    "If the context lacks the answer, say so. Be concise and concrete."
)


@app.get("/")
def health():
    return {"status": "ok", "chunks": len(CHUNKS), "llm": LLM_MODEL}


@app.post("/ask")
async def ask(body: Query, request: Request):
    ip = request.headers.get("x-forwarded-for", request.client.host).split(",")[0]

    async def run():
        if limited(ip):
            yield evt("error", {"message": "Rate limit hit. Try again in a minute."})
            return
        try:
            q = body.question.strip()
            yield evt("start", {"question": q, "chunks_indexed": len(CHUNKS)})

            v, ms = await asyncio.to_thread(embed_query, q)
            yield evt("embedding", {"model": EMBED_MODEL, "dims": len(v),
                                    "preview": [round(float(x), 3) for x in v[:8]], "ms": round(ms, 1)})

            (vec, vms), (kw, kms) = await asyncio.gather(
                asyncio.to_thread(vector_search, v),
                asyncio.to_thread(keyword_search, q),
            )
            yield evt("vector", {"hits": vec, "ms": round(vms, 1)})
            yield evt("keyword", {"hits": kw, "ms": round(kms, 1)})

            fused = rrf([vec, kw])
            yield evt("fusion", {"hits": fused, "method": "Reciprocal Rank Fusion (k=60)"})

            ctx = "\n\n".join(
                f"[{n+1}] ({h['title']})\n{CHUNKS[h['id']]['text']}" for n, h in enumerate(fused)
            )
            yield evt("llm_start", {"model": LLM_MODEL})
            stream = await llm.chat_completion(
                messages=[{"role": "system", "content": SYSTEM},
                          {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {q}"}],
                max_tokens=450, temperature=0.2, stream=True,
            )
            async for chunk in stream:
                tok = chunk.choices[0].delta.content if chunk.choices else None
                if tok:
                    yield evt("token", {"text": tok})
            yield evt("done", {})
        except Exception as e:
            yield evt("error", {"message": f"{type(e).__name__}: {e}"[:200]})

    return StreamingResponse(run(), media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "7860")))