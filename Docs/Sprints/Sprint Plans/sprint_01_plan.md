# Sprint 01 Plan

## 1 · Sprint Goal (≤25 words)
**Fix CI pipeline by resolving submodule dependency and establish green build foundation for strategic analysis development.**

## 2 · Deliverables & Acceptance Criteria

### Task 1: Remove Broken Submodule Dependency
- **AC1**: Remove `common-utils` submodule from `.gitmodules` and repository
- **AC2**: Update CI workflow to remove submodule references
- **AC3**: Verify local `common-utils` directory cleanup

### Task 2: Fix CI Pipeline Dependencies  
- **AC1**: Update `requirements.txt` to remove `common-utils` dependency
- **AC2**: Modify CI workflow to remove `pip install -e ./common-utils/` step
- **AC3**: All 3 Python versions (3.9, 3.10, 3.11) pass checkout step

### Task 3: Establish Green Build Foundation
- **AC1**: Create minimal test suite that verifies `StrategicAnalyzer` functionality
- **AC2**: All CI jobs pass with green badges
- **AC3**: Repository ready for feature development in Sprint 02

## 3 · Time-box & LOC Budget
**60 minutes · ≤30 net LOC changes across ≤4 files**

**File Change Targets:**
- `.gitmodules` (delete)
- `.github/workflows/ci.yml` (modify)
- `requirements.txt` (modify) 
- `tests/test_analyzer.py` (create)

## 4 · Workflow
1. **Think**: Analyze current submodule configuration and CI dependencies
2. **Plan**: Map exact file changes needed to remove submodule cleanly
3. **Code**: Execute submodule removal, update CI workflow, create basic tests
4. **Test**: Verify CI passes on all Python versions with green badges

## 5 · Self-Review Rubric
- [ ] **Submodule Clean**: No references to `common-utils` in `.gitmodules` or CI  
- [ ] **CI Green**: All Python matrix jobs pass successfully
- [ ] **Test Coverage**: Basic `StrategicAnalyzer` test validates core functionality
- [ ] **Dependencies**: `requirements.txt` contains only available packages
- [ ] **Repository Clean**: No broken references or dead code paths

## 6 · Proposed Next Sprint
**Sprint 02: Goal-Based Analysis Foundation** - Implement Goal data model and enhanced content scoring system. 