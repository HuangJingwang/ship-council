# Demo: Organization Filter Across Web And Backend

This demo shows the intended artifact shape for a Ship Council run.

## Prompt

```text
Use ship-council in auto mode, up to 3 fix loops, to add organization filtering to the work item list. Update backend and web.
```

## Generated Workspace

```text
.ship-council/tasks/2026-07-09-org-filter/
  ship-council.json
  prd.md
  surface-map.md
  impact-analysis.md
  research.md
  deliberation.md
  contract.md
  test-plan.md
  environment-report.md
  implementation-plan.md
  findings/
    review-findings.json
    security-findings.json
  fix-packets/
    SC-001-permission.md
  verification-report.md
  retrospective.md
  memory-suggestions.md
  final-report.md
```

## Contract Excerpt

```text
GET /api/work-items?orgId=<id>

Rules:
- backend validates the requesting user can access orgId;
- missing orgId preserves the existing default list behavior;
- web shows loading, empty, and permission-denied states;
- response schema does not change except filtered result set.
```

## Surface Playbooks

```text
backend:
- organization access validation
- API integration tests
- query performance for orgId filter

web:
- filter state
- loading/empty/error states
- permission denied state
- responsive layout check
```

## Finding Excerpt

```json
{
  "id": "SC-001",
  "stage": "security",
  "target_surface": "backend",
  "severity": "high",
  "category": "authorization",
  "files": ["src/main/java/example/WorkItemController.java"],
  "evidence": "orgId is accepted from the request but not checked against the current user's allowed organizations.",
  "required_change": "Add service-layer organization access validation before querying work items.",
  "acceptance": "Integration test covers allowed org and forbidden org.",
  "status": "open"
}
```

## Fix Packet Excerpt

```text
Target Surface: backend
Required Changes: Add organization access validation before query execution.
Acceptance Checks: Integration test passes for allowed and forbidden orgs.
Loop Index: 1
```

## Verification Excerpt

```text
Command: ./gradlew test
Exit: 0
Result: backend tests passed

Command: pnpm test
Exit: 0
Result: web tests passed
```

## Final Report Excerpt

```text
Summary:
- Added orgId filter support to backend list endpoint.
- Added web organization filter state and empty state.
- Added authorization regression tests.

Remaining gaps:
- E2E smoke was skipped because no local browser test harness exists.
```

## Memory Suggestion Excerpt

```text
Target file: security-constraints.md
Proposed addition:
- Any endpoint accepting orgId must validate the current user's access to that organization in the service layer.

Evidence:
- Security finding SC-001 found orgId filtering without an access check.

Requires approval: yes
```
