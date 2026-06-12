<!-- VCB:BEGIN_TOPIC id=vcb.concepts.api_basics version=0.1.0 -->
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
id: vcb.concepts.api_basics
title: API Basics
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
- vcb.shortcut.vague_prompt
- vcb.shortcut.accepting_looks_done
durable_principles:
- an API is a contract between software components
- API behavior must be specified by inputs, outputs, errors, auth, and side effects
- Codex needs concrete API examples before safely changing API code
likely_to_change:
- framework-specific route conventions
- API client generator behavior
- API documentation tooling and UI
obsolete_when:
- software stops needing explicit boundaries between components
related_topics:
- vcb.concepts.frontend_backend
- vcb.concepts.authentication
- vcb.concepts.authorization
- vcb.concepts.test
- vcb.concepts.ci
- vcb.chapter.codex_playbooks
---

> Summary:
> An API is the contract one piece of software exposes so another piece of software can ask it to do something or give back data.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.api_basics.human -->
## 1. For the Human: Plain-Language Concept

### What this means

An **API** is a way for software to talk to other software. A button is a human interface. An API is a software interface. Your frontend might call `/api/invoices` to ask the backend for invoices. A payment service might expose an API so your app can create a checkout session.

### Why it matters

Codex can make convincing API code that is wrong in small but expensive ways: wrong URL, wrong request body, missing auth, forgotten error state, or mismatched response shape. API work needs a contract, not just vibes.

### The mental model

Think of an API as a restaurant menu for code. The menu says what you can order, what information you must provide, what comes back, and what can go wrong. Codex should not invent off-menu dishes unless you explicitly ask it to design a new API.

### What good looks like

- endpoint name and purpose are clear
- request inputs are named and validated
- response shape is documented or tested
- errors and permissions are specified
- the frontend and backend agree on the same contract

### What bad looks like

- Codex guesses an endpoint that does not exist
- frontend assumes fields the backend never returns
- API silently changes shape without updating callers
- auth and error cases are treated as afterthoughts

### Minimal example

A good API request is not just “save user.” It is: `POST /api/profile` with `{ displayName }`, requires logged-in user, validates length, returns the updated profile, and returns `401` if not logged in.

### Checklist

- Name the caller and the service being called.
- Specify inputs, outputs, errors, and auth.
- Point Codex to an existing nearby API route before asking for a new one.
- Ask for one test or manual check proving the contract.
- Review both sides of the API change.
<!-- VCB:END_SECTION id=vcb.concepts.api_basics.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.api_basics.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that API work is contract work. Do not let Codex invent endpoints, fields, or side effects without grounding them in existing files or explicit acceptance criteria.

### Diagnose the human’s current model

- Can the human state who calls the API and what must come back?
- Do they know what errors are possible?
- Are auth and authorization explicit?
- Is this adding a new contract or changing an existing one?

### Explanation strategy

Start with the menu metaphor. Then convert the user request into a contract table: route/function, inputs, outputs, errors, auth, side effects, tests. Ask Codex to inspect existing patterns before editing.

### Useful metaphors

- API = menu for software.
- Request = order ticket.
- Response = what the kitchen sends back.
- Error status = “we cannot serve this order” with a reason.

### Coaching tactics

- Ask for existing API examples in the repo.
- Force Codex to list request/response shapes before code.
- Separate API design from implementation when risk is high.
- For auth/payment/data APIs, require tests and explicit permissions checks.

### Prompt patterns

```text
Inspect existing API routes and summarize the route conventions before adding a new endpoint.
```

```text
Define the API contract first: caller, route/function, inputs, outputs, error cases, auth, side effects, and tests. Do not edit yet.
```

### Red flags to call out directly

- “Just wire it up” with no contract.
- Codex invents a client method or backend route.
- Only happy-path response is described.
- Auth, permissions, or validation are missing.

### Exercises

- Have the human write a five-line API contract for one feature before asking Codex to implement it.
- Ask the human to identify one failure case and one permission case.
<!-- VCB:END_SECTION id=vcb.concepts.api_basics.ai_coach -->

## Shortcut Reality

### The ideal practice

Define or inspect the API contract before changing code. Update both caller and provider together and verify the contract with a test or exact manual check.

### What users often do instead

Users ask Codex to “connect the frontend to the backend” and accept whatever route/client code it invents.

### When the shortcut may be fine

A throwaway prototype with fake data and no stable API consumers.

### When the shortcut is a bad idea

Public API, auth, payments, webhooks, integrations, mobile clients, or anything other software already depends on.

### Risk profile

- Probability of failure: medium
- Impact if it fails: low in demos, high for real integrations
- Ease of recovery: medium if diff is small
- Blast radius: caller + service + stored data
- Skill needed to recover: API debugging and contract reading
- Hidden cost: clients silently depend on accidental behavior

### Minimum guardrails

- Write the contract first.
- Use existing route/client patterns.
- Avoid broad rewrites.
- Run one caller/provider check.
- Document changed behavior.

### Recovery plan

Revert the API change if callers break, restore the previous response shape if external clients depend on it, then reintroduce changes behind a versioned route or compatibility wrapper.

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

- an API is a contract between software components
- API behavior must be specified by inputs, outputs, errors, auth, and side effects
- Codex needs concrete API examples before safely changing API code

## Volatile Surface

- framework-specific route conventions
- API client generator behavior
- API documentation tooling and UI

## Obsolescence Watch

Obsolete or review this topic when:

- software stops needing explicit boundaries between components

## Evidence and Sources

- `mdn.glossary.api` — source anchor for this concept.
- `mdn.learn_web_apis` — source anchor for this concept.
- `owasp.rest_security` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.frontend_backend
- vcb.concepts.authentication
- vcb.concepts.authorization
- vcb.concepts.test
- vcb.concepts.ci
- vcb.chapter.codex_playbooks

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.api_basics -->
