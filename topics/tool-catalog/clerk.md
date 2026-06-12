<!-- VCB:BEGIN_TOPIC id=tool.clerk version=0.1.0 -->
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
evidence_scope: official vendor documentation plus VCB maintainer synthesis for setup, risk,
  budget, and coaching guidance
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
id: tool.clerk
title: Clerk
name: Clerk
type: tool_card
category: auth
status: active
review_cadence: quarterly
next_review_due: '2026-09-11'
last_pricing_reviewed: '2026-06-11'
pricing_volatility: very_high
pricing_snapshot_required: false
setup_effort: 'medium: prebuilt auth surfaces are fast, but session, organization, role, route,
  backend validation, and user-data decisions require design review'
maintenance_effort: 'medium-high: auth flows, organizations, roles, user metadata, session
  behavior, SDKs, and security settings change with product and app needs'
debugging_effort: 'medium-high: failures may involve session tokens, route protection, org
  context, backend authorization checks, webhooks, or frontend auth state'
lock_in_risk: 'moderate-high: prebuilt UI/components, session semantics, org model, user schema,
  and SDK integration can become app architecture'
hidden_cost_risk: 'high: fast sign-in hides authorization, user-data, org-role, migration,
  compliance, and support costs'
codex_integration_value: 'medium-high: useful as implementation or verification infrastructure,
  but Codex must still work from explicit diffs, logs, tests, docs, and human-reviewed acceptance
  criteria'
best_for:
- startup auth and user management
- B2B organization-aware prototypes
- prebuilt auth UI with backend validation
- user/profile/session workflows
- auth surface before custom IAM complexity
not_for:
- treating login as authorization
- unreviewed role/permission logic
- production access rules without backend checks
- stable prose about current SDK/plan behavior
- security-sensitive flows without threat review
integrates_with_codex:
- Supabase/Vercel app stack
- Stripe customer/account workflows
- PostHog identify/group analytics
- Sentry user-context debugging
- Codex Security auth review
hidden_costs:
- setup and migration cleanup
- secrets and account-permission review
- maintenance and incident-response work
- vendor-specific integration drift
- human review of generated changes
applies_to:
- Clerk
- hosting/backend/auth/payment/observability/product-analytics workflows
- Codex-assisted development
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
- Treat platform output as evidence, not approval.
- Keep secrets, production data, money movement, and account authority behind explicit review
  gates.
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
- and current capability claims
obsolete_when:
- Clerk is no longer available, no longer documented by its vendor, or no longer serves its
  stated auth role.
related_topics:
- tool.supabase
- tool.auth0
- tool.stripe
- tool.posthog
- vcb.concepts.authentication
- vcb.concepts.authorization
- vcb.safety.security_review
---

# Clerk

> Summary:
> Clerk is a authentication, user management, sessions, organizations, and auth UI workflows for application identity tool. Use it to make product infrastructure more explicit, not to skip design, review, security, or operational ownership.

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

<!-- VCB:BEGIN_SECTION id=tool.clerk.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Clerk is for authentication, user management, sessions, organizations, and auth UI workflows for application identity. It belongs in the tool stack when the project needs that infrastructure role to be explicit and reviewable.

### Why it matters

This tool can make serious app work faster, but it also moves the project closer to real users, real data, real money, account authority, or production operations. That raises the cost of sloppy review.

### What good looks like

Good use starts with a clear project phase, a named owner, fake-versus-real data boundaries, and the evidence required before trusting the result. For production-bound work, require reviewable configuration, logs/checks, rollback path, and security/privacy review.

### What bad looks like

Bad use is treating a dashboard, generated integration, passing setup wizard, green check, or clean summary as proof that the system is production-ready. Tool output is a signal. It is not approval.

### Best-fit cases

- startup auth and user management
- B2B organization-aware prototypes
- prebuilt auth UI with backend validation
- user/profile/session workflows
- auth surface before custom IAM complexity

### Not-fit cases

- treating login as authorization
- unreviewed role/permission logic
- production access rules without backend checks
- stable prose about current SDK/plan behavior
- security-sensitive flows without threat review

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: prebuilt auth surfaces are fast, but session, organization, role, route, backend validation, and user-data decisions require design review |
| Maintenance effort | medium-high: auth flows, organizations, roles, user metadata, session behavior, SDKs, and security settings change with product and app needs |
| Debugging effort | medium-high: failures may involve session tokens, route protection, org context, backend authorization checks, webhooks, or frontend auth state |
| Lock-in risk | moderate-high: prebuilt UI/components, session semantics, org model, user schema, and SDK integration can become app architecture |
| Hidden cost risk | high: fast sign-in hides authorization, user-data, org-role, migration, compliance, and support costs |

### Human checklist

- State whether the work is a throwaway prototype, MVP, production build, or maintenance change.
- Identify what the tool can touch: users, secrets, databases, payments, logs, analytics, deployments, or third-party accounts.
- Define the evidence before trusting the change: diff, config, logs, tests, preview, webhook event, trace, dashboard, or rollback drill.
- Keep exact pricing, limits, quotas, SDK setup, UI labels, and default permissions source-checked instead of memorized.
- Decide the exit path: keep, harden, replace, migrate, roll back, or discard.

<!-- VCB:END_SECTION id=tool.clerk.human -->

<!-- VCB:BEGIN_SECTION id=tool.clerk.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach `tool.clerk` as a production-infrastructure tool card. The human should use it to expose risk, evidence, and ownership, not to outsource judgment to a vendor dashboard or generated integration.

### Diagnostic questions

- What is the smallest project outcome that needs this tool?
- What exact account, environment, repo, deployment, database, identity surface, payment object, event stream, or telemetry surface can it affect?
- What proof will show the tool is configured correctly?
- What would be expensive or irreversible if the tool is wrong?
- Who owns review, rollback, billing, privacy, and support after launch?

