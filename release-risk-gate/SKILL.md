---
name: release-risk-gate
description: "Assess deploy, launch, rollback, migration, config, worker, and smoke-test readiness. Use when a release or production/staging deploy decision is in scope."
---

# Release Risk Gate

Answer: is this deploy safe enough, and what is rollback?

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/evidence-and-scope.md`
- `../coding-common/references/verification-gates.md`
- `../coding-common/references/review-gates.md`

Workflow:
1. Identify target environment and deploy surface.
2. Check migrations, config/env, contracts, workers, build artifacts, runtime image/dependency support, tests, readiness/health checks, and smoke paths as relevant.
3. Identify rollback path and irreversible steps.
4. Classify go / go with watchpoints / hold / block.
5. Do not deploy or push without explicit approval.

Output:
- verdict: go / go with watchpoints / hold / block
- release surface reviewed
- proof checked
- missing proof
- rollback/watchpoint risk
- smallest safe next action
