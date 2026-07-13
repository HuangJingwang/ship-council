# Memory Policy

Change Crew uses file-backed memory to preserve project constraints across tasks without hiding them in chat history.

## Memory Files

Long-term memory lives under:

```text
.change-crew/memory/
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

1. If `.change-crew/memory/` exists, read the relevant files.
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

## Red Flags

These thoughts mean STOP; you are rationalizing around memory discipline:

| Thought | Reality |
| --- | --- |
| "This is obvious enough to remember." | Chat history is not durable memory. Write a memory suggestion. |
| "I'll record it at the end." | Explicit memory requests should be captured when they appear. |
| "The new rule is clearly better." | Do not replace old rules without user choice. |
| "This conflict is minor." | Minor ordering or command differences can break verification. Ask. |
| "The current task is unrelated." | Reusable project constraints belong in memory even when discovered during another task. |
| "I can summarize the old rule loosely." | Quote or precisely paraphrase the existing rule before asking the user to choose. |

When this happens:

1. Convert the request into a concrete proposed memory entry.
2. Choose the target memory file, usually `verification-recipes.md`, `coding-constraints.md`, `security-constraints.md`, or `decisions.md`.
3. Check existing memory for overlapping or conflicting rules before writing.
4. In semi-auto mode, ask the user to approve the memory update.
5. In auto mode, write only when automatic memory updates were explicitly allowed and no conflict exists.

## Required Checklist

Before updating long-term memory, you MUST complete these steps:

1. Identify the exact reusable rule.
2. Choose the target memory file.
3. Read the existing target memory file.
4. Read related memory files when the rule touches verification, security, coding style, surfaces, or decisions.
5. Run or perform conflict detection.
6. Record conflict status in `memory-suggestions.md`.
7. Ask for user approval when required.
8. Only then write `.change-crew/memory/...`.

Cannot complete every step? Do not write long-term memory yet.

## Decision Table

| Situation | Action |
| --- | --- |
| No related memory exists | Propose a new memory entry. |
| The same rule already exists | Do not duplicate it; record that memory is already covered. |
| Proposed rule adds detail to an existing rule | Merge only if compatible; otherwise ask. |
| Proposed rule contradicts an existing rule | Ask the user to keep, replace, merge, or reject. |
| Existing rule is broader than proposed rule | Add the new rule as an exception only with user approval. |
| Current code contradicts memory | Treat memory as possibly stale and ask before changing it. |
| Proposed rule includes secrets or credentials | Do not store it; ask for a redacted process instead. |
| Proposed rule is temporary or task-only | Keep it in task artifacts, not long-term memory. |

## Task End

At task end:

1. Write `memory-suggestions.md`.
2. Suggest only reusable knowledge, not one-off task details.
3. Include evidence for every proposed memory update.
4. In semi-auto mode, ask the user before updating `.change-crew/memory/`.
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

## Examples And Non-Examples

### Example: New Verification Recipe

User says: "Before e2e tests, always start the API server, then the web app."

Good:

- propose an update to `verification-recipes.md`;
- check for existing e2e startup rules;
- record `Conflict status: none found` or list conflicts;
- ask for approval before writing in semi-auto mode.

Bad:

- remember it only in chat;
- run tests differently next time without writing project memory.

### Example: Conflicting Order

Existing memory says: "Before e2e tests, start backend before frontend."

User says: "From now on, start frontend before backend for e2e."

Good:

- mark this as a possible direct conflict;
- show both rules;
- ask the user to keep, replace, merge with conditions, or reject both.

Bad:

- overwrite the old rule because the new one is more recent;
- keep both rules without explaining when each applies.

### Non-Example: One-Off Detail

User says: "For this one bug, try running the test once with debug logs."

Good:

- keep it in `verification-report.md` or task notes.

Bad:

- store it as a long-term verification recipe.

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

Only update `.change-crew/memory/` after the user chooses. If the user chooses replacement, move the old rule to a `Superseded` or `History` section when the target memory file has one; otherwise annotate the replacement with the date and reason.

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
