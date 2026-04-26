# Verification Gates

Pick the smallest gate that proves the changed behavior.

Every implementation or review result must name:

- the intended proof gate
- the proof actually run
- the result, with command/test/screenshot/log/diff when available
- any proof blocker

## Repo-native command selection

Prefer commands already declared by the repo:

- package manager lockfile/scripts: `pnpm`, `npm`, `yarn`, or `bun`
- Python config: `pyproject.toml`, `pytest.ini`, `tox.ini`, `noxfile.py`
- CI workflows: `.github/workflows`, `gitlab-ci.yml`, `justfile`, `Makefile`
- frontend tools: Vite/Vitest, Playwright, ESLint, Biome, Prettier, TypeScript
- Python tools: pytest, Ruff, mypy, pyright

Do not invent a heavyweight full-suite command when a targeted repo-native gate exists.
If a declared repo-native gate is structurally unavailable or misconfigured, run the smallest safe secondary check if possible, then report the original gate blocker explicitly.

## Generic gates

- syntax/typecheck for touched language
- targeted unit/integration test for the changed path
- lint/format when the repo uses it as a safety gate
- build/compile when interface or frontend code changed
- manual/browser repro when the symptom is browser-visible
- diff inspection for unintended scope/API changes

## Backend

- route/service test for success and failure path
- request replay when the bug is request-specific
- migration dry check or schema diff when schema changes

## Frontend

- TypeScript/build for changed components/routes
- interaction/browser check for changed UX
- screenshot/reference comparison when visual parity matters
- console/network check when browser behavior changed

## Security/release

- evidence is acceptable only if it covers the actual threat/deploy path
- narrative confidence is not a gate
- missing proof is a finding, not a pass


## Target safety

Default browser checks, request replay, and mutation tests to local/dev targets.
Ask before using staging/prod, logged-in user sessions, authenticated mutations, external writes, or non-disposable data.
