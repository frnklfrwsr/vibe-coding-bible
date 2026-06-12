<!-- VCB:BEGIN_TOPIC id=vcb.concepts.authentication version=0.1.0 -->
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
id: vcb.concepts.authentication
title: Authentication
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
- vcb.shortcut.real_secrets_in_prototype
- vcb.shortcut.skipping_security_review
durable_principles:
- authentication verifies identity
- authentication is not the same as authorization
- auth changes require explicit security review and test users
likely_to_change:
- provider SDKs
- session/token formats
- passkey and MFA product flows
obsolete_when:
- apps stop needing identity checks
related_topics:
- vcb.concepts.authorization
- vcb.concepts.environment_variable
- vcb.concepts.api_basics
- vcb.chapter.security_for_vibe_coders
---

> Summary:
> Authentication proves who someone or something is; it is the login/identity layer, not the permissions layer.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.authentication.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Authentication answers: **who are you?** It includes sign-in, passwords, passkeys, sessions, tokens, MFA, OAuth, and service credentials.

### Why it matters

Codex can easily make a screen that looks logged in while weakening real identity checks. Authentication bugs can expose accounts, sessions, tokens, and admin paths.

### The mental model

Authentication is the front desk checking your ID. Authorization is what rooms your badge opens after ID check.

### What good looks like

- session creation and expiration are explicit
- tokens/secrets are not exposed to the browser unless intended
- auth provider callbacks are validated
- logout and expired-session states are handled

### What bad looks like

- frontend-only login state
- test users with real secrets
- tokens logged to console
- Codex disables checks to make a demo work

### Minimal example

A user entering an email/password is authentication. Checking whether that logged-in user can delete a team is authorization.

### Checklist

- Separate identity from permission.
- Use fake credentials in prototypes.
- Never paste real secrets into prompts.
- Test logged-out, logged-in, expired, and wrong-user cases.
<!-- VCB:END_SECTION id=vcb.concepts.authentication.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.authentication.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Make the auth/permission distinction automatic and stop frontend-only authentication illusions.

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
Inspect the current auth flow and list where identity is established, stored, refreshed, and cleared. Do not edit yet.
```

```text
Add this auth behavior using fake credentials and existing provider patterns. Include logged-out and expired-session checks.
```

### Red flags to call out directly

- UI state used as proof of identity
- real tokens in local prototypes
- auth callbacks accepted without verification
- Codex says “secured” without showing server-side checks

### Exercises

- Ask the human to find one real example in their repo.
- Ask them what would break if this concept were wrong.
<!-- VCB:END_SECTION id=vcb.concepts.authentication.ai_coach -->

## Shortcut Reality

### The ideal practice

Use established auth patterns/providers, fake credentials in dev, and server-side identity verification.

### What users often do instead

Users build a fake login gate or paste real provider keys into a prototype so the demo works quickly.

### When the shortcut may be fine

Local mock login with fake users and no real data.

### When the shortcut is a bad idea

Anything with real accounts, user data, admin functions, payment, or production credentials.

### Risk profile

- Probability of failure: medium
- Impact if it fails: high
- Ease of recovery: low if tokens/secrets leak
- Blast radius: accounts, sessions, APIs, production data
- Skill needed to recover: security + provider-specific cleanup
- Hidden cost: invisible unauthorized access

### Minimum guardrails

- Use fake env values.
- Keep secrets out of prompts and Git.
- Verify server-side session checks.
- Test logged-out and wrong-user paths.
- Review logs for token exposure.

### Recovery plan

Rotate leaked credentials, revoke sessions/tokens, restore server-side checks, audit access logs, and add regression/security tests before resuming work.

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

- authentication verifies identity
- authentication is not the same as authorization
- auth changes require explicit security review and test users

## Volatile Surface

- provider SDKs
- session/token formats
- passkey and MFA product flows

## Obsolescence Watch

Obsolete or review this topic when:

- apps stop needing identity checks

## Evidence and Sources

- `owasp.authentication_cheat_sheet` — source anchor for this concept.
- `owasp.session_management` — source anchor for this concept.
- `github.docs.actions_secrets` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.authorization
- vcb.concepts.environment_variable
- vcb.concepts.api_basics
- vcb.chapter.security_for_vibe_coders

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.authentication -->
