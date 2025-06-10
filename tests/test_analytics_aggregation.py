import datetime

from analytics.aggregation import aggregate_transcripts
from goal_model import SOLAR_DEVELOPMENT, CARBON_REMOVAL


def _sample_transcripts():
    return [
        {
            "text": "We will reduce costs with automation to improve efficiency.",
            "timestamp": datetime.datetime(2025, 6, 1),
        },
        {
            "text": (
                "We plan to monetize through new pricing models for our solar project "
                "which will reach 120 MW."
            ),
            "timestamp": datetime.datetime(2025, 6, 2),
        },
        {
            "text": "We plan to innovate with biochar to enable gigaton-scale carbon capture.",
            "timestamp": datetime.datetime(2025, 6, 3),
        },
    ]


def test_aggregation_basic():
    trans = _sample_transcripts()
    goals = [SOLAR_DEVELOPMENT, CARBON_REMOVAL]
    result = aggregate_transcripts(trans, goals)
    data = result.to_dict()
    assert data["category_counts"]
    assert data["goal_scores"][SOLAR_DEVELOPMENT.name] > 0
    assert data["goal_scores"][CARBON_REMOVAL.name] > 0
    assert data["trend"]


def test_filtering():
    trans = _sample_transcripts()
    goals = [SOLAR_DEVELOPMENT, CARBON_REMOVAL]
    start = datetime.datetime(2025, 6, 2)
    result = aggregate_transcripts(trans, goals, start=start, category="Revenue Strategy")
    data = result.to_dict()
    assert len(data["trend"]) == 1
