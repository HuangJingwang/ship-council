# Risk Rubric

Use this rubric for review and security findings.

## Severity

- `critical`: likely data breach, remote code execution, destructive data loss, auth bypass, or production outage with no workaround.
- `high`: exploitable authorization bug, cross-tenant data exposure, injection path, migration risk that can corrupt data, or contract break for important consumers.
- `medium`: correctness bug, missing important validation, incomplete tests for risky behavior, performance issue at expected scale, or non-critical compatibility risk.
- `low`: maintainability issue, minor edge case, weak naming, localized UX inconsistency, or small test gap.
- `info`: observation that does not require a fix.

## Blocker Rules

Block `DONE` when:

- any `critical` finding is open;
- any `high` security finding is open;
- verification failed for a required acceptance criterion;
- contract and implementation disagree;
- required docs or migration notes are missing.

## Status

- `open`: not resolved.
- `fixed`: implemented and verified.
- `accepted-risk`: user explicitly accepted the risk.
- `false-positive`: evidence shows the finding is not valid.
