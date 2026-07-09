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

## Explicit Memory Capture

<MEMORY-CAPTURE-GATE>
When the user asks to preserve a reusable preference, workflow, command order, verification recipe, constraint, or forbidden pattern, treat it as a memory-capture event. Do not leave it only in chat history.
</MEMORY-CAPTURE-GATE>

Treat the user's wording as an explicit memory request when they say things like:

- "remember this";
- "from now on";
- "always";
- "never";
- "before every test";
- "every time";
- "this is the required flow";
- "do not do X again";
- "use this as the rule".

## Anti-Pattern: "This Is Just A Small Preference"

Small preferences become future regressions when they affect repeated development behavior. If the preference changes how future tasks should be planned, implemented, reviewed, or verified, capture it as a memory suggestion.

When this happens:

1. Convert the request into a concrete proposed memory entry.
2. Choose the target memory file, usually `verification-recipes.md`, `coding-constraints.md`, `security-constraints.md`, or `decisions.md`.
3. Check existing memory for overlapping or conflicting rules before writing.
4. In semi-auto mode, ask the user to approve the memory update.
5. In auto mode, write only when automatic memory updates were explicitly allowed and no conflict exists.

## Task End

At task end:

1. Write `memory-suggestions.md`.
2. Suggest only reusable knowledge, not one-off task details.
3. Include evidence for every proposed memory update.
4. In semi-auto mode, ask the user before updating `.ship-council/memory/`.
5. In auto mode, do not update long-term memory unless the user explicitly allowed automatic memory writes.

## Conflict Detection

<MEMORY-CONFLICT-GATE>
Do NOT update long-term memory until the target memory file and related memory files have been checked for conflicts. If a possible conflict exists, do NOT overwrite, delete, or supersede the existing rule. Ask the user to choose keep, replace, merge, or reject.
</MEMORY-CONFLICT-GATE>

Before writing any long-term memory update:

1. Read the target memory file and any related memory files.
2. Compare the proposed rule against existing rules for:
   - opposite instructions, such as "always start A" vs "never start A";
   - changed ordering, such as "run backend before frontend" vs "run frontend before backend";
   - different commands for the same verification step;
   - different ports, services, environments, credentials, branches, modules, or scripts;
   - narrower exceptions that should be merged rather than replacing the general rule;
   - stale rules contradicted by current repository files.
3. Use `scripts/check_memory_conflicts.py` to surface nearby existing rules when useful.
4. If there is no conflict, record `Conflict status: none found`.
5. If there is a possible conflict, record it in `memory-suggestions.md` and ask the user to choose.

Do not silently overwrite, delete, or supersede an existing memory rule.

## Conflict Resolution

When conflicts exist, present the user with choices:

```text
Conflict:
- Existing rule: ...
- Proposed rule: ...
- Why they conflict: ...

Choose one:
1. Keep existing rule
2. Replace with proposed rule
3. Merge both with conditions
4. Reject both and write a new rule
```

Only update `.ship-council/memory/` after the user chooses. If the user chooses replacement, move the old rule to a `Superseded` or `History` section when the target memory file has one; otherwise annotate the replacement with the date and reason.

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
conflict_status
conflicting_existing_rules
user_decision_required
requires_approval
```
