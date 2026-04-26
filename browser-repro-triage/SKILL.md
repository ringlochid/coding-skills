---
name: browser-repro-triage
description: "Reproduce and triage browser-visible bugs using UI, console, network, screenshot, and local app evidence. Use for blank screens, broken clicks, visual glitches, or auth/session behavior seen in-browser."
---

# Browser Repro Triage

Use this when the browser is the truth surface.

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/evidence-and-scope.md`
- `../coding-common/references/framework-react-frontend.md`
- `../coding-common/references/framework-contracts.md`

Workflow:
1. Open the app path and reproduce the symptom.
2. Capture screenshot, console errors, network request/response, and route/state clues.
3. Classify likely owner: UI code, client state, API contract, auth/session, backend, config/deploy.
4. Avoid patching UI to hide backend or contract failures.
5. Define the proof needed for a fix.
6. If a live browser/server is unavailable, collect static runtime-error evidence with file/line refs, state missing browser proof, and do not install dependencies unless authorized.

Output:
- repro status
- evidence collected
- likely owner lane
- next focused skill or fix gate
- proof checked / missing proof

Safety: Redact secrets, auth/session material, and unnecessary PII from browser evidence, logs, screenshots, and handoff packs.
