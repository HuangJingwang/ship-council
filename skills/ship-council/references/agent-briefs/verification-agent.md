# Verification Agent Brief

## Mission

Run real verification commands and record evidence.

## Inputs

- `environment-report.md`
- `test-plan.md`
- `contract.md`
- changed files or diff

## Rules

- Do not claim success without command output.
- Do not print secrets.
- If credentials or services are missing, record the blocker exactly.
- If a command fails, capture the important output and stop or continue only when later checks are independent.

## Output

Write `verification-report.md`:

```text
commands
cwd
exit_status
important_output
result
manual_gaps
```
