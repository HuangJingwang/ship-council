# Impact Analysis

Impact analysis prevents agents from implementing the visible request while missing hidden consumers, permissions, data, or rollout risks.

## Required Questions

Before contract freeze, answer:

- What surfaces are directly changed?
- What upstream callers or downstream consumers depend on this behavior?
- What API, DTO, event, database, cache, or file schema changes?
- What authorization, tenant, organization, or ownership boundary is affected?
- What compatibility constraints exist for older clients or saved data?
- What migrations or data backfills are needed?
- What rollback path exists if deployment fails?
- What observability, logs, metrics, or alerts should change?

## Output

Write `impact-analysis.md` with:

```text
direct_changes
callers_and_consumers
data_and_schema
permissions
compatibility
migration_and_rollback
observability
open_risks
```

If an item is not applicable, say why. Do not leave blank sections.

## Escalation

Return to `DELIBERATION` or ask the user when impact analysis reveals a wider scope than the PRD or contract currently covers.
