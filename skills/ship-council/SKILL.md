---
name: ship-council
description: Use when a software change is large, cross-surface, risky, needs multiple agents, independent critique, review/security/verification loops, or persistent project memory.
---

# Ship Council

## Core Rule

Stay context-light by default. Do not preload references, templates, or every agent brief. Load the smallest set needed for the current risk.

The main Codex thread is the orchestrator. Use worker agents only for context isolation, independent judgment, or parallel non-overlapping work.

## Pick A Profile

| Profile | Use when | Minimum behavior |
| --- | --- | --- |
| `quick` | Small, single-surface, low-risk change | No council ceremony. Identify scope, implement, review your diff, verify. |
| `standard` | Normal feature/fix with some risk | Create task workspace, discover surfaces, freeze a short contract, implement, review, verify. |
| `full` | Cross-repo, multi-surface, security/data/migration/release risk | Use deliberation, proposal critic, specialist agents, security, docs, bounded fix loops, memory capture. |

Default to `quick` unless the user asks for council workflow, multiple agents, auto mode, memory, security review, or the task clearly spans multiple surfaces.

## Start

Use scripts instead of reading templates into context:

```bash
python3 skills/ship-council/scripts/init_task.py <repo> "<task title>"
python3 skills/ship-council/scripts/detect_surfaces.py <repo>
python3 skills/ship-council/scripts/discover_commands.py <repo>
```

Use `scripts/init_memory.py <repo>` only when persistent memory is needed or `.ship-council/memory/` is missing and the task should record reusable constraints.

## Gates

For `standard` and `full`, do not implement until these exist, even if short:

- `prd.md`: user intent and acceptance criteria.
- `surface-map.md`: affected backend/web/mobile/data/infra/docs/tests surfaces.
- `contract.md`: API/schema/UI/client behavior and compatibility decisions.
- `test-plan.md` or `environment-report.md`: commands and verification path.

For `full`, also require impact analysis, proposal critique, and explicit fix-loop policy. Read `references/state-machine.md` only when transitions or stop conditions are non-trivial.

## Agent Routing

Read `references/agent-topology.md` only before spawning multiple agents. Then load only the needed brief from `references/agent-briefs/`.

- Research: current external facts, APIs, vulnerabilities, or best practices.
- Proposal critic: score plans before approval and reduce sycophancy.
- Surface developer: one bounded backend/web/mobile/data/infra/docs/tests scope.
- Review: read-only quality/spec review.
- Security: read-only vulnerability/risk review.
- Verification: commands and evidence.
- Specialists: dependency, migration, external service, rollout/observability, memory.

Never run parallel developers on overlapping files. Prefer read-only specialists over broad developer prompts.

## Reference Router

Load exactly one or two references at a time:

- Surfaces unclear: `references/surface-detection.md`, then `references/surface-playbooks.md`.
- UI/design task: `references/design-skill-integration.md`.
- Contracts or caller risk: `references/impact-analysis.md`.
- Proposal approval: `references/proposal-critique-policy.md`.
- Failed review/verification: `references/loop-policy.md`.
- Quality/security gate: `references/review-security-policy.md`, `references/risk-rubric.md`.
- Verification claims: `references/verification-policy.md`.
- Git/PR actions: `references/git-pr-policy.md`.
- Docs/API/migration notes: `references/documentation-policy.md`.
- Memory capture or conflict: `references/memory-policy.md`.
- Release of this skill: `references/publish-quality.md`.

Do not read all references "just in case".

## Memory

Memory is suggest-only by default. When the user explicitly says to remember a rule, workflow, command, or preference, write a memory suggestion immediately.

Before changing long-term memory, run:

```bash
python3 skills/ship-council/scripts/check_memory_conflicts.py <repo> <memory-file> --text "<proposed rule>"
```

If there is a conflict, show both rules and ask the user to keep, replace, or merge. Never silently overwrite memory.

## Done

Do not claim done unless verification evidence exists or the blocker is explicit. For `standard` and `full`, record changed files, open findings, commands run, exit status, and remaining risks in `final-report.md`.
