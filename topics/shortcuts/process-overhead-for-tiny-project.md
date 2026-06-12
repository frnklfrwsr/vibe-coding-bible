<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.process_overhead_for_tiny_project version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-10'
last_reviewed: '2026-06-10'
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
evidence_scope: official OpenAI/Codex skills, MCP, plugins, hooks, best-practices,
  workflow, configuration, and security guidance; official vendor/security documentation
  where cited; VCB maintainer synthesis for tool-sprawl, skill, and process shortcut
  harm reduction
budget_profiles:
- plus_constrained
- pro_high_throughput
- api_pay_as_you_go
- team_shared_budget
cost_postures:
- cheapest_reliable
- balanced
- fastest_possible
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
id: vcb.shortcut.process_overhead_for_tiny_project
title: Process Overhead for Tiny Project
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- solo prototypes
- small scripts
- tiny apps
- repo process
- skills
- hooks
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- process
- prototype
- budget
- maintenance
risk_level:
  prototype: LOW_RISK_SHORTCUT
  personal_tool: LOW_RISK_SHORTCUT
  internal_tool: MODERATE_RISK_SHORTCUT
  public_app: MODERATE_RISK_SHORTCUT
  security_sensitive: HIGH_RISK_SHORTCUT
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- use smallest durable artifact
- promote only after repeated friction
- delete unused process
- favor checklist over ceremony
shortcut_profiles:
- vcb.shortcut.process_overhead_for_tiny_project
durable_principles:
- reuse should reduce repeated risk, not create hidden process drag
- tools, skills, hooks, and workflows need ownership, scope, and deletion criteria
- external tool/context surfaces require provenance, least privilege, and evidence-backed
  review
likely_to_change:
- Codex skill/plugin setup costs
- team workflow features
- process templates and playbooks
- project phase assumptions
obsolete_when:
- Codex can reliably infer project scale and recommend a right-sized durable workflow
  without overfitting to large-team practices
related_topics:
- vcb.constraints.scope_budget
- vcb.constraints.attention_budget
- vcb.shortcut.skill_overkill
- vcb.shortcut.team_workflow_without_team
- vcb.chapter.prompt_library_to_team_workflow
---

# Process Overhead for Tiny Project

> Summary:
> Process overhead for tiny project is adding skills, hooks, plugins, team workflows, long docs, or heavy ceremonies before a small project has repeated friction to justify them.

## Quick Navigation

- 1. For the Human: Plain-Language Concept
- 2. For the AI Coach: How to Teach This to Your Human
- Shortcut Reality
- Budget and Constraint Notes
- Stable Core
- Volatile Surface
- Obsolescence Watch
- Evidence and Sources
- Related Topics

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.process_overhead_for_tiny_project.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A tiny project does not need a full operating system on day one. The shortcut is copying mature-team process into work that needs one clear next step.

### Why it matters

Process has a carrying cost. Too much of it can consume the attention and budget that should go into building, checking, and learning from the first slice.

### What good looks like

Good: “Use the smallest artifact that prevents the next repeat mistake: a saved prompt, a short README note, or one checklist.”

### What bad looks like

Bad: “Create a plugin, skill library, governance doc, release process, and hook stack for a weekend script with one user.”

### Minimal example

For a 200-line personal tool, keep a two-line setup note and one test command. Do not build a team workflow until someone else needs to use it.

### Checklist

- name the repeated friction
- choose the smallest artifact
- avoid role/process theater
- set deletion criteria
- revisit after project grows

<!-- VCB:END_SECTION id=vcb.shortcut.process_overhead_for_tiny_project.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.process_overhead_for_tiny_project.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that process should be earned by repeated need, not borrowed from larger projects for credibility.

### Diagnostic questions

- Is this project disposable, personal, shared, or production-bound?
- What mistake has repeated?
- Would a checklist solve it?
- Who pays maintenance cost?

### Coaching tactics

- cap process artifacts for prototypes
- prefer prompt snippets before skills
- replace ceremony with one acceptance checklist
- schedule process review after milestone changes

