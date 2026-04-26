---
name: frontend-architecture-review
description: "Review React/TypeScript frontend architecture for routing, component boundaries, state ownership, data fetching, TypeScript strictness, and maintainability."
---

# Frontend Architecture Review

Answer: is the frontend structure healthy enough for the current product shape?

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/framework-react-frontend.md`
- `../coding-common/references/evidence-and-scope.md`
- `../coding-common/references/review-gates.md`

Workflow:
1. Map routes/pages, component boundaries, state ownership, and data fetching; inspect adjacent imported components/hooks/API clients when needed to validate boundaries. For frontend libraries/frameworks, map package/public API boundaries, example apps, provider/controller/rendering layers, and exported component contracts before app pages/routes.
2. Look for real friction: giant components, manual page switches, prop drilling, dense state transitions, `any` on API shapes.
3. Prefer `useReducer` before heavier state escalation.
4. Do not flag style preference as architecture risk.
5. Output high/medium/low findings with concrete paths.

Output:
- scope reviewed
- evidence-backed architecture findings
- proof checked
- missing proof
- smallest improvement path
