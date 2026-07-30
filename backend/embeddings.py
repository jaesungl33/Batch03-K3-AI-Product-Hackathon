"""Pluggable embedding layer.

We compute embeddings ourselves and hand dense vectors to Chroma, so Chroma
never needs to download its own model. Two backends:

  * "st"   -> sentence-transformers multilingual model (best quality for VI).
  * "tfidf" -> a character/word TF-IDF projection. No downloads, works offline,
              good enough to demo the retrieval logic anywhere.

The active backend is chosen in config.EMBED_BACKEND. A fitted TF-IDF vectorizer
is persisted next to the Chroma store so queries embed the same way as ingest.
"""
from __future__ import annotations
import pickle
from pathlib import Path
from typing import List
import numpy as np

from . import config


class BaseEmbedder:
    dim: int
    def embed(self, texts: List[str]) -> List[List[float]]:
        raise NotImplementedError


class STEmbedder(BaseEmbedder):
    """sentence-transformers backend (downloads the model on first use)."""
    def __init__(self):
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(config.ST_MODEL)
        self.dim = self.model.get_sentence_embedding_dimension()

    def embed(self, texts: List[str]) -> List[List[float]]:
        vecs = self.model.encode(texts, normalize_embeddings=True, show_progress_bar=False)
        return np.asarray(vecs, dtype="float32").tolist()


class TfidfEmbedder(BaseEmbedder):
    """Offline fallback. Fit once during ingest, reuse for queries."""
    STORE = config.CHROMA_DIR / "tfidf.pkl"

    def __init__(self):
        self.vectorizer = None
        self.svd = None
        self.dim = config.TFIDF_DIM
        if self.STORE.exists():
            self._load()

    def fit(self, corpus: List[str]):
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.decomposition import TruncatedSVD
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1, max_features=20000)
        X = self.vectorizer.fit_transform(corpus)
        n_comp = min(config.TFIDF_DIM, X.shape[1] - 1, max(2, X.shape[0] - 1))
        self.svd = TruncatedSVD(n_components=n_comp, random_state=42)
        self.svd.fit(X)
        self.dim = n_comp
        self._save()

    def _save(self):
        self.STORE.parent.mkdir(parents=True, exist_ok=True)
        with open(self.STORE, "wb") as f:
            pickle.dump({"vec": self.vectorizer, "svd": self.svd, "dim": self.dim}, f)

    def _load(self):
        with open(self.STORE, "rb") as f:
            d = pickle.load(f)
        self.vectorizer, self.svd, self.dim = d["vec"], d["svd"], d["dim"]

    def embed(self, texts: List[str]) -> List[List[float]]:
        if self.vectorizer is None:
            raise RuntimeError("TF-IDF embedder not fitted yet. Run ingest first.")
        X = self.vectorizer.transform(texts)
        Z = self.svd.transform(X)
        # L2 normalize so cosine == dot product
        norms = np.linalg.norm(Z, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        return (Z / norms).astype("float32").tolist()


def get_embedder() -> BaseEmbedder:
    if config.EMBED_BACKEND == "tfidf":
        return TfidfEmbedder()
    return STEmbedder()
