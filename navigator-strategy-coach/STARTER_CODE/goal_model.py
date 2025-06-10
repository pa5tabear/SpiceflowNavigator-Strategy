"""
Starter Code: Goal Data Model for Strategic Analysis

This demonstrates how to structure strategic goals for content scoring.
Use this as a foundation for Feature 1: Goal-Based Analysis.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
import json


@dataclass
class Goal:
    """Represents a user's strategic business objective."""
    
    name: str
    description: str
    keywords: list[str] = field(default_factory=list)
    weight: float = 1.0  # Importance multiplier (0.1 to 2.0)
    category: str = "general"  # business_function category
    
    def __post_init__(self):
        """Validate goal data after initialization."""
        if not self.name or not self.description:
            raise ValueError("Goal must have name and description")
        
        if not 0.1 <= self.weight <= 2.0:
            raise ValueError("Goal weight must be between 0.1 and 2.0")
            
        # Normalize keywords to lowercase
        self.keywords = [k.lower().strip() for k in self.keywords if k.strip()]

    def score_content(self, content: str) -> float:
        """
        Score content relevance to this goal (0.0 to 1.0).
        
        This is a simple starter implementation.
        Your team should evolve this into sophisticated semantic analysis.
        """
        content_lower = content.lower()
        
        # Calculate keyword match score
        matches = sum(1 for keyword in self.keywords if keyword in content_lower)
        if not self.keywords:
            return 0.0
            
        keyword_score = min(matches / len(self.keywords), 1.0)
        
        # Apply goal weight
        return keyword_score * self.weight

    def to_dict(self) -> dict[str, Any]:
        """Convert goal to dictionary for storage/API."""
        return {
            "name": self.name,
            "description": self.description, 
            "keywords": self.keywords,
            "weight": self.weight,
            "category": self.category,
        }
    
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Goal:
        """Create goal from dictionary."""
        return cls(
            name=data["name"],
            description=data["description"],
            keywords=data.get("keywords", []),
            weight=data.get("weight", 1.0),
            category=data.get("category", "general"),
        )


@dataclass 
class GoalSet:
    """Collection of strategic goals for a user."""
    
    goals: list[Goal] = field(default_factory=list)
    
    def add_goal(self, goal: Goal) -> None:
        """Add a goal to the set."""
        if goal.name in [g.name for g in self.goals]:
            raise ValueError(f"Goal '{goal.name}' already exists")
        self.goals.append(goal)
    
    def remove_goal(self, name: str) -> bool:
        """Remove goal by name. Returns True if found and removed."""
        for i, goal in enumerate(self.goals):
            if goal.name == name:
                del self.goals[i]
                return True
        return False
    
    def get_goal(self, name: str) -> Goal | None:
        """Get goal by name."""
        for goal in self.goals:
            if goal.name == name:
                return goal
        return None
    
    def score_content(self, content: str) -> dict[str, float]:
        """Score content against all goals."""
        return {goal.name: goal.score_content(content) for goal in self.goals}
    
    def get_top_goals(self, content: str, limit: int = 3) -> list[tuple[Goal, float]]:
        """Get top-scoring goals for content."""
        scores = [(goal, goal.score_content(content)) for goal in self.goals]
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:limit]


# Example usage and test data
def create_example_goals() -> GoalSet:
    """Create example goals for testing and demonstration."""
    
    goals = GoalSet()
    
    # Revenue growth goal
    goals.add_goal(Goal(
        name="Revenue Growth",
        description="Strategies to increase recurring revenue and customer lifetime value",
        keywords=["revenue", "monetization", "pricing", "sales", "growth", "retention"],
        weight=1.5,
        category="revenue"
    ))
    
    # Product-market fit goal  
    goals.add_goal(Goal(
        name="Product-Market Fit",
        description="Finding the right product for the right market segment",
        keywords=["product-market fit", "customer validation", "market research", "user feedback"],
        weight=1.8,
        category="product"
    ))
    
    # Operational efficiency goal
    goals.add_goal(Goal(
        name="Operational Efficiency", 
        description="Streamlining processes and reducing operational costs",
        keywords=["automation", "efficiency", "process", "optimization", "costs"],
        weight=1.0,
        category="operations"
    ))
    
    return goals


if __name__ == "__main__":
    # Demo the goal system
    goals = create_example_goals()
    
    # Example content to score
    content = """
    We increased our monthly recurring revenue by 40% this quarter by implementing 
    a new customer retention program and optimizing our pricing strategy.
    """
    
    print("🎯 Goal Scoring Demo")
    print("=" * 50)
    print(f"Content: {content}")
    print()
    
    scores = goals.score_content(content)
    for goal_name, score in scores.items():
        print(f"{goal_name}: {score:.2f}")
    
    print()
    print("Top 2 relevant goals:")
    top_goals = goals.get_top_goals(content, limit=2)
    for goal, score in top_goals:
        print(f"  {goal.name}: {score:.2f} (weight: {goal.weight})") 