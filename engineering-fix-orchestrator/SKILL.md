---
name: engineering-fix-orchestrator
description: "Coordinate a multi-layer engineering issue from evidenced bug/feature request to implementation sequence and verification. Use when backend, frontend, contracts, migrations, workers, or release concerns must be sequenced; not for PM/product roadmap planning."
---

# Engineering Fix Orchestrator

Use this after evidence exists and more than one engineering layer may need coordinated changes.

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/routing-matrix.md`
- `../coding-common/references/coding-agent-handoff.md`
- `../coding-common/references/implementation-loop.md`
- `../coding-common/references/verification-gates.md`

Workflow:
1. State the evidenced problem and affected layers.
2. Separate root-cause fixes from symptom patches.
3. Sequence dependencies: schema -> backend contract -> frontend/client -> worker/release checks when relevant.
4. Route each step to one focused skill or keep it local if simple.
5. Use bounded helpers only for separated read/review/implementation scopes.
6. Verify each layer and then run one end-to-end proof gate.

Output:
- engineering sequence
- focused skill or owner for each step
- verification gates
- proof collected
- residual risk / blocker
- if proof cannot run: exact dependency/environment blocker and smallest setup command, without installing unless authorized

Boundary: do not turn engineering sequencing into product roadmap, design direction, legal review, or marketing planning.
