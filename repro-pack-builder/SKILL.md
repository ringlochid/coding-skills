---
name: repro-pack-builder
description: "Create a concise reproduction handoff pack for bugs that are hard to communicate or need another engineer to fix/retest. Not for first-pass diagnosis unless packaging is the task."
---

# Repro Pack Builder

Use this when communication quality is the problem.

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/coding-agent-handoff.md`
- `../coding-common/references/evidence-and-scope.md`
- `../coding-common/references/output-shapes.md`

Workflow:
1. Normalize environment, starting state, steps, expected, and actual behavior.
2. Attach or link screenshots, logs, console/network evidence, request/response samples, and commit/version info. If referenced artifacts are placeholder or absent, list them as missing proof, not evidence.
3. State what is confirmed vs inferred.
4. Add verification criteria for the eventual fix.
5. Keep it short enough another engineer can run it.

Output:
- environment
- steps
- expected vs actual
- redacted evidence
- verification criteria
- missing proof / unknowns

Safety: Redact secrets, auth/session material, and unnecessary PII from browser evidence, logs, screenshots, and handoff packs.
