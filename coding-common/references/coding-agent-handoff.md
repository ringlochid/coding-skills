# Coding Agent Handoff

Use this when a subagent, Codex/ACP-style coding agent, or other implementation helper is genuinely useful.

## Default

Stay local for small edits, narrow reviews, and owner-critical decisions.

## Use a helper for

- independent second-pass review before high-risk acceptance
- broad read-only exploration while the parent preserves direction
- isolated implementation with clear files, success gate, and no overlapping write scope
- repetitive mechanical edits that are easy to verify

## Handoff contract

Provide:

- task goal
- exact scope and non-goals
- allowed paths/files
- verification gate to run
- output shape: changed files, proof, residual risks, blockers

## Parent responsibilities

- integrate or reject helper output
- resolve conflicts
- run or inspect final verification
- write the user-facing summary

Helpers do not commit, push, deploy, delete, or perform external writes unless explicitly authorized.


Irreversible or external actions require explicit user approval for that action in the handoff; prefer the parent performs irreversible/external writes after reviewing helper output.
