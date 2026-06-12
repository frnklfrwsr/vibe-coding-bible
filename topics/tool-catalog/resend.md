<!-- VCB:BEGIN_TOPIC id=tool.resend version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-11'
last_reviewed: '2026-06-11'
audiences:
- human
- ai_coach
source_status:
  official_openai: false
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: official Resend documentation anchors for email API, send-email behavior,
  templates, and VCB maintainer synthesis for email risk and coaching guidance.
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
project_phases:
- prototype
- mvp
- production_build
- maintenance
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: tool.resend
title: Resend
name: Resend
type: tool_card
category: email_delivery
status: active
review_cadence: quarterly
next_review_due: '2026-09-11'
last_pricing_reviewed: '2026-06-11'
pricing_volatility: very_high
pricing_snapshot_required: false
setup_effort: 'medium: API integration can be simple, but domains, API keys, templates,
  event triggers, sender identity, and recipient policy need review'
maintenance_effort: 'medium-high: templates, deliverability, suppression/error handling,
  domain state, secret rotation, and event triggers drift'
debugging_effort: 'medium-high: failures can involve DNS, sender/domain validation,
  templates, API errors, spam filtering, webhooks, or bad recipient data'
lock_in_risk: 'moderate: templates, event names, SDK/API conventions, domains, and
  delivery diagnostics can become platform-specific'
hidden_cost_risk: 'medium-high: domain setup, compliance review, deliverability debugging,
  support tickets, and accidental real-user sends are hidden costs'
codex_integration_value: 'medium-high: useful as evidence infrastructure or implementation
  context, but Codex must still work from explicit diffs, logs, tests, docs, and human-reviewed
  acceptance criteria'
best_for:
- transactional email prototypes and production flows
- passwordless/auth-adjacent notification flows after review
- domain and sending policy review
- template and event-trigger evidence
- Codex-assisted email integration with fake recipients first
not_for:
- sending to real users from unreviewed generated code
- stable prose about quotas, pricing, deliverability guarantees, or UI labels
- putting API keys in prompts or logs
- using a successful send as approval of privacy/compliance
- bulk marketing without consent and legal review
integrates_with_codex:
- GitHub PR and branch review
- GitHub Actions checks
- Codex implementation/review loops
- production-readiness evidence
- tool-stack risk review
hidden_costs:
- setup and migration cleanup
- secrets and account-permission review
- maintenance and incident-response work
- vendor-specific integration drift
- human review of generated changes
applies_to:
- Resend
- Codex-assisted development
- tool-catalog coverage-gap review
stability:
  principle: CORE_ENGINEERING
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.tool_sprawl
- vcb.shortcut.trusting_external_tool_output
- vcb.shortcut.real_secrets_in_prototype
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.skipping_tests
durable_principles:
- Treat tool output as evidence, not approval.
- Keep secrets, production data, money movement, and account authority behind explicit
  review gates.
- Prefer small reversible changes, clear owners, and observable rollback paths.
- Separate prototype convenience from production ownership and maintenance.
likely_to_change:
- pricing
- plans
- quota limits
- UI labels
- SDK setup mechanics
- feature availability
- default permissions
- integration behavior
- retention or deployment limits
- current capability claims
obsolete_when:
- Resend is no longer available, no longer documented by its vendor, or no longer
  serves its stated tool-catalog role.
related_topics:
- tool.clerk
- tool.auth0
- tool.stripe
- tool.sentry
- tool.posthog
- vcb.safety.production_red_lines
---

# Resend

> Summary:
> Resend is for transactional email API, sending-domain review, templates, delivery evidence, and notification workflows. Use it to make evidence more explicit, not to skip design, review, security, or operational ownership.

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

<!-- VCB:BEGIN_SECTION id=tool.resend.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Resend is an email API/product for developers building transactional and related email workflows.

### Why it matters

Email is often treated as an afterthought, but it touches user trust, domains, deliverability, privacy, secrets, account state, and sometimes payments or auth flows.

### What good looks like

Good use starts with a clear project phase, a named owner, fake-versus-real data boundaries, and the evidence required before trusting the result. For production-bound work, require reviewable configuration, logs/checks, rollback path, and security/privacy review.

### What bad looks like

