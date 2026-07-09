# Verification Policy

Verification is evidence, not confidence.

## Required Behavior

Before claiming completion, run the commands that prove the claim or explain exactly why they cannot run.

Verification may include:

- unit tests;
- integration tests;
- backend startup;
- frontend/mobile build;
- lint/typecheck;
- database migration dry run;
- API smoke test;
- browser or device E2E;
- security scanner when configured.

Select commands and manual checks using the relevant surface checklist in `surface-playbooks.md`.

## Report Format

Record:

```text
command
cwd
environment notes
exit status
important output
result
```

If a command fails, do not continue to `DONE`. Create a fix packet or mark `BLOCKED` with the exact blocker.

## Partial Verification

Partial verification is allowed only when explicit. The final report must say what was not verified and why.
