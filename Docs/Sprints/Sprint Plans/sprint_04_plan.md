---
number:          4
title:           "Cross-Transcript Aggregation & Simple Pattern Detection"
goal:            "Aggregate insights across transcripts and detect simple patterns in our 307KB corpus"
timebox_minutes: 120
loc_budget:      unlimited
coverage_min:    85
test_pattern:    "test_aggregation"
template_version: 2.0 (2025-06-08)
require_golden_path: false
---

# Sprint 4 · Cross-Transcript Aggregation & Simple Pattern Detection

## **1 · Sprint Goal (≤25 words)**

Build simple aggregation engine to combine insights across our 5 transcripts and detect basic patterns.

## **2 · Deliverables & Acceptance Criteria**

### Task 1: Create insight aggregation engine
- `pytest -k test_aggregation_insights` green
- Combine insights from all 5 transcripts into summary collections
- Group insights by business function (Revenue, Operations, Technology, etc.)
- Calculate frequency and prominence of insight themes

### Task 2: Build simple pattern detection
- `pytest -k test_aggregation_patterns` green  
- Identify topics mentioned across multiple transcripts
- Find recurring themes and common business concepts
- Count frequency of entities and topics across corpus

### Task 3: Create basic trend analysis dashboard
- `pytest -k test_aggregation_dashboard` green
- Generate summary of most common insights across transcripts
- Create simple ranking of topics by frequency and importance
- Export aggregated data as structured JSON for future visualization

## **4 · Workflow**

1. **Think:** Design simple aggregation - combine insights → find patterns → create dashboard
2. **Plan:** Create failing tests for all three aggregation components  
3. **Code:** Build insight aggregation engine combining all 5 transcripts
4. **Test:** Implement simple pattern detection for recurring themes
5. **Code:** Create basic dashboard data structure for trend visualization
6. **Test:** Validate aggregation pipeline processes full 307KB corpus correctly
7. **Review:** Self-check against incremental complexity standards
8. **PR:** Open to `sprint-4` branch with solid aggregation foundation

### **Simple Architecture Components**
- **Insight Aggregator**: Combines insights from all transcripts by category
- **Pattern Detector**: Finds recurring themes and common entities across corpus  
- **Trend Analyzer**: Ranks topics by frequency and strategic importance
- **Dashboard Generator**: Creates structured data for future visualization

## **5 · Self-Review Rubric**

- [ ] All `test_aggregation*` tests green with real 307KB+ data corpus
- [ ] Insight aggregation successfully combines insights from all 5 transcripts
- [ ] Pattern detection identifies themes appearing across multiple sources  
- [ ] Trend analysis ranks topics by frequency and strategic importance
- [ ] Dashboard data structure exports clean JSON for future UI consumption
- [ ] Aggregation maintains connection to original transcript sources
- [ ] Clean integration with existing goal scoring and insight extraction systems
- [ ] Comprehensive error handling for missing or malformed data
- [ ] No new dependencies added to requirements.txt
- [ ] Commit message begins `feat(s4): cross-transcript aggregation`

## **6 · Proposed Next Sprint**

Sprint 5: Enhanced Pattern Detection & Simple Entity Tracking - Build on aggregation foundation with basic relationship mapping. 