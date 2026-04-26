---
name: style-system-review
description: "Review Tailwind/CSS/UI style-system consistency, token drift, utility sprawl, duplicated patterns, responsiveness, and polish debt."
---

# Style System Review

Answer: is the UI styling system coherent and maintainable?

Read first:
- `../coding-common/references/workflow-contract.md`
- `../coding-common/references/framework-react-frontend.md`
- `../coding-common/references/evidence-and-scope.md`
- `../coding-common/references/review-gates.md`

Workflow:
1. Identify the active style system first: Tailwind, CSS Modules, MUI/Emotion, styled-components, vanilla CSS, design tokens, or mixed; verify integration files/package dependencies before assuming utilities are active.
2. Check token use, repeated utility patterns, custom CSS ownership, responsiveness, and interaction states.
3. Keep one-off styling local; extract only repeated patterns.
4. Use screenshot/reference evidence when visual parity matters.
5. Report concrete cleanup targets, not aesthetic taste.

Output:
- style scope reviewed
- evidence-backed consistency findings
- proof checked
- missing proof
- smallest cleanup target
