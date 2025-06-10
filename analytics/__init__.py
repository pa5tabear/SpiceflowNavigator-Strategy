"""Analytics utilities for SpiceflowNavigator-Strategy."""

from .aggregation import aggregate_transcripts, aggregate_corpus, detect_patterns, build_dashboard
from .entity import track_entities, detect_relationships, build_timeline
from .correlation import cross_source_correlation, build_advanced_network, run_correlation_demo

__all__ = [
    "aggregate_transcripts",
    "aggregate_corpus",
    "detect_patterns",
    "build_dashboard",
    "track_entities",
    "detect_relationships",
    "build_timeline",
    "cross_source_correlation",
    "build_advanced_network",
    "run_correlation_demo",
]
