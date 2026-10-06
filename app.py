import asyncio
import json
import os
import re
import threading
import time
from collections import defaultdict, deque

import numpy as np
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from huggingface_hub import AsyncInferenceClient
from pydantic import BaseModel, Field
from rank_bm25 import BM25Okapi
from rag_index import BASE_DIR, EMBED_MODEL, chunks_fingerprint, load_chunks

# ---------- config ----------
LLM_MODEL = os.getenv("LLM_MODEL", "meta-llama/Llama-3.1-8B-Instruct")
CACHE = os.getenv("FASTEMBED_CACHE_PATH") or None
ORIGINS = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "*").split(",")]
RATE_LIMIT = int(os.getenv("RATE_LIMIT_PER_MIN", "8"))
TOP_K = 5   # chunks sent to the LLM
POOL = 8    # candidates per retriever before fusion

app = FastAPI(title="Portfolio RAG API")
app.add_middleware(
    CORSMiddleware, allow_origins=ORIGINS, allow_methods=["*"], allow_headers=["*"]
)

llm = AsyncInferenceClient(model=LLM_MODEL, token=os.getenv("HF_TOKEN"))
_embedder = None
_embedder_lock = threading.Lock()


def get_embedder():
    global _embedder
    if _embedder is None:
        with _embedder_lock:
            if _embedder is None:
                from fastembed import TextEmbedding

                _embedder = TextEmbedding(EMBED_MODEL, cache_dir=CACHE, threads=1)
    return _embedder


STOP = {"what", "which", "who", "how", "has", "have", "had", "is", "are", "was",
        "were", "does", "did", "do", "the", "a", "an", "of", "on", "in", "to",
        "and", "or", "for", "with", "about", "his", "her", "he", "she", "tell",
        "me", "you", "your"}


def tokenize(t: str):
    toks = re.findall(r"\w+", t.lower())
    return [w[:-1] if len(w) > 3 and w.endswith("s") else w
            for w in toks if w not in STOP]


CHUNKS = load_chunks()
VECTOR_PATH = BASE_DIR / "data" / "embeddings.npy"
METADATA_PATH = BASE_DIR / "data" / "embeddings.json"
if not VECTOR_PATH.exists() or not METADATA_PATH.exists():
    raise RuntimeError(
        "Precomputed index missing. Run `python build_index.py` and deploy "
        "data/embeddings.npy and data/embeddings.json."
    )
INDEX_METADATA = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
if (
    INDEX_METADATA.get("model") != EMBED_MODEL
    or INDEX_METADATA.get("chunks_sha256") != chunks_fingerprint(CHUNKS)
):
    raise RuntimeError(
        "Precomputed index is stale or uses a different model. Run `python build_index.py` again."
    )
VECS = np.load(VECTOR_PATH, mmap_mode="r")
if (
    VECS.ndim != 2
    or VECS.shape[0] != len(CHUNKS)
    or VECS.shape[0] != INDEX_METADATA.get("count")
    or VECS.shape[1] != INDEX_METADATA.get("dimensions")
):
    raise RuntimeError("Precomputed index shape is invalid. Run `python build_index.py` again.")
BM25 = BM25Okapi([tokenize(c["title"] + " " + c["text"]) for c in CHUNKS])


def _warmup():
    # Load the ONNX model in the background so the API starts fast
    # but the first visitor doesn't wait ~10s for the model.
    try:
        list(get_embedder().query_embed("warmup"))
    except Exception:
        pass


threading.Thread(target=_warmup, daemon=True).start()


# ---------- retrieval ----------
def view(i, score):
    c = CHUNKS[i]
    return {"id": c["id"], "source": c["source"], "title": c["title"],
            "text": c["text"][:400], "score": round(float(score), 4)}


def embed_query(q: str):
    t = time.perf_counter()
    v = np.array(list(get_embedder().query_embed(q))[0], dtype="float32")
    v /= np.linalg.norm(v)
    return v, (time.perf_counter() - t) * 1000


def vector_search(v):
    t = time.perf_counter()
    sims = VECS @ v
    idx = np.argsort(-sims)[:POOL]
    return [view(i, sims[i]) for i in idx], (time.perf_counter() - t) * 1000


def keyword_search(q: str):
    t = time.perf_counter()
    scores = BM25.get_scores(tokenize(q))
    idx = [i for i in np.argsort(-scores)[:POOL] if scores[i] > 0]
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
    "Use ONLY the provided context and cite sources like [1]. "
    "Lead with a direct answer, then name specific projects, technologies and results. "
    "Never repeat a point, never define generic terms, and never present interests "
    "as projects. Do not speculate. If the context lacks the answer, say so briefly. "
    "Keep it under 120 words."
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
            yield evt("vector", {"hits": vec[:TOP_K], "ms": round(vms, 1)})
            yield evt("keyword", {"hits": kw[:TOP_K], "ms": round(kms, 1)})

            fused = rrf([vec, kw])
            yield evt("fusion", {"hits": fused, "method": "Reciprocal Rank Fusion (k=60)"})

            ctx = "\n\n".join(
                f"[{n+1}] ({h['title']})\n{CHUNKS[h['id']]['text']}" for n, h in enumerate(fused)
            )
            yield evt("llm_start", {"model": LLM_MODEL})
            stream = await llm.chat_completion(
                messages=[{"role": "system", "content": SYSTEM},
                          {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {q}"}],
                max_tokens=350, temperature=0.1, stream=True,
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

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "10000")))