Bad use is treating a dashboard, generated integration, passing setup wizard, green check, or clean summary as proof that the system is production-ready. Tool output is a signal. It is not approval.

### Best-fit cases

- transactional email prototypes and production flows
- passwordless/auth-adjacent notification flows after review
- domain and sending policy review
- template and event-trigger evidence
- Codex-assisted email integration with fake recipients first

### Not-fit cases

- sending to real users from unreviewed generated code
- stable prose about quotas, pricing, deliverability guarantees, or UI labels
- putting API keys in prompts or logs
- using a successful send as approval of privacy/compliance
- bulk marketing without consent and legal review

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: API integration can be simple, but domains, API keys, templates, event triggers, sender identity, and recipient policy need review |
| Maintenance effort | medium-high: templates, deliverability, suppression/error handling, domain state, secret rotation, and event triggers drift |
| Debugging effort | medium-high: failures can involve DNS, sender/domain validation, templates, API errors, spam filtering, webhooks, or bad recipient data |
| Lock-in risk | moderate: templates, event names, SDK/API conventions, domains, and delivery diagnostics can become platform-specific |
| Hidden cost risk | medium-high: domain setup, compliance review, deliverability debugging, support tickets, and accidental real-user sends are hidden costs |

### Human checklist

- State whether the work is a throwaway prototype, MVP, production build, or maintenance change.
- Identify what the tool can touch: users, secrets, databases, payments, logs, analytics, deployments, domains, local state, or third-party accounts.
- Define the evidence before trusting the change: diff, config, logs, tests, preview, trace, dashboard, event, email, story, branch, or rollback drill.
- Keep exact pricing, limits, quotas, setup, UI labels, and default permissions source-checked instead of memorized.
- Decide the exit path: keep, harden, replace, migrate, roll back, or discard.

<!-- VCB:END_SECTION id=tool.resend.human -->

<!-- VCB:BEGIN_SECTION id=tool.resend.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Coaching stance

Treat `tool.resend` as a tool-selection and evidence-routing card. The goal is not to make the user use Resend; it is to decide whether this surface is the smallest reliable tool for the job and what evidence is required before trusting it.

### Diagnostic questions

- What is the project phase: disposable prototype, MVP, production build, or maintenance?
- What can the tool touch: source code, domains, users, secrets, data, money, CI, deployment, browser state, or team workflow?
- What exact artifact will prove the result: diff, log, test, branch, trace, screenshot, email, preview, story, dashboard, or rollback drill?
- What must remain out of prompts and screenshots: secrets, real customer data, payment state, auth tokens, and private account context?
- What is the rollback, disable, or migration path?

### Coaching tactics

- Ask for the smallest useful tool surface before adding a new account, integration, or vendor dependency.
- Convert vague tool requests into a task, risk, owner, evidence, and rollback plan.
- For generated code or setup instructions, require current vendor docs for exact mechanics.
- Keep broad chapters as companions; route the user to the smallest active tool card first when the intent is tool-specific.

### Red flags

- The user says "it deployed", "the dashboard is green", "the email sent", "the story renders", or "the test passes" as if that proves product correctness.
- Real users, secrets, production data, money, or public domains enter the task without review gates.
- The user wants pricing, quotas, limits, UI paths, command flags, or setup details from memory.
- The tool is being added because the user is stuck, not because it reduces project risk.

### Prompt pattern

```text
Use `tool.resend` only as a bounded tool in this project. First identify what it can touch, what evidence proves it is configured or used correctly, what can be rolled back, and what must not be changed without human approval. Do not rely on remembered pricing, limits, UI labels, commands, or setup mechanics; route those to current vendor docs.
```

<!-- VCB:END_SECTION id=tool.resend.ai_coach -->

## Shortcut Reality

### The shortcut people take

They add Resend because it appears to solve a whole category quickly, then accept the default setup, polished artifact, dashboard status, generated integration, or green check as proof.

### When the shortcut is acceptable

It is acceptable for a bounded prototype, learning task, or low-risk review spike where fake data is used, permissions are limited, and the output will be reviewed before promotion.

### When it becomes a bad trade

It becomes a bad trade when real users, secrets, payments, production data, account authority, release gates, or team commitments depend on settings or artifacts nobody reviewed.

### Risk profile

