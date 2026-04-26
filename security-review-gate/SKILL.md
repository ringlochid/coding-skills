---
name: security-review-gate
description: "Run evidence-led static security review for application code/config. Use for auth, session, access control, secrets, validation, API exposure, and dependency-risk review; not for unauthorized probing."
---

# Security Review Gate

Answer: what security risks does the evidence support?

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/security-boundaries.md`
- `../coding-common/references/evidence-and-scope.md`
- `../coding-common/references/review-gates.md`

Workflow:
1. Confirm scope: app, PR, route, config, or release surface.
2. Map auth/session, access control, validation, secrets, API exposure, dependency surfaces, and auth-sensitive abuse controls that are actually present. For login, signup, password reset/recovery, invite, MFA, and token refresh endpoints, explicitly record abuse-control evidence: rate limit, CAPTCHA/step-up, lockout, email throttling, or `missing`.
3. Report only evidence-backed findings.
4. Do not print secret values.
5. Separate confirmed findings from unassessed areas.

Output:
- scope reviewed
- confirmed findings
- proof checked
- missing proof / unassessed areas
- smallest safe fix

Route to `security-attacker-validation` only when adversarial testing is explicitly authorized.
