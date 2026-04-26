---
name: bug-triage
description: "Reproduce, isolate, and root-cause a bug or failing build/test before implementation. Use for unclear failures; not for already-scoped edits or PR review."
---

# Bug Triage

Use this to turn a bug report into a repro, root cause, and smallest fix direction. Domain-specific specialists should not override this when the user asks for general failing-test triage unless they explicitly ask for that specialist lane.

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/karpathy-coding-rules.md`
- `../coding-common/references/evidence-and-scope.md`
- `../coding-common/references/output-shapes.md`

Workflow:
1. Capture expected vs actual behavior, environment, and reproduction steps. If invoked for repo smoke/evaluation with no symptom or failing command, output `blocked: no concrete symptom`, list nearest native gates, and do not infer a root cause.
2. Reproduce with the smallest command/browser path available.
3. Localize to one layer or file path before suggesting edits.
4. Confirm the root-cause hypothesis with evidence.
5. Define the verification gate for the eventual fix.

Route away when:
- browser tools are the main evidence surface -> `browser-repro-triage`
- root cause is known and edits are requested -> `coding-implementation`
- the goal is a handoff artifact -> `repro-pack-builder`

Output:
- symptom
- repro status
- root cause or strongest hypothesis
- evidence
- fix direction
- proof checked / missing proof
- blockers / unknowns
