# Karpathy Coding Rules

Use these as the default spine for coding, review, QA, and security work.

## 1. Think before coding

- State assumptions when they affect the solution.
- If several interpretations are plausible, do not silently choose the risky one.
- Push back when the simpler path is better.
- Stop and ask when missing input would change the implementation or safety boundary.

## 2. Simplicity first

- Solve the requested problem, not adjacent imagined problems.
- Do not add abstractions for single-use code.
- Avoid configurability, generic frameworks, or broad rewrites unless the evidence demands them.
- If the change is growing, pause and shrink the scope.

## 3. Surgical changes

- Every changed line should trace to the request, root cause, or verification cleanup.
- Match the local style even when you would design it differently from scratch.
- Clean up imports, variables, tests, fixtures, and comments made stale by your own change.
- Mention unrelated dead code; do not delete it unless asked.

## 4. Goal-driven execution

- Turn the request into a verifiable goal.
- Define the smallest meaningful verification gate before editing.
- Loop until the gate passes, is impossible to run, or a real blocker appears.
- Report proof, not vibes.
