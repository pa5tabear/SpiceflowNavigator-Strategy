from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple
from collections import defaultdict

from .entity import _extract_entities, track_entities, EntityTrackingResult, detect_relationships, EntityNetwork


@dataclass
class SourceCorrelation:
    """Correlation score and shared entities between two sources."""

    sources: Tuple[str, str]
    score: float
    shared_entities: List[str]

    def to_dict(self) -> Dict[str, object]:
        return {
            "sources": self.sources,
            "score": self.score,
            "shared_entities": self.shared_entities,
        }


@dataclass
class CorrelationAnalysis:
    correlations: List[SourceCorrelation]

    def to_dict(self) -> Dict[str, object]:
        return {"correlations": [c.to_dict() for c in self.correlations]}


def cross_source_correlation(transcripts: Dict[str, str]) -> CorrelationAnalysis:
    """Compute correlation scores between transcript sources based on shared entities."""

    entity_sets: Dict[str, set[str]] = {
        name: {e[0] for e in _extract_entities(text)} for name, text in transcripts.items()
    }
    sources = list(entity_sets.keys())
    correlations: List[SourceCorrelation] = []
    for i in range(len(sources)):
        for j in range(i + 1, len(sources)):
            s1, s2 = sources[i], sources[j]
            e1, e2 = entity_sets[s1], entity_sets[s2]
            shared = e1 & e2
            union = e1 | e2
            score = len(shared) / len(union) if union else 0.0
            correlations.append(SourceCorrelation((s1, s2), score, sorted(shared)))
    correlations.sort(key=lambda c: c.score, reverse=True)
    return CorrelationAnalysis(correlations)


@dataclass
class AdvancedEntityNetwork:
    """Entity network with relationship strength, density and clusters."""

    edges: List[Tuple[str, str, float]]
    density: float
    clusters: List[List[str]]

    def to_dict(self) -> Dict[str, object]:
        return {
            "edges": [(a, b, w) for a, b, w in self.edges],
            "density": self.density,
            "clusters": self.clusters,
        }


def build_advanced_network(tracking: EntityTrackingResult) -> AdvancedEntityNetwork:
    """Build entity relationship network with normalized strength and clustering."""

    basic_network: EntityNetwork = detect_relationships(tracking)
    if not basic_network.edges:
        return AdvancedEntityNetwork([], 0.0, [])

    max_weight = max(weight for _, _, weight in basic_network.edges)
    edges = [(a, b, weight / max_weight) for a, b, weight in basic_network.edges]

    n = len(tracking.mentions)
    possible_edges = n * (n - 1) / 2 if n > 1 else 0
    density = len(edges) / possible_edges if possible_edges else 0.0

    adj: Dict[str, set[str]] = defaultdict(set)
    for a, b, _ in basic_network.edges:
        adj[a].add(b)
        adj[b].add(a)

    visited: set[str] = set()
    clusters: List[List[str]] = []
    for node in tracking.mentions.keys():
        if node in visited:
            continue
        stack = [node]
        comp: List[str] = []
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            comp.append(cur)
            stack.extend(adj[cur] - visited)
        if comp:
            clusters.append(sorted(comp))

    return AdvancedEntityNetwork(edges, density, clusters)


def run_correlation_demo(transcripts: Iterable[str]) -> Dict[str, object]:
    """Run end-to-end correlation demonstration over transcripts."""

    names = [f"source_{i}" for i in range(len(transcripts))]
    transcript_map = dict(zip(names, transcripts))
    tracking = track_entities(transcripts)
    network = build_advanced_network(tracking)
    analysis = cross_source_correlation(transcript_map)
    return {"network": network.to_dict(), "correlations": analysis.to_dict()}
