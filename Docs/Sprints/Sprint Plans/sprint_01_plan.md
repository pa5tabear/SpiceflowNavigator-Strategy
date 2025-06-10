---
number:          1
title:           "CI Pipeline Foundation Fix"
goal:            "Fix CI pipeline by resolving submodule dependency and establish green build foundation"
timebox_minutes: 60          # wall-clock limit Codex may spend
loc_budget:      30          # net new/changed lines allowed
coverage_min:    85          # pytest --cov fail-under
test_pattern:    "test_analyzer"   # pytest -k filter for this sprint
template_version: 2.0 (2025-06-08)
require_golden_path: false
---

# Sprint 1 · CI Pipeline Foundation Fix

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

**Goal:** Fix CI pipeline by resolving submodule dependency and establish green build foundation

**Why now:** CI is 100% failing, blocking all PR merges and development workflows. Must fix foundation before any strategic analysis features can be developed.

## 2 · Tasks ("Rule of Three")

| # | Task Name (imperative) | Acceptance Criteria (autotested) |
|---|---|---|
| 1 | Remove broken submodule dependency | `pytest -k test_analyzer` green; no `.gitmodules` file exists; CI checkout step passes |
| 2 | Fix CI pipeline configuration | All 3 Python versions (3.9, 3.10, 3.11) pass; no submodule references in CI workflow |
| 3 | Create basic test foundation | `pytest tests/test_analyzer.py` green; `StrategicAnalyzer` basic functionality validated |

## 3 · Interfaces Changed / Added
(append only; one row per file or endpoint)

| File / API | Brief Change | Inputs → Outputs |
|---|---|---|
| `.gitmodules` | Remove entire file | N/A → File deleted |
| `.github/workflows/ci.yml` | Remove submodule references | CI workflow → Clean checkout without submodules |
| `requirements.txt` | Remove common-utils dependency | Package list → Clean installable dependencies |
| `tests/test_analyzer.py` | Create basic analyzer tests | Test input → StrategicAnalyzer validation |

## 4 · Success Metrics (CI-Enforced)

✅ **Green CI badge** for branch `sprint-1`

✅ **scripts/ci/check_loc_budget.sh 30** ✅

✅ **Coverage ≥ 85%** on changed files

✅ **ruff format --check & ruff --fail-level error** ✅

✅ **No new deps** (scripts/ci/check_new_deps.sh) ✅

✅ **Golden-Path script passes** iff require_golden_path = false

## 5 · Codex Workflow (MUST follow)

1. **Think privately** (outline in comments)
2. **Add failing test** matching `test_analyzer` pattern
3. **Implement code** to pass test within 30 LOC budget
4. **Run all CI checks locally**
5. **Self-Review Checklist** (below)
6. **Open PR** to `sprint-1` branch

### Self-Review Checklist (5-point)
- [ ] All tests green locally
- [ ] No binary files, no new deps  
- [ ] LOC delta ≤ 30
- [ ] Docs updated only for shipped features
- [ ] Commit message begins `feat(s1):` or `fix(s1):`

*(Fail → iterate once, else open PR.)*

## 6 · Guard-Rails & Refusals

**Repo uses linear history & merge-queue** – Codex must respect.

**Hard-refuse tasks** that violate guard-rails; respond `REFUSE: <reason>`.

**Root-cause analysis file** `Docs/Sprints/RCAs/rca_s1.md` is mandatory if CI fails at any point.

## 7 · Post-Sprint Review Hooks (for Cursor)

Cursor will create `sprint_1_review.md` summarizing progress, metrics, blockers, decisions.

Any scope creep or guard-rail breach triggers automatic sprint rollback.

## 8 · Celebration Criteria 🎉

**Success** = ✅ CI green • ✅ Coverage ↑ • ✅ No guard-rail hits • ✅ Honest docs

Anything else = re-scope next sprint.

---
**End of Sprint-Plan Template v2.0**  
*(If this template and a future command ever conflict, the template wins.)* 