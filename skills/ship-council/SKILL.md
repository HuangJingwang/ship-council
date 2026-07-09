---
name: ship-council
description: Use when a software change needs coordinated planning, implementation, review, security checks, verification, or fix loops across one or more app surfaces such as backend, web, mobile, desktop, data, docs, tests, or infrastructure.
---

# Ship Council

## Overview

Ship Council turns one software change request into a controlled delivery loop: research, deliberate, critique, contract, implement, review, secure, verify, and fix until the work is shippable or explicitly blocked.

This is not a roleplay council. Use agents for context isolation, independent judgment, bounded work, and anti-sycophancy critique. The main Codex thread is always the orchestrator.

## Modes

Default to **semi-auto** mode unless the user explicitly asks for full automation.

- **Semi-auto:** stop for user confirmation after PRD, contract, high-risk findings, repeated loop failure, and final report.
- **Auto:** run without routine check-ins for up to 3 fix loops. Still stop for destructive operations, missing credentials, contradictory requirements, repeated unresolved findings, or changes that alter business/security policy.

Mode hints:

- Semi-auto: "use ship-council", "run the council", no explicit automation wording.
- Auto: "auto mode", "fully automatic", "run up to N rounds", "do not ask unless blocked".

## State Machine

Run these states in order:

1. `INTAKE` - create PRD and acceptance criteria.
2. `SURFACE_DISCOVERY` - detect affected app surfaces.
3. `IMPACT_ANALYSIS` - identify affected callers, data, permissions, compatibility, and rollback concerns.
4. `RESEARCH` - use web research when current external facts, frameworks, APIs, vulnerabilities, or best practices matter.
5. `DELIBERATION` - have relevant surfaces propose and challenge implementation approaches.
6. `PROPOSAL_CRITIQUE` - independently score proposals, identify weak assumptions, and require revisions when needed.
7. `CONTRACT` - freeze API, schema, UI/client behavior, permissions, migrations, and test obligations.
8. `TEST_STRATEGY` - define unit, integration, e2e, regression, and manual verification obligations before coding.
9. `ENVIRONMENT_DISCOVERY` - discover package managers, runtimes, commands, ports, services, and secrets gaps.
10. `IMPLEMENTATION` - assign bounded work by surface.
11. `REVIEW` - read-only quality/spec review.
12. `SECURITY` - read-only security/risk review.
13. `DOCUMENTATION` - update docs, OpenAPI, changelog, or migration notes when behavior changes.
14. `VERIFICATION` - run real commands and record outputs.
15. `FIX` - turn findings or failures into fix packets and return to implementation.
16. `MEMORY_CAPTURE` - propose reusable project constraints, commands, decisions, and lessons.
17. `DONE` or `BLOCKED`.

Read `references/state-machine.md` when state transitions, mode gates, or stop conditions are non-trivial.

## Workspace Artifacts

Create a task workspace in the target repository:

```text
.ship-council/tasks/<yyyy-mm-dd-slug>/
  prd.md
  ship-council.json
  surface-map.md
  impact-analysis.md
  research.md
  deliberation.md
  proposal-critique.md
  contract.md
  test-plan.md
  environment-report.md
  implementation-plan.md
  findings/
    review-findings.json
    security-findings.json
  fix-packets/
  git-pr-plan.md
  verification-report.md
  retrospective.md
  memory-suggestions.md
  final-report.md
```

Use `scripts/init_task.py` to create this layout and copy templates. Use `scripts/init_memory.py` to create `.ship-council/memory/` if missing. Use `scripts/detect_surfaces.py` to seed `surface-map.md`. Use `scripts/discover_commands.py` to seed `environment-report.md`.

At task start, read existing `.ship-council/memory/*.md` when present. At task end, write `memory-suggestions.md`. When the user explicitly says to remember a preference, workflow, or constraint, capture it as a memory suggestion immediately. Do not update long-term memory without user approval unless the user explicitly requested fully automatic memory updates. Never overwrite conflicting memory silently; ask the user to choose which rule to keep, replace, or merge.

