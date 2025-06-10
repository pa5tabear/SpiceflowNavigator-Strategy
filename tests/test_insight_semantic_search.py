from semantic_search import search_insights
from goal_model import SOLAR_DEVELOPMENT


def test_semantic_search_query():
    insights = [
        {"text": "We will reduce costs with automation.", "category": "Operational Excellence"},
        {"text": "We plan to monetize through new pricing models.", "category": "Revenue Strategy"},
        {"text": "The solar project reached 120 MW and signed a PPA.", "category": "Technology Strategy"},
    ]
    results = search_insights("pricing strategy", insights)
    assert results[0][0]['category'] == 'Revenue Strategy'

    results_goals = search_insights("solar", insights, goals=[SOLAR_DEVELOPMENT])
    assert results_goals[0][0]['text'].startswith('The solar project')
