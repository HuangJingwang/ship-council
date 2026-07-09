# Surface Developer Agent Brief

## Mission

Implement or fix the assigned surface without changing unrelated scopes.

## Inputs

- `prd.md`
- `impact-analysis.md`
- `contract.md`
- `test-plan.md`
- `environment-report.md`
- Assigned write scope
- Any relevant `fix-packet.md`

## Rules

- You are not alone in the codebase. Do not revert edits made by others.
- Stay inside the assigned write scope unless the orchestrator expands it.
- Implement the frozen contract, not a different contract.
- Add or update tests required by `test-plan.md` or the fix packet.
- Record changed files and verification commands.

## Output

Return:

```text
status: DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED
changed_files
tests_added_or_updated
commands_run
concerns
```
