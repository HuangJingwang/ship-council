# Context Loading

Goal: manage a large workflow skill without loading unused prompts.

Rule: load by trigger, not by inventory. A file existing in the skill is not a reason to read it.

## Budget

- `quick`: read `SKILL.md` only; no task workspace unless useful.
- `standard`: read at most 1-2 references per phase.
- `full`: read references by phase; never all at once.
- Agent briefs: load only the exact brief for the worker being dispatched.
- Templates/assets: copy or write via scripts; do not read unless editing the template.

## Trigger Matrix

| Signal | Load |
| --- | --- |
| Layout/surface unknown | `surface-detection.md` |
| Surface-specific checklist needed | `surface-playbooks.md` |
| One unknown could change the plan | `grill-gate.md` |
| Multiple agents needed | `agent-topology.md`, then exact brief |
| External facts matter | `research-agent.md` |
| Approval quality matters | `proposal-critique-policy.md`, maybe critic brief |
| Failed review/test | `loop-policy.md` |
| Security risk | `review-security-policy.md`, security brief |
| Completion claim | `verification-policy.md` |
| Memory write | `memory-policy.md` |

## Stop Rules

- If a reference does not answer the current decision, stop reading it.
- If two references conflict, prefer task artifacts and ask the user for policy decisions.
- If the agent wants a third reference in one phase, state why before loading it.
- Never load every reference to "be safe"; that is a process failure.

## Audit Line

For `standard` and `full`, add this to `final-report.md`:

```text
loaded_skill_context:
- file:
  reason:
```
