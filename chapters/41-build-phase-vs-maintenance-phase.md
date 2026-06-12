<!-- VCB:BEGIN_TOPIC id=vcb.chapter.build_phase_vs_maintenance_phase version=0.1.0 -->
---
id: vcb.chapter.build_phase_vs_maintenance_phase
title: "Chapter 41 — Build Phase vs Maintenance Phase"
type: chapter
chapter_number: 41
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
- vcb.shortcut.permanent_high_usage_plan
- vcb.shortcut.generated_prototype_as_production_foundation
- vcb.shortcut.overbuilding_first_app
- vcb.shortcut.skipping_maintenance_cleanup

durable_principles:
- Project phase changes the right Codex workflow.
- Maintenance cost matters as much as build speed.
- Launch hardening is a phase, not an afterthought.

likely_to_change:
- product packaging
- current pricing and limits
- model-specific behavior

obsolete_when:
- Codex product behavior or pricing model materially changes.

related_topics:
- vcb.chapter.first_serious_app
- vcb.chapter.budget_aware_codex_workflows
- vcb.chapter.senior_engineer_checklist
- vcb.chapter.maintaining_updating_bible
---

> Summary:
> AI usage should change over the life of a project. Build phases reward exploration and throughput; maintenance rewards narrow changes, low cost, and low surprise.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.build_phase_vs_maintenance_phase.human -->
## 1. For the Human: Plain-Language Concept

### What this means

The same app has different needs at different times. Early on, you need speed and learning. Near launch, you need hardening. After launch, you need stability and cheap maintenance.

Using the same Codex workflow forever is a mistake.

### Phase map

| Phase | Main goal | Codex posture |
|---|---|---|
| Prototype | learn if the idea is worth building | fast, disposable, fake data |
| MVP build | create the first usable vertical slice | small feature slices, review checkpoints |
| Launch hardening | reduce production risk | tests, security review, rollback, docs |
| Maintenance | fix and improve without surprise | narrow tasks, small diffs, cheap checks |
| Major refactor | preserve behavior while changing structure | plan-first, tests, branches, milestones |
| Emergency hotfix | restore service safely | minimal patch, repro, rollback, postmortem note |

### Build-heavy does not mean process-free

A build phase can justify more Codex usage, more parallel work, and faster iteration. It does not justify ignoring Git, tests, secrets, or review.

### Maintenance-heavy does not mean no Codex

Maintenance is where Codex can be cheap and useful if you keep tasks small:

```text
Fix one bug.
Update one doc page.
Review one dependency change.
Summarize one failing CI job.
Add one regression test.
```

### The build-high / maintain-low design rule

Build in a way your future cheaper self can maintain:

- fewer services;
- fewer dependencies;
- clear setup commands;
- real tests for critical paths;
- `AGENTS.md` with durable project rules;
- simple rollback paths;
- documentation for the first operator: you.

<!-- VCB:END_SECTION id=vcb.chapter.build_phase_vs_maintenance_phase.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.build_phase_vs_maintenance_phase.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to name the project phase before choosing task size, review depth, and budget posture.

### Diagnostic questions

- Are we discovering, building, hardening, maintaining, refactoring, or firefighting?
- Is current speed creating future maintenance debt?
- Is the user treating a prototype as if it is production-ready?
- Does the project have commands/tests/docs that support low-cost maintenance?

### Useful metaphor

A project has seasons. You plant differently than you harvest. Build season can be intense; maintenance season should be sustainable.

### Coaching tactics

- In prototype phase, preserve learning and document what must be rebuilt.
- In MVP phase, force vertical slices and checkpoints.
- In launch phase, push review/security/test/rollback harder.
- In maintenance, reject broad “while you’re there” cleanup unless explicitly scoped.

### Red flags

- “Just ship the prototype” with real users or payments.
- “Keep Pro forever because I might need it” without measuring usage.
- “Let’s rewrite it” during a hotfix.
- “Maintenance is boring, skip tests.”

<!-- VCB:END_SECTION id=vcb.chapter.build_phase_vs_maintenance_phase.ai_coach -->

## Shortcut Reality

### The ideal practice

Re-evaluate workflow at every phase change.

### What users often do instead

They keep build-mode speed after launch, or keep prototype shortcuts after user data appears.

### When the shortcut may be fine

Fast prototype mode is fine before real data, real users, or long-term maintenance matters.

### When the shortcut is a bad idea

It is dangerous when production work still uses prototype assumptions: no rollback, no tests, no secrets discipline, no review.

### Risk profile

- Probability of failure: medium/high at phase transitions.
- Impact if it fails: high when users/data/money are present.
- Ease of recovery: good if vertical slices and Git checkpoints exist.
- Blast radius: grows at launch and during refactors.
- Hidden cost: maintenance debt and plan inertia.

### Minimum guardrails

- Declare the phase in prompts.
- Declare whether compatibility matters.
- Require launch hardening before production.
- Review plan/budget monthly.
- Keep a “maintenance commands” section in README/AGENTS.

### Recovery plan

If a prototype slipped into production, freeze new feature work, identify real user/data/security paths, add rollback/backups/logging, write smoke tests, and harden one risk path at a time.

## Budget and Constraint Notes

### Cheapest reliable path

Use high discipline instead of high usage: small scoped tasks, fewer dependencies, and commands that make maintenance cheap.

### Fastest high-usage path

Use high throughput during build and hardening windows, then intentionally downgrade the workflow after stabilization.

### Low-attention path

Maintenance can be low-attention only when work is narrow, checks are reliable, and final reports are evidence-based.

### Production-quality path

Treat launch hardening as required work: tests, review, secrets, monitoring, rollback, docs, and operating notes.

## Stable Core

Project phases are stable. Tool names change, but the distinction between discovery, build, hardening, maintenance, refactor, and emergency work does not.

## Volatile Surface

Current plan economics, cloud delegation features, and automation surfaces change. Review plan strategy when pricing or Codex capabilities change.

## Obsolescence Watch

Obsolete if Codex gains reliable autonomous phase detection, risk-aware plan selection, and native maintenance-cost forecasting. Until then, humans and AI coaches must name the phase explicitly.

## Evidence and Sources

- `openai.codex.workflows` — official Codex workflow examples with context, checks, and reports
- `openai.codex.guide_ai_native_engineering_team` — official guide for AI-native engineering practices and tests as source of truth
- `openai.codex.use_cases.idea_to_proof_of_concept` — official use-case anchor for prototype/proof-of-concept work
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for phase-based operating mode

## Related Topics

- `vcb.chapter.first_serious_app`
- `vcb.chapter.budget_aware_codex_workflows`
- `vcb.chapter.refactoring_without_breaking_everything`
- `vcb.chapter.senior_engineer_checklist`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.build_phase_vs_maintenance_phase -->
