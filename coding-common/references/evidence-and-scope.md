# Evidence and Scope

## Scope first

Collect the smallest scope that can answer the request:

- explicit paths/files/PR/diff from the user
- changed files from git when the user asks about current work
- nearest failing test, route, component, job, migration, or endpoint
- runtime evidence only when it changes the answer

If no scope is clear, ask for one concise missing input.

## Evidence ladder

Prefer direct evidence in this order:

1. code and tests in the repo
2. failing command output, logs, stack traces, browser console/network evidence
3. schema/contracts/config/deploy files
4. official docs or advisories when version behavior matters
5. user report, explicitly marked as unverified until reproduced

## Do not over-collect

Do not scan the whole repo when a narrow diff answers the question. Do not run broad test suites when a targeted gate gives enough signal.


## Evidence safety

Before output, handoff, screenshots, logs, request/response samples, or repro packs, redact:

- cookies and session IDs
- auth headers and bearer tokens
- API keys, passwords, secrets, and `.env` values
- private keys and credential file contents
- unnecessary PII or user data

Report secret locations by path/key/header name only; never print raw values.
