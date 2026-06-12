<!-- VCB:BEGIN_TOPIC id=vcb.concepts.authorization version=0.1.0 -->
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
id: vcb.concepts.authorization
title: Authorization
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
- vcb.shortcut.skipping_security_review
- vcb.shortcut.accepting_looks_done
durable_principles:
- authorization is about permission, not identity
- server-side authorization is required for real security
- UI hiding is not a permission boundary
likely_to_change:
- policy libraries
- framework middleware
- role/permission models
obsolete_when:
- software stops enforcing access boundaries
related_topics:
- vcb.concepts.authentication
- vcb.concepts.api_basics
- vcb.concepts.database_schema
- vcb.chapter.security_for_vibe_coders
---

> Summary:
> Authorization decides what an already-authenticated user or service is allowed to do.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.authorization.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Authorization answers: **what are you allowed to do?** After the app knows who the user is, authorization decides which records, actions, pages, or admin tools they may access.

### Why it matters

Most severe vibe-coded security bugs happen when Codex hides a button but forgets to protect the backend action. Anyone who can call the API can bypass the hidden button.

### The mental model

Authentication checks your ID. Authorization checks whether your badge opens this door.

### What good looks like

- permission checks run on the server/API
- tests cover wrong-user and non-admin cases
- resource ownership is checked
- admin and user paths are separated

### What bad looks like

- button hidden but API still works
- Codex checks only `isLoggedIn`
- all users can read all records
- role names are hardcoded inconsistently

### Minimal example

A logged-in user may view their own invoices. That does not mean they may view every invoice or refund payments.

### Checklist

- Name the actor.
- Name the resource.
- Name the action.
- Check ownership/role server-side.
- Test denied cases.
<!-- VCB:END_SECTION id=vcb.concepts.authorization.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.authorization.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach authorization as actor-action-resource policy and escalate hard around data/auth/payments/admin actions.

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
Define authorization as actor, action, resource, and rule. Inspect current policy locations before editing.
```

```text
Add server-side authorization for this action and include tests for allowed user, denied user, and logged-out user.
```

### Red flags to call out directly

- Only frontend visibility changes
- No denied-case test
- Admin checks mixed into random UI code
- API returns records without ownership filter

### Exercises

- Ask the human to find one real example in their repo.
- Ask them what would break if this concept were wrong.
<!-- VCB:END_SECTION id=vcb.concepts.authorization.ai_coach -->

## Shortcut Reality

### The ideal practice

Define and enforce permission rules at the backend boundary.

### What users often do instead

Users rely on the UI hiding restricted actions.

### When the shortcut may be fine

Local demo with fake data and no shared backend.

### When the shortcut is a bad idea

Production, admin tools, organization/team data, payment, deletion, uploads, or private records.

### Risk profile

- Probability of failure: high when rushed
- Impact if it fails: severe
- Ease of recovery: low if data was exposed
- Blast radius: users, records, admin actions
- Skill needed to recover: security + data audit
- Hidden cost: breach investigation

### Minimum guardrails

- Write actor/action/resource rule.
- Check on server.
- Add denied-case tests.
- Use fake users.
- Review data query filters.

### Recovery plan

Disable the affected action, patch server-side checks, audit logs for unauthorized access, notify/escalate if real data was exposed, and add regression tests.

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

- authorization is about permission, not identity
- server-side authorization is required for real security
- UI hiding is not a permission boundary

## Volatile Surface

- policy libraries
- framework middleware
- role/permission models

## Obsolescence Watch

Obsolete or review this topic when:

- software stops enforcing access boundaries

## Evidence and Sources

- `owasp.authorization_cheat_sheet` — source anchor for this concept.
- `owasp.top10_web` — source anchor for this concept.
- `github.docs.branch_protection` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.authentication
- vcb.concepts.api_basics
- vcb.concepts.database_schema
- vcb.chapter.security_for_vibe_coders

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.authorization -->
