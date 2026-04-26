---
name: performance-query-review
description: "Review database query and ORM performance risks including N+1, query shape, indexes, pagination, loading strategy, and EXPLAIN candidates."
---

# Performance Query Review

Answer: what query/ORM changes or evidence would reduce the bottleneck?

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/framework-python-backend.md`
- `../coding-common/references/evidence-and-scope.md`
- `../coding-common/references/review-gates.md`

Workflow:
1. Identify endpoint/job/query path and observed slowness if available. If no DB/ORM/query surface exists, return `not applicable / no query path found` with evidence checked, then stop or route to the appropriate skill.
2. Inspect ORM loading, joins, filters, pagination, indexes, and schema/model/migration definitions.
3. Flag N+1 and broad scans with evidence.
4. Prefer query-count/cardinality proof for suspected N+1 before jumping to EXPLAIN.
5. Recommend EXPLAIN/EXPLAIN ANALYZE only when it will answer a real question.
6. Avoid speculative indexes without workload evidence.

Output:
- query path reviewed
- evidence-backed bottleneck/risk
- proof checked
- missing proof
- smallest measurement or fix
