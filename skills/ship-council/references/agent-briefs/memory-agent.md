# Memory Agent Brief

## Mission

Capture reusable project constraints, verification recipes, decisions, and lessons without silently overwriting existing memory.

## Inputs

- current task artifacts
- existing `.ship-council/memory/*.md`
- user statements that ask to preserve a reusable rule
- `references/memory-policy.md`

## Rules

- Do not edit project code.
- Follow `MEMORY-CAPTURE-GATE` and `MEMORY-CONFLICT-GATE`.
- Suggest only reusable knowledge, not one-off task details.
- Check target and related memory files for conflicts before proposing a write.
- If conflict exists, ask the user to keep, replace, merge, or reject. Do not decide silently.
- Never store secrets, credentials, private user data, or unverified commands.

## Output

Write or update `memory-suggestions.md`:

```text
target_file
proposed_addition
evidence
reason
conflict_status
conflicting_existing_rules
user_decision_required
requires_approval
```
