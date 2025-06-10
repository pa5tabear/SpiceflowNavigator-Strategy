---
number:          2
title:           "Goal-Based Analysis Foundation"
goal:            "Implement Goal data model and enhanced content scoring system for strategic analysis"
timebox_minutes: 90          # wall-clock limit Codex may spend
loc_budget:      120         # net new/changed lines allowed
coverage_min:    85          # pytest --cov fail-under
test_pattern:    "test_goal"   # pytest -k filter for this sprint
template_version: 2.0 (2025-06-08)
require_golden_path: false
---

# Sprint 2 · Goal-Based Analysis Foundation

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

**Goal:** Implement Goal data model and enhanced content scoring system for strategic analysis

**Why now:** CI foundation enables feature development. Goal-based scoring is Feature #1 priority from roadmap, foundational for all strategic analysis capabilities.

## 2 · Tasks ("Rule of Three")

| # | Task Name (imperative) | Acceptance Criteria (autotested) |
|---|---|---|
| 1 | Create Goal data model class | `pytest -k test_goal_model` green; Goal class with name, keywords, weight properties |
| 2 | Implement goal-based content scoring | `pytest -k test_goal_scoring` green; Goal.score_content() method returns 0.0-1.0 relevance |
| 3 | Integrate goals with StrategicAnalyzer | `pytest -k test_goal_integration` green; analyzer accepts goals list, returns goal-scored results |

## 3 · Interfaces Changed / Added
(append only; one row per file or endpoint)

| File / API | Brief Change | Inputs → Outputs |
|---|---|---|
| `goal_model.py` | Create new file | Goal specifications → Goal class with scoring |
| `analyzer.py` | Add goal-based analysis | (transcript, goals) → goal-scored analysis results |
| `tests/test_goal_model.py` | Create goal model tests | Test inputs → Goal validation and scoring tests |
| `tests/test_analyzer.py` | Extend analyzer tests | Test scenarios → Goal integration validation |

## 4 · Success Metrics (CI-Enforced)

✅ **Green CI badge** for branch `sprint-2`

✅ **LOC budget ≤ 120** within 4 files

✅ **Coverage ≥ 85%** on changed files

✅ **All tests pass** with `PYTHONPATH=.` setup

✅ **No new deps** added to requirements.txt

## 5 · Codex Workflow (MUST follow)

1. **Think privately** (outline Goal model design in comments)
2. **Add failing tests** matching `test_goal` pattern for all 3 tasks
3. **Implement Goal class** with scoring algorithm within LOC budget
4. **Update StrategicAnalyzer** to accept and use goals
5. **Self-Review Checklist** (below)
6. **Open PR** to `sprint-2` branch

### Self-Review Checklist (5-point)
- [ ] All tests green with `PYTHONPATH=.`
- [ ] No binary files, no new deps  
- [ ] LOC delta ≤ 120 across 4 files
- [ ] Goal class validates inputs and scores content 0.0-1.0
- [ ] Commit message begins `feat(s2):` 

*(Fail → iterate once, else open PR.)*

## 6 · Guard-Rails & Refusals

**Repo uses linear history & merge-queue** – Codex must respect.

**Hard-refuse tasks** that violate guard-rails; respond `REFUSE: <reason>`.

**Root-cause analysis file** `Docs/Sprints/RCAs/rca_s2.md` is mandatory if CI fails at any point.

## 7 · Post-Sprint Review Hooks (for Cursor)

Cursor will create `sprint_2_review.md` summarizing progress, metrics, blockers, decisions.

Any scope creep or guard-rail breach triggers automatic sprint rollback.

## 8 · Celebration Criteria 🎉

**Success** = ✅ CI green • ✅ Coverage ≥85% • ✅ Goal-based scoring works • ✅ Strategic analyzer enhanced

Anything else = re-scope next sprint.

---
**End of Sprint-Plan Template v2.0**  
*(If this template and a future command ever conflict, the template wins.)* 