### Red flags

- process added before first working slice
- roles invented for one person
- long docs with no owner
- setup takes longer than the task

### Prompt pattern

```text
Right-size the process for this small project. Identify the project phase, repeated friction, minimum useful artifact, process to defer, deletion criteria, and when to promote to skills/hooks/team workflow.
```

<!-- VCB:END_SECTION id=vcb.shortcut.process_overhead_for_tiny_project.ai_coach -->

## Shortcut Reality

### Ideal practice

Add process only when it reduces repeated mistakes, review cost, or onboarding friction more than it costs to maintain.

### What people often do instead

People add mature-process artifacts because they feel safer than shipping a small checked slice.

### When the shortcut may be acceptable

Acceptable to keep process minimal for disposable prototypes, as long as production/security/data work gets explicit guardrails before promotion.

### When it becomes a bad trade

Bad when minimal process becomes an excuse to skip tests, review, secrets handling, or recovery planning for work that is no longer tiny.

### Risk profile

- Probability: high for ambitious solo builders; medium for teams importing templates.
- Impact: low for disposable prototypes; medium when process hides real verification gaps.
- Recoverability: high if artifacts are small and deletable; lower if workflows and tools depend on them.

### Blast radius

Over-process burns attention and can make the human avoid the actual build-review-recover loop.

### Minimum guardrails

- use smallest durable artifact
- promote only after repeated friction
- delete unused process
- favor checklist over ceremony

### Recovery plan

1. Inventory process artifacts.
2. Keep only the artifact tied to a repeated mistake.
3. Archive the rest.
4. Return to one current milestone and one acceptance check.
5. Set a promotion rule for when the project grows.

## Budget and Constraint Notes

### Cheapest reliable path

Use the smallest durable artifact that prevents the next likely mistake. That may be a saved prompt, one disabled-by-default skill, one scoped MCP server, one report-only hook, or one short workflow note.

### Fastest high-usage path

High-throughput users should template only the workflows that repeat. Spend throughput on clear inputs, expected outputs, and review evidence rather than on broad libraries of tools, skills, hooks, or ceremonies.

### Low-attention path

Low-attention delegation needs stricter defaults: fewer enabled tools, explicit triggers, report-only or read-only behavior first, branch isolation, and a required review packet before mutation is accepted.

### Production-quality path

Production-quality work requires provenance, least privilege, maintained guidance, current setup facts, artifact-backed review, and deletion or disablement paths for unused process surfaces.

### Prototype versus production

A prototype may stay light and messy if it is disposable. Once the work becomes shared, persistent, security-sensitive, or production-bound, the shortcut needs explicit boundaries and review evidence.

### Maintenance phase

Maintenance is where tool/process shortcuts compound. Review skills, hooks, MCP servers, plugins, tool choices, and reusable workflows after stack changes, onboarding, incidents, repeated failures, and major phase transitions.

## Stable Core

- reuse should reduce repeated risk, not create hidden process drag
- tools, skills, hooks, and workflows need ownership, scope, and deletion criteria
- external tool/context surfaces require provenance, least privilege, and evidence-backed review

## Volatile Surface

- Codex skill/plugin setup costs
- team workflow features
- process templates and playbooks
- project phase assumptions

## Obsolescence Watch

This card should be revised if:

- Codex can reliably infer project scale and recommend a right-sized durable workflow without overfitting to large-team practices

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for goals, context, constraints, done-when criteria, planning, checks, review, and reusable project guidance.
- `openai.codex.skills` — Official OpenAI Codex skills guidance for SKILL.md structure, progressive disclosure, invocation, skill locations, plugin distribution, and best practices.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.constraints.scope_budget`
- `vcb.constraints.attention_budget`
- `vcb.shortcut.skill_overkill`
- `vcb.shortcut.team_workflow_without_team`
- `vcb.chapter.prompt_library_to_team_workflow`


<!-- VCB:STOP_RETRIEVAL reason="process_overhead_for_tiny_project_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.process_overhead_for_tiny_project -->
