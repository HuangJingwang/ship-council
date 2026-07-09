# Agent Topology

Use agents for context isolation, parallel research, independent review, and bounded implementation. Do not create agents only to imitate an org chart.

## Default Topology

The main Codex thread is the orchestrator. It owns state, artifacts, user communication, and transitions.

Core worker types:

- Research agent: sourced investigation, no code edits.
- Proposal critic agent: read-only critique and scorecard for proposals before approval.
- Surface developer agent: implementation for one bounded surface or repo. Instantiate as backend, web, mobile, data, infra, docs, or tests based on discovered surfaces.
- Review agent: read-only quality/spec review.
- Security agent: read-only vulnerability/risk review.
- Verification agent: command execution and evidence recording.

On-demand specialist workers:

- Dependency agent: dependency additions, removals, upgrades, license, package health, and vulnerability review.
- Data migration agent: schema, SQL, migrations, indexes, backfills, generated database code, and production data safety.
- External service agent: third-party APIs, credentials, sandbox/prod separation, webhooks, retries, timeouts, and mocks.
- Rollout observability agent: feature flags, staged rollout, rollback, logs, metrics, traces, alerts, and runbooks.
- Memory agent: explicit memory capture, memory suggestions, and conflict detection.

## Selection Rules

| Situation | Agents |
| --- | --- |
| Any non-trivial task | Proposal critic, review, verification |
| Current external facts matter | Research |
| Code changes are needed | One surface developer per non-overlapping surface or repo |
| Auth, tenant boundaries, sensitive data, file/network input, or user data are touched | Security |
| Dependency manifest changes | Dependency |
| Database, migration, generated DB code, backfill, index, or analytics change | Data migration |
| Third-party service, credential, webhook, email, payment, storage, AI API, or remote call | External service |
| User-facing production behavior or risky release | Rollout observability |
| User asks to remember a rule, or reusable lessons emerge | Memory |

## Concurrency Defaults

- Small task: orchestrator only plus optional critic or review.
- Medium task: 2-4 workers.
- Large or multi-repo task: 4-6 workers.
- More than 6 active workers is allowed only for clearly independent read-only scans.

Default waves:

1. Research, discovery, and impact analysis can run in parallel.
2. Surface developers can run in parallel only when write scopes do not overlap.
3. Review, security, dependency, migration, external service, and rollout checks can run in parallel after implementation or against a frozen plan.
4. Verification is usually single-orchestrated because services, ports, databases, and caches are shared.

## Handoff Rules

- Give each agent a narrow scope and required artifact path.
- Agents should write outputs to files when possible.
- The orchestrator reads the file output directly instead of paraphrasing intermediate chat.
- Avoid more than 3-5 active workers unless the task is clearly decomposable; never exceed 6 active write-capable workers.
- Do not run parallel implementers against overlapping write sets.
- Do not let agents freeze contracts, approve user-facing decisions, or mark done. The orchestrator owns those transitions.
- Prefer read-only specialist agents over adding more developer agents when risk is unclear.

## Deliberation Protocol

Round 1: each relevant surface proposes:

```text
proposed_changes
contract_needs
risks
questions_for_other_surfaces
```

Round 2: each relevant surface challenges:

```text
objections
tradeoffs
required_contract_decisions
fallback_option
```

After two rounds, the orchestrator must freeze a contract, ask the user, or block. Do not keep arguing.

## Proposal Critique Protocol

Use a proposal critic after PRD, deliberation decisions, contract plus implementation plan, and final report when they require user approval or gate implementation.

The critic receives artifacts and evidence, not the orchestrator's desired conclusion. It writes `proposal-critique.md` with:

```text
recommendation: approve|revise|block
overall_score: 1-5
must_change
should_consider
assumptions_to_verify
strongest_rejection_reason
```

The orchestrator must incorporate `revise` findings or explicitly accept the risk. It cannot override `block` without user confirmation.
