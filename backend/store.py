"""Thin wrapper around a persistent Chroma collection.

We always pass our own precomputed embeddings, so Chroma is used purely as a
metadata-aware vector index. Metadata schema per chunk:

    { day, day_label, topic, section, type, source_file, segment_code }
"""
from __future__ import annotations
from typing import List, Dict, Any, Optional
import chromadb

from . import config


class Store:
    def __init__(self):
        config.CHROMA_DIR.mkdir(parents=True, exist_ok=True)
        self.client = chromadb.PersistentClient(path=str(config.CHROMA_DIR))
        self.col = self.client.get_or_create_collection(
            name=config.COLLECTION, metadata={"hnsw:space": "cosine"}
        )

    def reset(self):
        try:
            self.client.delete_collection(config.COLLECTION)
        except Exception:
            pass
        self.col = self.client.get_or_create_collection(
            name=config.COLLECTION, metadata={"hnsw:space": "cosine"}
        )

    def add(self, ids, embeddings, documents, metadatas):
        self.col.add(ids=ids, embeddings=embeddings, documents=documents, metadatas=metadatas)

    def count(self) -> int:
        return self.col.count()

    def query(self, embedding: List[float], k: int, where: Optional[Dict[str, Any]] = None):
        res = self.col.query(
            query_embeddings=[embedding], n_results=k, where=where,
            include=["documents", "metadatas", "distances"],
        )
        out = []
        for doc, meta, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0]):
            out.append({"text": doc, "meta": meta, "score": 1 - dist})
        return out

    def inventory(self) -> List[Dict[str, Any]]:
        """Aggregate what's in the store by (day, topic, type) for the coach view."""
        got = self.col.get(include=["metadatas"])
        agg: Dict[tuple, Dict[str, Any]] = {}
        for m in got["metadatas"]:
            key = (m.get("day"), m.get("topic"), m.get("type"))
            row = agg.setdefault(key, {
                "day": m.get("day"), "day_label": m.get("day_label"),
                "topic": m.get("topic"), "type": m.get("type"), "chunks": 0,
            })
            row["chunks"] += 1
        rows = sorted(agg.values(), key=lambda r: (str(r["day"]), str(r["topic"]), str(r["type"])))
        return rows
