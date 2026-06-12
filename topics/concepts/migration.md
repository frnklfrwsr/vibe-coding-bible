<!-- VCB:BEGIN_TOPIC id=vcb.concepts.migration version=0.1.0 -->
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
id: vcb.concepts.migration
title: Migration
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
- vcb.shortcut.broad_refactor
- vcb.shortcut.skipping_tests
durable_principles:
- migrations need ordering, review, and rollback/forward-fix thinking
- data changes are harder to undo than code changes
- Codex should not run destructive migrations casually
likely_to_change:
- migration tool syntax
- online migration patterns
- database-specific locking behavior
obsolete_when:
- apps stop evolving persistent data
related_topics:
- vcb.concepts.database_schema
- vcb.concepts.rollback
- vcb.concepts.ci
- vcb.chapter.security_for_vibe_coders
---

> Summary:
> A migration is a controlled change to persisted data or database structure, usually tracked as a script or ordered change file.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.migration.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A migration is how you change data structure over time: add a column, create a table, rename a field, backfill data, or change constraints. Good migrations are ordered and repeatable.

### Why it matters

Code rollback is easy compared with data rollback. Codex must not casually change migrations or run destructive database commands against real data.

### The mental model

A migration is remodeling a building while people may still live in it. You need staging, order, and a way to avoid trapping people inside.

### What good looks like

- migration is small and named
- old data compatibility is considered
- backfill and rollback/forward-fix plan are explicit
- production database is backed up or protected
- checks run against staging/dev first

### What bad looks like

- drop column in same patch as code change
- migration generated without reading current schema
- data backfill untested
- Codex runs migration against production by accident

### Minimal example

Adding a nullable column is often easier than renaming a required column that existing code and data depend on.

### Checklist

- Ask whether real data exists.
- Inspect current schema/migrations first.
- Use dev/staging before production.
- Back up production.
- Prefer expand/migrate/contract for risky changes.
<!-- VCB:END_SECTION id=vcb.concepts.migration.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.migration.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Escalate migration risk and separate data-shape changes from feature polish.

### Diagnose the human’s current model

- What part of the concept is the human treating as magic?
- What evidence would show this is working?
- What is the risky production version of this concept?
- Can the human name the boundary, data, or check involved?

### Explanation strategy

Start with a concrete everyday analogy, then tie it to the exact files, commands, checks, or data flow Codex is likely to touch. Keep the explanation practical and risk-scaled.

### Useful metaphors

- Use one simple metaphor, then return to the actual repo.
- Treat the concept as an operational control, not trivia.

### Coaching tactics

- Ask Codex to inspect current project conventions before editing.
- Convert the concept into a small checklist.
- Escalate when the concept touches production, secrets, data, auth, payments, or CI.

### Prompt patterns

```text
Plan this migration only. Include current schema, data compatibility, lock/backfill risk, deploy order, rollback or forward-fix path, and checks.
```

```text
Inspect migration history and propose the smallest safe migration. Do not run it against production.
```

### Red flags to call out directly

- destructive migration without backup
- rename/drop mixed with feature change
- no deploy-order plan
- Codex cannot explain existing migration pattern

### Exercises

- Ask the human to find one real example in their repo.
- Ask them what would break if this concept were wrong.
<!-- VCB:END_SECTION id=vcb.concepts.migration.ai_coach -->

## Shortcut Reality

### The ideal practice

Plan, review, and test migrations before touching real data.

### What users often do instead

Users let Codex generate and run migrations to make code compile.

### When the shortcut may be fine

Empty local database with fake data.

### When the shortcut is a bad idea

Production DB, user data, billing/auth records, irreversible deletes, or large tables.

### Risk profile

- Probability of failure: medium
- Impact if it fails: high
- Ease of recovery: low with real data
- Blast radius: database + all code depending on it
- Skill needed to recover: database operations
- Hidden cost: downtime/backfills/manual repair

### Minimum guardrails

- Commit first.
- Use fake/dev DB first.
- Back up production.
- Review generated SQL.
- Separate code deploy order.

### Recovery plan

Stop writes if needed, restore backup or roll forward with corrective migration, audit affected records, and add deploy checklist preventing direct production migration by Codex.

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

- migrations need ordering, review, and rollback/forward-fix thinking
- data changes are harder to undo than code changes
- Codex should not run destructive migrations casually

## Volatile Surface

- migration tool syntax
- online migration patterns
- database-specific locking behavior

## Obsolescence Watch

Obsolete or review this topic when:

- apps stop evolving persistent data

## Evidence and Sources

- `liquibase.docs.intro` — source anchor for this concept.
- `flyway.docs.migrations` — source anchor for this concept.
- `prisma.docs.models` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.database_schema
- vcb.concepts.rollback
- vcb.concepts.ci
- vcb.chapter.security_for_vibe_coders

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.migration -->
