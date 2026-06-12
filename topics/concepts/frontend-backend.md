<!-- VCB:BEGIN_TOPIC id=vcb.concepts.frontend_backend version=0.1.0 -->
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
id: vcb.concepts.frontend_backend
title: Frontend vs Backend
type: concept
next_review_due: '2027-06-09'
source_status:
  official_openai: true
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
- vcb.shortcut.generated_prototype_as_production_foundation
durable_principles:
- frontend and backend have different responsibilities
- bugs often happen at the boundary between UI state and server state
- Codex needs to know which side of the boundary it should change
likely_to_change:
- framework conventions
- hosting platforms
- full-stack starter patterns
obsolete_when:
- software stops separating user interface concerns from server/data concerns
related_topics:
- vcb.concepts.api_basics
- vcb.concepts.state
- vcb.concepts.database_schema
- vcb.chapter.frontend_work
- vcb.chapter.first_serious_app
---

> Summary:
> Frontend is what the user sees and interacts with; backend is the server-side logic, data, and integrations that support it.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.frontend_backend.human -->
## 1. For the Human: Plain-Language Concept

### What this means

The **frontend** is the part of an app the user sees: pages, buttons, forms, layouts, loading states, and error messages. The **backend** is the part that runs behind the scenes: database reads/writes, business rules, authentication checks, jobs, integrations, and APIs.

### Why it matters

Vibe coders often ask for “the feature” without naming which side needs work. Codex may fix the UI while leaving the backend broken, or change backend behavior while the screen still shows the wrong thing.

### The mental model

Frontend is the waiter and dining room. Backend is the kitchen, inventory, and payment terminal. A good restaurant needs both, and the handoff between them is where many mistakes happen.

### What good looks like

- UI state matches backend truth
- forms validate locally and server-side
- API errors show useful messages
- backend enforces permissions even if frontend hides buttons
- changes are tested at the boundary

### What bad looks like

- frontend-only permission checks
- fake data left in production UI
- backend returns data but UI never handles loading/error/empty states
- Codex changes both sides in one huge diff without explaining the boundary

### Minimal example

A “delete account” button is frontend. The server route that verifies the user, deletes records, logs the action, and returns a result is backend. Hiding the button is not enough; the backend must reject unauthorized deletion.

### Checklist

- Identify whether the bug is UI, backend, or boundary.
- Name the API or action connecting the two.
- Check loading, empty, error, and success states.
- Verify backend permission checks.
- Review both UI diff and server diff.
<!-- VCB:END_SECTION id=vcb.concepts.frontend_backend.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.frontend_backend.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Help the human classify work by responsibility boundary and prevent frontend-only fixes for backend/security/data problems.

### Diagnose the human’s current model

- Is the requested behavior visible-only, data-changing, or both?
- Does the backend enforce the rule independently of the frontend?
- Is stale client state involved?
- Which file owns the data flow?

### Explanation strategy

Draw the request path: user action → frontend state → API/action → backend logic → database/integration → response → frontend render. Then identify the smallest boundary to change.

### Useful metaphors

- Frontend = dining room. Backend = kitchen. API = order ticket.
- Frontend is the dashboard; backend is the engine and brakes.

### Coaching tactics

- Ask Codex for a data-flow map before broad full-stack edits.
- Require backend checks for security-sensitive UI actions.
- Split UI polish from backend logic changes when possible.
- Tell Codex to preserve existing API contracts unless explicitly changing them.

### Prompt patterns

```text
Map the frontend/backend boundary for this feature before editing. Name the files, route/action, data shape, and state transitions.
```

```text
Implement only the frontend state handling first; do not change backend behavior unless you find it is necessary and explain why.
```

### Red flags to call out directly

- “Hide this from non-admins” implemented only in JSX.
- Mock data remains after backend is available.
- Codex changes schema, API, and UI in one unreviewable patch.
- UI says success before server confirms.

### Exercises

- Ask the human to place five files into frontend, backend, or boundary categories.
- Have them trace one button click from UI to database and back.
<!-- VCB:END_SECTION id=vcb.concepts.frontend_backend.ai_coach -->

## Shortcut Reality

### The ideal practice

Identify the boundary and make small verified changes on the correct side.

### What users often do instead

Users ask Codex to build the whole feature at once and accept a mixed frontend/backend diff.

### When the shortcut may be fine

Disposable MVP sketches with fake data, no secrets, no real users, and a clear rebuild path.

### When the shortcut is a bad idea

Auth, payments, persistent data, production admin tools, or shared APIs.

### Risk profile

- Probability of failure: medium
- Impact if it fails: medium/high at security or data boundaries
- Ease of recovery: medium if separated, low if mixed into a huge diff
- Blast radius: UI + server + database
- Skill needed to recover: full-stack debugging
- Hidden cost: false sense that a screen working means the system is safe

### Minimum guardrails

- Ask for a boundary map.
- Split UI and backend commits.
- Use fake data only in prototypes.
- Require backend permission checks.
- Run one end-to-end path check.

### Recovery plan

Separate the diff by frontend/backend responsibility, revert the incorrect side, restore API compatibility, and add a boundary test or manual path checklist.

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

- frontend and backend have different responsibilities
- bugs often happen at the boundary between UI state and server state
- Codex needs to know which side of the boundary it should change

## Volatile Surface

- framework conventions
- hosting platforms
- full-stack starter patterns

## Obsolescence Watch

Obsolete or review this topic when:

- software stops separating user interface concerns from server/data concerns

## Evidence and Sources

- `mdn.learn_web_development` — source anchor for this concept.
- `mdn.curriculum_frontend` — source anchor for this concept.
- `openai.codex.use_cases.web_development` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.api_basics
- vcb.concepts.state
- vcb.concepts.database_schema
- vcb.chapter.frontend_work
- vcb.chapter.first_serious_app

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.frontend_backend -->
