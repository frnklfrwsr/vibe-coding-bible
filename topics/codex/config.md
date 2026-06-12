<!-- VCB:BEGIN_TOPIC id=vcb.codex.config version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
audiences:
- human
- ai_coach
source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: official OpenAI product behavior anchors plus VCB maintainer synthesis
  for risk, workflow, and coaching guidance
budget_profiles:
- plus_constrained
- pro_high_throughput
- api_pay_as_you_go
- team_shared_budget
cost_postures:
- cheapest_reliable
- balanced
- fastest_possible
- unattended_high_throughput
- production_quality
project_phases:
- prototype
- mvp
- production_build
- maintenance
- emergency_hotfix
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.codex.config
title: Codex Config
type: codex_feature
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex CLI
- Codex IDE Extension
- Local repositories
- Project configuration
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.default_config_forever
- vcb.shortcut.broad_agent_permissions
durable_principles:
- config turns repeated runtime choices into defaults
- project config should be trusted deliberately
- profiles help separate prototype speed from production safety
likely_to_change:
- config keys and precedence details
- profile mechanics
- trusted-project behavior
- approval and sandbox setting names
obsolete_when:
- Codex no longer uses config files or official config precedence changes materially
related_topics:
- vcb.chapter.codex_config_defaults
- vcb.codex.cli
- vcb.codex.ide_extension
- vcb.codex.mcp
- vcb.codex.hooks
- vcb.safety.permissions
---

> Summary:
> Codex config is how repeated default behavior—permissions, profiles, sandboxing, MCP, and related settings—becomes durable instead of retyped every session.

## Quick Navigation
- For the Human
- For the AI Coach
- Shortcut Reality
- Budget and Constraint Notes
- Stable Core
- Volatile Surface
- Obsolescence Watch
- Evidence and Sources
- Related Topics

<!-- VCB:BEGIN_SECTION id=vcb.codex.config.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Codex config is the settings layer for how Codex should behave by default. Prompts say what to do for this task. Config says what Codex is allowed to do, what profile it should use, and what durable setup applies before the task starts.

### Why it matters

Config matters because repeated decisions waste attention. If you always want a safer sandbox for production repos or a faster profile for throwaway experiments, that belongs in config or profiles, not in memory and vibes.

### The mental model

Config is the shop’s default safety setup. You can override it for a specific job, but bad defaults make every job noisier or riskier.

### What good looks like

Good use: keep conservative defaults, create separate profiles for prototype and production work, and use project config only in trusted projects.

### What bad looks like

Bad use: one global full-access config for every repo, including projects with secrets, production credentials, or sensitive data.

### Minimal example

Example: create a production-review profile that prefers read-only or workspace-bounded behavior and a prototype profile for isolated disposable repos.

### Checklist

- Name the task and the Codex surface explicitly.
- Confirm whether the work is prototype, maintenance, production, or emergency work.
- Choose permissions and attention level before starting.
- Require a diff, report, or artifact that proves what changed.
- Review volatile details against official docs before freezing commands or UI instructions.
<!-- VCB:END_SECTION id=vcb.codex.config.human -->

<!-- VCB:BEGIN_SECTION id=vcb.codex.config.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach config as durable defaults that must reflect risk class, not convenience alone.

### Diagnose the human’s current model

- Is the user repeating the same setup instructions?
- Does current config match project risk?
- Is the repo trusted enough for project-local config?
- Would a profile prevent accidental broad permissions?

### Explanation strategy

Start with task/surface fit. Explain what this Codex feature is good at, what it does not prove, and which guardrails become mandatory as blast radius grows. Tie the explanation to the user’s actual repository, risk level, and attention budget.

### Useful metaphors

Config is the seatbelt setting. You do not want to negotiate it every time the car starts.

### Coaching tactics

