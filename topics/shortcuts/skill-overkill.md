<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.skill_overkill version=0.1.0 -->
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
id: vcb.shortcut.skill_overkill
title: Skill Overkill
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- Codex skills
- SKILL.md
- reusable workflows
- saved prompts
- plugins
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- skills
- reusable_workflows
- process
- context_budget
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
- use a saved prompt first
- promote only after repeated use
- define trigger and non-trigger cases
- prefer instruction-only skills until scripts are justified
shortcut_profiles:
- vcb.shortcut.skill_overkill
durable_principles:
- reuse should reduce repeated risk, not create hidden process drag
- tools, skills, hooks, and workflows need ownership, scope, and deletion criteria
- external tool/context surfaces require provenance, least privilege, and evidence-backed
  review
likely_to_change:
- skill invocation mechanics
- skill discovery limits
- plugin distribution behavior
- UI controls for skill enablement
obsolete_when:
- Codex provides automatic skill lifecycle analysis that reliably promotes, scopes,
  and retires reusable workflows without hidden trigger risk
related_topics:
- vcb.codex.skills
- vcb.prompting.four_part_prompt
- vcb.constraints.scope_budget
- vcb.shortcut.process_overhead_for_tiny_project
---

# Skill Overkill

> Summary:
> Skill overkill is turning a one-off prompt or barely repeated workflow into a Codex skill before the workflow has stable triggers, inputs, outputs, and maintenance ownership.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.skill_overkill.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A skill is useful when the same workflow keeps coming back. The shortcut is creating a formal skill because it feels more professional, not because the workflow has earned a durable wrapper.

### Why it matters

Every skill adds discovery, naming, trigger, and review cost. A premature skill can fire at the wrong time, hide assumptions in SKILL.md, or crowd out simpler project context.

### What good looks like

Good: “Keep a saved prompt until the workflow repeats several times with stable inputs and a predictable output. Then convert the proven pattern into a narrow skill.”

### What bad looks like

Bad: “Create a skill for one weird migration task, give it a broad description, and let Codex invoke it on unrelated future work.”

### Minimal example

Before creating a “release helper” skill, use the same prompt for three releases. If the inputs, output format, and checks stay stable, promote it.

### Checklist

- count how often the workflow repeats
- write trigger and non-trigger examples
- start instruction-only
- keep the skill scoped to one job
- set a review date

<!-- VCB:END_SECTION id=vcb.shortcut.skill_overkill.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.skill_overkill.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to distinguish reuse from premature abstraction. A skill should remove repeated friction, not make a one-off task look mature.

### Diagnostic questions

- Has this workflow repeated with the same inputs and outputs?
- Would a saved prompt be enough?
- What exact phrase should trigger the skill?
- What should never trigger it?

### Coaching tactics

- ask for repeat evidence before skill creation
- draft non-trigger cases with the human
- prefer instruction-only first
- schedule deletion if the skill is not reused

### Red flags

- skill created for a one-time task
- description contains vague words like “help with coding”
- skill includes scripts before the workflow is stable
- no owner or review date

### Prompt pattern

```text
Decide whether this should become a Codex skill. List repeated use evidence, stable inputs, stable outputs, trigger cases, non-trigger cases, whether a saved prompt is enough, and the smallest skill shape if promotion is justified.
```

<!-- VCB:END_SECTION id=vcb.shortcut.skill_overkill.ai_coach -->

## Shortcut Reality

### Ideal practice

Create skills only for repeated, stable workflows with clear trigger language, bounded instructions, and a maintenance owner.

### What people often do instead

People formalize one-off prompts because a skill feels like progress. The workflow then becomes harder to change than the task deserves.

### When the shortcut may be acceptable

Acceptable in disposable local experiments when the skill is explicitly marked experimental and can be deleted without affecting shared repos or future production work.

### When it becomes a bad trade

Bad when broad skill descriptions or unreviewed scripts will affect many future Codex runs, shared repos, security-sensitive work, or team workflows.

### Risk profile

- Probability: low for local experiments; medium when a repo starts accumulating half-used skills.
- Impact: low for unused prompt snippets; medium/high when broad skills steer production-adjacent work.
- Recoverability: high if the skill is isolated and disabled quickly; lower if multiple tasks already relied on it.

### Blast radius

A premature skill can alter future prompts silently by making Codex choose a workflow the user did not intend.

### Minimum guardrails

- use a saved prompt first
- promote only after repeated use
- define trigger and non-trigger cases
- prefer instruction-only skills until scripts are justified

### Recovery plan

1. Disable the skill or set it explicit-only.
2. Replace it with a saved prompt while the workflow stabilizes.
3. Audit recent runs where the skill may have fired.
4. Rewrite the skill with narrow trigger/non-trigger language if it remains useful.

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

- skill invocation mechanics
- skill discovery limits
- plugin distribution behavior
- UI controls for skill enablement

## Obsolescence Watch

This card should be revised if:

- Codex provides automatic skill lifecycle analysis that reliably promotes, scopes, and retires reusable workflows without hidden trigger risk

## Evidence and Sources

- `openai.codex.skills` — Official OpenAI Codex skills guidance for SKILL.md structure, progressive disclosure, invocation, skill locations, plugin distribution, and best practices.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for goals, context, constraints, done-when criteria, planning, checks, review, and reusable project guidance.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.skills`
- `vcb.prompting.four_part_prompt`
- `vcb.constraints.scope_budget`
- `vcb.shortcut.process_overhead_for_tiny_project`


<!-- VCB:STOP_RETRIEVAL reason="skill_overkill_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.skill_overkill -->
