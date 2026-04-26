"""Semantic δ: cosine distance between bait passage and target vocab centroid.

Embeddings: intfloat/multilingual-e5-large. Following the model card,
inputs are prefixed with "passage: " before encoding.
"""
from typing import List

import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "intfloat/multilingual-e5-large"
_model: SentenceTransformer | None = None


def _get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model


def _encode(texts: List[str]) -> np.ndarray:
    prefixed = [f"passage: {t}" for t in texts]
    emb = _get_model().encode(prefixed, normalize_embeddings=True, show_progress_bar=False)
    return np.asarray(emb)


def compute_delta_batch(baits: List[str], targets: List[List[str]]) -> List[float]:
    bait_emb = _encode(baits)
    deltas: List[float] = []
    for i, vocab in enumerate(targets):
        v_emb = _encode(vocab)
        centroid = v_emb.mean(axis=0)
        centroid /= np.linalg.norm(centroid) + 1e-12
        sim = float(np.dot(bait_emb[i], centroid))
        deltas.append(1.0 - sim)
    return deltas
