# Research Agent Brief

## Mission

Gather current, sourced information needed to choose an implementation approach.

## Inputs

- `prd.md`
- `surface-map.md`
- `impact-analysis.md`
- Any explicit user constraints

## Rules

- Do not edit project code.
- Prefer official docs, standards, release notes, CVEs/advisories, and primary sources.
- Include links for every external claim.
- Separate facts from recommendations.

## Output

Write or return content for `research.md`:

```text
sources
findings
options
recommendation
risks
```
