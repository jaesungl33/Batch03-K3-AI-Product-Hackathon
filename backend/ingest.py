"""Parse VLearn lecture transcripts into retrievable segment-chunks.

Each transcript file looks like:

    # Transcript ... — Day 1 — Foundation: cách LLM hoạt động
    > Nguồn: ...  (metadata block)
    ## <section header>
    **[T04-001]** paragraph text...
    **[T04-002]** ...

We produce one chunk per **[Txx-NNN]** segment, tagged with:
    day, day_label, topic, section, type, source_file, segment_code

`segment_code` (e.g. T04-001) is the citation handle the UI "pulls up" as the
detailed source — the same role a slide number plays in the flow.
"""
from __future__ import annotations
import re
from pathlib import Path
from typing import List, Dict, Any

from . import config
from .embeddings import get_embedder, TfidfEmbedder
from .store import Store

SEG_RE = re.compile(r"\*\*\[(T\d{2}-\d{3})\]\*\*\s*(.*)")
DAY_RE = re.compile(r"Day\s*(\d+)", re.IGNORECASE)
# Class-activity / inaudible markers we skip as low-value context
SKIP_MARKERS = ("[Hoạt động lớp", "[không nghe rõ]")


def _day_from_title(title: str) -> Dict[str, str]:
    m = DAY_RE.search(title)
    day = f"{int(m.group(1)):02d}" if m else "NA"
    # topic = the part after the last em dash in the title
    parts = [p.strip() for p in re.split(r"—|-{2,}", title) if p.strip()]
    topic = parts[-1] if parts else title.strip()
    label = f"Day {int(day)}" if day != "NA" else "Chưa gắn buổi"
    return {"day": day, "day_label": label, "topic": topic}


def parse_file(path: Path) -> List[Dict[str, Any]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    title = ""
    for ln in lines:
        if ln.startswith("# ") and "Transcript" in ln:
            title = ln.lstrip("# ").strip()
            break
    meta = _day_from_title(title)

    chunks: List[Dict[str, Any]] = []
    section = meta["topic"]
    for ln in lines:
        s = ln.strip()
        if s.startswith("## "):
            section = s[3:].strip()
            continue
        m = SEG_RE.match(s)
        if not m:
            continue
        code, text = m.group(1), m.group(2).strip()
        if not text or text.startswith(SKIP_MARKERS):
            continue
        chunks.append({
            "id": f"{path.stem}:{code}",
            "text": text,
            "meta": {
                "day": meta["day"],
                "day_label": meta["day_label"],
                "topic": meta["topic"],
                "section": section,
                "type": "theory",           # transcripts are lecture theory
                "source_file": path.name,
                "segment_code": code,
            },
        })
    return chunks


def load_all() -> List[Dict[str, Any]]:
    files = sorted(config.TRANSCRIPT_DIR.glob("*.md"))
    all_chunks: List[Dict[str, Any]] = []
    for f in files:
        all_chunks.extend(parse_file(f))
    return all_chunks


def run(reset: bool = True) -> Dict[str, Any]:
    chunks = load_all()
    if not chunks:
        raise SystemExit(f"No transcript chunks found in {config.TRANSCRIPT_DIR}")

    embedder = get_embedder()
    # TF-IDF must be fitted on the corpus before it can embed.
    if isinstance(embedder, TfidfEmbedder):
        embedder.fit([c["text"] for c in chunks])

    store = Store()
    if reset:
        store.reset()

    B = 128
    for i in range(0, len(chunks), B):
        batch = chunks[i:i + B]
        vecs = embedder.embed([c["text"] for c in batch])
        store.add(
            ids=[c["id"] for c in batch],
            embeddings=vecs,
            documents=[c["text"] for c in batch],
            metadatas=[c["meta"] for c in batch],
        )

    days = sorted({c["meta"]["day_label"] for c in chunks})
    return {"chunks": len(chunks), "days": days, "backend": config.EMBED_BACKEND,
            "count_in_store": store.count()}


if __name__ == "__main__":
    print(run())
