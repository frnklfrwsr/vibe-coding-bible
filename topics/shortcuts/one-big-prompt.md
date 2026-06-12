<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.one_big_prompt version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex workflow guidance plus VCB maintainer synthesis for risk-managed shortcut harm reduction
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
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.shortcut.one_big_prompt
title: One Big Prompt
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-12'
applies_to:
- feature builds
- prototypes
- app generation
- refactors
- Codex Cloud
- Codex App
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- scope
- slicing
- reviewability
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: MODERATE_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: DO_NOT_DO_IN_PRODUCTION
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- slice into milestones
- branch checkpoint
- one vertical path first
- review before next slice
shortcut_profiles:
- vcb.shortcut.one_big_prompt
durable_principles:
- large goals need small reviewable increments
- first useful slice beats broad unfinished surface area
- each slice needs its own evidence
likely_to_change:
- Codex app-builder examples
- cloud task limits and handoff behavior
- UI generation workflows
- model ability to keep large task state coherent
obsolete_when:
- agents can complete large multi-surface work with trustworthy staged evidence and reviewable checkpoints by default
related_topics:
- vcb.workflow.feature_slicing
- vcb.prompting.four_part_prompt
- vcb.prompting.acceptance_criteria
- vcb.constraints.scope_budget
- vcb.constraints.recovery_budget
- vcb.chapter.feature_slicing
---

# One Big Prompt

> Summary:
> One big prompt is asking Codex to build or change too much in one run while still expecting a coherent, reviewable, production-ready result.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.one_big_prompt.human -->
## 1. For the Human: Plain-Language Concept

### What this means

One big prompt is the urge to describe the entire app, migration, redesign, or refactor at once and let Codex figure out the sequence. It feels efficient because it avoids breaking the work down.

### Why it matters

Large prompts create large ambiguous diffs. Codex may satisfy the visible parts while missing edge states, tests, security boundaries, migration details, or product constraints. Review becomes expensive precisely when risk is highest.

### What good looks like

Good: "Build the first vertical slice only. Stop after login plus one happy-path flow works and is verified."

### What bad looks like

Bad: "Build the whole SaaS app with auth, billing, admin, analytics, emails, dashboard, and deployment."

### Minimal example

For a new app, start with one user, one screen, one backend path, one check, and a fake-data boundary before adding auth, payments, or integrations.

### Checklist

- name the first vertical slice
- defer nonessential surfaces
- keep generated output reviewable
- run one check before expanding scope
- treat broad generated output as prototype until hardened

<!-- VCB:END_SECTION id=vcb.shortcut.one_big_prompt.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.one_big_prompt.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that slicing is not less ambition. It is how ambition survives contact with review, tests, and real users.

### Diagnostic questions

- Can the user name the smallest useful slice?
- How many systems would the one prompt touch?
- Which part must be verified first?
- Is the user asking for production quality or a disposable sketch?
- What can be deferred without harming learning?

### Coaching tactics

- convert the big prompt into milestone cards
- ask for slice 1 before full implementation
- separate prototype generation from production hardening
- require a stop point after each slice
- keep auth, billing, data deletion, and deployment out of the first broad prototype unless they are the slice

### Red flags

- too many unrelated workflows in one request
- "make it production ready" without acceptance evidence
- generated backend plus auth plus payments plus deployment in one pass
- no stop point before expansion
- no branch checkpoint

### Prompt pattern

```text
Turn this big request into 3-5 milestones. Implement only milestone 1 now. Use fake data if needed. Stop after changed files, checks run, gaps, and next milestone recommendation.
```

<!-- VCB:END_SECTION id=vcb.shortcut.one_big_prompt.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the best-practice alternative named in `SHORTCUT_REGISTER.md`, then scale the guardrails by project phase, blast radius, and recoverability.

### What people often do instead

They hand Codex the whole vision because prompting the whole thing feels cheaper than deciding the first slice.

### When the shortcut may be acceptable

Acceptable for disposable prototypes, concept sketches, or learning exercises where generated output is explicitly throwaway and fake-data-only.

### When it becomes a bad trade

Bad when output is treated as production foundation, touches auth/payments/data/secrets, spans many files, or cannot be reviewed honestly in one pass.

### Risk profile

- Probability: medium for prototypes; high when the prompt spans unrelated systems.
- Impact: low for throwaway sketches; high for production, shared repos, and security-sensitive apps.
- Recoverability: good when each milestone is branched; poor when a giant generated diff becomes the foundation.

### Blast radius

One big prompt can create architecture drift, unreviewed dependencies, fake completeness, missing tests, hidden security assumptions, and a codebase no one wants to untangle.

### Minimum guardrails

- slice into milestones
- branch checkpoint
- one vertical path first
- review before next slice

### Recovery plan

1. Stop expanding the generated work.
2. Save a checkpoint or branch.
3. Ask Codex to identify independent slices in the diff.
4. Keep or rebuild only the first useful slice.
5. Remove or park unfinished generated surfaces.
6. Add checks before continuing to the next slice.

## Budget and Constraint Notes

### Cheapest reliable path

Spend a small prompt on slicing before spending many prompts reviewing a broad diff.

### Fastest high-usage path

High-throughput users can parallelize research or design, but implementation should remain sliced by ownership and review path.

### Low-attention path

Low-attention work should produce one review packet per slice, not one giant final surprise.

### Production-quality path

Production quality requires staged evidence, tests, security review, and rollback per slice.

### Prototype versus production

A one-big-prompt prototype may be useful for learning. It is not automatically a production foundation.

### Maintenance phase

Maintenance tasks should avoid broad prompt bundles; each bug, refactor, and dependency change needs separate evidence.

## Stable Core

- large goals need small reviewable increments
- first useful slice beats broad unfinished surface area
- each slice needs its own evidence

## Volatile Surface

- Codex app-builder examples
- cloud task limits and handoff behavior
- UI generation workflows
- model ability to keep large task state coherent

## Obsolescence Watch

This card should be revised if:

- agents can complete large multi-surface work with trustworthy staged evidence and reviewable checkpoints by default

## Evidence and Sources

- `openai.codex.best_practices` - Official OpenAI Codex guidance for prompt structure, validation, and review.
- `openai.codex.workflows` - Official OpenAI Codex workflow guidance for explicit context, done criteria, and local-to-cloud patterns.
- `openai.codex.use_cases.idea_to_proof_of_concept` - Official OpenAI Codex use case for idea-to-proof-of-concept work and prototype validation.
- `vcb.synthesis.stable_engineering_practice` - VCB maintainer synthesis for durable risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.workflow.feature_slicing`
- `vcb.prompting.four_part_prompt`
- `vcb.prompting.acceptance_criteria`
- `vcb.constraints.scope_budget`
- `vcb.constraints.recovery_budget`
- `vcb.chapter.feature_slicing`

<!-- VCB:STOP_RETRIEVAL reason="one_big_prompt_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.one_big_prompt -->
