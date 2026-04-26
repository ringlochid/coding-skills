# Python Backend Reference

Use repo-local conventions first. When the repo is loose, default to these patterns.

## Ownership

- routes/controllers: HTTP transport, auth dependencies, status codes
- services: business rules and orchestration
- repositories/query helpers: persistence and query shape
- schemas/DTOs: validation and serialization
- tasks/workers: async/background behavior only

## FastAPI / Pydantic / SQLAlchemy

- keep FastAPI routes thin
- use explicit dependencies for auth/permissions
- prefer Pydantic v2 style where the repo already uses it
- Pydantic v2 cues: `model_validate`, `model_dump`, `field_validator`, `model_config`, `from_attributes`
- prefer SQLAlchemy 2 style: `select`, `session.execute`, `scalars`
- keep transaction/session ownership explicit; do not mix async and sync DB paths casually
- do not hide DB writes inside validators or serializers

## Verification

- targeted pytest for changed services/routes
- request replay for endpoint bugs
- type/lint gates when configured