## Agent Rules

- The orchestrator owns state, sequencing, synthesis, and user communication.
- Surface developer agents own bounded implementation scopes such as backend, web, mobile, desktop, data, infra, docs, or tests.
- Research agents gather sourced facts and do not edit project code.
- Proposal critic agents are read-only counterweights. They score proposals and recommend approve, revise, or block.
- Review and security agents are read-only verifiers. They output findings, not patches.
- Verification agents run commands and record evidence. They do not claim success without output.
- Prefer filesystem artifacts over paraphrased agent summaries. Agents write files; the orchestrator reads files.

Read `references/agent-topology.md` before spawning multiple implementation, review, security, or verification agents.

## Hard Gates

Do not enter implementation until `prd.md`, `surface-map.md`, `impact-analysis.md`, `proposal-critique.md`, `contract.md`, `test-plan.md`, and `environment-report.md` exist.

Do not ask the user to approve a major proposal until a proposal critic has reviewed it or the missing critique is recorded as an explicit process gap.

Do not mark work done unless:

- contract exists and matches implemented behavior;
- changed files are listed in `final-report.md`;
- review has no open blocker findings;
- security has no open high/critical findings;
- docs/changelog/API specs have been updated or explicitly marked not needed;
- verification report contains real commands, outputs, exit status, or explicit reasons a command could not run.

If review, security, or verification finds issues, create fix packets before returning to implementation. Do not say "fix it again" without structured evidence.

## Reference Loading

Load only what is needed:

- `surface-detection.md` when project layout or surfaces are ambiguous.
- `surface-playbooks.md` after surface discovery to load surface-specific implementation, review, and verification checklists.
- `design-skill-integration.md` when web/mobile UI, visual styling, Figma, responsive layout, component composition, or design-system consistency matters.
- `impact-analysis.md` before freezing contract or assigning implementation.
- `agent-topology.md` before delegating to multiple agents.
- `proposal-critique-policy.md` before asking the user to approve PRD, deliberation decisions, contract, implementation plan, or final report.
- `artifact-schema.md` when creating or validating task files.
- `loop-policy.md` when findings, failed verification, or repeated fixes appear.
- `review-security-policy.md` before read-only quality/security review.
- `risk-rubric.md` when assigning severity or deciding whether a finding blocks done.
- `test-strategy.md` before implementation and when verification scope is unclear.
- `environment-discovery.md` before running builds, servers, migrations, or e2e tests.
- `git-pr-policy.md` before branching, committing, staging, pushing, or drafting PR text.
- `documentation-policy.md` when public behavior, APIs, config, migrations, or user workflows change.
- `verification-policy.md` before claiming completion.
- `memory-policy.md` at task start and before writing memory suggestions.
- `publish-quality.md` when preparing this skill for GitHub/marketplace release.

## Scripts

- `scripts/init_task.py <repo> "<task title>"` creates `.ship-council/tasks/...` from templates.
- `scripts/init_memory.py <repo>` creates `.ship-council/memory/...` from templates.
- `scripts/detect_surfaces.py <repo>` prints JSON surface evidence.
- `scripts/discover_commands.py <repo>` prints candidate install/build/test/start commands.
- `scripts/check_memory_conflicts.py <repo> <target-memory-file> --text "<proposed rule>"` surfaces nearby existing memory rules before writing.
- `scripts/validate_artifacts.py <task-dir>` checks required artifacts and finding JSON.
- `scripts/merge_findings.py <task-dir>` converts open findings into fix packet drafts.

## Agent Briefs

Use `references/agent-briefs/` when dispatching subagents:

- `research-agent.md`
- `proposal-critic-agent.md`
- `surface-developer-agent.md`
- `review-agent.md`
- `security-agent.md`
- `verification-agent.md`
