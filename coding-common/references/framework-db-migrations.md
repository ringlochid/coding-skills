# DB Migration Reference

## Review concerns

- destructive operations
- table locks and rewrite risk
- adding NOT NULL columns without backfill/default strategy
- model/schema drift
- migration script imports/runtime validity, e.g. Alembic `op` import and revision metadata
- downgrade realism
- rolling deploy compatibility
- data migration idempotence

## Safe patterns

- expand/contract for incompatible changes
- nullable add + backfill + enforce later for large tables
- explicit indexes for new query paths
- Alembic autogenerate must be manually reviewed; it is a draft, not proof
- use batched backfills for large tables
- account for index/table locks; use concurrent/online patterns when supported
- reversible downgrade when realistic; document when not

## Verification

- inspect generated migration against model changes
- run targeted migration upgrade/downgrade locally when possible
- check app compatibility across old/new code during deploy windows


## Target safety

Run migration upgrade/downgrade checks only against disposable local databases by default.
Ask before touching staging/prod or any database with real data.
Never run destructive migration checks against live data.
