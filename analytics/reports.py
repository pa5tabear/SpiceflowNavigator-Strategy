from __future__ import annotations

from typing import Iterable, Dict, Any

from goal_model import Goal


def generate_report(
    aggregation: Dict[str, Any],
    goals: Iterable[Goal],
    format: str = "markdown",
) -> str | Dict[str, Any]:
    """Generate an executive summary report from aggregated insights."""

    cat_counts = aggregation.get("category_counts", {})
    goal_scores = aggregation.get("goal_scores", {})

    total_insights = sum(cat_counts.values())
    summary_lines = [f"Total insights: {total_insights}"]
    for name, count in cat_counts.items():
        summary_lines.append(f"{name}: {count}")

    recommendations = []
    for g in goals:
        if goal_scores.get(g.name, 0) > 0:
            recommendations.append(f"Focus on {g.name.lower()} opportunities")

    if format == "markdown":
        lines = ["# Executive Summary", ""]
        lines.extend(f"- {line}" for line in summary_lines)
        if recommendations:
            lines.append("\n## Recommendations")
            lines.extend(f"- {r}" for r in recommendations)
        return "\n".join(lines)

    return {"summary": summary_lines, "recommendations": recommendations}
