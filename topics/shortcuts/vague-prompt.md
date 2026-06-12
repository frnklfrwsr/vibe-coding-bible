<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.vague_prompt version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-12'
last_reviewed: '2026-06-12'
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
evidence_scope: official OpenAI/Codex prompting guidance plus VCB maintainer synthesis for risk-managed shortcut harm reduction
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
- emergency_hotfix
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.shortcut.vague_prompt
title: Vague Prompt
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-12'
applies_to:
- prompts
- work orders
- bug reports
- feature requests
- Codex App
- Codex CLI
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- prompting
- context
- acceptance criteria
risk_level:
  prototype: LOW_RISK_SHORTCUT
  personal_tool: MODERATE_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: DO_NOT_DO_IN_PRODUCTION
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- state goal
- add context
- name constraints
- define done
shortcut_profiles:
- vcb.shortcut.vague_prompt
durable_principles:
- ambiguity becomes model guesswork
- constraints are part of the task
- done-when criteria turn output into evidence
likely_to_change:
- prompt UI affordances
- context attachment mechanisms
- model behavior around ambiguous requests
obsolete_when:
- agents can ask perfect clarifying questions and refuse risky ambiguous work by default
related_topics:
- vcb.prompting.four_part_prompt
- vcb.prompting.acceptance_criteria
- vcb.prompting.context_management
- vcb.failure.context_pollution
- vcb.failure.done_claim_without_evidence
- vcb.constraints.scope_budget
---

# Vague Prompt

> Summary:
> Vague prompt is asking Codex for a result without enough goal, context, constraints, and done-when evidence to avoid dangerous guesses.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.vague_prompt.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A vague prompt gives Codex a wish instead of a work order. The model must invent missing intent, missing files, missing constraints, and missing proof.

### Why it matters

Codex is good at filling gaps. That is useful for exploration and dangerous for engineering. When the prompt is vague, the diff may look polished while solving the wrong problem.

### What good looks like

Good: "Goal, context, constraints, and done when" in a few lines.

### What bad looks like

Bad: "Make this better."

### Minimal example

Instead of "fix the dashboard," ask: "Goal: fix the empty-state chart. Context: `Dashboard.tsx` and bug screenshot. Constraints: no new chart library. Done when: empty data shows the approved message and existing chart tests pass."

### Checklist

- name one outcome
- include relevant file, screenshot, log, or user flow
- state forbidden changes
- define checks or review evidence
- ask Codex to restate assumptions if anything is missing

<!-- VCB:END_SECTION id=vcb.shortcut.vague_prompt.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.vague_prompt.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to convert intent into a bounded work order before the model starts guessing.

### Diagnostic questions

- What is the one outcome?
- What context should Codex inspect?
- What must not change?
- What evidence proves done?
- Is the prompt vague because the user is exploring or because they are avoiding decisions?

### Coaching tactics

- rewrite vague prompts into four-part prompts
- ask for assumptions before implementation
- keep exploratory prompts read-only
- require done-when criteria for mutation
- separate product taste, bug reports, and implementation tasks

### Red flags

- "improve," "clean up," "fix," or "make it work" without details
- no file or user flow named
- no forbidden areas
- no acceptance evidence
- production or security-sensitive work from a one-line ask

### Prompt pattern

```text
Rewrite my request as a four-part Codex work order: Goal, Context, Constraints, Done when. If required context is missing, ask up to three questions before editing.
```

<!-- VCB:END_SECTION id=vcb.shortcut.vague_prompt.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the best-practice alternative named in `SHORTCUT_REGISTER.md`, then scale the guardrails by project phase, blast radius, and recoverability.

### What people often do instead

They ask for the result in ordinary language and let Codex infer the engineering contract.

### When the shortcut may be acceptable

Acceptable for brainstorming, explanation, or disposable exploration when Codex is not mutating a real project or claiming implementation is complete.

### When it becomes a bad trade

Bad when the prompt asks for code changes, production fixes, broad refactors, security-sensitive work, or any output the user plans to merge.

### Risk profile

- Probability: low for explanation-only work; high for mutation from unclear requests.
- Impact: low in throwaway exploration; high when hidden assumptions ship to users.
- Recoverability: good if caught before edits; worse after ambiguous changes stack.

### Blast radius

A vague prompt can spread into wrong files, wrong design, wrong tests, and false completion evidence because the model had to invent the missing contract.

### Minimum guardrails

- state goal
- add context
- name constraints
- define done

### Recovery plan

1. Stop accepting new edits.
2. Ask Codex to list assumptions it made.
3. Rewrite the prompt with goal, context, constraints, and done-when.
4. Compare the current diff to the rewritten prompt.
5. Revert or split changes that do not match.
6. Run the nearest check before continuing.

## Budget and Constraint Notes

### Cheapest reliable path

Spend one extra prompt clarifying the work order instead of paying for cleanup after a wrong diff.

### Fastest high-usage path

High-throughput users can save a reusable four-part skeleton for common tasks.

### Low-attention path

Low-attention work should never start from a vague mutating prompt; require explicit scope and stop conditions.

### Production-quality path

Production work needs specific context, forbidden changes, verification, and review ownership.

### Prototype versus production

Vague prototype prompts are acceptable when output is throwaway. Production prompts need evidence.

### Maintenance phase

Maintenance prompts should name current behavior, intended behavior, nearest check, and files or areas to avoid.

## Stable Core

- ambiguity becomes model guesswork
- constraints are part of the task
- done-when criteria turn output into evidence

## Volatile Surface

- prompt UI affordances
- context attachment mechanisms
- model behavior around ambiguous requests

## Obsolescence Watch

This card should be revised if:

- agents can ask perfect clarifying questions and refuse risky ambiguous work by default

## Evidence and Sources

- `openai.codex.best_practices` - Official OpenAI Codex guidance for goals, context, constraints, validation, and review.
- `openai.codex.prompting` - Official OpenAI Codex prompting guidance for focused task loops and context.
- `openai.codex.workflows` - Official OpenAI Codex workflow guidance for explicit context and definition of done.
- `vcb.synthesis.stable_engineering_practice` - VCB maintainer synthesis for durable risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.prompting.four_part_prompt`
- `vcb.prompting.acceptance_criteria`
- `vcb.prompting.context_management`
- `vcb.failure.context_pollution`
- `vcb.failure.done_claim_without_evidence`
- `vcb.constraints.scope_budget`

<!-- VCB:STOP_RETRIEVAL reason="vague_prompt_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.vague_prompt -->
