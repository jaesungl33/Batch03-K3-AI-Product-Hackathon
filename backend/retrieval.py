"""Two-tier retrieval — the core of the RAG flow.

Tier 1 (LOCATE):  embed the question, search the WHOLE collection unfiltered,
                  read the metadata of the top hits and vote on which (day, topic)
                  the knowledge lives in.

Tier 2 (CONTEXT): re-query filtered to that day (and topic), pulling a fuller set
                  of segments so the answer has complete context instead of one
                  stray chunk.

CROSS-LINK:       look for lab-type material in the same day/topic to suggest
                  hands-on practice.
"""
from __future__ import annotations
from collections import Counter
import re
import unicodedata
from typing import Dict, Any, List

from . import config
from .embeddings import get_embedder
from .store import Store

_embedder = None
_store = None

AMBIGUOUS_PATTERNS = (
    r"\b(nó|cái này|cái đó|điều đó)\s+(là gì|nghĩa là gì)\b",
    r"\b(buổi trước|hôm trước).*\b(cái đó|điều đó|nó)\b",
)
OUT_OF_SCOPE_PATTERNS = (
    r"\b(công thức|cách)\s+(nấu|làm)\s+(phở|bún|cơm|món ăn)\b",
    r"\b(giá|tỷ giá).*\b(bitcoin|btc|crypto|cổ phiếu)\b",
    r"\b(kubernetes|k8s).*\b(cluster|production|deploy)\b",
    r"\b(email|thư).*\b(xin nghỉ việc|gửi sếp)\b",
    r"\b(chấm|sửa).*\b(code|mã nguồn|python).*\b(nộp bài|điểm)\b",
    r"\b(bài tập|lab).*\b(ở đâu|nộp đâu|link nào|chiều nay|ngày mai)\b",
)


def _lazy():
    global _embedder, _store
    if _embedder is None:
        _embedder = get_embedder()
    if _store is None:
        _store = Store()
    return _embedder, _store


def _normalized(text: str) -> str:
    text = unicodedata.normalize("NFC", text).casefold()
    return " ".join(text.split())


def preflight_scope(question: str) -> Dict[str, Any] | None:
    """Reject clearly ambiguous, realtime, action, or non-course requests."""
    normalized = _normalized(question)
    if any(re.search(pattern, normalized) for pattern in AMBIGUOUS_PATTERNS):
        return {"found": False, "reason": "ambiguous"}
    if any(re.search(pattern, normalized) for pattern in OUT_OF_SCOPE_PATTERNS):
        return {"found": False, "reason": "out_of_scope"}
    return None


def locate(question: str) -> Dict[str, Any]:
    rejected = preflight_scope(question)
    if rejected:
        return rejected
    embedder, store = _lazy()
    qvec = embedder.embed([question])[0]
    hits = store.query(qvec, k=config.LOCATE_K)
    if not hits:
        return {"found": False}
    if hits[0]["score"] <= 0.05:
        return {"found": False, "reason": "no_lexical_or_semantic_overlap"}
    # weighted vote on day, then topic within that day
    day_votes = Counter()
    for h in hits:
        day_votes[h["meta"]["day"]] += max(h["score"], 0.01)
    best_day = day_votes.most_common(1)[0][0]

    topic_votes = Counter()
    label = ""
    for h in hits:
        if h["meta"]["day"] == best_day:
            topic_votes[h["meta"]["topic"]] += max(h["score"], 0.01)
            label = h["meta"]["day_label"]
    best_topic = topic_votes.most_common(1)[0][0]
    return {"found": True, "day": best_day, "day_label": label,
            "topic": best_topic, "qvec": qvec, "top_score": hits[0]["score"]}


def retrieve(question: str) -> Dict[str, Any]:
    embedder, store = _lazy()
    loc = locate(question)
    if not loc.get("found"):
        return {"found": False}

    qvec = loc["qvec"]
    # Tier 2: filtered to the located day for full context
    context = store.query(qvec, k=config.CONTEXT_K, where={"day": loc["day"]})

    # Cross-link: any lab material in the same day?
    lab = store.query(qvec, k=3, where={"$and": [{"day": loc["day"]}, {"type": "lab"}]})

    return {
        "found": True,
        "day": loc["day"],
        "day_label": loc["day_label"],
        "topic": loc["topic"],
        "context": context,
        "lab": lab,
        "sources": [
            {"segment_code": c["meta"]["segment_code"],
             "section": c["meta"]["section"],
             "source_file": c["meta"]["source_file"],
             "text": c["text"],
             "score": round(c["score"], 3)}
            for c in context
        ],
    }
