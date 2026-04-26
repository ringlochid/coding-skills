# Implementation Loop

Use this whenever a skill makes or directs code changes.

## Loop

1. Name the goal and smallest verification gate.
2. Capture baseline proof when practical: failing test, repro, current metric, screenshot, or source evidence.
3. Inspect the owning code path and nearest tests.
4. Make the smallest diff that addresses the evidenced cause.
5. Inspect the diff for scope creep, stale imports, formatting churn, and unintended API changes.
6. Run the verification gate.
7. If it fails, use the failure as new evidence and repeat with a smaller hypothesis.
8. Keep the change only when proof improves or the requested behavior is verified; otherwise revert or report the blocker.

## Rules

- Do not broaden the fix just because adjacent code looks imperfect.
- Do not claim done without proof or an explicit proof blocker.
- Do not hide backend/contract failures with frontend-only patches.
- Do not combine unrelated cleanup with behavior changes.
- Prefer delete/simplify when it preserves or improves proof.
