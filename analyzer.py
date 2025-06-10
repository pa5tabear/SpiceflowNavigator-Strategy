"""Generate short strategic summaries from transcripts."""
# pragma: no cover

from __future__ import annotations

import re
from textwrap import shorten
from typing import Iterable, Dict, List

from insight_extractor import extract_insights
from semantic_search import search_insights

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

    # ------------------------------------------------------------------
    def analyze_with_insights(
        self,
        transcript: str,
        goals: Iterable[Goal],
        max_words: int = 40,
    ) -> dict[str, object]:
        """Return summary, goal scores, insights and semantic index."""

        result = self.analyze(transcript, max_words=max_words, goals=goals)
        assert isinstance(result, dict)
        insights = extract_insights(transcript)
        semantic_index = insights  # simple list used by search_insights
        return {
            "summary": result["summary"],
            "scores": result["scores"],
            "insights": insights,
            "semantic_index": semantic_index,
        }
