from __future__ import annotations

from dataclasses import dataclass, asdict, field
from typing import List, Dict, Any, Iterable
from collections import defaultdict, Counter
import json
import re

# ---------------------------------------------------------------------------
@dataclass
class EntityMention:
    """Represents a single entity mention within a transcript."""

    name: str
    type: str
    source: str
    index: int

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class EntityTrackingResult:
    """Aggregated entity statistics across transcripts."""

    mentions: Dict[str, List[EntityMention]] = field(default_factory=dict)
    frequency: Dict[str, int] = field(default_factory=dict)
    prominence: Dict[str, float] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "mentions": {
                k: [m.to_dict() for m in v]
                for k, v in self.mentions.items()
            },
            "frequency": self.frequency,
            "prominence": self.prominence,
        }


@dataclass
class EntityNetwork:
    """Co-occurrence network of entities."""

    edges: List[tuple[str, str, int]]

    def to_dict(self) -> Dict[str, Any]:
        return {"edges": self.edges}


@dataclass
class EntityTimeline:
    """Temporal data for entity mentions."""

    timeline: Dict[str, List[tuple[int, int]]]

    def to_dict(self) -> Dict[str, Any]:
        return self.timeline

    def to_json(self) -> str:
        return json.dumps(self.timeline)


# ---------------------------------------------------------------------------
TECH_TERMS = [
    "solar",
    "hydrogen",
    "data center",
    "carbon removal",
    "geothermal",
    "nuclear",
    "ai",
    "fusion",
    "wind",
    "storage",
]

COMPANY_KEYWORDS = [
    "Microsoft",
    "Google",
    "Amazon",
    "Meta",
    "BP",
]

COMPANY_SUFFIXES = [
    "Inc",
    "Corporation",
    "Corp",
    "Company",
    "LLC",
    "Ltd",
    "Holdings",
    "Group",
]


def _extract_entities(text: str) -> List[tuple[str, str]]:
    """Return list of (entity, type) pairs from text."""

    results: List[tuple[str, str]] = []
    lower = text.lower()

    # detect technology terms
    for term in TECH_TERMS:
        pattern = r"\b" + re.escape(term) + r"s?\b"
        for _ in re.finditer(pattern, lower):
            results.append((term.title(), "technology"))

    # detect well-known company names
    for company in COMPANY_KEYWORDS:
        for _ in re.finditer(r"\b" + re.escape(company) + r"\b", text):
            results.append((company, "company"))

    # collapse whitespace for name extraction
    clean = re.sub(r"'s\b", "", text)
    clean = re.sub(r"\s+", " ", clean)

    pattern = r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,2})\b"
    for sentence in re.split(r"[.!?\n|]", clean):
        for m in re.finditer(pattern, sentence):
            name = m.group(1).strip()
            words = name.split()
            if len(words) >= 2 and not any(w.lower() in {"the", "and", "for", "of"} for w in words):
                if len(words) > 2:
                    name = " ".join(words[-2:])
                    words = name.split()
                ent_type = "person"
                if any(w in COMPANY_SUFFIXES for w in words):
                    ent_type = "company"
                results.append((name, ent_type))

    # remove duplicates while preserving order
    seen: set[tuple[str, str]] = set()
    unique: List[tuple[str, str]] = []
    for ent in results:
        if ent not in seen:
            unique.append(ent)
            seen.add(ent)
    return unique


# ---------------------------------------------------------------------------

def track_entities(transcripts: Iterable[str]) -> EntityTrackingResult:
    """Track entities across a list of transcript texts."""

    mentions: Dict[str, List[EntityMention]] = defaultdict(list)
    total_mentions = 0

    for idx, text in enumerate(transcripts):
        entities = _extract_entities(text)
        source = f"transcript_{idx}"
        for name, etype in entities:
            mentions[name].append(EntityMention(name, etype, source, idx))
            total_mentions += 1

    frequency = {name: len(m) for name, m in mentions.items()}
    max_freq = max(frequency.values() or [1])
    prominence = {name: freq / max_freq for name, freq in frequency.items()}

    return EntityTrackingResult(dict(mentions), frequency, prominence)


# ---------------------------------------------------------------------------

def detect_relationships(tracking: EntityTrackingResult) -> EntityNetwork:
    """Compute simple co-occurrence counts between entity pairs."""

    pair_counts: Counter[tuple[str, str]] = Counter()

    # gather mentions by transcript index
    entities_by_index: Dict[int, set[str]] = defaultdict(set)
    for name, mlist in tracking.mentions.items():
        for m in mlist:
            entities_by_index[m.index].add(name)

    for idx_entities in entities_by_index.values():
        items = sorted(idx_entities)
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                pair_counts[(items[i], items[j])] += 1

    edges = [(a, b, c) for (a, b), c in pair_counts.items() if c > 0]
    edges.sort(key=lambda x: x[2], reverse=True)
    return EntityNetwork(edges)


# ---------------------------------------------------------------------------

def build_timeline(tracking: EntityTrackingResult) -> EntityTimeline:
    """Create timeline data for entity mentions across transcripts."""

    timeline: Dict[str, Dict[int, int]] = defaultdict(lambda: defaultdict(int))

    for name, mlist in tracking.mentions.items():
        for m in mlist:
            timeline[name][m.index] += 1

    timeline_sorted: Dict[str, List[tuple[int, int]]] = {
        name: sorted(data.items()) for name, data in timeline.items()
    }
    return EntityTimeline(timeline_sorted)

