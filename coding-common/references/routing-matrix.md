# Routing Matrix

Use this to choose the first lane, not the entire workflow.

| Signal | First lane |
|---|---|
| unclear bug or failing test | `bug-triage` |
| browser-visible symptom, console/network evidence needed | `browser-repro-triage` |
| scoped coding task with known files/root cause | `coding-implementation` |
| multi-layer engineering issue with evidenced impacted layers | `engineering-fix-orchestrator` |
| PR/diff correctness/regression review | `code-review-gate` |
| missing or weak tests | `coverage-review-gate` |
| static app security review | `security-review-gate` |
| explicit authorized adversarial probe | `security-attacker-validation` |
| deploy/rollback readiness | `release-risk-gate` |
| frontend/backend API shape drift | `contract-review-gate` |
| migration/schema safety | `migration-review-gate` |
| frontend code architecture | `frontend-architecture-review` |
| Tailwind/CSS implementation consistency | `style-system-review` |
| queue/task/scheduler failure | `worker-pipeline-triage` |
| query/ORM/index performance | `performance-query-review` |
| clean handoff artifact for another engineer | `repro-pack-builder` |
| local setup will not start | `dev-bootstrap-repair` |

Tie-breaks:

- repro before implementation
- browser evidence before backend speculation for browser-visible failures, even when a migration is mentioned, unless the request is explicitly deploy/migration safety
- security/migration/release gates before acceptance confidence
- implementation only after scope/root cause is clear
- product/design/PM/legal/marketing strategy routes out of this bundle
