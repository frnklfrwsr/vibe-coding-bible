<!-- VCB:BEGIN_TOPIC id=vcb.codex.agents_md version=0.1.0 -->
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
id: vcb.codex.agents_md
title: AGENTS.md
type: codex_feature
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- Repositories
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: STABLE
shortcut_profiles:
- vcb.shortcut.skipping_agents_md
- vcb.shortcut.overstuffing_agents_md
- vcb.shortcut.stale_agents_md
durable_principles:
- durable repo guidance reduces repeated correction
- instructions should be short, testable, and current
- nested guidance is useful only when it clarifies local context
likely_to_change:
- discovery order and fallback filenames
- size limits and override behavior
- loaded-instruction reporting
- interaction with skills/config/hooks
obsolete_when:
- Codex replaces AGENTS.md with a different official durable instruction mechanism
related_topics:
- vcb.chapter.agents_md_operating_manual
- vcb.codex.config
- vcb.codex.skills
- vcb.codex.hooks
- vcb.chapter.prompt_library_to_team_workflow
---

> Summary:
> AGENTS.md is the durable project instruction file that tells Codex how to work in a repo without retyping the same guidance every task.

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

<!-- VCB:BEGIN_SECTION id=vcb.codex.agents_md.human -->
## 1. For the Human: Plain-Language Concept

### What this means

AGENTS.md is like a short operating manual for Codex. It tells Codex the repo layout, commands, conventions, rules, and “do not do this” items that should apply across tasks.

### Why it matters

It matters because Codex will otherwise rediscover or forget your project rules repeatedly. Good AGENTS.md guidance saves usage and reduces repeated mistakes. Bad AGENTS.md guidance pollutes every task.

### The mental model

AGENTS.md is a label on the toolbox: “use these commands, avoid these traps, and check this before calling the job done.”

### What good looks like

Good use: keep a concise root AGENTS.md with setup commands, test commands, architecture notes, dependency rules, and done criteria.

### What bad looks like

Bad use: paste a giant stale policy document that contradicts the actual repo and forces Codex to drag irrelevant instructions into every task.

### Minimal example

Example: add “Run npm run lint and npm test for changed JavaScript files; ask before adding production dependencies; do not edit generated files.”

### Checklist

- Name the task and the Codex surface explicitly.
- Confirm whether the work is prototype, maintenance, production, or emergency work.
- Choose permissions and attention level before starting.
- Require a diff, report, or artifact that proves what changed.
- Review volatile details against official docs before freezing commands or UI instructions.
<!-- VCB:END_SECTION id=vcb.codex.agents_md.human -->

<!-- VCB:BEGIN_SECTION id=vcb.codex.agents_md.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Turn repeated user corrections into durable, concise, testable repo guidance.

### Diagnose the human’s current model

- What correction has the user repeated more than twice?
- Is the instruction concrete enough to follow?
- Is any guidance stale or contradictory?
- Does the repo need nested guidance for risky subdirectories?

### Explanation strategy

Start with task/surface fit. Explain what this Codex feature is good at, what it does not prove, and which guardrails become mandatory as blast radius grows. Tie the explanation to the user’s actual repository, risk level, and attention budget.

### Useful metaphors

AGENTS.md is the house manual for a contractor. It should say where the breaker box is and what walls not to cut—not contain the whole history of the house.

### Coaching tactics

- Ask the user what surface they are actually using before giving feature-specific advice.
- Separate stable workflow principle from volatile product mechanics.
- Convert broad requests into scoped work orders with explicit done-when criteria.
- Escalate hard for production, secrets, auth, payments, migrations, CI credentials, browser state, or unattended mutation.
- Prefer reviewable artifacts over confident summaries.

### Prompt patterns

```text
Draft or update AGENTS.md with only durable repo guidance: layout, setup commands, test/build/lint commands, dependency rules, risky areas, and done criteria. Keep it short and remove stale advice.
```

### Red flags to call out directly

- AGENTS.md used as a dumping ground
- rules that cannot be checked
- stale commands
- conflicting nested instructions
- user skipping durable guidance in a long-lived repo

### Exercises

1. Ask the human to choose this feature for one low-risk task and one high-risk task, then explain what guardrails change.
2. Ask the human to name which part of this feature is stable principle and which part must be rechecked against official docs.
3. Ask the human to write a final-report template for work done through this feature.
<!-- VCB:END_SECTION id=vcb.codex.agents_md.ai_coach -->

## Shortcut Reality

### The ideal practice

Maintain AGENTS.md as the smallest durable instruction set that prevents repeated Codex mistakes.

### What users often do instead

Users often skip AGENTS.md or overstuff it because both feel easier than curating durable rules.

### When the shortcut may be fine

Skipping is fine for throwaway scripts. Overstuffing may be harmless if the repo is tiny and the file is temporary.

### When the shortcut is a bad idea

Skipping is expensive in long-lived repos. Overstuffing is bad when stale rules affect production tasks.

### Risk profile

- Probability of failure: Medium failure probability from stale or absent guidance
- Impact if it fails: rises sharply with production data, secrets, real users, payments, auth, CI credentials, or deployment paths.
- Ease of recovery: good only when work is branch-isolated, committed, fake-data backed, and reviewable.
- Blast radius: small for local prototypes; large for shared repos, cloud work, external tools, GUI control, and automated mutation.
- Skill needed to recover: low for small Git-backed diffs; medium/high for secrets, data, deployment, or account-state mistakes.
- Hidden cost: stale configuration, noisy automation, false confidence, usage burn, and future maintenance load.

### Minimum guardrails

- write only durable rules
- include commands and do-not-touch areas
- review monthly or after repeated mistakes
- prefer nested guidance only for real local differences
- ask Codex to summarize loaded instructions

### Recovery plan

Remove stale sections, add missing rules from recent failures, ask Codex to report loaded guidance, then rerun the task with explicit constraints.

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

- durable repo guidance reduces repeated correction
- instructions should be short, testable, and current
- nested guidance is useful only when it clarifies local context

## Volatile Surface

- discovery order and fallback filenames
- size limits and override behavior
- loaded-instruction reporting
- interaction with skills/config/hooks

## Obsolescence Watch

- Codex replaces AGENTS.md with a different official durable instruction mechanism

## Evidence and Sources

- `openai.codex.agents_md` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.best_practices` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.customization` — official source anchor for this card's current Codex feature behavior.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for blast radius, recoverability, workflow fit, and AI-coach intervention guidance.

## Related Topics

- `vcb.chapter.agents_md_operating_manual`
- `vcb.codex.config`
- `vcb.codex.skills`
- `vcb.codex.hooks`
- `vcb.chapter.prompt_library_to_team_workflow`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.codex.agents_md -->
