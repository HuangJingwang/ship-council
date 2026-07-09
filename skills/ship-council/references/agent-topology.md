# Agent Topology

Use agents for context isolation, parallel research, independent review, and bounded implementation. Do not create agents only to imitate an org chart.

## Default Topology

The main Codex thread is the orchestrator. It owns state, artifacts, user communication, and transitions.

Worker types:

- Research agent: sourced investigation, no code edits.
- Proposal critic agent: read-only critique and scorecard for proposals before approval.
- Surface developer agent: implementation for one bounded surface.
- Review agent: read-only quality/spec review.
- Security agent: read-only vulnerability/risk review.
- Verification agent: command execution and evidence recording.

## Handoff Rules

- Give each agent a narrow scope and required artifact path.
- Agents should write outputs to files when possible.
- The orchestrator reads the file output directly instead of paraphrasing intermediate chat.
- Avoid more than 3-5 active workers unless the task is clearly decomposable.
- Do not run parallel implementers against overlapping write sets.

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
