from analyzer import StrategicAnalyzer


def test_keywords_summary():
    transcript = (
        "Our growth strategy is strong. We will cut costs. Competition is fierce."
    )
    analyzer = StrategicAnalyzer()
    result = analyzer.analyze(transcript, max_words=20)
    assert result == "Our growth strategy is strong. Competition is fierce."


def test_no_keyword_fallback():
    transcript = "Hello world. Nothing about business here."
    analyzer = StrategicAnalyzer()
    result = analyzer.analyze(transcript, max_words=10)
    assert result == "Hello world."
