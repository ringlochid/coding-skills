# Workflow Contract

This is the mandatory spine for every coding-bundle skill.

## Lifecycle

1. Route to one first lane unless the user explicitly asks for parallel outputs.
2. Establish scope: repo/path/diff/command/symptom/target.
3. Gather the smallest evidence that changes the answer.
4. Reproduce, inspect, or review before proposing code changes unless the task is already scoped.
5. Choose the next lane: triage, implementation, review gate, handoff pack, or blocked.
6. If editing, use `implementation-loop.md`.
7. If delegating, use `coding-agent-handoff.md`.
8. Finish with proof: command/test/build/screenshot/log/diff, or state why proof could not run.

## Stop conditions

Stop and ask or mark blocked when:

- scope is missing and guessing would change files, safety, or external state
- required credentials/secrets/accounts are needed
- the next step is destructive, public, or externally visible
- the verification gate cannot be run and no equivalent proof exists

## Boundaries

- Coding bundle owns engineering execution: code, bugs, tests, contracts, migrations, workers, browser repro, dev bootstrap, and code-facing security review.
- Product/design/PM/legal/marketing/business-risk work belongs in other bundle families.
- Heartbeats do not start or resume coding workflows; see `heartbeat-boundary.md`.
