# Example: Backend-Only Change

Prompt:

```text
Use ship-council to add an audit field to the user export API. Backend only. Semi-auto mode.
```

Expected flow:

```text
INTAKE
SURFACE_DISCOVERY -> backend, data, test
IMPACT_ANALYSIS -> API consumers, permissions, export schema
CONTRACT -> response field, compatibility, error behavior
TEST_STRATEGY -> service unit test, API integration test
ENVIRONMENT_DISCOVERY -> Maven/Gradle commands, required database
IMPLEMENTATION
REVIEW
SECURITY
DOCUMENTATION -> API docs or changelog if public
VERIFICATION
DONE
```

Expected artifacts:

```text
.ship-council/tasks/<date>-audit-field/
  prd.md
  impact-analysis.md
  contract.md
  test-plan.md
  environment-report.md
  verification-report.md
  final-report.md
```
