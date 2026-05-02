# Coding Orchestrator Workflows

Use this WBS reference for broad coding work. Do not use it when one focused leaf skill plus one proof gate can satisfy the request. Coding conductors expose sequence and gates; parent/work orchestrator owns packages, dependencies, final synthesis, and install/deploy decisions.

Gate proof rule: each gate names intended check, artifact/command inspected, pass/degraded/blocked result, and blocker if proof could not run. Narrative confidence is not a gate.

## Browser-visible bug to fix

WBS phases: `repro -> root_cause -> fix_sequence -> implementation -> verification -> risk_review`.

Packages:
- `bug-repro`: `browser-repro-triage` or `bug-triage`; gate: exact failing evidence or blocker.
- `bug-root-cause`: owner layer/path; gate: scope clear enough for one implementation package.
- `bug-fix`: `coding-implementation`; gate: minimal diff plus local proof.
- `bug-proof`: repo-native test/build/browser proof; gate: failing evidence becomes passing evidence.
- `bug-risk-review`: coverage/security/release gate when warranted.

Parallelism: repro/root cause are serial unless symptoms are independent; read-only reviews can run after diff/artifact.

Degraded complete output: root-cause report or minimal diff plus proof blocker, residual risk, and next command.

## Design handoff to React implementation

WBS phases: `handoff_read -> architecture_scope -> implementation -> browser_qa -> review`.

Packages:
- `fe-handoff-read`: inspect handoff and repo; gate: owner paths and success criteria.
- `fe-architecture`: `frontend-architecture-review`; gate: implementation plan or blocker.
- `fe-implementation`: `coding-implementation`; gate: build/test/lint proof or blocker.
- `fe-browser-proof`: browser evidence; gate: screenshot/console proof.
- `fe-review`: style/coverage/code review; gate: pass/degraded/blocked verdict.

Parallelism: architecture review can run before implementation if source/handoff is stable; browser QA waits for implementation.

Degraded complete output: minimal diff or implementation plan plus proof blocker, residual risk, and next verification command.

## Contract drift across backend/frontend

WBS phases: `contract_evidence -> backend_or_schema_fix -> frontend_client_fix -> verification -> review`.

Packages:
- `contract-evidence`: `contract-review-gate`; gate: concrete schema/API/type mismatch.
- `contract-backend`: backend/schema owner change; gate: backend test or blocker.
- `contract-frontend`: client/UI usage update; gate: typecheck/browser proof or blocker.
- `contract-review`: final contract/code review.

Gate: no frontend guesswork before contract owner is identified.

Degraded complete output: contract drift report with owner path, failing evidence, and next fix package.

## Migration/backend/frontend coordinated change

WBS phases: `migration_review -> backend_contract -> frontend_update -> worker_release -> e2e_proof`.

Packages:
- `migration-review`: `migration-review-gate`; gate: deploy/rollback/lock verdict.
- `backend-contract`: backend/API change; gate: tests or blocker.
- `frontend-update`: client/UI change; gate: typecheck/browser proof.
- `worker-release`: worker/release gates if relevant.
- `integrated-proof`: one E2E proof or named blocker.

Gate: migration/release risk must be explicit before deploy confidence.

Degraded complete output: deploy-blocking risk report plus safest next verification package.

## Review-only coding work

WBS phases: `scope_evidence -> focused_review_gate -> verdict -> optional_repair_package`.

Packages: route to `code-review-gate`, `frontend-architecture-review`, `coverage-review-gate`, `security-review-gate`, `release-risk-gate`, or another focused review gate.

Gate: inspected diff/files/artifacts plus verdict and residual risk. Mutation requires a separate explicit package.

Degraded complete output: review blocker naming missing diff/files/tests.

## Coding handoff package

WBS phases: `scope -> evidence -> package -> proof_blockers -> next_owner`.

Packages: use `repro-pack-builder` or `coding-agent-handoff` guidance.

Gate: exact paths, commands, expected output, blocker/risk, and next owner are present.

Degraded complete output: partial handoff with missing evidence explicitly named.
