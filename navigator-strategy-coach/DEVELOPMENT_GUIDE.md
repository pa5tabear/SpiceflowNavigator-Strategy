# 🛠️ Navigator-Strategy Development Guide

## 🚀 Environment Setup

### **Prerequisites**
- Python 3.9+ 
- Git 2.20+
- GitHub CLI (`gh`) for repository management
- Virtual environment manager (recommended: `venv` or `conda`)

### **Initial Setup**

#### 1. Clone Your Repository
```bash
# Clone the Navigator-Strategy repository
git clone --recursive https://github.com/pa5tabear/SpiceflowNavigator-Strategy.git
cd SpiceflowNavigator-Strategy

# Initialize CommonUtils submodule (shared utilities)
git submodule update --init --recursive
```

#### 2. Create Development Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode (allows editing)
pip install -e .
```

#### 3. Verify Setup
```bash
# Run tests to verify everything works
python -m pytest tests/ -v

# Run the existing analyzer
python -c "from analyzer import StrategicAnalyzer; print('✅ Setup complete!')"
```

## 🎯 Development Workflow

### **Daily Development Cycle**

#### 1. Start Development Session
```bash
# Activate environment
source .venv/bin/activate

# Pull latest changes
git pull origin main

# Run tests to ensure clean state
make test
```

#### 2. Feature Development
```bash
# Create feature branch
git checkout -b feature/goal-based-analysis

# Run tests continuously during development
pytest tests/ --watch  # If pytest-watch is installed
```

#### 3. Testing & Quality
```bash
# Run full test suite
make test

# Check code coverage
make coverage

# Run linting and formatting
make lint
make format
```

## 🏗️ Architecture Patterns

### **File Organization**
```
SpiceflowNavigator-Strategy/
├── analyzer.py              ← Main strategic analyzer (current)
├── models/                  ← Data models (Goal, Insight, etc.)
│   ├── goal.py
│   ├── insight.py
│   └── analysis_result.py
├── extractors/              ← Content analysis engines
│   ├── insight_extractor.py
│   ├── entity_extractor.py
│   └── metric_extractor.py
├── common-utils/            ← Shared utilities (git submodule)
│   ├── config.py
│   └── runpod_client.py
├── tests/                   ← Test suite
│   ├── unit/
│   ├── integration/
│   └── fixtures/
└── examples/                ← Usage examples
```

### **Coding Standards**

#### **Python Style**
- Follow PEP 8 style guidelines
- Use type hints for all function signatures
- Use dataclasses for data models
- Write docstrings for all public functions

#### **Example Function Signature**
```python
from typing import List
from dataclasses import dataclass

@dataclass
class AnalysisResult:
    """Result of strategic content analysis."""
    insights: List[Insight]
    relevance_score: float
    categories: List[str]

def analyze_content(
    content: str, 
    goals: List[Goal], 
    min_confidence: float = 0.5
) -> AnalysisResult:
    """
    Analyze content for strategic insights aligned with user goals.
    
    Args:
        content: Text content to analyze
        goals: User's strategic objectives
        min_confidence: Minimum confidence threshold
        
    Returns:
        Analysis result with insights and scores
    """
    pass
```

## 🧪 Testing Strategy

### **Unit Tests** (Fast, Isolated)
```python
def test_goal_content_scoring():
    """Test goal-based content scoring."""
    goal = Goal(
        name="Revenue Growth",
        keywords=["revenue", "growth"],
        weight=1.5
    )
    
    # Test exact match
    content = "Revenue growth increased 25%"
    score = goal.score_content(content)
    assert score == 1.5  # Both keywords * weight
```

### **Integration Tests** (Cross-Component)
```python
def test_end_to_end_analysis(sample_goals, sample_transcript):
    """Test complete analysis pipeline."""
    analyzer = StrategicAnalyzer(goals=sample_goals)
    result = analyzer.analyze(sample_transcript)
    
    assert len(result.insights) > 0
    assert result.relevance_score > 0.0
```

## 🔧 Performance Guidelines

### **Performance Targets**
- **Analysis Speed**: < 2 seconds per transcript
- **Memory Usage**: < 500MB for 1000 cached transcripts
- **Search Latency**: < 500ms for semantic search queries

### **Optimization Patterns**

#### **Caching Strategy**
```python
from functools import lru_cache

class PerformantAnalyzer:
    @lru_cache(maxsize=1000)
    def _extract_insights_cached(self, content_hash: str, content: str):
        """Cache insight extraction for repeated content."""
        return self._extract_insights(content)
```

## 🔄 Integration with Other Agents

### **Pipeline Integration**
```python
class StrategyAgent:
    def analyze_transcript(
        self, 
        transcript: str, 
        user_goals: List[Goal]
    ) -> AnalysisResult:
        """Main entry point for Pipeline agent."""
        pass
```

## 📊 Monitoring & Debugging

### **Logging Strategy**
```python
import logging

logger = logging.getLogger(__name__)

def analyze_with_monitoring(content: str, goals: List[Goal]):
    """Analyze content with comprehensive monitoring."""
    logger.info(f"Starting analysis: {len(content)} chars, {len(goals)} goals")
    
    try:
        result = self._perform_analysis(content, goals)
        logger.info(f"Analysis complete: {len(result.insights)} insights")
        return result
    except Exception as e:
        logger.error(f"Analysis failed: {e}")
        raise
```

## 🚀 Ready to Build!

With this development guide, you have everything needed to build robust strategic analysis features.

**Next step**: Set up your environment and start with Feature 1 from the roadmap! 🚀 