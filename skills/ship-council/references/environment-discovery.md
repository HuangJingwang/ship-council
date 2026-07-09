# Environment Discovery

Verification succeeds only when the workflow knows how the project runs.

## Discover

Inspect the repository for:

- language runtimes and versions;
- package managers (`npm`, `pnpm`, `yarn`, Maven, Gradle, Cargo, Go, Python, etc.);
- install, build, lint, test, and typecheck commands;
- server startup commands and ports;
- Docker Compose or service dependencies;
- database, cache, queue, and external service requirements;
- `.env` examples and required secrets;
- CI workflows that reveal canonical commands.

## Secrets Policy

Never print, copy, or invent secrets. If a command needs unavailable credentials, record the missing variable name and block or use a documented local fallback.

Do not read private secret files unless the user explicitly asks and it is necessary. Prefer `.env.example`, docs, CI variable names, and error messages.

## Output

Write `environment-report.md` with:

```text
runtimes
package_managers
commands
ports
services
env_vars
secrets_or_credentials_gaps
verification_plan
```

## Gate

Verification agents must read `environment-report.md` before running commands.
