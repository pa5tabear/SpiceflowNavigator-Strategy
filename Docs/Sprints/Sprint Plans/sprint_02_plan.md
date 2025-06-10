---
number:          2
title:           "Goal-Based Analysis Foundation + Test Data"
goal:            "Implement Goal data model with energy podcast test data for strategic analysis validation"
timebox_minutes: 120         # wall-clock limit Codex may spend
loc_budget:      150         # net new/changed lines allowed
coverage_min:    85          # pytest --cov fail-under
test_pattern:    "test_goal"   # pytest -k filter for this sprint
template_version: 2.0 (2025-06-08)
require_golden_path: false
---

# Sprint 2 · Goal-Based Analysis Foundation + Test Data

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

**Goal:** Implement Goal data model with energy podcast test data for strategic analysis validation

**Why now:** CI foundation enables feature development. Goal-based scoring needs real test data for validation. Energy podcasts provide diverse strategic content for analysis.

## 2 · Tasks ("Rule of Three")

| # | Task Name (imperative) | Acceptance Criteria (autotested) |
|---|---|---|
| 1 | Create Goal data model and scoring system | `pytest -k test_goal_model` green; Goal class with name, keywords, weight; score_content() returns 0.0-1.0 |
| 2 | Collect energy podcast test transcripts | 5 transcript files in `data/raw_podcasts/`; download script works; files readable by StrategicAnalyzer |
| 3 | Integrate goal-based analysis with test data | `pytest -k test_goal_integration` green; analyzer processes real transcripts with goal scoring |

## 3 · Interfaces Changed / Added
(append only; one row per file or endpoint)

| File / API | Brief Change | Inputs → Outputs |
|---|---|---|
| `goal_model.py` | Create new file | Goal specifications → Goal class with scoring algorithm |
| `scripts/util/download_transcript.py` | Create transcript downloader | URL → cleaned transcript text file |
| `data/raw_podcasts/*.txt` | Add 5 energy podcast transcripts | Raw content → test data for analysis |
| `analyzer.py` | Add goal-based analysis | (transcript, goals) → goal-scored analysis results |
| `tests/test_goal_model.py` | Create goal model tests | Test inputs → Goal validation and scoring tests |
| `tests/test_analyzer.py` | Extend with real data tests | Test scenarios → Goal integration with real transcripts |

## 4 · Success Metrics (CI-Enforced)

✅ **Green CI badge** for branch `sprint-2`

✅ **LOC budget ≤ 150** within 6 files

✅ **Coverage ≥ 85%** on changed files

✅ **All tests pass** with `PYTHONPATH=.` setup

✅ **5 energy transcripts** successfully collected and processable

✅ **No new deps** added to requirements.txt

## 5 · Codex Workflow (MUST follow)

1. **Think privately** (outline Goal model + data collection strategy in comments)
2. **Add failing tests** matching `test_goal` pattern for Goal model and integration
3. **Implement transcript download script** with BeautifulSoup HTML cleaning
4. **Create Goal class** with keyword-based scoring algorithm
5. **Collect 5 energy podcast transcripts** per `data/raw_podcasts/README.md` spec
6. **Update StrategicAnalyzer** to accept goals and score real transcript content
7. **Self-Review Checklist** (below)
8. **Open PR** to `sprint-2` branch

### Required Transcript Sources
- Volts: Clean energy supply chains (volts.wtf)
- Catalyst: Data center colocation (latitudemedia.com)  
- Catalyst: FOAK project financing (latitudemedia.com)
- Columbia Energy Exchange: America's energy priorities (energypolicy.columbia.edu)
- Cleaning Up: Global South clean energy (simplecast.com)

### Self-Review Checklist (5-point)
- [ ] All tests green with `PYTHONPATH=.`
- [ ] No binary files, no new deps (except BeautifulSoup if needed)
- [ ] LOC delta ≤ 150 across 6 files
- [ ] Goal class validates inputs and scores content 0.0-1.0
- [ ] 5 transcript files collected and readable
- [ ] StrategicAnalyzer processes real podcast content with goals
- [ ] Commit message begins `feat(s2):` 

*(Fail → iterate once, else open PR.)*

## 6 · Guard-Rails & Refusals

**Repo uses linear history & merge-queue** – Codex must respect.

**Hard-refuse tasks** that violate guard-rails; respond `REFUSE: <reason>`.

**Root-cause analysis file** `Docs/Sprints/RCAs/rca_s2.md` is mandatory if CI fails at any point.

**Copyright compliance**: Only collect publicly accessible transcripts with no paywalls.

## 7 · Post-Sprint Review Hooks (for Cursor)

Cursor will create `sprint_2_review.md` summarizing progress, metrics, blockers, decisions.

Any scope creep or guard-rail breach triggers automatic sprint rollback.

## 8 · Celebration Criteria 🎉

**Success** = ✅ CI green • ✅ Coverage ≥85% • ✅ Goal-based scoring works • ✅ Real energy data analyzed • ✅ Strategic analyzer enhanced

Anything else = re-scope next sprint.

---
**End of Sprint-Plan Template v2.0**  
*(If this template and a future command ever conflict, the template wins.)* 