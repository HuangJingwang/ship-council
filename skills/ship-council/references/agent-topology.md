# Agent Topology

Rule: use agents for isolation, independence, or parallel non-overlapping work; never for theatre.

## Roles

- Orchestrator: main thread; owns state, artifacts, user comms, transitions.
- Research: sourced facts; no code edits.
- Proposal critic: read-only scorecard before approval.
- Surface developer: one bounded backend/web/mobile/data/infra/docs/tests scope.
- Review: read-only quality/spec findings.
- Security: read-only exploit/policy findings.
- Verification: command evidence.
- Specialists: dependency, data migration, external service, rollout/observability, memory.

## Select

| Trigger | Add |
| --- | --- |
| Current external facts matter | Research |
| User approval or major plan | Proposal critic |
| Non-overlapping code scopes | Surface developers |
| Auth, tenant, secrets, user data, network/file input | Security |
| Package manifest changes | Dependency |
| DB/migration/backfill/index/generated DB code | Data migration |
| Third-party APIs, credentials, webhooks, remote calls | External service |
| Production rollout or hard-to-debug behavior | Rollout observability |
| User says remember, or reusable lesson emerges | Memory |

## Concurrency

- Small: orchestrator only; maybe critic/review.
- Medium: 2-4 workers.
- Large: 4-6 workers.
- More than 6 only for independent read-only scans.
- Never parallel-write overlapping files.
- Verification is usually single-orchestrated because services/ports/db state are shared.

## Handoff

Each agent gets: role brief, exact inputs, allowed paths, output file, stop condition.

Agents write files; orchestrator reads files. Do not approve contracts, user-facing decisions, or done status inside workers.

## Debate

Two rounds max:

1. Propose: `changes`, `contract_needs`, `risks`, `questions`.
2. Challenge: `objections`, `tradeoffs`, `required_decisions`, `fallback`.

Then freeze contract, ask user, or block.

## Critique

Critic receives artifacts and evidence, not the desired answer.

Output:
```text
recommendation: approve|revise|block
overall_score: N/5
must_change:
should_consider:
assumptions_to_verify:
strongest_rejection_reason:
```

Orchestrator must incorporate `revise`; user must confirm override of `block`.
