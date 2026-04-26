# Subagent Policy

Use subagents only when separation gives real value.

Default: stay local for small edits, narrow reviews, and owner-critical decisions.

Use one bounded subagent for:

- independent second-pass review before a high-risk conclusion
- broad read-only exploration while the parent keeps ownership
- isolated implementation when scope, paths, and verification are clear
- mechanical multi-file edits that are easy to verify

Rules:

- give explicit goal, scope, non-goals, paths, budget, and output shape
- avoid parallel agents on overlapping write scopes
- subagents do not commit, push, deploy, delete, or change external state
- parent owns synthesis, final edits, final verification, and user summary
- if a helper returns unverified output, treat it as a draft, not proof

For detailed handoff wording, read `coding-agent-handoff.md`.


Irreversible or external actions require explicit user approval for that action in the handoff; prefer the parent performs irreversible/external writes after reviewing helper output.
