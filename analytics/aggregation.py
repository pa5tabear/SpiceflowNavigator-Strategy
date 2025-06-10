from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, Dict, List, Any

from insight_extractor import extract_insights
from goal_model import Goal


@dataclass
class AggregationResult:
    category_counts: Dict[str, int]
    goal_scores: Dict[str, float]
    trend: List[tuple[str, int]]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "category_counts": dict(self.category_counts),
            "goal_scores": dict(self.goal_scores),
            "trend": list(self.trend),
        }


def aggregate_transcripts(
    transcripts: List[Dict[str, Any]],
    goals: Iterable[Goal],
    start: datetime | None = None,
    end: datetime | None = None,
    category: str | None = None,
    relevance: float = 0.0,
) -> AggregationResult:
    """Aggregate insights from transcripts by category and goal relevance."""

    cat_counts: Counter[str] = Counter()
    goal_scores: defaultdict[str, float] = defaultdict(float)
    trend_counts: defaultdict[str, int] = defaultdict(int)

    for item in transcripts:
        text = item["text"]
        ts: datetime = item.get("timestamp") or datetime.utcnow()
        if start and ts < start:
            continue
        if end and ts > end:
            continue

        insights = extract_insights(text)
        for ins in insights:
            if category and ins["category"] != category:
                continue
            score = sum(g.score_content(ins["text"]) for g in goals)
            if score < relevance:
                continue
            cat_counts[ins["category"]] += 1
            period = ts.strftime("%Y-%m")
            trend_counts[period] += 1

        for g in goals:
            goal_scores[g.name] += g.score_content(text)

    trend = sorted(trend_counts.items())
    return AggregationResult(cat_counts, dict(goal_scores), trend)
