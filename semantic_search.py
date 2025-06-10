from __future__ import annotations

import re
from typing import List, Dict, Iterable, Tuple

from goal_model import Goal


def _tokenize(text: str) -> set[str]:
    return set(re.findall(r"\b\w+\b", text.lower()))


def _jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def search_insights(
    query: str, insights: List[Dict[str, str]], goals: Iterable[Goal] | None = None, top_k: int = 5
) -> List[Tuple[Dict[str, str], float]]:
    """Return insights ranked by relevance to query and goals."""
    q_tokens = _tokenize(query)
    results: List[Tuple[Dict[str, str], float]] = []
    for ins in insights:
        ins_tokens = _tokenize(ins["text"])
        score = _jaccard(q_tokens, ins_tokens)
        if goals:
            score += sum(g.score_content(ins["text"]) for g in goals)
        results.append((ins, score))
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:top_k]
