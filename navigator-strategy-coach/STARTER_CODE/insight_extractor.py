"""
Starter Code: Insight Extraction Engine

This demonstrates how to extract actionable insights from podcast transcripts.
Use this as a foundation for Feature 2: Insight Extraction Engine.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
import re
from datetime import datetime


@dataclass
class Insight:
    """Represents an actionable strategic insight extracted from content."""
    
    content: str  # The insight text
    category: str  # Strategic category (revenue, growth, operations, etc.)
    confidence: float  # Extraction confidence (0.0 to 1.0)
    source_text: str  # Original text this insight was extracted from
    metrics: list[str] = field(default_factory=list)  # Mentioned metrics/numbers
    actions: list[str] = field(default_factory=list)  # Suggested actions
    entities: list[str] = field(default_factory=list)  # Companies, people, products
    timestamp: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> dict[str, Any]:
        """Convert insight to dictionary for storage/API."""
        return {
            "content": self.content,
            "category": self.category,
            "confidence": self.confidence,
            "source_text": self.source_text,
            "metrics": self.metrics,
            "actions": self.actions,
            "entities": self.entities,
            "timestamp": self.timestamp.isoformat(),
        }


class InsightExtractor:
    """Extracts strategic insights from text content."""
    
    def __init__(self):
        # Categories for business insights
        self.categories = {
            "revenue": ["revenue", "sales", "pricing", "monetization", "subscription"],
            "growth": ["growth", "scaling", "expansion", "market share", "acquisition"],
            "product": ["product", "feature", "development", "innovation", "user experience"],
            "operations": ["efficiency", "process", "automation", "cost", "optimization"],
            "leadership": ["leadership", "team", "culture", "hiring", "management"],
            "strategy": ["strategy", "competitive", "positioning", "vision", "roadmap"],
            "marketing": ["marketing", "brand", "customer", "acquisition", "retention"],
            "funding": ["funding", "investment", "capital", "valuation", "investors"]
        }
        
        # Patterns for extracting metrics and numbers
        self.metric_patterns = [
            r"\d+%",  # Percentages
            r"\$\d+[KMB]?",  # Dollar amounts
            r"\d+[KMB]?\s*users?",  # User counts
            r"\d+[KMB]?\s*customers?",  # Customer counts
            r"\d+x",  # Multipliers
            r"\d+\.\d+x",  # Decimal multipliers
        ]

    def extract_insights(self, text: str, min_confidence: float = 0.5) -> list[Insight]:
        """Extract strategic insights from text."""
        insights = []
        
        # Split text into sentences
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
        
        for sentence in sentences:
            insight = self._analyze_sentence(sentence)
            if insight and insight.confidence >= min_confidence:
                insights.append(insight)
        
        return insights
    
    def _analyze_sentence(self, sentence: str) -> Insight | None:
        """Analyze a single sentence for insights."""
        # Determine category
        category = self._categorize_content(sentence)
        if not category:
            return None
            
        # Calculate confidence
        confidence = self._calculate_confidence(sentence, category)
        if confidence < 0.3:
            return None
        
        # Extract metrics and entities
        metrics = self._extract_metrics(sentence)
        entities = self._extract_entities(sentence)
        
        return Insight(
            content=sentence,
            category=category,
            confidence=confidence,
            source_text=sentence,
            metrics=metrics,
            entities=entities,
        )
    
    def _categorize_content(self, text: str) -> str | None:
        """Determine the strategic category of content."""
        text_lower = text.lower()
        
        scores = {}
        for category, keywords in self.categories.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            if score > 0:
                scores[category] = score
        
        if scores:
            return max(scores.keys(), key=lambda k: scores[k])
        return None
    
    def _calculate_confidence(self, text: str, category: str) -> float:
        """Calculate confidence score for insight extraction."""
        confidence = 0.0
        text_lower = text.lower()
        
        # Base confidence from category keywords
        category_keywords = self.categories.get(category, [])
        keyword_matches = sum(1 for kw in category_keywords if kw in text_lower)
        confidence += min(keyword_matches * 0.2, 0.6)
        
        # Boost for specific business signals
        if any(pattern in text_lower for pattern in ["increased", "decreased", "improved", "reduced"]):
            confidence += 0.2
            
        if re.search(r'\d+', text):  # Contains numbers
            confidence += 0.1
        
        return min(confidence, 1.0)
    
    def _extract_metrics(self, text: str) -> list[str]:
        """Extract metrics and numerical data from text."""
        metrics = []
        for pattern in self.metric_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            metrics.extend(matches)
        return list(set(metrics))
    
    def _extract_entities(self, text: str) -> list[str]:
        """Extract named entities (companies, people, products)."""
        # Simple pattern for company names (capitalized words)
        company_pattern = r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b'
        potential_entities = re.findall(company_pattern, text)
        
        # Filter out common words
        common_words = {"The", "This", "That", "When", "Where", "How", "Why", "What"}
        entities = [entity for entity in potential_entities if entity not in common_words]
        
        return entities[:5]


# Demo function
def demo_insight_extraction():
    """Demonstrate insight extraction on sample content."""
    
    extractor = InsightExtractor()
    
    sample_text = """
    Netflix increased their subscription pricing by 15% for the premium tier this quarter.
    The strategy was to focus on content quality over quantity. 
    They reduced customer acquisition costs by 30% through improved targeting.
    Companies should prioritize customer retention over new acquisitions.
    Airbnb improved their host onboarding process, resulting in 40% faster time-to-first-booking.
    """
    
    print("🔍 Insight Extraction Demo")
    print("=" * 60)
    print(f"Sample Text:\n{sample_text}")
    print("\n" + "=" * 60)
    
    insights = extractor.extract_insights(sample_text)
    
    print(f"\nExtracted {len(insights)} insights:")
    print("-" * 40)
    
    for i, insight in enumerate(insights, 1):
        print(f"\n{i}. {insight.category.upper()} (confidence: {insight.confidence:.2f})")
        print(f"   Content: {insight.content}")
        if insight.metrics:
            print(f"   Metrics: {', '.join(insight.metrics)}")
        if insight.entities:
            print(f"   Entities: {', '.join(insight.entities)}")


if __name__ == "__main__":
    demo_insight_extraction() 