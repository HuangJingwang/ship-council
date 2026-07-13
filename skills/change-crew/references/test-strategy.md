# Test Strategy

Test strategy is defined before implementation so development agents know what proof they must create.

## Test Layers

Consider each layer:

- Unit tests for pure logic, validation, parsing, permissions, and state reducers.
- Integration tests for API/service/database boundaries.
- Contract tests for request/response, DTO, events, schemas, and generated clients.
- E2E tests for critical user workflows.
- Regression tests for the original bug or requested behavior.
- Manual checks only when automation is unavailable or disproportionately expensive.

Also apply surface-specific verification expectations from `surface-playbooks.md`.

## Required Output

Write `test-plan.md` with:

```text
behaviors_to_prove
unit_tests
integration_tests
contract_tests
e2e_tests
regression_tests
manual_checks
not_testing_and_why
```

## Gate

Do not enter implementation until `test-plan.md` names the verification obligations for each affected surface.

If the project has no existing test harness for an affected behavior, the plan must say whether to add one, use a smaller executable check, or mark the gap explicitly.
