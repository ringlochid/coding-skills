---
name: code-review-gate
description: "Review a diff or PR for correctness, regression risk, maintainability, and merge readiness. Use for code review only; not for implementing fixes unless separately requested."
---

# Code Review Gate

Answer: should this diff change before merge?

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/coding-agent-handoff.md`
- `../coding-common/references/evidence-and-scope.md`
- `../coding-common/references/review-gates.md`
- `../coding-common/references/output-shapes.md`

Workflow:
1. Identify the exact diff or file scope. If no reviewable diff/PR/commit range/file scope is available, do not perform a whole-repo review as a substitute; return `block` with the missing scope and smallest acceptable input: PR URL, `git diff`, commit range, or paths.
2. Map changed behavior and touched layers.
3. Review correctness, regression risk, tests, contracts, migrations, security, and release impact only as relevant.
4. Prioritize confirmed issues over style preferences.
5. Report missing evidence explicitly.

Use subagents only for large/high-risk diffs; read `subagent-policy.md` first.

Output:
- verdict
- scope reviewed
- evidence-backed findings
- proof checked
- missing proof
- smallest next action
