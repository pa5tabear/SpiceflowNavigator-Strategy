from analytics.dashboard import ChartData, Metric, RankedList, Dashboard


def test_dashboard_export():
    chart = ChartData(title="Insight Trend", series=[("2025-06", 3)])
    metric = Metric(name="Total Insights", value=3, unit="count")
    ranked = RankedList(title="Top Goals", items=[("Solar Development", 1.5)])
    dash = Dashboard(charts=[chart], metrics=[metric], rankings=[ranked])
    data = dash.to_dict()
    assert data["charts"][0]["title"] == "Insight Trend"
    assert data["metrics"][0]["name"] == "Total Insights"
    assert data["rankings"][0]["items"][0][0] == "Solar Development"
