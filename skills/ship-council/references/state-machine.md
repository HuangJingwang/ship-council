# State Machine

Ship Council is a state machine, not a free-form chat.

## States

| State | Required Output | Gate |
|---|---|---|
| `INTAKE` | `prd.md` | Goal, non-goals, acceptance criteria exist |
| `SURFACE_DISCOVERY` | `surface-map.md` | Affected surfaces and evidence are listed |
| `IMPACT_ANALYSIS` | `impact-analysis.md` | Callers, data, permissions, compatibility, rollback are considered |
| `RESEARCH` | `research.md` | Current external facts have sources, or research is explicitly not needed |
| `DELIBERATION` | `deliberation.md` | Relevant surfaces proposed and challenged approaches |
| `PROPOSAL_CRITIQUE` | `proposal-critique.md` | Independent critic recommends approve, revise, or block |
| `CONTRACT` | `contract.md`, `implementation-plan.md` | Interfaces, data, permissions, errors, tests are frozen |
| `TEST_STRATEGY` | `test-plan.md` | Required proof is defined before coding |
| `ENVIRONMENT_DISCOVERY` | `environment-report.md` | Commands, services, ports, env gaps are known |
| `IMPLEMENTATION` | code changes plus notes | Work is scoped by surface |
| `REVIEW` | `findings/review-findings.json` | No open blockers |
| `SECURITY` | `findings/security-findings.json` | No open high/critical findings |
| `DOCUMENTATION` | final report doc section | Required docs/specs are updated or explicitly not needed |
| `VERIFICATION` | `verification-report.md` | Real command evidence or explicit environment blocker |
| `FIX` | `fix-packets/*.md` | Findings have owners and acceptance checks |
| `MEMORY_CAPTURE` | `memory-suggestions.md` | Reusable constraints are proposed for approval |
| `DONE` | `final-report.md` | All gates pass |
| `BLOCKED` | `final-report.md` | Blocker is concrete and repeated or external |

## Semi-Auto Gates

Stop for the user after PRD, contract, high-risk findings, repeated loop failure, git operations, and final report.

## Auto Gates

Auto mode may continue through normal gates for up to 3 fix loops. It must still stop for destructive operations, missing credentials, contradictory requirements, repeated unresolved findings, security policy changes, or external systems the agent cannot access.

## Transition Rule

Never skip from implementation to done. Review, security, documentation, verification, and memory capture are all separate gates.

Do not move from proposal to user approval or implementation while the latest applicable critique recommends `block`. If critique recommends `revise`, update the proposal or record an accepted-risk rationale before continuing.
