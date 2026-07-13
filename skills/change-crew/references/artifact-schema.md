# Artifact Schema

Artifacts make agent work inspectable and loopable.

## Required Files

- `prd.md`: goal, non-goals, user stories, acceptance criteria, constraints, unknowns.
- `change-crew.json`: machine-readable mode, state, loop, surface, and blocker status.
- `surface-map.md`: detected surfaces, evidence, manual overrides, runtime assumptions.
- `impact-analysis.md`: direct changes, consumers, data, permissions, compatibility, rollback, observability.
- `research.md`: sources, findings, options, recommendation.
- `deliberation.md`: surface proposals, objections, decisions.
- `proposal-critique.md`: independent scorecards and revision/block recommendations for proposals.
- `contract.md`: interface/data/permission/error/test contract.
- `test-plan.md`: proof obligations by test layer and explicit gaps.
- `environment-report.md`: runtimes, commands, ports, services, env vars, secret gaps.
- `implementation-plan.md`: tasks, owners, write scopes, verification obligations.
- `findings/*.json`: machine-readable review/security findings.
- `fix-packets/*.md`: actionable work packets produced from findings.
- `git-pr-plan.md`: branch, commit, PR, rollout, and rollback notes when requested.
- `verification-report.md`: commands, output summaries, failures, gaps.
- `retrospective.md`: lessons and repeated workflow issues after completion.
- `memory-suggestions.md`: proposed updates to long-term project constraints and recipes.
- `final-report.md`: changes, risks, validation, remaining gaps.

## Finding JSON

```json
{
  "id": "SC-001",
  "stage": "review",
  "target_surface": "backend",
  "severity": "high",
  "category": "permission",
  "files": ["src/example/File.java"],
  "evidence": "Concrete proof from code, logs, or tests.",
  "required_change": "The smallest acceptable fix.",
  "acceptance": "How to prove the fix works.",
  "status": "open"
}
```

Valid severities: `critical`, `high`, `medium`, `low`, `info`.

Valid statuses: `open`, `fixed`, `accepted-risk`, `false-positive`.

## Manifest JSON

```json
{
  "task_id": "2026-07-09-example",
  "mode": "semi-auto",
  "state": "INTAKE",
  "loop_index": 0,
  "loop_limit": 3,
  "surfaces": [],
  "blocked": false,
  "blockers": [],
  "created_at": "2026-07-09"
}
```

Valid states are the states listed in `state-machine.md`.
