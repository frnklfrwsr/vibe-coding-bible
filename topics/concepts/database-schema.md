<!-- VCB:BEGIN_TOPIC id=vcb.concepts.database_schema version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
review_cadence: annual
audiences:
- human
- ai_coach
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- Human software work
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
id: vcb.concepts.database_schema
title: Database Schema
type: concept
next_review_due: '2027-06-09'
source_status:
  official_openai: false
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: concept definition anchored to official/vendor/expert sources; Codex-specific
  risk guidance is maintainer synthesis
stability:
  principle: CORE_ENGINEERING
  surface: STABLE
  pricing: STABLE
shortcut_profiles:
- vcb.shortcut.one_big_prompt
- vcb.shortcut.manual_testing_only
durable_principles:
- data shape decisions are harder to undo than UI decisions
- schema changes need migration and compatibility thinking
- Codex must not casually change persistent data structure
likely_to_change:
- ORM syntax
- migration tooling
- database platform features
obsolete_when:
- apps stop storing structured persistent data
related_topics:
- vcb.concepts.migration
- vcb.concepts.api_basics
- vcb.concepts.authorization
- vcb.concepts.rollback
- vcb.chapter.dependency_package_framework_decisions
---

> Summary:
> A database schema is the shape of stored data: tables, fields, relationships, constraints, and sometimes namespaces.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.database_schema.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A **database schema** is the plan for how your app stores data. It includes tables or collections, columns or fields, relationships, required values, unique rules, indexes, and constraints.

### Why it matters

Schema mistakes live longer than UI mistakes. A bad button can be restyled. Bad data shape can require migrations, cleanup scripts, downtime, and careful compatibility work.

### The mental model

A schema is the shelving system in a warehouse. If you label shelves badly, store fragile items in the wrong place, or mix incompatible things together, every future worker pays the price.

### What good looks like

- tables/models match real product concepts
- required fields are genuinely required
- relationships are explicit
- unique and foreign-key constraints protect data integrity
- migrations are small and reviewed

### What bad looks like

- Codex adds nullable fields everywhere to make errors go away
- stores multiple concepts in one string blob
- changes IDs or relationships without migration plan
- schema supports the prototype but blocks obvious next steps

### Minimal example

For a task app, `users`, `projects`, and `tasks` are separate concepts. A task likely has a `project_id`, `title`, `status`, and `created_at`. Storing all tasks as one JSON string in the user row might feel fast, but it makes querying, permissions, and migration harder.

### Checklist

- Name the real-world thing being stored.
- Ask whether each field belongs on this table/model.
- Decide which fields are required.
- Define relationships and ownership.
- Ask what happens to old data when the schema changes.
<!-- VCB:END_SECTION id=vcb.concepts.database_schema.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.database_schema.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach schema as product/data structure, not ORM syntax. Escalate when Codex wants to reshape persistent data casually.

### Diagnose the human’s current model

- Is this new data or a change to existing persisted data?
- Does the human understand which table/model owns the data?
- Are permissions tied to relationships?
- Is a migration required?

### Explanation strategy

Use concrete nouns: user, invoice, project, task, membership. Then map nouns to tables/models and verbs to API actions. Treat schema changes as high-recovery-cost unless proven otherwise.

### Useful metaphors

- Schema = warehouse shelving system.
- Foreign key = label showing which shelf an item belongs to.
- Constraint = rule the warehouse enforces, not a sticky note.

### Coaching tactics

- Ask for current schema inspection before edits.
- Require migration plan for existing data.
- Separate schema design from UI implementation.
- Ask Codex to list compatibility risks.

### Prompt patterns

```text
Inspect the current schema/models and summarize entities, relationships, required fields, and constraints. Do not edit yet.
```

```text
Propose the smallest schema change for this feature. Include migration risk, rollback difficulty, and affected code paths.
```

### Red flags to call out directly

- “Just add a field” when existing data exists.
- Dropping columns without backup.
- Weakening constraints to make tests pass.
- Schema changes mixed with unrelated refactors.

### Exercises

- Have the human model a simple blog with users, posts, comments, and permissions.
- Ask them which schema changes are easy vs hard to undo.
<!-- VCB:END_SECTION id=vcb.concepts.database_schema.ai_coach -->

## Shortcut Reality

### The ideal practice

Design or inspect schema deliberately, then migrate in small reversible steps.

### What users often do instead

Users let Codex change models until the feature compiles.

### When the shortcut may be fine

Brand-new throwaway prototype with fake data and no migration history.

### When the shortcut is a bad idea

Production data, customer records, billing, auth, analytics history, or shared reporting tables.

### Risk profile

- Probability of failure: medium
- Impact if it fails: high with real data
- Ease of recovery: low after migration/data loss
- Blast radius: database + APIs + UI + reports
- Skill needed to recover: database/migration skill
- Hidden cost: bad schema becomes future architecture

### Minimum guardrails

- Use fake data in prototypes.
- Commit before schema edits.
- Keep migrations small.
- Back up production data.
- Ask for rollback or forward-fix path.

### Recovery plan

Stop further writes, restore from backup if data was lost, roll forward with a corrective migration when possible, and add checks that prevent the same bad data shape from reappearing.

### AI coach guidance

Do not lecture first. Classify the project risk, then move the human one guardrail level up. If this touches real users, secrets, money, auth, production data, migrations, or CI credentials, be direct and require evidence before acceptance.

## Budget and Constraint Notes

### Cheapest reliable path

Use this card to clarify the concept before asking Codex to edit. Spend one short inspection or explanation pass, then make the smallest verified change.

### Fastest high-usage path

Run a plan/implementation/review loop, but keep diffs isolated and require Codex to report the concept-specific risk areas before acceptance.

### Low-attention path

Low-attention work needs stronger written constraints, not broader trust. Require a final report with files changed, checks run, known gaps, and any concept-specific risk.

### Production-quality path

Use the concept as a release gate: define the boundary, verify the important cases, review the diff, and preserve rollback/recovery options.

## Stable Core

- data shape decisions are harder to undo than UI decisions
- schema changes need migration and compatibility thinking
- Codex must not casually change persistent data structure

## Volatile Surface

- ORM syntax
- migration tooling
- database platform features

## Obsolescence Watch

Obsolete or review this topic when:

- apps stop storing structured persistent data

## Evidence and Sources

- `postgres.docs.schemas` — source anchor for this concept.
- `prisma.docs.schema` — source anchor for this concept.
- `prisma.docs.models` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.migration
- vcb.concepts.api_basics
- vcb.concepts.authorization
- vcb.concepts.rollback
- vcb.chapter.dependency_package_framework_decisions

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.database_schema -->
