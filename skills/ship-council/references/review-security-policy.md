# Review And Security Policy

Review and security are separate read-only gates.

## Review Gate

Review checks:

- contract compliance;
- surface-specific concerns from `surface-playbooks.md`;
- missing tests;
- type/null/bounds handling;
- duplicate logic;
- project conventions;
- cross-surface mismatch;
- maintainability risks.

The reviewer outputs findings JSON and does not edit code.

## Security Gate

Security checks:

- authentication and authorization;
- cross-tenant or cross-organization access;
- injection risks;
- XSS/CSRF/client-side trust;
- sensitive data leakage;
- unsafe deserialization or file handling;
- secrets in logs, config, or commits;
- dependency or deployment risk when relevant.

High and critical findings block `DONE` unless explicitly marked `accepted-risk` by the user.

Use `risk-rubric.md` for severity and blocker decisions.

## Evidence Standard

A finding must cite a file, behavior, command output, or concrete absence. Vague "could be better" notes should be `info` or omitted.
