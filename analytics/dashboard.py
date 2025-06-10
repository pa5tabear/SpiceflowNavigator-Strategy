from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import List, Dict, Any


@dataclass
class ChartData:
    """Represents chart series for dashboard visualization."""

    title: str
    series: List[tuple[str, float]]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Metric:
    name: str
    value: float
    unit: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class RankedList:
    title: str
    items: List[tuple[str, float]]

    def to_dict(self) -> Dict[str, Any]:
        return {"title": self.title, "items": self.items}


@dataclass
class Dashboard:
    charts: List[ChartData]
    metrics: List[Metric]
    rankings: List[RankedList]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "charts": [c.to_dict() for c in self.charts],
            "metrics": [m.to_dict() for m in self.metrics],
            "rankings": [r.to_dict() for r in self.rankings],
        }
