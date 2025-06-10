import pytest
from goal_model import Goal, SOLAR_DEVELOPMENT, CARBON_REMOVAL, REAL_ESTATE


def test_goal_validation():
    with pytest.raises(ValueError):
        Goal(name="", keywords=["x"])
    with pytest.raises(TypeError):
        Goal(name="Bad", keywords="x")
    with pytest.raises(ValueError):
        Goal(name="Bad", keywords=[])


def test_score_content_range():
    g = Goal(name="Test", keywords=["alpha", "beta"])
    text = "alpha gamma beta"
    score = g.score_content(text)
    assert 0.0 <= score <= 1.0
    assert score == 1.0


def test_predefined_goals_keywords():
    text = "We filed interconnection in MISO and signed a PPA for 120 MW project"
    score = SOLAR_DEVELOPMENT.score_content(text)
    assert score > 0

    text2 = "This biochar plant could reach gigaton-scale carbon capture"
    score2 = CARBON_REMOVAL.score_content(text2)
    assert score2 > 0

    text3 = "A subdivision project aims for 15% IRR with ADU development"
    score3 = REAL_ESTATE.score_content(text3)
    assert score3 > 0
