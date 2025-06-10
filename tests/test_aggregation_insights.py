import datetime

from analytics.aggregation import aggregate_corpus


def _sample_corpus():
    return [
        "We will reduce costs with automation to improve efficiency.",
        (
            "Our revenue strategy will increase pricing and we will reduce costs."
        ),
        "Technology innovation is key to automation and efficiency.",
    ]


def test_aggregation_insights_basic():
    corpus = _sample_corpus()
    result = aggregate_corpus(corpus)
    data = result.to_dict()
    assert data["category_counts"]["Operational Excellence"] >= 1
    assert data["category_counts"]["Revenue Strategy"] >= 1
    assert data["insight_frequency"]
