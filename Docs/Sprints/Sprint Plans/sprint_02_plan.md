---
number:          2
title:           "Goal-Based Analysis Foundation + Test Data"
goal:            "Implement Goal data model with user strategic objectives and energy podcast test data"
timebox_minutes: 120         # wall-clock limit Codex may spend
loc_budget:      unlimited   # no code length restrictions
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

**Goal:** Implement Goal data model with user strategic objectives and energy podcast test data

**Why now:** CI foundation enables features. Real user goals (solar, carbon removal, real estate, AI) + energy transcripts enable validated strategic analysis scoring.

## 2 · Tasks ("Rule of Three")

| # | Task Name (imperative) | Acceptance Criteria (autotested) |
|---|---|---|
| 1 | Create comprehensive Goal data model with user objectives | `pytest -k test_goal_model` green; Goal class handles solar/carbon/real estate keywords; score_content() 0.0-1.0; full validation |
| 2 | Collect energy podcast test transcripts | 5 transcript files in `data/raw_podcasts/`; download script works; files readable by StrategicAnalyzer; comprehensive parsing |
| 3 | Integrate strategic scoring with real data | `pytest -k test_strategic_scoring` green; user goals score energy transcripts; relevance ranking works; full analysis pipeline |

## 3 · Interfaces Changed / Added
(append only; one row per file or endpoint)

| File / API | Brief Change | Inputs → Outputs |
|---|---|---|
| `goal_model.py` | Create comprehensive Goal class with strategic categories | User objectives → Goal instances with sophisticated keyword scoring |
| `scripts/util/download_transcript.py` | Create robust transcript downloader | URL → cleaned transcript text file |
| `data/raw_podcasts/*.txt` | Add 5 energy podcast transcripts | Raw content → test data for analysis |
| `analyzer.py` | Add comprehensive goal-based strategic scoring | (transcript, user_goals) → relevance-scored analysis results |
| `tests/test_goal_model.py` | Test Goal model with user objectives | Solar/carbon/real estate goals → comprehensive scoring validation |
| `tests/test_analyzer.py` | Test strategic scoring integration | Real transcripts + user goals → relevance ranking tests |
| `User Goals/User_Goals_Template.md` | Reference for goal categories | Strategic objectives → keyword extraction for Goal model |

## 4 · Success Metrics (CI-Enforced)

✅ **Green CI badge** for branch `sprint-2`

✅ **Unlimited LOC** - no code length restrictions, implement comprehensively

✅ **Coverage ≥ 85%** on changed files

✅ **All tests pass** with `PYTHONPATH=.` setup

✅ **5 energy transcripts** successfully collected and processable

✅ **User strategic goals** (solar, carbon, real estate, AI) correctly score content

✅ **No new deps** added to requirements.txt (except BeautifulSoup if needed)

## 5 · Codex Workflow (MUST follow)

1. **Think privately** (outline comprehensive Goal model + strategic categories from User Goals template)
2. **Add failing tests** for Goal model with user objectives and strategic scoring
3. **Implement robust transcript download script** with BeautifulSoup HTML cleaning
4. **Create comprehensive Goal class** supporting strategic categories: Solar Development, Carbon Removal, Real Estate, AI Automation
5. **Collect 5 energy podcast transcripts** per `data/raw_podcasts/README.md` specification
6. **Update StrategicAnalyzer** to accept user goals and score real transcript content with relevance ranking
7. **Implement comprehensive test suite** validating all functionality
8. **Self-Review Checklist** (below)
9. **Open PR** to `sprint-2` branch

### Required Transcript Sources
- Volts: Clean energy supply chains (volts.wtf) → matches Solar Development goals
- Catalyst: Data center colocation (latitudemedia.com) → matches AI/energy intersection  
- Catalyst: FOAK project financing (latitudemedia.com) → matches financial keywords
- Columbia Energy Exchange: America's energy priorities (energypolicy.columbia.edu) → policy relevance
- Cleaning Up: Global South clean energy (simplecast.com) → carbon removal alignment

### Strategic Goal Categories (from User Goals template)
- **Solar Development**: utility-scale, PPA, interconnection, MISO, off-take, 10 GW, 120 MW
- **Carbon Removal**: BECCS, biochar, DAC, gigaton-scale, $100/t-CO₂
- **Real Estate**: subdivision, IRR, ADU, parcel scoring, $50M equity
- **AI Automation**: agents, automation, unit testing, 85% precision, 80% coverage

### Self-Review Checklist (Enhanced)
- [ ] All tests green with `PYTHONPATH=.`
- [ ] No binary files, no new deps (except BeautifulSoup if needed)
- [ ] **No LOC restrictions** - implement comprehensively without length limits
- [ ] Goal class validates inputs and scores content 0.0-1.0 with sophisticated algorithms
- [ ] 5 transcript files collected and readable
- [ ] StrategicAnalyzer processes real podcast content with user goal scoring
- [ ] Strategic categories from User Goals template correctly implemented
- [ ] Energy transcripts show meaningful relevance differences for different goal types
- [ ] Comprehensive error handling and edge case coverage
- [ ] Clean, well-documented, maintainable code
- [ ] Commit message begins `feat(s2):` 

*(Fail → iterate once, else open PR.)*

## 6 · Guard-Rails & Refusals

**Repo uses linear history & merge-queue** – Codex must respect.

**Hard-refuse tasks** that violate guard-rails; respond `REFUSE: <reason>`.

**Root-cause analysis file** `Docs/Sprints/RCAs/rca_s2.md` is mandatory if CI fails at any point.

**Copyright compliance**: Only collect publicly accessible transcripts with no paywalls.

**Code Quality**: No LOC limits - prioritize comprehensive, well-tested implementation.

## 7 · Post-Sprint Review Hooks (for Cursor)

Cursor will create `sprint_2_review.md` summarizing progress, metrics, blockers, decisions.

Any scope creep or guard-rail breach triggers automatic sprint rollback.

## 8 · Celebration Criteria 🎉

**Success** = ✅ CI green • ✅ Coverage ≥85% • ✅ Goal-based scoring works • ✅ Real energy data analyzed • ✅ User strategic objectives integrated • ✅ Relevance ranking functional • ✅ Comprehensive implementation complete

Anything else = re-scope next sprint.

---
**End of Sprint-Plan Template v2.0**  
*(If this template and a future command ever conflict, the template wins.)* 