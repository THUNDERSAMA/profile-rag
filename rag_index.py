import hashlib
import json
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
EMBED_MODEL = "BAAI/bge-small-en-v1.5"


def load_chunks():
    chunks = []
    for file in sorted(DATA_DIR.glob("*.md")):
        for block in re.split(r"\n(?=## )", file.read_text(encoding="utf-8")):
            block = block.strip()
            if len(block) < 30:
                continue
            title = block.splitlines()[0].lstrip("# ").strip()
            chunks.append({"id": len(chunks), "source": file.stem, "title": title, "text": block})
    return chunks


def chunks_fingerprint(chunks):
    content = json.dumps(chunks, ensure_ascii=False, sort_keys=True).encode("utf-8")
    return hashlib.sha256(content).hexdigest()
