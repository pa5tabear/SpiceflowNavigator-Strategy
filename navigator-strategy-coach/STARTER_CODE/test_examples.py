"""
Starter Code: Test Examples for Navigator-Strategy

This demonstrates testing patterns for strategic analysis components.
Use these patterns when building your features.
"""

import pytest
from unittest.mock import Mock
from goal_model import Goal, GoalSet
from insight_extractor import Insight, InsightExtractor


class TestGoal:
    """Test examples for Goal data model."""
    
    def test_goal_creation(self):
        """Test basic goal creation and validation."""
        goal = Goal(
            name="Revenue Growth",
            description="Increase monthly recurring revenue",
            keywords=["revenue", "growth", "mrr"],
            weight=1.5,
            category="revenue"
        )
        
        assert goal.name == "Revenue Growth"
        assert goal.weight == 1.5
        assert "revenue" in goal.keywords
    
    def test_goal_validation(self):
        """Test goal validation rules."""
        # Test missing name
        with pytest.raises(ValueError, match="Goal must have name and description"):
            Goal(name="", description="Test description")
        
        # Test invalid weight
        with pytest.raises(ValueError, match="Goal weight must be between 0.1 and 2.0"):
            Goal(name="Test", description="Test description", weight=3.0)
    
    def test_keyword_normalization(self):
        """Test that keywords are normalized to lowercase."""
        goal = Goal(
            name="Test Goal",
            description="Test description",
            keywords=["REVENUE", "Growth", "  MRR  "]
        )
        
        assert goal.keywords == ["revenue", "growth", "mrr"]
    
    def test_content_scoring(self):
        """Test content scoring against goals."""
        goal = Goal(
            name="Revenue Growth",
            description="Increase revenue",
            keywords=["revenue", "growth"],
            weight=1.0
        )
        
        # Test exact match
        content = "We increased revenue and saw significant growth"
        score = goal.score_content(content)
        assert score == 1.0  # Both keywords found, weight 1.0
        
        # Test partial match
        content = "Revenue increased this quarter"
        score = goal.score_content(content)
        assert score == 0.5  # One of two keywords found
        
        # Test no match
        content = "The weather is nice today"
        score = goal.score_content(content)
        assert score == 0.0
    
    def test_goal_serialization(self):
        """Test goal to/from dictionary conversion."""
        goal = Goal(
            name="Test Goal",
            description="Test description",
            keywords=["test", "goal"],
            weight=1.5,
            category="test"
        )
        
        # Test to_dict
        goal_dict = goal.to_dict()
        assert goal_dict["name"] == "Test Goal"
        assert goal_dict["weight"] == 1.5
        
        # Test from_dict
        reconstructed = Goal.from_dict(goal_dict)
        assert reconstructed.name == goal.name
        assert reconstructed.weight == goal.weight
        assert reconstructed.keywords == goal.keywords


class TestGoalSet:
    """Test examples for GoalSet collection."""
    
    def test_goal_set_operations(self):
        """Test adding, removing, and getting goals."""
        goals = GoalSet()
        
        goal1 = Goal(name="Revenue", description="Revenue goal", keywords=["revenue"])
        goal2 = Goal(name="Growth", description="Growth goal", keywords=["growth"])
        
        # Test adding goals
        goals.add_goal(goal1)
        goals.add_goal(goal2)
        assert len(goals.goals) == 2
        
        # Test duplicate prevention
        with pytest.raises(ValueError, match="Goal 'Revenue' already exists"):
            goals.add_goal(goal1)
        
        # Test getting goal
        retrieved = goals.get_goal("Revenue")
        assert retrieved == goal1
        
        # Test removing goal
        assert goals.remove_goal("Revenue") is True
        assert goals.remove_goal("NonExistent") is False
        assert len(goals.goals) == 1
    
    def test_content_scoring_multiple_goals(self):
        """Test scoring content against multiple goals."""
        goals = GoalSet()
        
        goals.add_goal(Goal(
            name="Revenue", 
            description="Revenue goal",
            keywords=["revenue", "sales"],
            weight=1.0
        ))
        
        goals.add_goal(Goal(
            name="Growth",
            description="Growth goal", 
            keywords=["growth", "expansion"],
            weight=1.5
        ))
        
        content = "We increased revenue and saw growth this quarter"
        scores = goals.score_content(content)
        
        assert "Revenue" in scores
        assert "Growth" in scores
        assert scores["Revenue"] == 1.0  # Both keywords found, weight 1.0
        assert scores["Growth"] == 1.5   # Both keywords found, weight 1.5
    
    def test_top_goals_ranking(self):
        """Test getting top-scoring goals for content."""
        goals = GoalSet()
        
        # Add goals with different weights
        goals.add_goal(Goal(name="Low", description="Low priority", keywords=["low"], weight=0.5))
        goals.add_goal(Goal(name="High", description="High priority", keywords=["high"], weight=2.0))
        goals.add_goal(Goal(name="Medium", description="Medium priority", keywords=["medium"], weight=1.0))
        
        content = "This content mentions high, medium, and low priority items"
        top_goals = goals.get_top_goals(content, limit=2)
        
        # Should be ranked by score (keyword match * weight)
        assert len(top_goals) == 2
        assert top_goals[0][0].name == "High"  # Highest score
        assert top_goals[1][0].name == "Medium"  # Second highest


