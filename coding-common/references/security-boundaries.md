# Security Boundaries

## Static review

Use `security-review-gate` for evidence-led review of code/config. Report only what the available evidence supports.

## Code-facing review checklist

Check only surfaces present in scope:

- object/property authorization and role checks
- CSRF when cookie auth mutates server state
- XSS/output encoding and unsafe HTML sinks
- SSRF, file upload, path traversal, and unsafe fetch/proxy behavior
- rate limits and abuse controls on sensitive endpoints
- cookie flags, CORS/credentials, session expiry, and token storage
- dependency or supply-chain risk visible in the diff/config


## Attacker validation

Use `security-attacker-validation` only when the user or task explicitly authorizes adversarial testing and identifies the in-scope target.

Rules:

- no internet-wide or opportunistic targeting
- no persistence, destructive actions, credential harvesting, or bulk exfiltration
- prefer minimal-impact proof
- stop when scope is ambiguous

## Secrets

Do not print secret values. Report path and line/symbol only.
