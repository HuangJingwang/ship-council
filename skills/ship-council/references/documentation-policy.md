# Documentation Policy

Documentation is a delivery gate when behavior changes.

## Check Whether Docs Must Change

Docs are likely required when the change affects:

- public or internal APIs;
- DTOs, events, schemas, or config;
- user-visible workflows;
- migrations, deployment, or rollback;
- permissions, security, or audit behavior;
- setup commands or environment variables.

## Possible Artifacts

- README or operator docs
- OpenAPI/Swagger/YApi docs
- changelog or release notes
- migration notes
- inline examples
- generated client docs
- troubleshooting notes

## Output

Record the decision in `final-report.md`:

```text
docs_updated
docs_not_needed_reason
api_spec_updated
migration_notes
```

If docs are required but not updated, block `DONE` unless the user explicitly accepts the gap.
