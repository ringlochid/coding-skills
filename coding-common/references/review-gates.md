# Review Gates

A gate answers whether the work is good enough for the next step. It does not implement fixes by default.

## Verdicts

- `pass`: adequate evidence, no blocking issue
- `pass with notes`: acceptable with non-blocking follow-up
- `changes requested`: fix before merge/acceptance
- `block`: serious correctness, security, data, deploy, or evidence failure

## Gate rules

- no findings without evidence
- no pass without scope
- severity must reflect exploitability/risk in this repo, not generic fear
- missing critical evidence is itself a finding
- recommend the smallest next action
