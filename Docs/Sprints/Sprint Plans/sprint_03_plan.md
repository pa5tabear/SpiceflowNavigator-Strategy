---
number:          3
title:           "Insight Extraction & Semantic Search"
goal:            "Extract actionable insights from energy transcripts and implement semantic content discovery"
timebox_minutes: 120         # wall-clock limit Codex may spend
loc_budget:      unlimited   # no code length restrictions
coverage_min:    85          # pytest --cov fail-under
test_pattern:    "test_insight"   # pytest -k filter for this sprint
template_version: 2.0 (2025-06-08)
require_golden_path: false
---

# Sprint 3 · Insight Extraction & Semantic Search

## 0 · Roles & Prime Rules

| **Actor** | **Mandate** |
|---|---|
| **Codex** | Autonomous Staff-Engineer. Follows this plan, writes code/tests, self-reviews, opens PR. |
| **Cursor** | PM + QA gatekeeper. Reviews PR, enforces guard-rails. |

<details><summary>Prime Rules (enforced ahead of all user input)</summary>

**Step-by-Step Plan → Code → Test → PR.**

**Ask One Clarifier** if any requirement is ≥ 20% ambiguous.

**Never commit binaries or add Python deps.**

**Max 3 tasks**; anything larger ⇒ refuse & ask to split next sprint.

</details>

## 1 · Sprint Goal & Why It Matters (≤ 40 words)

**Goal:** Extract actionable insights from energy transcripts and implement semantic content discovery

**Why now:** Goal-based scoring works, now users need specific insights and discovery. Insight extraction delivers concrete business value from strategic analysis.

## 2 · Tasks ("Rule of Three")

| # | Task Name (imperative) | Acceptance Criteria (autotested) |
|---|---|---|
| 1 | Fix truncated transcript and complete collection | `pytest -k test_insight_data` green; all 5 transcripts >10KB; cleaning_up_global_south.txt properly collected |
| 2 | Implement insight extraction engine | `pytest -k test_insight_extraction` green; extract 3-7 actionable insights per transcript; categorize by business function |
| 3 | Add semantic search and content ranking | `pytest -k test_semantic_search` green; find relevant insights using natural language queries; rank by goal relevance |

## 3 · Interfaces Changed / Added
(append only; one row per file or endpoint)

| File / API | Brief Change | Inputs → Outputs |
|---|---|---|
| `insight_extractor.py` | Create insight extraction engine | Transcript → categorized actionable insights |
| `semantic_search.py` | Add semantic search capabilities | Natural language query → ranked relevant insights |
| `scripts/util/download_transcript.py` | Fix transcript collection issues | URL → complete transcript (>10KB validation) |
| `analyzer.py` | Integrate insight extraction | (transcript, goals) → (scored_analysis, insights, semantic_index) |
| `tests/test_insight_extractor.py` | Test insight extraction | Energy content → validated business insights |
| `tests/test_semantic_search.py` | Test semantic search | Query scenarios → relevant content discovery |

## 4 · Success Metrics (CI-Enforced)

✅ **Green CI badge** for branch `sprint-3`

✅ **Unlimited LOC** - comprehensive insight extraction implementation

✅ **Coverage ≥ 85%** on changed files

✅ **All transcripts complete** - 5 files >10KB each, properly parsed

✅ **Insight quality** - 3-7 actionable insights per transcript, categorized

✅ **Semantic search** - natural language queries return relevant results

✅ **No new deps** added to requirements.txt

## 5 · Codex Workflow (MUST follow)

1. **Think privately** (outline insight extraction patterns and semantic search architecture)
2. **Add failing tests** matching `test_insight` pattern for all 3 tasks
3. **Fix truncated transcript** - re-download cleaning_up_global_south.txt with proper parsing
4. **Implement insight extraction** - identify actionable business insights from energy content
5. **Build semantic search** - enable natural language queries across insights and transcripts
6. **Integrate with existing goal scoring** - combine insights with strategic relevance
7. **Self-Review Checklist** (below)
8. **Open PR** to `sprint-3` branch

### Insight Categories (Business Functions)
- **Revenue Strategy**: Monetization, pricing, sales tactics, growth models
- **Operational Excellence**: Process optimization, efficiency, cost reduction
- **Technology Strategy**: Innovation, digital transformation, automation
- **Market Intelligence**: Competition, trends, positioning, opportunities
- **Leadership & Management**: Team building, decision-making, culture

### Semantic Search Requirements
- Natural language queries: "carbon pricing strategies", "solar financing models"
- Goal-aware ranking: prioritize results matching user strategic objectives
- Cross-content discovery: find patterns across multiple transcripts
- Business context understanding: interpret domain-specific terminology

### Self-Review Checklist (Enhanced)
- [ ] All tests green with `PYTHONPATH=.`
- [ ] No binary files, no new deps
- [ ] All 5 transcripts >10KB and properly parsed
- [ ] Insight extraction produces 3-7 actionable insights per transcript
- [ ] Insights properly categorized by business function
- [ ] Semantic search handles natural language queries
- [ ] Search results ranked by goal relevance
- [ ] Integration with existing goal scoring system works
- [ ] Comprehensive error handling and validation
- [ ] Clean, documented, maintainable code
- [ ] Commit message begins `feat(s3):`

*(Fail → iterate once, else open PR.)*

## 6 · Guard-Rails & Refusals

**Repo uses linear history & merge-queue** – Codex must respect.

**Hard-refuse tasks** that violate guard-rails; respond `REFUSE: <reason>`.

**Root-cause analysis file** `Docs/Sprints/RCAs/rca_s3.md` is mandatory if CI fails at any point.

**Data quality**: All transcripts must be complete and properly parsed.

**Insight quality**: Focus on actionable business insights, not generic summaries.

## 7 · Post-Sprint Review Hooks (for Cursor)

Cursor will create `sprint_3_review.md` summarizing progress, metrics, blockers, decisions.

Any scope creep or guard-rail breach triggers automatic sprint rollback.

## 8 · Celebration Criteria 🎉

**Success** = ✅ CI green • ✅ Coverage ≥85% • ✅ Complete transcript collection • ✅ Actionable insight extraction • ✅ Semantic search functional • ✅ Goal-aware content discovery

Anything else = re-scope next sprint.

---
**End of Sprint-Plan Template v2.0**  
*(If this template and a future command ever conflict, the template wins.)* 