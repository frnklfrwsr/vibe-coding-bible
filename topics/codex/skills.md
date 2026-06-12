<!-- VCB:BEGIN_TOPIC id=vcb.codex.skills version=0.1.0 -->
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
id: vcb.codex.skills
title: Codex Skills
type: codex_feature
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Reusable workflows
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.skill_overkill
- vcb.shortcut.skill_sprawl
- vcb.shortcut.stale_agents_md
durable_principles:
- skills package repeated workflows into reusable instructions and resources
- skills should be narrow, named, and triggerable
- do not create skills for rare one-off tasks
likely_to_change:
- skill file format details
- plugin packaging and distribution
- trigger behavior
- context budget rules
obsolete_when:
- Codex replaces skills with another official reusable-workflow mechanism
related_topics:
- vcb.chapter.skills_reusable_workflows
- vcb.codex.agents_md
- vcb.codex.mcp
- vcb.codex.automations
- vcb.chapter.codex_playbooks
---

> Summary:
> Codex skills are reusable workflow packages: instructions, optional scripts, and supporting files that Codex can load when a repeated task appears.

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

<!-- VCB:BEGIN_SECTION id=vcb.codex.skills.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A skill is a reusable playbook for Codex. If you keep pasting the same instructions for release notes, bug triage, or migration planning, a skill can package that method so Codex knows how to do it again.

### Why it matters

Skills matter because repeated work should not stay trapped in long prompts. But skills also add maintenance. A bad or stale skill can make Codex confidently repeat an old process.

### The mental model

A skill is a recipe card plus optional utensils. It should be specific enough to help and small enough not to clutter the kitchen.

### What good looks like

Good use: create a focused skill for a repeated workflow with clear trigger description, required inputs, method, checks, and output format.

### What bad looks like

Bad use: create dozens of vague skills that overlap, trigger unpredictably, and encode stale team preferences.

### Minimal example

Example: create a “release-notes-draft” skill that reads merged PRs, groups user-visible changes, flags uncertainty, and never invents product impact.

### Checklist

- Name the task and the Codex surface explicitly.
- Confirm whether the work is prototype, maintenance, production, or emergency work.
- Choose permissions and attention level before starting.
- Require a diff, report, or artifact that proves what changed.
- Review volatile details against official docs before freezing commands or UI instructions.
<!-- VCB:END_SECTION id=vcb.codex.skills.human -->

<!-- VCB:BEGIN_SECTION id=vcb.codex.skills.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Help the user recognize repeated prompt patterns and package only the stable workflow part as a skill.

### Diagnose the human’s current model

- Has the same prompt been pasted at least three times?
- Is the workflow stable enough to package?
- Does it need scripts or only instructions?
- How will the user know the skill triggered correctly?

### Explanation strategy

Start with task/surface fit. Explain what this Codex feature is good at, what it does not prove, and which guardrails become mandatory as blast radius grows. Tie the explanation to the user’s actual repository, risk level, and attention budget.

### Useful metaphors

A skill is a jig in a workshop: useful when you repeat the same cut, pointless when every board is different.

### Coaching tactics

- Ask the user what surface they are actually using before giving feature-specific advice.
- Separate stable workflow principle from volatile product mechanics.
- Convert broad requests into scoped work orders with explicit done-when criteria.
- Escalate hard for production, secrets, auth, payments, migrations, CI credentials, browser state, or unattended mutation.
- Prefer reviewable artifacts over confident summaries.

### Prompt patterns

```text
Design a Codex skill for [repeated workflow]. Include when it should trigger, required inputs, step-by-step method, checks, final output format, and cases where it should not run.
```

### Red flags to call out directly

- skill created for a one-off task
- overlapping skill descriptions
- skill hides risky steps
- skill not reviewed after process changes

### Exercises

1. Ask the human to choose this feature for one low-risk task and one high-risk task, then explain what guardrails change.
2. Ask the human to name which part of this feature is stable principle and which part must be rechecked against official docs.
3. Ask the human to write a final-report template for work done through this feature.
<!-- VCB:END_SECTION id=vcb.codex.skills.ai_coach -->

## Shortcut Reality

### The ideal practice

Create skills for repeated, stable workflows where packaged instructions reduce prompt waste and improve consistency.

### What users often do instead

Users often either never create skills and paste huge prompts forever, or create skills for every small preference.

### When the shortcut may be fine

Manual prompts are fine for rare tasks. Extra skills are fine in a disposable experiment.

### When the shortcut is a bad idea

Skill sprawl is bad when Codex spends context deciding among stale, overlapping instructions or triggers the wrong workflow on production work.

### Risk profile

- Probability of failure: Medium failure probability from stale or overlapping skills
- Impact if it fails: rises sharply with production data, secrets, real users, payments, auth, CI credentials, or deployment paths.
- Ease of recovery: good only when work is branch-isolated, committed, fake-data backed, and reviewable.
- Blast radius: small for local prototypes; large for shared repos, cloud work, external tools, GUI control, and automated mutation.
- Skill needed to recover: low for small Git-backed diffs; medium/high for secrets, data, deployment, or account-state mistakes.
- Hidden cost: stale configuration, noisy automation, false confidence, usage burn, and future maintenance load.

### Minimum guardrails

- one job per skill
- clear trigger description
- explicit non-trigger cases
- review skills after process changes
- prefer instructions before scripts unless scripts add real determinism

### Recovery plan

Disable or remove stale skills, inspect recent outputs that used them, merge overlapping skills, and add a test prompt to confirm trigger behavior.

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

- skills package repeated workflows into reusable instructions and resources
- skills should be narrow, named, and triggerable
- do not create skills for rare one-off tasks

## Volatile Surface

- skill file format details
- plugin packaging and distribution
- trigger behavior
- context budget rules

## Obsolescence Watch

- Codex replaces skills with another official reusable-workflow mechanism

## Evidence and Sources

- `openai.codex.skills` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.customization` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.best_practices` — official source anchor for this card's current Codex feature behavior.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for blast radius, recoverability, workflow fit, and AI-coach intervention guidance.

## Related Topics

- `vcb.chapter.skills_reusable_workflows`
- `vcb.codex.agents_md`
- `vcb.codex.mcp`
- `vcb.codex.automations`
- `vcb.chapter.codex_playbooks`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.codex.skills -->
