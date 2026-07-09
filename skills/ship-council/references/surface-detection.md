# Surface Detection

Surfaces are code ownership areas that can be planned, implemented, reviewed, and verified independently.

## Surface Types

- `backend`: APIs, services, controllers, jobs, server-side auth.
- `web`: React, Vue, Angular, Svelte, Next, Vite, browser UI.
- `mobile`: iOS, Android, Flutter, React Native, Expo.
- `desktop`: Electron, Tauri, native desktop apps.
- `data`: migrations, SQL, ETL, analytics, schemas.
- `infra`: Docker, CI, Kubernetes, Terraform, deployment.
- `docs`: user docs, API docs, changelogs.
- `test`: test harnesses, e2e, fixtures, QA automation.
- `unknown`: detected impact that does not fit a known surface.

## Detection Heuristics

Use `scripts/detect_surfaces.py <repo>` first. Then inspect manually when output is ambiguous.

Strong signals:

- `pom.xml`, `build.gradle`, `src/main/java`, `Controller`, `Service` -> `backend`
- `package.json`, `vite.config.*`, `next.config.*`, `src/components` -> `web`
- `ios/`, `android/`, `pubspec.yaml`, `app.json`, `expo` -> `mobile`
- `electron`, `tauri.conf.json`, `src-tauri` -> `desktop`
- `migrations/`, `prisma/`, `liquibase/`, `flyway`, `*.sql` -> `data`
- `docker-compose.yml`, `.github/workflows`, `k8s/`, `helm/`, `terraform` -> `infra`

## Manual Overrides

If the user provides paths, trust them over heuristics:

```text
frontend=packages/admin
backend=services/api
mobile=apps/mobile
```

Record overrides in `surface-map.md`.

After surfaces are identified, read `surface-playbooks.md` and apply the relevant checklist for each affected surface.
