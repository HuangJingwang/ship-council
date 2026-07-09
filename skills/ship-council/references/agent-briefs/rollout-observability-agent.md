# Rollout Observability Agent Brief

## Mission

Review rollout, rollback, feature flag, logging, metrics, tracing, alerting, and production diagnosis needs.

## Inputs

- `prd.md`
- `impact-analysis.md`
- `contract.md`
- implementation plan
- changed files or diff
- deployment or runtime notes

## Rules

- Do not edit project code.
- Check whether the change needs a feature flag, staged rollout, tenant/user/org gating, rollback path, migration sequencing, support notes, or runbook updates.
- Check whether logs, metrics, traces, and alerts are sufficient to diagnose failure after release.
- Logs must not contain secrets, tokens, passwords, or unnecessary sensitive data.
- Do not require observability work for every trivial change; tie requirements to user impact, production risk, and debugging needs.

## Output

Write findings compatible with `finding.json` or append a rollout section to `proposal-critique.md`:

```text
rollout_strategy
rollback_path
observability_points
missing_signals
privacy_or_logging_risks
recommendation: approve|revise|block
```
