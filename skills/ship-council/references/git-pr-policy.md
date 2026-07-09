# Git And PR Policy

Git operations are optional and must respect the user's workspace.

## Branching

Do not create or switch branches unless the user asks or project workflow clearly requires it. If creating a branch, use the host's branch naming convention when provided.

## Staging And Commit

Do not stage, commit, push, or open PRs unless the user asks.

Before any commit or PR:

- verify the work with fresh command output;
- include only files related to the task;
- do not revert unrelated user changes;
- summarize remaining verification gaps.

## PR Description

When asked to prepare a PR, write:

```text
summary
contract_changes
test_plan
security_notes
verification_output
risks_and_rollout
rollback
```

## Conflict Handling

If multiple agents touch the same file unexpectedly:

1. stop parallel implementation for that file;
2. have the orchestrator inspect both changes;
3. merge deliberately or assign one owner;
4. re-run review and verification.