class TestInsightExtractor:
    """Test examples for InsightExtractor."""
    
    def test_insight_extraction(self):
        """Test basic insight extraction."""
        extractor = InsightExtractor()
        
        text = "Netflix increased their subscription pricing by 15% this quarter."
        insights = extractor.extract_insights(text, min_confidence=0.3)
        
        assert len(insights) > 0
        insight = insights[0]
        assert isinstance(insight, Insight)
        assert insight.category in extractor.categories
        assert 0.0 <= insight.confidence <= 1.0
    
    def test_category_detection(self):
        """Test that content is categorized correctly."""
        extractor = InsightExtractor()
        
        # Test revenue category
        revenue_text = "We increased our monthly recurring revenue by 25%"
        category = extractor._categorize_content(revenue_text)
        assert category == "revenue"
        
        # Test growth category
        growth_text = "The company is scaling rapidly and expanding into new markets"
        category = extractor._categorize_content(growth_text)
        assert category == "growth"
        
        # Test no category
        irrelevant_text = "The weather is nice today"
        category = extractor._categorize_content(irrelevant_text)
        assert category is None
    
    def test_metric_extraction(self):
        """Test extraction of metrics from text."""
        extractor = InsightExtractor()
        
        text = "We increased revenue by 15% and gained 1M users"
        metrics = extractor._extract_metrics(text)
        
        assert "15%" in metrics
        assert "1M" in metrics or "1M users" in metrics
    
    def test_confidence_calculation(self):
        """Test confidence scoring for insights."""
        extractor = InsightExtractor()
        
        # High confidence: multiple keywords + numbers + action words
        high_confidence_text = "Revenue increased by 25% through improved sales strategy"
        confidence = extractor._calculate_confidence(high_confidence_text, "revenue")
        assert confidence > 0.5
        
        # Low confidence: minimal signals
        low_confidence_text = "Revenue was mentioned briefly"
        confidence = extractor._calculate_confidence(low_confidence_text, "revenue")
        assert confidence < 0.5
    
    @patch('insight_extractor.datetime')
    def test_insight_timestamp(self, mock_datetime):
        """Test that insights get timestamped."""
        mock_now = Mock()
        mock_datetime.now.return_value = mock_now
        
        insight = Insight(
            content="Test insight",
            category="test",
            confidence=0.8,
            source_text="Test source"
        )
        
        assert insight.timestamp == mock_now
    
    def test_insight_serialization(self):
        """Test insight to dictionary conversion."""
        insight = Insight(
            content="Test insight",
            category="revenue",
            confidence=0.8,
            source_text="Test source",
            metrics=["15%"],
            entities=["Netflix"]
        )
        
        insight_dict = insight.to_dict()
        assert insight_dict["content"] == "Test insight"
        assert insight_dict["category"] == "revenue"
        assert insight_dict["confidence"] == 0.8
        assert insight_dict["metrics"] == ["15%"]
        assert insight_dict["entities"] == ["Netflix"]
        assert "timestamp" in insight_dict


# Integration test examples
class TestIntegration:
    """Test examples for component integration."""
    
    def test_goal_guided_insight_filtering(self):
        """Test using goals to filter and score insights."""
        # Create goals focused on revenue
        goals = GoalSet()
        goals.add_goal(Goal(
            name="Revenue Growth",
            description="Increase revenue",
            keywords=["revenue", "pricing", "sales"],
            weight=1.5
        ))
        
        # Extract insights
        extractor = InsightExtractor()
        text = """
        Netflix increased subscription pricing by 15%.
        The weather was nice yesterday.
        Customer retention improved through better support.
        """
        
        insights = extractor.extract_insights(text, min_confidence=0.3)
        
        # Score insights against goals
        scored_insights = []
        for insight in insights:
            scores = goals.score_content(insight.content)
            if scores:
                max_score = max(scores.values())
                scored_insights.append((insight, max_score))
        
        # Should prefer revenue-related insights
        scored_insights.sort(key=lambda x: x[1], reverse=True)
        
        assert len(scored_insights) > 0
        top_insight = scored_insights[0][0]
        assert "pricing" in top_insight.content.lower() or "revenue" in top_insight.content.lower()


# Pytest fixtures for common test data
@pytest.fixture
def sample_goals():
    """Fixture providing a standard set of test goals."""
    goals = GoalSet()
    
    goals.add_goal(Goal(
        name="Revenue Growth",
        description="Increase monthly recurring revenue",
        keywords=["revenue", "pricing", "sales"],
        weight=1.5,
        category="revenue"
    ))
    
    return goals


@pytest.fixture
def sample_extractor():
    """Fixture providing a configured insight extractor."""
    return InsightExtractor()


# Example of how to run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 