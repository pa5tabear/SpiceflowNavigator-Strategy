"""Generate short strategic summaries from transcripts."""
# pragma: no cover

from __future__ import annotations

import re
from textwrap import shorten
from typing import Iterable, Dict, List

from goal_model import Goal


class StrategicAnalyzer:
    """Heuristic analyzer for podcast transcripts."""

    def __init__(self, keywords: list[str] | None = None) -> None:
        default = [
            "strategy",
            "revenue",
            "growth",
            "roadmap",
            "competition",
        ]
        self.keywords = [k.lower() for k in (keywords or default)]

    # ------------------------------------------------------------------
    def analyze(
        self,
        transcript: str,
        max_words: int = 40,
        goals: Iterable[Goal] | None = None,
    ) -> str | dict[str, object]:
        """Return a short summary focusing on strategic sentences.

        If ``goals`` provided, return a dictionary with the summary and
        relevance scores per goal.
        """

        sentences = re.split(r"(?<=[.!?])\s+", transcript.strip())
        picked: list[str] = []
        for sentence in sentences:
            text = sentence.lower()
            if any(k in text for k in self.keywords):
                picked.append(sentence.strip())
                if len(" ".join(picked).split()) >= max_words:
                    break
        if not picked:
            picked = sentences[:1]
        summary = " ".join(picked)
        summary = shorten(summary, width=max_words * 6, placeholder="...")

        if goals:
            scores: Dict[str, float] = {
                goal.name: goal.score_content(transcript) for goal in goals
            }
            return {"summary": summary, "scores": scores}

        return summary

    # ------------------------------------------------------------------
    def rank_transcripts(
        self, transcripts: List[str], goals: Iterable[Goal]
    ) -> List[tuple[int, float]]:
        """Return list of transcript indices ranked by total score."""
        ranking: List[tuple[int, float]] = []
        for idx, text in enumerate(transcripts):
            total = sum(goal.score_content(text) for goal in goals)
            ranking.append((idx, total))
        ranking.sort(key=lambda x: x[1], reverse=True)
        return ranking
