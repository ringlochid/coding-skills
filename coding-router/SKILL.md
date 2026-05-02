---
name: coding-router
description: "Route coding, bug, review, QA, security, release, and repro requests to the right first coding skill. Use when several adjacent coding skills could apply and a thin first-pass decision is needed."
---

# Coding Router

Use this as the thin front door for coding-related requests. Choose the first lane; do not perform deep work here.

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/routing-matrix.md`
- `../coding-common/references/karpathy-coding-rules.md`
- `../coding-common/references/orchestrator-workflows.md`

Workflow:
1. Identify the user's real first need: reproduce, orchestrate, implement, review, test, security, release, contract, migration, or handoff.
2. Route to exactly one first skill unless the user explicitly asks for parallel outputs.
3. For broad multi-layer work, accepted design-handoff implementation, or scoped work that needs implementation plus browser QA/review gates, route to `engineering-fix-orchestrator` as the WBS phase playbook. If evidence/root cause is unclear, route first to `bug-triage` or `browser-repro-triage`.
4. If scope is already obvious, skip this router and use the focused skill directly.

Tie-breaks:
- browser evidence before backend speculation
- repro before implementation
- migration/security/release gates before merge/deploy confidence
- implementation only after scope/root cause is clear

Output:
- selected skill
- one-sentence reason
- evidence/scope used for routing
- missing input if routing is blocked
