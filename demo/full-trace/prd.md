# PRD

## Goal

Add organization filtering to a work item list so users only see work items for the selected organization.

## Non-Goals

- Do not redesign the work item page.
- Do not change global authorization policy.
- Do not add new organization-management screens.

## Acceptance Criteria

- Backend accepts an organization filter and applies it before pagination.
- Frontend sends the selected organization id when loading work items.
- Empty, loading, error, and permission-denied states remain intact.
- Verification proves backend filtering and frontend request behavior.

## Constraints

- Preserve existing API response shape.
- Reuse existing organization permission checks.
- Do not introduce a new frontend state library.
