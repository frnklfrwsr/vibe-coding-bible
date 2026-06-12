<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.skill_sprawl version=0.1.0 -->
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
id: vcb.shortcut.skill_sprawl
title: Skill Sprawl
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- Codex skills
- skill descriptions
- plugin-bundled skills
- team skill libraries
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- skills
- context_budget
- maintenance
- team_workflow
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: MODERATE_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: HIGH_RISK_SHORTCUT
  security_sensitive: HIGH_RISK_SHORTCUT
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- one job per skill
- audit overlapping descriptions
- disable unused skills
- write non-trigger cases
shortcut_profiles:
- vcb.shortcut.skill_sprawl
durable_principles:
- reuse should reduce repeated risk, not create hidden process drag
- tools, skills, hooks, and workflows need ownership, scope, and deletion criteria
- external tool/context surfaces require provenance, least privilege, and evidence-backed
  review
likely_to_change:
- skill discovery ordering
- description truncation behavior
- skill disablement controls
- team/admin skill locations
obsolete_when:
- Codex offers reliable skill conflict detection, trigger simulation, and automated
  stale-skill retirement
related_topics:
- vcb.codex.skills
- vcb.shortcut.skill_overkill
- vcb.failure.context_pollution
- vcb.prompting.context_management
- vcb.constraints.review_budget
---

# Skill Sprawl

> Summary:
> Skill sprawl is installing or writing many overlapping skills until Codex cannot reliably pick the right one and humans cannot maintain the set.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.skill_sprawl.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A large skill collection sounds powerful, but Codex has to decide which skill to use. If many skills overlap, the selection step becomes noisy.

### Why it matters

OpenAI documents that skills depend on names, descriptions, and progressive disclosure. Too many broad descriptions create selection ambiguity and maintenance drag.

### What good looks like

Good: “Maintain a small skill set with distinct names, specific trigger phrases, explicit non-trigger cases, and disabled stale skills.”

### What bad looks like

Bad: “Install every interesting skill, leave all enabled, and expect Codex to infer the right workflow from overlapping descriptions.”

### Minimal example

Two skills named “frontend helper” and “UI reviewer” both mention accessibility, screenshots, and CSS. Merge, rename, or split their triggers before relying on implicit invocation.

### Checklist

- list all enabled skills
- group overlaps by trigger phrase
- disable stale or unused skills
- add non-trigger examples
- test prompts against descriptions

<!-- VCB:END_SECTION id=vcb.shortcut.skill_sprawl.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.skill_sprawl.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that skill libraries need information architecture. More skills can mean worse retrieval.

### Diagnostic questions

- Which skills overlap in name or description?
- Which skills have not been used recently?
- Do descriptions front-load the real trigger?
- Can the human explain when each skill should not run?

### Coaching tactics

- run a skill audit before adding another one
- make descriptions narrower before writing more instructions
- disable unused skills instead of deleting immediately
- create a “skill map” for teams

### Red flags

- three skills claim the same workflow
- skill descriptions are long and generic
- Codex keeps choosing the wrong skill
- no one owns stale skill cleanup

### Prompt pattern

```text
Audit this Codex skill set. Identify overlapping triggers, ambiguous names, stale skills, skills that should be disabled, and concise description rewrites with explicit non-trigger cases.
```

<!-- VCB:END_SECTION id=vcb.shortcut.skill_sprawl.ai_coach -->

## Shortcut Reality

### Ideal practice

Keep skills small, distinct, and reviewed. A skill library should behave like a clean route map, not a junk drawer.

### What people often do instead

People accumulate skills because each one seems individually useful. The collection becomes less reliable than a small set of prompts.

### When the shortcut may be acceptable

Acceptable while exploring locally if unused skills are disabled and no team or production workflow depends on implicit selection.

### When it becomes a bad trade

Bad when a shared repo or team starts relying on overlapping skills that can trigger different instructions for the same task.

### Risk profile

- Probability: medium once more than a few skills are installed; high in teams without ownership.
- Impact: medium for wrong workflow selection; high if the wrong skill changes tests, dependencies, or security-sensitive code.
- Recoverability: medium: disabling is easy, but finding which runs were affected may require review.

### Blast radius

Skill sprawl can pollute many future sessions through implicit invocation, stale instructions, and hidden dependencies.

### Minimum guardrails

- one job per skill
- audit overlapping descriptions
- disable unused skills
- write non-trigger cases

### Recovery plan

1. Export/list enabled skills.
2. Disable or explicit-only the overlapping set.
3. Re-run recent affected tasks with no skills or one named skill.
4. Rewrite descriptions and document ownership.

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

- skill discovery ordering
- description truncation behavior
- skill disablement controls
- team/admin skill locations

## Obsolescence Watch

This card should be revised if:

- Codex offers reliable skill conflict detection, trigger simulation, and automated stale-skill retirement

## Evidence and Sources

- `openai.codex.skills` — Official OpenAI Codex skills guidance for SKILL.md structure, progressive disclosure, invocation, skill locations, plugin distribution, and best practices.
- `openai.codex.config_basic` — Official OpenAI Codex config basics for config precedence, trusted project layers, approval/sandbox settings, and project/user config boundaries.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.skills`
- `vcb.shortcut.skill_overkill`
- `vcb.failure.context_pollution`
- `vcb.prompting.context_management`
- `vcb.constraints.review_budget`


<!-- VCB:STOP_RETRIEVAL reason="skill_sprawl_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.skill_sprawl -->
