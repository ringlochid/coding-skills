---
name: contract-review-gate
description: "Review frontend/backend contract drift across API schema, request/response shapes, auth/session transport, CORS, enums, nullability, and generated types."
---

# Contract Review Gate

Answer: do client and server still agree?

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/framework-contracts.md`
- `../coding-common/references/evidence-and-scope.md`
- `../coding-common/references/review-gates.md`

Workflow:
1. Locate the contract source: OpenAPI/schema/types/client calls/routes and the route handler that applies it. Check generated artifact freshness: schema input exists, generation command is declared, and generated client/types are current; if proof cannot run, mark missing proof.
2. Compare frontend sends vs backend validates.
3. Compare backend returns vs frontend renders.
4. Check auth/session/CORS transport agreement.
5. Recommend the smallest side to change, or a staged compatibility path.

Output:
- verdict: pass / pass with notes / changes requested / block
- contract surface reviewed
- evidence of match/drift
- proof checked
- missing proof
- smallest compatible fix
