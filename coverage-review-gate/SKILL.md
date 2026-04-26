---
name: coverage-review-gate
description: "Identify the highest-leverage missing or weak tests for a change. Use when the question is whether coverage is adequate or what tests to add next."
---

# Coverage Review Gate

Answer: what minimum tests are missing?

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/evidence-and-scope.md`
- `../coding-common/references/verification-gates.md`
- `../coding-common/references/review-gates.md`

Workflow:
1. Map changed user/system behavior. If no diff/change is supplied, switch to baseline mode: inventory nearest tests and CI gates, but verdict must say `diff-specific coverage not assessable`.
2. Find nearest existing tests and fixtures.
3. Distinguish real coverage from superficial assertions.
4. Prioritize critical success, failure, auth, edge, async, route, and migration paths.
5. Recommend a short ordered list, not a giant matrix.
6. If tests cannot run, still inspect nearest tests and separate existing proof, missing proof, and proof blocker.

Output:
- behavior scope reviewed
- existing proof checked
- missing proof
- highest-leverage tests to add
- smallest next action

Verdict: adequate / thin / risky.
