<!-- VCB:BEGIN_TOPIC id=vcb.chapter.choosing_codex_operating_mode version=0.1.0 -->
---
id: vcb.chapter.choosing_codex_operating_mode
title: "Chapter 39 — Choosing Your Codex Operating Mode"
type: chapter
chapter_number: 39
version: 0.1.0
last_verified: '2026-06-09'
next_review_due: '2026-09-09'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- all project types

source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE

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
- disposable_prototype

project_phases:
- prototype
- mvp
- production_build
- maintenance
- major_refactor
- emergency_hotfix

attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation

shortcut_profiles:
- vcb.shortcut.process_overhead_for_tiny_project
- vcb.shortcut.unattended_long_runs
- vcb.shortcut.broad_agent_permissions
- vcb.shortcut.defaulting_to_high_throughput

durable_principles:
- Fit workflow to constraints instead of copying someone else’s setup.
- Spend attention when usage is scarce; spend usage when attention is scarce and risk is contained.
- Production work needs both more usage and more human review.

likely_to_change:
- product packaging
- current pricing and limits
- model-specific behavior

obsolete_when:
- Codex product behavior or pricing model materially changes.

related_topics:
- vcb.chapter.budget_aware_codex_workflows
- vcb.chapter.build_phase_vs_maintenance_phase
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.chapter.risk_managed_shortcuts
---

> Summary:
> There is no universal best Codex workflow. The right operating mode depends on budget, risk, phase, attention, test coverage, and recoverability.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.choosing_codex_operating_mode.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Your Codex operating mode is the way you usually use Codex on a project. It includes the surface you choose, the size of tasks you hand over, how much permission you grant, how often you check in, and what evidence you require before accepting work.

A good operating mode is not the fanciest one. It is the one that fits the situation.

### The operating-mode inputs

Before choosing a workflow, answer these questions:

| Input | Question | Why it matters |
|---|---|---|
| Usage budget | Am I constrained or high-throughput? | Determines whether to spend attention or usage. |
| Project phase | Prototype, build, maintenance, refactor, hotfix? | Determines how much exploration is worth it. |
| Risk | Does this touch real users, data, auth, payments, secrets, or deploys? | Determines guardrail strength. |
| Attention | Will I supervise, check periodically, or review later? | Low attention requires stronger isolation. |
| Test suite | Do checks catch real breakage? | Weak checks mean more manual review. |
| Recoverability | Can I undo safely? | Easy rollback permits more speed. |

### The common modes

| Mode | Use when | Avoid when |
|---|---|---|
| Manual-guided | low usage, high risk, unclear task | task is boring and well-scoped |
| Small scoped Codex task | most maintenance and feature slices | task is cross-cutting and ambiguous |
| Plan-first task | unknown repo, refactor, security-sensitive work | typo-sized edits |
| High-throughput delegation | lots of usage, isolated branches, review later | same files, production secrets, poor rollback |
| Report-only automation | CI, audits, recurring checks | you need immediate mutation |
| Production-quality mode | real users/data/money involved | disposable prototype |

### The wrong question

The wrong question is:

```text
What is the best Codex workflow?
```

The better question is:

```text
Given this budget, risk, attention level, and rollback path, what is the cheapest workflow that is still safe enough?
```

### Minimal operating-mode prompt

```text
Choose the right Codex operating mode for this task.

Project phase:
Usage budget:
Human attention:
Risk areas:
Test/check coverage:
Rollback path:

Recommend:
- task size,
- Codex surface,
- permission level,
- review/check requirements,
- when to stop and ask me.
```

<!-- VCB:END_SECTION id=vcb.chapter.choosing_codex_operating_mode.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.choosing_codex_operating_mode.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to choose workflows by constraints, not habit or status. The target behavior is explicit tradeoff selection.

### Diagnose the human’s current model

Ask:

- Are they defaulting to high-throughput because it feels advanced?
- Are they defaulting to manual work because they fear using usage?
- Are they treating prototype and production work the same?
- Are they trying to leave Codex unattended without isolation?

