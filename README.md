# Ship Council

Multi-agent development workflow for Codex.

Ship Council turns one software change request into a structured loop:

```text
intake -> impact -> research -> debate -> critique -> contract -> test plan -> build -> review -> secure -> verify -> fix -> ship
```

It is a Codex Skill for coordinating work across one or more app surfaces: backend, web, mobile, desktop, data, infrastructure, docs, and tests. It is designed for monorepos, single-service repositories, and mixed stacks.

## Why

Most agentic coding failures happen at the handoff boundaries:

- frontend and backend implement different contracts;
- UI agents ship generic layouts that ignore the product's design system;
- proposal authors drift into agreeable, optimistic plans without an independent critic;
- review finds problems but does not turn them into actionable work;
- security checks are skipped or mixed into normal review;
- hidden callers, migrations, rollback, and docs are forgotten;
- verification is claimed without running commands;
- agents debate forever instead of shipping.

Ship Council makes those boundaries explicit with artifacts, gates, and bounded fix loops.

## Install

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/OWNER/ship-council /tmp/ship-council
cp -R /tmp/ship-council/skills/ship-council ~/.codex/skills/
```

For cross-agent installs, copy the same skill folder into `~/.agents/skills/`.

## Use

```text
Use ship-council to implement organization filtering in the work item list.
```

Auto mode:

```text
Use ship-council in auto mode, up to 3 fix loops, to add password reset across web and backend.
```

Ship Council creates a task workspace in the target repository:

```text
.ship-council/tasks/2026-07-09-org-filter/
  ship-council.json
  prd.md
  surface-map.md
  impact-analysis.md
  research.md
  deliberation.md
  proposal-critique.md
  contract.md
  test-plan.md
  environment-report.md
  implementation-plan.md
  findings/
  fix-packets/
  git-pr-plan.md
  verification-report.md
  retrospective.md
  memory-suggestions.md
  final-report.md
```

Long-term project constraints can live beside task history:

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

Ship Council suggests memory updates at the end of a task. In normal mode, it does not write long-term memory without approval.

## Design Principles

- Debate before coding.
- Independent critique before major approval.
- Contract before parallel work.
- Impact analysis before contract.
- Test strategy before implementation.
- Files over paraphrased handoffs.
- Review and security are read-only gates.
- Findings become fix packets.
- Verification must run, not pretend.
- Documentation and rollout are checked before done.
- Design-heavy web/mobile tasks route to specialist design guidance instead of inventing a generic UI.
- Reusable constraints become explicit memory suggestions.
- Loops have a time-to-live.

## Included Tooling

- task workspace initialization
- surface detection
- command discovery
- artifact validation
- finding-to-fix-packet generation
- long-term memory initialization
- reusable agent brief templates

## Architecture

The skill follows Codex's progressive-disclosure layout:

- `SKILL.md` is the small trigger and orchestration entrypoint.
- `references/` contains policy, workflow, and agent guidance that should be read only when relevant.
- `references/agent-briefs/` contains reusable subagent prompts for research, critique, implementation, review, security, and verification.
- `assets/templates/` contains files copied into a target repository's `.ship-council/tasks/...` workspace.
- `scripts/` contains deterministic helpers for task initialization, surface detection, command discovery, validation, and fix packet generation.

## Examples

- [Backend-only change](examples/backend-only.md)
- [Web and backend change](examples/web-backend.md)

## Demo

- [Organization filter demo](demo/org-filter-demo.md)

## Repository Layout

```text
skills/ship-council/
  SKILL.md
  agents/openai.yaml
  references/
    agent-briefs/
  assets/templates/
  scripts/
```

## License

MIT
