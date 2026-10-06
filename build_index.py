"""Generate the document vectors locally before deploying the app."""

import json
import os
from pathlib import Path

import numpy as np
from fastembed import TextEmbedding

from rag_index import BASE_DIR, EMBED_MODEL, chunks_fingerprint, load_chunks


def main():
    chunks = load_chunks()
    if not chunks:
        raise RuntimeError("No Markdown chunks found in data/")

    cache_dir = os.getenv("FASTEMBED_CACHE_PATH") or None
    embedder = TextEmbedding(EMBED_MODEL, cache_dir=cache_dir, threads=1)
    vectors = np.asarray(
        list(embedder.embed([chunk["text"] for chunk in chunks], batch_size=8)),
        dtype=np.float32,
    )
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    vectors /= np.maximum(norms, 1e-12)

    vector_path = BASE_DIR / "data" / "embeddings.npy"
    metadata_path = BASE_DIR / "data" / "embeddings.json"
    with vector_path.open("wb") as output:
        np.save(output, vectors)
    metadata = {
        "model": EMBED_MODEL,
        "chunks_sha256": chunks_fingerprint(chunks),
        "count": len(chunks),
        "dimensions": int(vectors.shape[1]),
    }
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(f"Saved {len(chunks)} vectors ({vectors.shape[1]} dimensions) to {vector_path}")


if __name__ == "__main__":
    main()
