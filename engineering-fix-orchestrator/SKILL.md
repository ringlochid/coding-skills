---
name: engineering-fix-orchestrator
description: "Coordinate multi-layer engineering issues or accepted design handoffs into implementation, verification, browser proof, and review sequences; not for PM/product roadmap planning."
---

# Engineering Fix Orchestrator

Use this after evidence exists and more than one engineering layer, verification phase, or accepted design-handoff implementation step must be coordinated.

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/routing-matrix.md`
- `../coding-common/references/coding-agent-handoff.md`
- `../coding-common/references/implementation-loop.md`
- `../coding-common/references/verification-gates.md`
- `../coding-common/references/orchestrator-workflows.md`

Workflow:
1. State the evidenced problem and affected layers.
2. Separate root-cause fixes from symptom patches.
3. Sequence dependencies: schema -> backend contract -> frontend/client -> worker/release checks when relevant.
4. Route each step to one focused skill or keep it local if simple.
5. Use bounded helpers only for separated read/review/implementation scopes.
6. Verify each layer and then run one end-to-end proof gate.


## Orchestrator WBS exposure

For broad coding work, use `../coding-common/references/orchestrator-workflows.md` as the WBS reference. This skill sequences affected layers and gates; `work-orchestrator` owns package splitting, subagents, dependencies, and final synthesis. Do not make one helper own repro, implementation, review, and release confidence at once.

Output:
- engineering sequence
- focused skill or owner for each step
- verification gates
- proof collected
- residual risk / blocker
- if proof cannot run: exact dependency/environment blocker and smallest setup command, without installing unless authorized

Boundary: do not turn engineering sequencing into product roadmap, design direction, legal review, or marketing planning.
