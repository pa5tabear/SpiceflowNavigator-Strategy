from analyzer import StrategicAnalyzer
from goal_model import SOLAR_DEVELOPMENT, CARBON_REMOVAL


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


def test_goal_scoring_integration(tmp_path):
    analyzer = StrategicAnalyzer()
    transcripts = [
        "The utility-scale solar project reached 120 MW with a strong PPA.",
        "Biochar plants could enable gigaton-scale carbon capture soon.",
    ]
    goals = [SOLAR_DEVELOPMENT, CARBON_REMOVAL]
    ranking = analyzer.rank_transcripts(transcripts, goals)
    assert ranking[0][0] in (0, 1)
    assert ranking[0][1] >= ranking[1][1]

    result = analyzer.analyze(transcripts[0], goals=goals)
    assert isinstance(result, dict)
    assert "summary" in result and "scores" in result
    assert set(result["scores"].keys()) == {g.name for g in goals}
