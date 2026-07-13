# Loop Policy

Fix loops convert evidence into bounded development work.

## Loop Limits

Default auto-mode loop limit: 3.

Stop early when:

- the same finding remains open after two fix attempts;
- a fix would change product, permission, or data-retention policy;
- the agent lacks credentials or runtime access;
- verification failure points to an environment issue the agent cannot resolve;
- three unrelated fixes reveal an architectural mismatch.

## Fix Packet Requirements

Every fix packet must include:

```text
source_finding
target_surface
target_agent
severity
files_in_scope
required_changes
out_of_scope
acceptance_checks
loop_index
```

Never send a vague retry instruction. If a finding cannot be converted into a fix packet, escalate to the user or mark it with a justified status.

## Root Cause Rule

For verification failures and repeated findings, investigate root cause before patching. Do not stack speculative fixes.
