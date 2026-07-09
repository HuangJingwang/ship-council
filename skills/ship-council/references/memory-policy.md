# Memory Policy

Ship Council uses file-backed memory to preserve project constraints across tasks without hiding them in chat history.

## Memory Files

Long-term memory lives under:

```text
.ship-council/memory/
  project-profile.md
  coding-constraints.md
  surface-map.md
  verification-recipes.md
  security-constraints.md
  decisions.md
  lessons-learned.md
```

## Task Start

At task start:

1. If `.ship-council/memory/` exists, read the relevant files.
2. Use memory as project guidance, not unquestionable truth.
3. If memory conflicts with current code or user instructions, current code and user instructions win.
4. Record conflicts in `impact-analysis.md` or `retrospective.md`.

## Task End

At task end:

1. Write `memory-suggestions.md`.
2. Suggest only reusable knowledge, not one-off task details.
3. Include evidence for every proposed memory update.
4. In semi-auto mode, ask the user before updating `.ship-council/memory/`.
5. In auto mode, do not update long-term memory unless the user explicitly allowed automatic memory writes.

## What Belongs In Memory

- stable project structure and surface boundaries;
- coding constraints and forbidden patterns;
- verified commands and environment recipes;
- security and permission invariants;
- architectural decisions that should not be re-litigated;
- repeated bugs or lessons learned.

## What Does Not Belong

- secrets or credentials;
- speculative conclusions;
- temporary task details;
- user private data not needed for development;
- unverified commands;
- stale constraints contradicted by current code.

## Approval Format

When proposing a memory update, identify:

```text
target_file
proposed_addition
evidence
reason
requires_approval
```
