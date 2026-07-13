# Example: Web And Backend Change

Prompt:

```text
Use change-crew in auto mode, up to 3 fix loops, to add organization filtering to the work item list. Update backend and web.
```

Expected flow:

```text
INTAKE
SURFACE_DISCOVERY -> backend, web, test
IMPACT_ANALYSIS -> API callers, query performance, permission boundary
RESEARCH -> current framework/API docs if needed
DELIBERATION -> backend proposes API; web proposes UI state and loading/error behavior
CONTRACT -> request params, response schema, empty state, permissions
TEST_STRATEGY -> backend integration, web component/state, e2e smoke
ENVIRONMENT_DISCOVERY -> backend start/test, frontend build/test, ports
IMPLEMENTATION -> bounded write scopes
REVIEW -> findings JSON
SECURITY -> cross-organization access check
DOCUMENTATION -> API docs if contract changed
VERIFICATION -> commands and outputs
FIX -> fix packet loop if needed
DONE
```

Key invariant:

```text
The web agent does not invent API fields. The backend agent does not invent UI behavior. Both implement the frozen contract.
```