- Ask the user what surface they are actually using before giving feature-specific advice.
- Separate stable workflow principle from volatile product mechanics.
- Convert broad requests into scoped work orders with explicit done-when criteria.
- Escalate hard for production, secrets, auth, payments, migrations, CI credentials, browser state, or unattended mutation.
- Prefer reviewable artifacts over confident summaries.

### Prompt patterns

```text
Before changing config, inspect current Codex configuration layers and summarize what each layer controls. Recommend the smallest config change that solves repeated friction without broadening permissions unnecessarily.
```

### Red flags to call out directly

- full-access defaults
- project config in an untrusted repo
- config used to hide risky permission choices
- old profile still used after project risk changes

### Exercises

1. Ask the human to choose this feature for one low-risk task and one high-risk task, then explain what guardrails change.
2. Ask the human to name which part of this feature is stable principle and which part must be rechecked against official docs.
3. Ask the human to write a final-report template for work done through this feature.
<!-- VCB:END_SECTION id=vcb.codex.config.ai_coach -->

## Shortcut Reality

### The ideal practice

Use config to make safe defaults automatic and reserve overrides for explicit, understood exceptions.

### What users often do instead

Users often leave defaults forever or use one global config because it “works.”

### When the shortcut may be fine

This is fine until repeated friction or risk appears, especially in tiny prototypes.

### When the shortcut is a bad idea

It is bad when the same config is used for production, secrets, CI, or destructive tasks as for disposable experiments.

### Risk profile

- Probability of failure: Medium probability of hidden risk
- Impact if it fails: rises sharply with production data, secrets, real users, payments, auth, CI credentials, or deployment paths.
- Ease of recovery: good only when work is branch-isolated, committed, fake-data backed, and reviewable.
- Blast radius: small for local prototypes; large for shared repos, cloud work, external tools, GUI control, and automated mutation.
- Skill needed to recover: low for small Git-backed diffs; medium/high for secrets, data, deployment, or account-state mistakes.
- Hidden cost: stale configuration, noisy automation, false confidence, usage burn, and future maintenance load.

### Minimum guardrails

- document intended profiles
- keep production defaults conservative
- review project-local config before trusting a repo
- avoid full access as default
- update config after repeated mistakes

### Recovery plan

Revert config to conservative defaults, identify sessions run under unsafe config, inspect affected diffs/logs, rotate secrets if exposed, and create clearer profiles.

### AI coach guidance

Do not moralize the shortcut. Name the tradeoff, reduce blast radius, improve recoverability, and require the smallest guardrail that changes the risk profile.

## Budget and Constraint Notes

### Cheapest reliable path

Use this feature for one narrow task with curated context, conservative permissions, and one relevant check. Do not spend usage exploring broad unknowns unless the task is important enough to justify it.

### Fastest high-usage path

Use this feature aggressively only with branch/worktree isolation, clear acceptance criteria, structured final reports, and independent review for risky diffs.

### Low-attention path

Low-attention work requires stronger isolation, report-only or read-only posture when possible, fake credentials, and a final report that names files changed, checks run, unresolved risks, and review needs.

### Production-quality path

Use least privilege, clear done-when criteria, Git checkpoints, tests/build/lint where relevant, diff review, source-register discipline, and a rollback plan before accepting work.

## Stable Core

- config turns repeated runtime choices into defaults
- project config should be trusted deliberately
- profiles help separate prototype speed from production safety

## Volatile Surface

- config keys and precedence details
- profile mechanics
- trusted-project behavior
- approval and sandbox setting names

## Obsolescence Watch

- Codex no longer uses config files or official config precedence changes materially

## Evidence and Sources

- `openai.codex.config_basic` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.config_reference` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.config_advanced` — official source anchor for this card's current Codex feature behavior.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for blast radius, recoverability, workflow fit, and AI-coach intervention guidance.

## Related Topics

- `vcb.chapter.codex_config_defaults`
- `vcb.codex.cli`
- `vcb.codex.ide_extension`
- `vcb.codex.mcp`
- `vcb.codex.hooks`
- `vcb.safety.permissions`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.codex.config -->
