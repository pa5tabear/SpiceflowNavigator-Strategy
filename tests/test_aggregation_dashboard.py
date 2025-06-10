from analytics.aggregation import aggregate_corpus, detect_patterns, build_dashboard


def _sample_corpus():
    return [
        "We will reduce costs with automation to improve efficiency.",
        "Our revenue strategy will increase pricing and we will reduce costs.",
        "Technology innovation is key and we must reduce costs through automation.",
    ]


def test_dashboard_creation():
    agg = aggregate_corpus(_sample_corpus())
    patterns = detect_patterns(agg)
    dash = build_dashboard(agg, patterns)
    data = dash.to_dict()
    assert data["charts"][0]["title"] == "Insights by Category"
    assert data["metrics"][0]["name"] == "Total Insights"
    assert data["rankings"][0]["title"] == "Recurring Topics"