### Coaching tactics

- Force a phase label: prototype, MVP, production build, or maintenance.
- Ask for a real artifact before trust: config diff, test output, preview URL, webhook log, database migration, dashboard screenshot with timestamp, or incident note.
- Convert tool-specific enthusiasm into a risk matrix: data touched, users affected, reversibility, owner, and rollback path.
- Route setup mechanics to current vendor docs and keep stable VCB prose focused on principles.

### Red flags

- The human says the tool proves the app is safe or production-ready.
- Real secrets, production data, payments, or user accounts are involved before review.
- Dashboard output is accepted without logs, diffs, tests, or rollback plan.
- The tool has broad account permissions but no named owner.
- Pricing, quota, retention, or default behavior is described from memory.

### Prompt pattern

```text
Use `tool.clerk` only as a bounded tool in this project. First identify what it can touch, what evidence proves it is configured correctly, what can be rolled back, and what must not be changed without human approval. Do not rely on remembered pricing, limits, UI labels, or setup mechanics; route those to current vendor docs.
```

<!-- VCB:END_SECTION id=tool.clerk.ai_coach -->

## Shortcut Reality

### The shortcut people take

They add Clerk because it appears to solve a whole infrastructure category quickly, then accept the default setup or generated integration as production evidence.

### When the shortcut is acceptable

It is acceptable for a bounded prototype, learning app, or low-risk review spike where fake data is used, the tool account is low privilege, and the output will be reviewed before promotion.

### When it becomes a bad trade

It becomes a bad trade when real users, secrets, payments, production data, identity, deployment, or incident response depend on settings nobody reviewed.

### Risk profile

| Dimension | Rating |
|---|---|
| Probability of misuse | medium-high |
| Impact of misuse | high for production-bound apps, auth/payment/data surfaces, and user-facing releases |
| Recoverability | medium when isolated; low after real data, money movement, account compromise, or customer-visible rollout |
| Blast radius | project, users, data, account permissions, invoices, incidents, and vendor lock-in |

### Minimum guardrails

- Use fake data and restricted accounts until the tool is explicitly production-approved.
- Keep secrets in approved secret stores, not prompts, screenshots, logs, or generated code.
- Require a rollback or disable path before release.
- Record owners for configuration, billing, alerts, user support, and incident response.
- Review current official vendor docs before exact setup or limit-sensitive decisions.

### Recovery plan

1. Freeze further changes and identify what the tool touched.
2. Rotate exposed secrets, revoke risky tokens, or narrow permissions.
3. Roll back config/deployment/data/flag/payment changes where possible.
4. Reconstruct evidence from logs, diffs, events, dashboards, and account history.
5. Add the missing guardrail: test, alert, review owner, migration plan, or rollback checklist.

## Budget and Constraint Notes

### Cheapest reliable path

Use the smallest supported surface, fake data, limited permissions, and manual review. Avoid paid/usage-sensitive features until the tool's role is justified.

### Fastest high-usage path

Use the tool only with explicit environment separation, owner assignment, review artifacts, and usage/billing watch. Speed is acceptable only when rollback and observability are already defined.

### Low-attention path

Use report-only or read-only workflows where possible. Do not let low-attention operation mutate production infrastructure, user accounts, payments, or customer data without a human checkpoint.

### Production-quality path

Production use requires source-checked setup, tests/checks, security/privacy review, rollback plan, owner map, and operational monitoring. Exact pricing, quotas, retention, defaults, and feature availability belong in volatile/snapshot review, not stable prose.

### Prototype vs production

Prototype use can optimize for speed and learning. Production use must optimize for ownership, auditability, reversibility, support, and user safety.

### Build vs maintenance

During build, use the tool to clarify architecture. During maintenance, use it to reduce incident time, update risk, and regression risk without adding hidden platform sprawl.

## Stable Core

- Tool choice should follow project risk, data sensitivity, reversibility, and evidence needs.
- A working integration is not proof of correctness.
- Auth, data, payments, deployments, observability, and analytics require explicit owners.
- Vendor dashboards and AI summaries are evidence sources, not decision-makers.
- Production-bound systems need rollback, monitoring, and review before launch.

## Volatile Surface

Review current vendor docs before relying on:

- exact pricing, plan limits, quotas, or retention windows;
- current UI labels, setup steps, SDK names, command flags, or default permissions;
- hosting/runtime limits, database limits, auth/session defaults, payment fees, analytics volume, or observability retention;
- current integrations, export behavior, deployment mechanics, or feature availability.

## Obsolescence Watch

Re-check this card when:

- the vendor changes docs, pricing, product packaging, SDK setup, or limits;
- the project moves from prototype to production;
- real users, secrets, money, production data, or regulated data enter scope;
- the tool becomes a source of incidents, hidden costs, or lock-in;
- a smaller active VCB card supersedes this tool for the user intent.

## Evidence and Sources

- `clerk.docs.overview` — official vendor documentation anchor.
- `clerk.docs.user_management` — official vendor documentation anchor.
- `clerk.docs.session_tokens` — official vendor documentation anchor.
- `clerk.docs.organizations` — official vendor documentation anchor.
- `clerk.docs.restrictions` — official vendor documentation anchor.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for stable engineering control loops, risk framing, and coaching guidance.

## Related Topics

- `tool.supabase`
- `tool.auth0`
- `tool.stripe`
- `tool.posthog`
- `vcb.concepts.authentication`
- `vcb.concepts.authorization`
- `vcb.safety.security_review`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" -->
<!-- VCB:END_TOPIC id=tool.clerk -->
