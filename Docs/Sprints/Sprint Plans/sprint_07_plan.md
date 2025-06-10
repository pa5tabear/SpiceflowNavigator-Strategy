---
number:          7
title:           "Natural Language Query Interface Foundation"
goal:            "Build simple natural language querying with instant strategic answers on intelligence foundation"
timebox_minutes: 120
loc_budget:      unlimited
coverage_min:    85
test_pattern:    "test_query"
template_version: 2.0 (2025-06-08)
require_golden_path: false
---

# Sprint 7 · Natural Language Query Interface Foundation

## **1 · Sprint Goal (≤25 words)**

Build simple natural language querying with instant strategic answers using complete intelligence pipeline foundation.

## **2 · Deliverables & Acceptance Criteria**

### Task 1: Implement basic natural language query processor
- `pytest -k test_query_processor` green
- Parse simple strategic queries like "Show me solar insights" or "What entities are trending?"
- Route queries to appropriate intelligence modules (insights, entities, correlations)
- Generate structured responses with supporting evidence and confidence scoring

### Task 2: Create query result ranking and formatting
- `pytest -k test_query_results` green  
- Rank query results by relevance to user strategic goals
- Format responses with supporting evidence and source attribution
- Implement smart suggestions for related follow-up queries

### Task 3: Build interactive query demonstration interface
- `pytest -k test_query_demo` green
- Create demonstration script showcasing natural language query capabilities
- Generate sample query scenarios with realistic strategic questions
- Export query results as structured data ready for future UI integration

## **4 · Workflow**

1. **Think:** Design query architecture - parse queries → route to modules → format responses
2. **Plan:** Create failing tests for all three query components  
3. **Code:** Build natural language query processor using existing intelligence foundation
4. **Test:** Implement result ranking and formatting with goal-aware prioritization
5. **Code:** Create interactive demonstration interface with sample strategic queries
6. **Test:** Validate query pipeline processes strategic questions with professional responses
7. **Review:** Self-check against ThoughtSpot-style query quality standards
8. **PR:** Open to `sprint-7` branch with natural language query capabilities

### **Query Architecture Components**
- **Query Parser**: Natural language interpretation and intent recognition
- **Intelligence Router**: Routes queries to appropriate analysis modules  
- **Result Formatter**: Professional response generation with evidence
- **Demo Interface**: Interactive query demonstration with strategic scenarios

## **5 · Self-Review Rubric**

- [ ] All `test_query*` tests green with realistic strategic query scenarios
- [ ] Natural language query processor handles common strategic questions
- [ ] Result ranking prioritizes responses by user goal relevance  
- [ ] Query responses include supporting evidence and source attribution
- [ ] Smart follow-up suggestions enhance query exploration experience
- [ ] Demo interface showcases professional-grade strategic query capabilities
- [ ] Clean integration with complete intelligence pipeline (goals, insights, entities, correlations)
- [ ] Comprehensive error handling for ambiguous or unsupported queries
- [ ] No new dependencies added to requirements.txt
- [ ] Commit message begins `feat(s7): natural language query foundation`

## **6 · Proposed Next Sprint**

Sprint 8: Visual Analytics Dashboard - Interactive dashboards and drill-down capabilities for strategic intelligence visualization. 