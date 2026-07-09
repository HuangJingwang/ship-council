# Contract

## Interfaces

- Backend work item list endpoint accepts `organizationId`.
- Response shape remains unchanged.
- Frontend includes `organizationId` in list requests when an organization is selected.

## Data

- Filtering must happen before pagination and sorting.
- Existing pagination metadata continues to describe the filtered result set.

## Permissions

- User must have access to the requested organization.
- Unauthorized organization ids must not leak whether work items exist.

## Errors

- Missing organization selection follows existing default behavior.
- Unauthorized organization selection returns the existing permission error shape.

## Testing Obligations

- Backend service/API test for filtered results.
- Backend permission failure test.
- Frontend request-mapping test or component smoke check.
- Verification report records real commands or explicit environment blockers.
