---
name: security-attacker-validation
description: "Perform explicitly authorized, minimal-impact attacker-style validation against in-scope local/staging/test targets. Use only when adversarial probing is clearly authorized."
---

# Security Attacker Validation

Use only with explicit authorization and exact in-scope targets.

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/security-boundaries.md`
- `../coding-common/references/karpathy-coding-rules.md`

Workflow:
1. Confirm target, scope, allowed techniques, and stop conditions. If the prompt already gives explicit local-only authorization, proceed while restating that scope.
2. Choose the narrowest hypothesis that proves or disproves real risk.
3. Use minimal-impact probes only.
4. Stop once proof is strong enough.
5. Report proof, limits, and residual uncertainty.

Block immediately when target or permission is ambiguous.

Output:
- authorized target/scope
- hypothesis tested
- proof collected
- limits / missing proof
- residual risk
