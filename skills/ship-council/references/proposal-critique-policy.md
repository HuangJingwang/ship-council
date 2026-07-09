# Proposal Critique Policy

Use this policy whenever Ship Council produces a proposal that asks the user to approve direction, scope, contract, implementation plan, or final acceptance.

The critic is independent from the proposal author. It does not implement code and does not rewrite the proposal directly. Its job is to reduce agreement bias, optimism bias, and vague approval-seeking.

## What Must Be Critiqued

Run critique after these artifacts are drafted and before treating them as accepted:

- `prd.md` when requirements or acceptance criteria are inferred;
- `deliberation.md` before freezing architecture or cross-surface direction;
- `contract.md` and `implementation-plan.md` before coding;
- `final-report.md` before claiming done;
- any high-risk alternative selection, dependency choice, migration plan, auth/permission plan, or rollout plan.

For very small, low-risk tasks, one short critique section in `proposal-critique.md` is enough. Do not skip it because the proposal "looks reasonable."

## Critic Rules

- Be specific, not contrarian for theater.
- Score against evidence, not confidence.
- Prefer actionable changes over broad warnings.
- State the strongest reason to reject or delay the proposal.
- Identify assumptions that should be verified before implementation.
- Call out when the proposal overfits the user's likely preference instead of the codebase evidence.
- Do not praise unless a concrete strength affects delivery safety.

## Scorecard

Use 1-5 scores:

| Dimension | Question |
| --- | --- |
| Requirement clarity | Are goals, non-goals, and acceptance criteria testable? |
| Evidence quality | Is the proposal grounded in codebase inspection, memory, research, or explicit user input? |
| Contract safety | Are API, data, permissions, errors, migrations, and compatibility covered where relevant? |
| Implementation fit | Does the plan match existing project patterns and minimize unnecessary change? |
| Risk coverage | Are security, data loss, rollout, rollback, performance, and hidden callers considered? |
| Verification strength | Would the planned tests and commands actually prove the behavior? |
| User-value alignment | Does the solution solve the user's problem without adding unrelated scope? |

Overall recommendation:

- `approve`: no blocking changes; minor suggestions only.
- `revise`: proposal is directionally useful but needs changes before approval.
- `block`: do not proceed until listed blockers are resolved.

## Output Format

Append a section to `proposal-critique.md`:

```text
## <Artifact Or Proposal Name>

Recommendation: approve|revise|block
Overall score: N/5

Scores:
- Requirement clarity:
- Evidence quality:
- Contract safety:
- Implementation fit:
- Risk coverage:
- Verification strength:
- User-value alignment:

Must change:
- ...

Should consider:
- ...

Assumptions to verify:
- ...

Strongest rejection reason:
- ...
```

If recommendation is `revise` or `block`, the orchestrator must either update the proposal or explicitly record why the critique is accepted as risk.
