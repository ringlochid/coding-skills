---
name: worker-pipeline-triage
description: "Diagnose background worker, queue, scheduler, broker, retry, and async pipeline failures. Use when jobs do not run, drain, retry, schedule, or publish results correctly."
---

# Worker Pipeline Triage

Answer: where is the async pipeline broken?

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/framework-worker-queues.md`
- `../coding-common/references/evidence-and-scope.md`
- `../coding-common/references/output-shapes.md`

Workflow:
1. Confirm producer, broker, worker, queue, result path, and scheduler/beat when present.
2. Inspect registration/routing/config before changing code.
3. Check retries, idempotence, serialization, and stale worker code.
4. Verify with one representative task when possible.
5. Route to implementation only after the broken segment is clear.

For no-symptom audits, do not invent a broken segment. Return `no broken segment observed from current evidence` and list missing runtime proof.

Output:
- pipeline segment reviewed
- broken segment or strongest hypothesis
- evidence
- proof checked
- missing proof
- smallest next action
