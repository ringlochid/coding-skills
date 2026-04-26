---
name: dev-bootstrap-repair
description: "Restore or bootstrap a local development environment when a repo will not start, dependencies are broken, services drifted, or smoke checks fail."
---

# Dev Bootstrap Repair

Use this to get a repo running without destructive resets.

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/coding-agent-handoff.md`
- `../coding-common/references/implementation-loop.md`
- `../coding-common/references/evidence-and-scope.md`
- `../coding-common/references/surgical-change-policy.md`
- `../coding-common/references/verification-gates.md`

Workflow:
1. Read repo setup docs and detect package/service tooling.
2. Reproduce the startup or smoke failure when safe; in checklist-only/no-edit/read-only mode, avoid commands with write side effects such as DB creation, Compose builds/up, service/container creation, cache writes, and persistent volume writes unless a disposable target is approved. In strict read-only mode, prefer static gates first: setup docs, tooling files, config validation, syntax parse, and the first blocked runtime gate.
3. Classify dependency, env, service, port, migration, cache, or build drift.
4. Apply the minimum reversible repair.
5. Re-run the smallest startup/smoke gate.

Output:
- failure class
- minimal repair applied or proposed
- proof run and result
- proof blocker / remaining dependency
- next safe action

Ask before deleting data, resetting DBs, changing global services, or installing privileged packages.
