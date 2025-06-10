from __future__ import annotations

from dataclasses import dataclass, field
import re
from typing import Iterable, List


@dataclass
class Goal:
    """Represents a strategic goal with keywords."""

    name: str
    keywords: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("Goal name required")
        if not isinstance(self.keywords, list) or not all(isinstance(k, str) for k in self.keywords):
            raise TypeError("Keywords must be list of strings")
        if not self.keywords:
            raise ValueError("At least one keyword required")
        self.keywords = [k.lower() for k in self.keywords]

    # ------------------------------------------------------------------
    def score_content(self, text: str) -> float:
        """Return relevance score (0-1) based on keyword frequency."""
        if not text:
            return 0.0
        text_lower = text.lower()
        hits = sum(1 for k in self.keywords if re.search(r"\b" + re.escape(k) + r"\b", text_lower))
        return hits / len(self.keywords)


# Pre-defined goal categories
SOLAR_DEVELOPMENT = Goal(
    name="Solar Development",
    keywords=["utility-scale", "ppa", "interconnection", "miso", "off-take", "10 gw", "120 mw"],
)

CARBON_REMOVAL = Goal(
    name="Carbon Removal",
    keywords=["beccs", "biochar", "dac", "gigaton-scale", "$100/t-co2"],
)

REAL_ESTATE = Goal(
    name="Real Estate",
    keywords=["subdivision", "irr", "adu", "parcel", "$50m"],
)

AI_AUTOMATION = Goal(
    name="AI Automation",
    keywords=["agents", "automation", "unit testing", "precision", "coverage"],
)


def all_goals() -> list[Goal]:
    return [SOLAR_DEVELOPMENT, CARBON_REMOVAL, REAL_ESTATE, AI_AUTOMATION]
