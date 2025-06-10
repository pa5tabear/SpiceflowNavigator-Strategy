from __future__ import annotations

import re
from typing import List, Dict

# Insight categories and associated keywords
CATEGORIES: dict[str, list[str]] = {
    "Revenue Strategy": ["revenue", "pricing", "sales", "monetization", "growth"],
    "Operational Excellence": ["cost", "efficiency", "process", "optimization", "reduction"],
    "Technology Strategy": ["technology", "innovation", "digital", "automation", "software"],
    "Market Intelligence": ["market", "competition", "trend", "opportunity", "policy"],
    "Leadership & Management": ["team", "leadership", "management", "culture", "decision"],
}

ACTION_WORDS = [
    "should",
    "need",
    "plan",
    "must",
    "will",
    "target",
    "expect",
    "aim",
    "strategy",
    "invest",
    "support",
    "develop",
    "launch",
    "expand",
    "reduce",
    "increase",
]


def extract_insights(transcript: str, max_insights: int = 7) -> List[Dict[str, str]]:
    """Return actionable insights categorized by business function."""
    if not transcript:
        return []
    sentences = re.split(r"(?<=[.!?])\s+", transcript)
    insights: List[Dict[str, str]] = []
    for sentence in sentences:
        text = sentence.strip()
        if not text:
            continue
        lower = text.lower()
        if any(word in lower for word in ACTION_WORDS):
            for cat, keywords in CATEGORIES.items():
                if any(k in lower for k in keywords):
                    insights.append({"text": text, "category": cat})
                    break
        if len(insights) >= max_insights:
            break
    return insights
