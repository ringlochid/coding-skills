# Worker / Queue Reference

## Ownership

- API enqueues work and returns user-facing status
- workers own retries, idempotence, side effects, and result updates
- scheduler/beat owns periodic trigger only
- broker/backend config must match across app and worker processes

## Failure checks

- task registered under the expected name
- queue routing matches worker subscriptions
- broker reachable from both producer and worker
- retries are bounded and observable
- ack/visibility timeout behavior matches task duration
- poison messages have a DLQ/quarantine or clear operator path
- side effects are idempotent; use idempotency keys/outbox where needed
- serialization format supports payload shape and schema versioning
- worker code is not stale after deploy

## Verification

- enqueue one representative task
- confirm it is consumed and result/side effect appears
- inspect retry/error logs for silent failures
