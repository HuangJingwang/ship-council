# Surface Playbooks

Use the relevant checklist after `SURFACE_DISCOVERY`. Apply it during deliberation, contract, implementation, review, security, and verification.

## Web UI

Use for React, Vue, Angular, Svelte, Next, Vite, browser UI, CSS, design systems, and visual behavior.

When the change is visually significant, also read `design-skill-integration.md` and choose a design route:

- marketing, landing, portfolio, brand site, or redesign: use specialist design guidance such as `design-taste-frontend` or `frontend-design`;
- product app, dashboard, admin, SaaS, CRM, or internal tooling: preserve the existing design system and prioritize dense, scannable workflows;
- component-only change: stay within local component APIs, tokens, icons, and spacing unless the task explicitly requests a redesign.

Focus on:

- API contract alignment and client data mapping;
- visual direction, design-system fit, component hierarchy, and typography;
- layout correctness across desktop and mobile;
- responsive behavior and stable dimensions;
- loading, empty, error, disabled, optimistic, and permission-denied states;
- accessibility: semantic controls, labels, keyboard navigation, focus, contrast;
- interaction details: debounce, pagination, sorting, filters, modals, navigation;
- visual consistency with the existing design system;
- text overflow, wrapping, hidden overflow, and overlap;
- browser/runtime verification and screenshots when layout matters;
- avoiding invented UI libraries or icons not present in the project.

Review should ask:

- Does every user-visible state exist?
- Does text fit at common viewport sizes?
- Does the component follow existing local patterns?
- Does it handle API errors and authorization failures?

Verification should include, when available:

- unit/component tests;
- typecheck/lint/build;
- browser smoke or screenshot check for visual changes;
- viewport checks for narrow, medium, and wide layouts when the UI is user-facing.

## Backend

Use for APIs, controllers, services, jobs, server-side validation, auth, and business logic.

Focus on:

- API/DTO contract and backward compatibility;
- authentication and authorization;
- tenant, organization, ownership, and role boundaries;
- input validation and error mapping;
- transaction boundaries and rollback behavior;
- idempotency, retries, and concurrency;
- query performance, pagination, filtering, indexes, and N+1 risks;
- logging and observability without secrets or sensitive data;
- service-level and API-level tests;
- compatibility with existing clients and migrations.

Review should ask:

- Is permission checked at the right layer?
- Are invalid inputs handled deterministically?
- Does the code reuse existing service/repository patterns?
- Are errors mapped to the expected API shape?

Verification should include, when available:

- unit/service tests;
- API/integration tests;
- build and static checks;
- migration dry run or local startup for risky changes.

## Mobile

Use for iOS, Android, Flutter, React Native, Expo, and mobile-specific UX.

When the change touches visual UI or navigation, also read `design-skill-integration.md` and choose the platform route: iOS/SwiftUI, Android/Material, Flutter, React Native, Expo, or Figma-linked implementation.

Focus on platform navigation and lifecycle, native component expectations, safe areas, keyboard overlap, accessibility labels, touch targets, dynamic type or text scaling, offline/retry states, API cache invalidation, native permissions, and device or emulator smoke checks when possible.

Review should ask:

- Does the UI follow platform conventions rather than generic web patterns?
- Are touch targets, safe areas, keyboard behavior, and text scaling handled?
- Are permissions, offline states, and navigation/back behavior clear?

Verification should include, when available:

- unit/component/widget tests;
- typecheck/lint/build;
- simulator, emulator, preview, or screenshot smoke checks for visual or navigation changes.

## Desktop

Use for Electron, Tauri, native desktop, and desktop shell integrations.

Focus on window lifecycle, menus, shortcuts, file dialogs, renderer/main trust boundaries, local file access, path validation, signing, packaging, keyboard workflows, and accessibility.

## Data And Migration

Use for SQL, migrations, schema changes, ETL, analytics, and generated database code.

Focus on backward and forward compatibility, data safety, rollback, idempotency, locks, production volume, indexes, query plan impact, generated code synchronization, and migration dry runs.

Block done when a destructive migration lacks rollback or explicit user acceptance.

## Infrastructure

Use for Docker, CI, Kubernetes, Helm, Terraform, deployment, and runtime config.

Focus on environment variables, secrets handling, least privilege, network exposure, health checks, probes, resource limits, rollout strategy, CI reproducibility, cache behavior, rollback, and local developer ergonomics.

## Docs

Use for README, API docs, OpenAPI/YApi, changelog, runbooks, and migration notes.

Focus on accuracy against implemented behavior, examples that match real API shape, migration and rollback instructions, environment variables, commands, known limitations, and verification gaps.

## Test And QA

Use for test harnesses, fixtures, e2e, smoke tests, visual tests, and CI checks.

Focus on proving behavior rather than implementation details, stable fixtures, deterministic timing, negative cases, permission failures, realistic integration boundaries, avoiding brittle sleeps, and clear failure messages.
