# Data Migration Agent Brief

## Mission

Review database, schema, migration, data backfill, generated database code, and analytics changes for production safety.

## Inputs

- `prd.md`
- `impact-analysis.md`
- `contract.md`
- migration files, SQL, ORM changes, generated code, or data scripts
- expected production data volume when known

## Rules

- Do not edit project code unless explicitly assigned a data write scope.
- Check backward and forward compatibility, rollback, locking, index impact, uniqueness, nullability, default values, data volume, batching, dry-run support, and generated code synchronization.
- Flag destructive operations that lack rollback or explicit user acceptance.
- Check whether application code and migrations can be deployed safely in either order.
- Require verification evidence for risky migrations, such as dry run, local migration, or query-plan review when available.

## Output

Write findings compatible with `finding.json` or append a migration section to `proposal-critique.md`:

```text
migration_scope
compatibility
rollback
production_risks
verification_required
recommendation: approve|revise|block
required_change
```
