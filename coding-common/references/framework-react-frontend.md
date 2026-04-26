# React Frontend Reference

Use repo-local conventions first. When loose, default to these patterns.

## Ownership

- routes/pages own screen-level flow
- components render and handle local interaction
- hooks own reusable side effects or data access
- API clients own transport and response parsing
- state stores/context own shared state, not ephemeral leaf UI

## React / TypeScript

- use a router for real multi-screen products
- use `useReducer` when local transitions become dense
- avoid speculative memoization
- keep render pure; no side effects during render
- keep hook dependencies honest instead of suppressing lint by default
- avoid `any` on API response shapes
- keep loading/error/empty states explicit
- use typed data-fetching boundaries and error boundaries where the app pattern supports them
- preserve accessibility: focus, keyboard, labels, and semantic controls

## Tailwind / style

- in Tailwind v4 repos, prefer CSS-first `@theme` for tokens and `@utility` for repeated patterns
- keep one-off layout utilities local
- extract only when repetition or ownership pressure exists

## Verification

- typecheck/build for changed components/routes
- interaction/browser check for UX behavior
- screenshot/reference check when visual fidelity is the requirement
