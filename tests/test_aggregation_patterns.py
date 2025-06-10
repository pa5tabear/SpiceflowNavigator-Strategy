from analytics.aggregation import aggregate_corpus, detect_patterns


def _sample_corpus():
    return [
        "We will reduce costs with automation to improve efficiency.",
        "Our revenue strategy will increase pricing and we will reduce costs.",
        "Technology innovation is key and we must reduce costs through automation.",
    ]


def test_pattern_detection():
    agg = aggregate_corpus(_sample_corpus())
    patterns = detect_patterns(agg)
    topics = [p[0] for p in patterns.patterns]
    assert any("reduce costs" in t for t in topics)
    assert patterns.patterns[0][1] >= 2
