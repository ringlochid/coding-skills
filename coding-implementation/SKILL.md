---
name: coding-implementation
description: "Implement or refactor scoped code changes with minimal diffs and verification. Use only after the goal, affected layer, and success criteria are clear."
---

# Coding Implementation

Use this for scoped edits, not first-pass diagnosis.

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/coding-agent-handoff.md`
- `../coding-common/references/implementation-loop.md`
- `../coding-common/references/karpathy-coding-rules.md`
- `../coding-common/references/surgical-change-policy.md`
- `../coding-common/references/verification-gates.md`

Then read only relevant framework refs:
- Python/backend -> `framework-python-backend.md`
- React/frontend -> `framework-react-frontend.md`
- contracts -> `framework-contracts.md`
- migrations -> `framework-db-migrations.md`
- workers -> `framework-worker-queues.md`

Workflow:
1. Restate the goal and success gate briefly.
2. Inspect the owning code path and nearest tests.
3. Make the smallest change that solves the root cause.
4. Clean up only stale artifacts caused by this change.
5. Run the smallest meaningful verification gate.

Block when scope, repo path, required evidence, or approval boundary is missing.

Output:
- changed files
- why the change is minimal
- intended proof gate
- proof run and result
- proof blocker / residual risk
