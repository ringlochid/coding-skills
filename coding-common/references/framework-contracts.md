# Frontend / Backend Contract Reference

## Contract surfaces

- route path and method
- request body, query params, path params
- response model and status codes
- auth/session/cookie behavior
- enum values, nullability, pagination shape
- generated OpenAPI or generated TypeScript types

## Drift checks

- frontend sends the shape backend validates
- backend returns the shape frontend renders
- optional/nullable fields mean the same thing on both sides
- auth transport matches: cookie, bearer token, API key, etc.
- CORS and credentials settings match the chosen auth model

## Verification

- schema diff when available
- request replay for failing endpoint
- frontend type/build check when client types changed