| Dimension | Rating |
|---|---|
| Probability of misuse | medium |
| Impact of misuse | medium-high for shared or production-bound work; high when secrets, data, money, account authority, public domains, or release state are involved |
| Recoverability | medium when isolated; low after real data, customer-visible state, money movement, or public production state |
| Blast radius | project files, vendor account, local environment, CI/release state, users, team process, and source-of-truth evidence |

### Minimum guardrails

- Use fake data and restricted accounts until the tool is explicitly production-approved.
- Keep secrets in approved secret stores, not prompts, screenshots, design files, tickets, logs, generated config, or test fixtures.
- Require a rollback, archive, disable, or migration path before using the tool as part of a release path.
- Record owners for configuration, billing, access, review, and maintenance.
- Review current official vendor docs before exact setup or limit-sensitive decisions.

### Recovery plan

1. Freeze further changes and identify what the tool touched.
2. Revoke risky permissions, rotate exposed secrets, and isolate affected environments or accounts.
3. Roll back config, deployment, database, email, UI, test, workflow, or release-state changes where possible.
4. Reconstruct evidence from logs, diffs, links, comments, dashboards, account history, and review notes.
5. Add the missing guardrail: test, owner, approval gate, cleanup policy, rollback checklist, or source-checked setup note.

## Budget and Constraint Notes

### Cheapest reliable path

Use the smallest supported surface, fake data, limited permissions, and manual review. Avoid paid, seat-sensitive, usage-sensitive, or migration-heavy features until the tool's role is justified.

### Fastest high-usage path

Use the tool only with explicit owner assignment, review artifacts, usage/billing watch, and a stop condition. Speed is acceptable only when rollback and evidence are already defined.

### Low-attention path

Use read-only, report-only, or planning-only workflows where possible. Do not let low-attention operation mutate production infrastructure, user accounts, money, source-of-truth tickets, domains, or customer data without a human checkpoint.

### Production-quality path

Production use requires source-checked setup, review artifacts, tests/checks where relevant, privacy/security review, owner map, and operational maintenance plan. Exact pricing, quotas, limits, defaults, and feature availability belong in volatile/source review, not stable prose.

### Prototype vs production

Prototype use can optimize for speed and learning. Production use must optimize for ownership, auditability, reversibility, support, and user safety.

### Build vs maintenance

During build, use the tool to clarify architecture, design, workflow, or environment assumptions. During maintenance, use it to reduce incident time, stale-state drift, and regression risk without adding hidden tool sprawl.

## Stable Core

- Tool choice should follow project risk, data sensitivity, reversibility, and evidence needs.
- A working integration, design, issue status, test result, deployment, or running service is not proof of correctness.
- Tools that touch production state, external users, domains, secrets, money, or team workflow require explicit owners.
- Vendor dashboards and AI summaries are evidence sources, not decision-makers.
- Production-bound systems need rollback, monitoring, and review before launch.

## Volatile Surface

Review current vendor docs before relying on:

- exact pricing, plan limits, seats, quotas, retention windows, or usage tiers;
- current UI labels, setup steps, command flags, SDK names, or default permissions;
- deployment, runtime, database, email, testing, component, integration, and hosting mechanics;
- export/import behavior, account permissions, admin controls, feature packaging, and current capability claims.

## Obsolescence Watch

Re-check this card when:

- the vendor changes docs, pricing, product packaging, setup mechanics, or limits;
- the project moves from prototype to production;
- real users, secrets, money, production data, or regulated data enter scope;
- the tool becomes a source of incidents, hidden costs, stale work, or lock-in;
- a smaller active VCB card supersedes this tool for the user intent.

## Evidence and Sources

- `resend.docs.introduction` — official vendor documentation anchor for Resend facts and volatile setup/product mechanics.
- `resend.docs.send_email` — official vendor documentation anchor for Resend facts and volatile setup/product mechanics.
- `resend.docs.templates` — official vendor documentation anchor for Resend facts and volatile setup/product mechanics.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for stable engineering control loops, risk framing, and coaching guidance.

## Related Topics

- `tool.clerk`
- `tool.auth0`
- `tool.stripe`
- `tool.sentry`
- `tool.posthog`
- `vcb.safety.production_red_lines`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" -->
<!-- VCB:END_TOPIC id=tool.resend -->
