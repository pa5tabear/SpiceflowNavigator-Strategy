from insight_extractor import extract_insights, CATEGORIES


def test_insight_extraction_basic():
    text = (
        "We plan to increase revenues through better pricing. "
        "Our team will focus on process optimization to reduce costs. "
        "Competition in the market is intensifying. "
        "We aim to innovate with new automation software."
    )
    insights = extract_insights(text, max_insights=5)
    assert 3 <= len(insights) <= 5
    for ins in insights:
        assert ins['category'] in CATEGORIES
        assert ins['text']