### Useful metaphor

Codex operating modes are driving modes. City traffic, racetrack, and snowstorm do not use the same speed, steering, or braking distance.

### Coaching tactics

- Start with risk: secrets, auth, payments, production data, deploys.
- Then ask attention: present, periodic, review later.
- Then ask recoverability: branch, rollback, backup, fake data.
- Then choose surface and task size.

### Red flags to call out directly

- “I want Codex to handle everything while I’m gone” with production access.
- “This is just a prototype” while using real auth, real payments, or real data.
- “I have Pro, so I should use parallel agents” when the task touches the same files.

### Prompt pattern

```text
Do not implement yet. First classify this task by risk, attention requirement, recoverability, and budget posture. Then recommend the smallest safe operating mode.
```

<!-- VCB:END_SECTION id=vcb.chapter.choosing_codex_operating_mode.ai_coach -->

## Shortcut Reality

### The ideal practice

Choose an operating mode deliberately before each major task.

### What users often do instead

They copy the last workflow that felt good: one big prompt, full permissions, cloud delegation, or manual micromanagement.

### When the shortcut may be fine

Habit-based mode selection is acceptable for repeated low-risk tasks in the same repo when the failure pattern is already understood.

### When the shortcut is a bad idea

It is a bad idea when project phase, risk, or attention level changes: prototype to production, local to cloud, fake data to real data, supervised to unattended.

### Risk profile

- Probability of failure: medium when context changes.
- Impact if it fails: low for prototypes, high for production/secrets/data.
- Ease of recovery: depends on branch, backup, and rollback.
- Blast radius: grows sharply with permissions and unattended work.
- Skill needed to recover: low for code-only branches, high for data/security failures.
- Hidden cost: wasted usage, tool sprawl, and unreviewable diffs.

### Minimum guardrails

- Name the project phase.
- Name the risk areas.
- Choose attention mode.
- Set permission level.
- Require evidence before acceptance.

### Recovery plan

If the chosen mode was too aggressive, stop Codex, inspect Git status, isolate intended changes from accidental changes, roll back unsafe diffs, and restart with a narrower mode.

### AI coach guidance

Do not debate whether the user is “doing it right.” Reframe the decision as fit-to-context.

## Budget and Constraint Notes

### Cheapest reliable path

Use short tasks, curated context, plan-only where uncertainty is high, and the smallest relevant check.

### Fastest high-usage path

Use cloud tasks, worktrees, subagents, and fresh reviews only when tasks are isolated and reviewable.

### Low-attention path

Prefer report-only, read-only, or isolated branch/worktree workflows. Low attention does not justify broad mutation.

### Production-quality path

Use plan-first, scoped permissions, tests/checks, diff review, PR review, rollback, and post-change monitoring.

## Stable Core

The stable principle is constraint matching: budget, risk, attention, phase, test coverage, and recoverability determine the workflow. This remains true even as Codex surfaces and plans change.

## Volatile Surface

Plan names, included usage, credit rates, model routing, cloud availability, and feature packaging are volatile. Exact values belong in dated pricing snapshots and current official docs.

## Obsolescence Watch

Review when OpenAI changes Codex plan packaging, usage limits, model routing, cloud/local feature access, or credit economics. Obsolete if Codex introduces a native workflow recommender that reliably accounts for risk, budget, and recoverability.

## Evidence and Sources

- `openai.codex.best_practices` — official OpenAI source for plan-first, validation, and durable guidance anchors
- `openai.codex.pricing` — official OpenAI anchor for volatile plan and usage constraints
- `openai.help.codex_chatgpt_plan` — official Help Center source for plan-based Codex usage and limits
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for risk/attention/recoverability operating modes

## Related Topics

- `vcb.chapter.budget_aware_codex_workflows`
- `vcb.chapter.build_phase_vs_maintenance_phase`
- `vcb.chapter.cost_benefit_analysis`
- `vcb.concepts.blast_radius`
- `vcb.concepts.recoverability`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.choosing_codex_operating_mode -->
