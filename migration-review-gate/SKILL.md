---
name: migration-review-gate
description: "Review database migrations and schema changes for safety, deploy compatibility, lock risk, rollback, and model/schema drift."
---

# Migration Review Gate

Answer: is this schema change safe to apply?

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/framework-db-migrations.md`
- `../coding-common/references/review-gates.md`

Workflow:
1. Compare migration to model/schema intent.
2. Classify destructive ops, lock risk, nullability/backfill risk, and downgrade realism.
3. Check rolling deploy compatibility.
4. Recommend expand/contract or staged migration when needed.
5. Do not run destructive DB operations without approval.

Output:
- migration/schema scope
- safety findings
- proof checked
- missing proof
- rollback/compatibility risk
- smallest safe next action
