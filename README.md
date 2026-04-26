# Coding Skills Bundle

Karpathy-style coding, audit, QA, and engineering execution skills.

Public model:

- `coding-router` chooses the first lane.
- `bug-triage` reproduces and isolates failures.
- `coding-implementation` makes scoped edits after evidence exists.
- `engineering-fix-orchestrator` sequences evidenced multi-layer engineering fixes.
- review gates answer one question each: code, coverage, security, release, contract, migration.
- specialist leaves cover frontend code architecture, style systems, worker pipelines, query performance, browser repro, repro packs, and dev bootstrap.

Workflow lock:

- shared lifecycle lives in `coding-common/references/workflow-contract.md`
- edits use `coding-common/references/implementation-loop.md`
- helpers/subagents use `coding-common/references/coding-agent-handoff.md`
- heartbeat boundaries live in `coding-common/references/heartbeat-boundary.md`

Bundle boundary:

- in scope: code, tests, browser repro, contracts, migrations, workers, dev bootstrap, code-facing security review
- out of scope: PM roadmap, product/design ideation, org/product architecture strategy, law/compliance/marketing, broad security/legal/privacy policy

`coding-common/` is shared support only and intentionally has no `SKILL.md`.
