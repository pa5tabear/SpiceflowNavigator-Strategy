from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
import re
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

@dataclass
class CorpusAggregation:
    """Aggregated insights across multiple transcripts."""

    insights_by_category: Dict[str, List[str]]
    category_counts: Dict[str, int]
    insight_frequency: Dict[str, int]
    topic_frequency: Dict[str, int]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "insights_by_category": self.insights_by_category,
            "category_counts": self.category_counts,
            "insight_frequency": self.insight_frequency,
            "topic_frequency": self.topic_frequency,
        }


def aggregate_corpus(transcripts: Iterable[str]) -> CorpusAggregation:
    """Aggregate insights across a corpus of transcript texts."""

    cat_groups: defaultdict[str, List[str]] = defaultdict(list)
    insight_freq: Counter[str] = Counter()
    topic_freq: Counter[str] = Counter()

    for text in transcripts:
        for ins in extract_insights(text):
            cat_groups[ins["category"]].append(ins["text"])
            norm = ins["text"].lower()
            insight_freq[norm] += 1
            tokens = [t for t in re.findall(r"\b\w+\b", norm) if len(t) > 3]
            for token in tokens:
                topic_freq[token] += 1
            for i in range(len(tokens) - 1):
                bigram = f"{tokens[i]} {tokens[i+1]}"
                topic_freq[bigram] += 1

    cat_counts = {cat: len(items) for cat, items in cat_groups.items()}
    return CorpusAggregation(
        dict(cat_groups),
        cat_counts,
        dict(insight_freq),
        dict(topic_freq),
    )


@dataclass
class PatternResult:
    patterns: List[tuple[str, int]]

    def to_dict(self) -> Dict[str, Any]:
        return {"patterns": self.patterns}


def detect_patterns(agg: CorpusAggregation, threshold: int = 2) -> PatternResult:
    """Detect recurring topics across insights based on frequency."""

    items = [(text, count) for text, count in agg.insight_frequency.items() if count >= threshold]
    if not items:
        items = [(tok, cnt) for tok, cnt in agg.topic_frequency.items() if cnt >= threshold]
    items.sort(key=lambda x: x[1], reverse=True)
    return PatternResult(items)


from analytics.dashboard import ChartData, Metric, RankedList, Dashboard


def build_dashboard(agg: CorpusAggregation, patterns: PatternResult) -> Dashboard:
    """Create a dashboard summarizing aggregated insights and patterns."""

    chart = ChartData(
        title="Insights by Category",
        series=sorted(agg.category_counts.items()),
    )
    metric = Metric(name="Total Insights", value=sum(agg.category_counts.values()), unit="count")
    ranked = RankedList(title="Recurring Topics", items=patterns.patterns)
    return Dashboard(charts=[chart], metrics=[metric], rankings=[ranked])
