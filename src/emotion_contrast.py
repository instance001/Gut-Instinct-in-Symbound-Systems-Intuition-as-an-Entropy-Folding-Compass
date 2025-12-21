"""
Contrast semantic similarity vs emotional distinctiveness.
Stub: plug your own embedding models; this file only sketches the API.
"""

from typing import Sequence, Tuple


def semantic_overlap_score(a: str, b: str) -> float:
    """Placeholder semantic score."""
    return 0.0


def emotional_distinctiveness(a: str, b: str) -> float:
    """Placeholder emotional contrast score; higher = more distinct."""
    return 0.0


def choose_by_emotion(pairs: Sequence[Tuple[str, str]]) -> Tuple[str, str]:
    """
    Given candidate pairs, pick the one with highest emotional distinctiveness.
    """
    if not pairs:
        return "", ""
    scored = [(emotional_distinctiveness(x, y), (x, y)) for x, y in pairs]
    scored.sort(key=lambda t: t[0], reverse=True)
    return scored[0][1]
