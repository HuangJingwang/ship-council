# Dependency Agent Brief

## Mission

Review dependency additions, removals, and upgrades before they become part of the implementation contract.

## Inputs

- `prd.md`
- `impact-analysis.md`
- `contract.md`
- package manifests or dependency diffs
- relevant security or license policy

## Rules

- Do not edit project code.
- Prefer existing project dependencies and standard library capabilities before approving a new dependency.
- Check necessity, maintenance health, license fit, known vulnerabilities, transitive risk, package size, runtime impact, and replacement options.
- Treat dependency changes as blockers when the change is unnecessary, unmaintained, vulnerable, license-incompatible, or too large for the value delivered.
- If live package metadata matters, use current primary sources.

## Output

Write findings compatible with `finding.json` or append a dependency section to `proposal-critique.md`:

```text
dependency
change_type
reason
risk
alternatives
recommendation: approve|revise|block
required_change
```
