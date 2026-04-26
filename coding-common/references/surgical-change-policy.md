# Surgical Change Policy

Use for any skill that edits files.

## Allowed by default

- local read-only inspection
- targeted local edits inside the requested repo/scope
- formatting/lint cleanup caused by the change
- targeted tests or builds for the touched layer

## Ask first

- destructive commands or data resets
- public pushes, PR creation, deploys, external writes
- secret/env inspection
- broad rewrites not implied by the request

## Edit discipline

- Keep the diff focused.
- Preserve existing APIs unless the task is explicitly an API change.
- Do not combine behavior changes with unrelated formatting churn.
- Prefer one small fix over a general framework.
