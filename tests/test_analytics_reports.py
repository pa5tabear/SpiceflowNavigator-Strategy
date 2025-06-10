from analytics.reports import generate_report
from goal_model import SOLAR_DEVELOPMENT


def test_report_generation():
    aggregation = {
        "category_counts": {"Revenue Strategy": 2},
        "goal_scores": {SOLAR_DEVELOPMENT.name: 1.0},
        "trend": [("2025-06", 2)],
    }
    report_md = generate_report(aggregation, [SOLAR_DEVELOPMENT], format="markdown")
    assert "# Executive Summary" in report_md
    assert "Revenue Strategy" in report_md

    report_dict = generate_report(aggregation, [SOLAR_DEVELOPMENT], format="dict")
    assert isinstance(report_dict, dict)
    assert "recommendations" in report_dict
