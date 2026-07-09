# TEST-LOG — skill_research_report_generator
> Golden test set regression log. Update this table EVERY time the skill version changes, BEFORE committing the new version.

## How to Run a Test Cycle

1. Invoke the skill using `tests/test-01-government/input.md` as input.
2. Check the output against every criterion in `tests/test-01-government/expected.md`.
3. Repeat for `tests/test-02-healthcare/`.
4. Record results below. If any criterion fails, note the criterion ID (e.g., C7) in Notes.
5. A version may only be committed as stable if BOTH tests pass. A test that passed in a previous version but fails now is a **regression** — fix before pushing.

## Results

| Date | Skill Version | Test 01 (Government) | Test 02 (Healthcare) | Notes |
|------|--------------|----------------------|----------------------|-------|
| 2026-07-09 | v1.1 | ⏳ Pending | ⏳ Pending | Baseline run pending — golden test set added to repository |

## Legend

- ✅ Pass — all criteria satisfied
- ❌ Fail — one or more criteria failed (list IDs in Notes)
- ⏳ Pending — not yet run against this version
