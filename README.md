# Coding Skills Bundle

Coding Skills is an OpenClaw skill bundle for evidence-led engineering work: triage first, scoped edits second, and verification before handoff.

It is designed for real software maintenance: bugs, tests, frontend architecture, contracts, migrations, worker pipelines, browser repros, security review, release readiness, and focused implementation.

## What it can do

- Route coding requests to the smallest useful first skill.
- Reproduce and isolate bugs before changing code.
- Implement scoped fixes with minimal diffs and explicit verification.
- Review diffs, contracts, security posture, migrations, release risk, and test coverage.
- Package hard-to-share bugs into concise repro handoffs.
- Diagnose local dev bootstraps, browser-visible failures, workers, queues, and performance issues.

## Core workflow

```text
request
  → route
  → gather evidence
  → isolate the change or risk
  → edit or review
  → run the smallest meaningful verification
  → hand off result, blocker, or next action
```

The bundle is intentionally not “just write code.” It tries to avoid the expensive failure mode where an agent patches symptoms before it understands the system.

## Skills map

| Need | Skill |
|---|---|
| Choose the first coding lane | `coding-router` |
| Reproduce/root-cause a bug | `bug-triage` |
| Make a scoped code change | `coding-implementation` |
| Sequence multi-layer fixes | `engineering-fix-orchestrator` |
| Browser UI/console/network repro | `browser-repro-triage` |
| Hard-to-share reproduction pack | `repro-pack-builder` |
| Local environment will not start | `dev-bootstrap-repair` |
| Diff or PR review | `code-review-gate` |
| Missing/weak tests | `coverage-review-gate` |
| Auth/session/access-control/static security review | `security-review-gate` |
| Authorized attacker-style validation | `security-attacker-validation` |
| Deploy/release/rollback readiness | `release-risk-gate` |
| API/schema/frontend-backend drift | `contract-review-gate` |
| Database migration safety | `migration-review-gate` |
| React/TypeScript architecture | `frontend-architecture-review` |
| Tailwind/CSS/style-system drift | `style-system-review` |
| Query/ORM/index/pagination performance | `performance-query-review` |
| Queues, workers, schedulers, async pipelines | `worker-pipeline-triage` |

`coding-common/` contains the shared workflow contract, implementation loop, handoff rules, and runtime references. It is not an installable skill.

## Design philosophy

- **Evidence beats confidence.** Repro logs, tests, screenshots, diffs, and tool output matter more than narrative certainty.
- **Small diffs are safer.** The default implementation path is narrow, reversible, and verified.
- **One gate, one question.** Review skills answer specific readiness questions instead of becoming generic audits.
- **Boundaries are explicit.** Product strategy, design ideation, legal/compliance, marketing, and broad policy work live outside this bundle.
- **Verification is part of the work.** A fix without an appropriate test, build, lint, smoke, screenshot, or named blocker is incomplete.

## Example requests

- “This test started failing after the auth refactor; find the root cause before patching.”
- “Review this PR for contract drift and migration risk.”
- “The page is blank in browser but tests pass; capture console/network evidence.”
- “Implement the smallest fix and run the relevant verification.”

## Validation

Run from the bundle root:

```bash
python3 coding-common/scripts/validate_coding_bundle.py
```

Expected shape: 18 public skills plus `coding-common/` shared support.

## Installation notes

Copy the public skill directories plus `coding-common/` into the active OpenClaw skills path. Do not vendor project repos, build artifacts, node modules, virtualenvs, generated repro folders, or scratch logs into the skill bundle.
