# Grill Gate

Purpose: sharpen a plan with one high-value question at a time before contract, approval, or implementation.

Use when: a missing answer could change scope, contract, risk, test plan, rollout, or acceptance criteria.

Do:
- Search repo/artifacts first; do not ask what can be discovered.
- Ask one question only.
- Make the question adversarial but useful.
- Explain in one sentence what decision the answer affects.
- Stop after 3-5 questions, or earlier when the contract is stable.

Question filter:
- Would a different answer change the implementation?
- Would it expose a hidden user, data, security, or migration risk?
- Would it split one task into multiple tasks?
- Would it change acceptance criteria or verification?

Never:
- Ask broad questionnaires.
- Ask preference questions disguised as blockers.
- Continue grilling after the riskiest branch is resolved.
- Use grilling to avoid implementing a clear task.

Output:
```text
question:
why_it_matters:
affected_artifact: prd|contract|test-plan|implementation-plan|risk
stop_or_continue:
```
