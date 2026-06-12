<!-- VCB:BEGIN_TOPIC id=vcb.chapter.tool_stack_catalog version=0.1.0 -->
---
id: vcb.chapter.tool_stack_catalog
title: "Chapter 42 — The Tool Stack Catalog"
type: chapter
chapter_number: 42
version: 0.1.0
last_verified: '2026-06-09'
next_review_due: '2026-07-09'
review_cadence: monthly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- all project types

source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: AGENTIC_PRINCIPLE
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE

budget_profiles:
- plus_constrained
- pro_high_throughput
- api_pay_as_you_go
- team_shared_budget

cost_postures:
- cheapest_reliable
- balanced
- fastest_possible
- unattended_high_throughput
- production_quality
- disposable_prototype

project_phases:
- prototype
- mvp
- production_build
- maintenance
- major_refactor
- emergency_hotfix

attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation

shortcut_profiles:
- vcb.shortcut.tool_sprawl
- vcb.shortcut.buying_tools_as_progress
- vcb.shortcut.adding_dependencies_fast
- vcb.shortcut.framework_churn

durable_principles:
- Every tool adds setup, maintenance, debugging, lock-in, and hidden-cost risk.
- Recommend the smallest stack for the next milestone.
- Exact pricing and feature access belong in snapshots/tool cards.

likely_to_change:
- vendor pricing
- tool capabilities
- integrations
- AI product positioning
- plan packaging

obsolete_when:
- Codex product behavior or pricing model materially changes.

related_topics:
- vcb.chapter.cost_benefit_analysis
- vcb.chapter.dependency_package_framework_decisions
- vcb.chapter.when_to_use_other_ais
- tool.ai_coding_tools
- tool.hosting_and_deployment
- tool.databases_and_backend
---

> Summary:
> Tools add capability and complexity. This catalog teaches how to select the smallest stack that reaches the next milestone without creating needless lock-in, hidden cost, or maintenance load.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.tool_stack_catalog.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A tool stack is the set of services and products your project depends on: repo, CI, hosting, database, auth, payments, email, analytics, observability, design, docs, secrets, and AI tools.

A tool is not just a feature. It is a relationship. It adds setup work, billing, failure modes, docs, permissions, migration cost, and things Codex must understand.

### The smallest-useful-stack rule

Use the smallest stack that reaches the next milestone.

For a first serious app, the default should usually be:

```text
Repo + deploy target + database if needed + auth if needed + one error/log path + one AI implementer + Git checks.
```

Everything else needs a reason.

### Catalog by category

| Category | Representative tools | Use when | Delay when |
|---|---|---|---|
| AI coding | Codex, ChatGPT, Cursor, Copilot, Claude, Windsurf | planning, implementation, review, explanation | tools fight over files or duplicate roles |
| Repo/CI | GitHub, GitHub Actions | collaboration, checks, PRs, automation | no stable commands exist yet |
| Hosting | Vercel, Netlify, Cloudflare, Render, Railway, Fly.io | deploy and preview environments | platform-specific debugging exceeds value |
| Database/backend | Supabase, Neon, Firebase, Prisma, Drizzle | persistent data and APIs | local files or mock data are enough |
| Auth | Clerk, Auth0, Supabase Auth, Firebase Auth, Auth.js | real user identity | prototype can use fake users |
| Payments | Stripe, Paddle, Lemon Squeezy | real monetization | pricing/product loop is unproven |
| Email/SMS | Resend, Postmark, SendGrid, Twilio | notifications, login, transactional email | manual/demo notification is enough |
| Observability | Sentry, Better Stack, platform logs | production debugging | no users yet and local logs suffice |
| Analytics | PostHog, Plausible, product events | product behavior questions | you do not know what decisions analytics will drive |
| Design/prototype | Figma, v0, Lovable, Bolt, Replit | visual iteration or quick demo | output becomes unreviewed production |
| Project/docs | Linear, GitHub Issues, Notion, Docs | repeated work and team context | solo backlog fits in Markdown |
| Local dev/secrets | Docker, Dev Containers, 1Password, Doppler, Infisical | reproducible setup and safer secrets | setup cost exceeds project risk |

### Bad buying patterns

| Pattern | Why it feels good | Why it hurts |
|---|---|---|
| Buying every AI coding tool | feels like optionality | produces conflicting advice and subscription drag |
| Adding enterprise auth early | feels serious | creates complexity before users exist |
| Adding observability before traffic | feels professional | produces empty dashboards and setup overhead |
| Choosing cloud infra too early | feels scalable | creates debugging and billing burden |
| Using app builders as production | fast dopamine | creates opaque architecture unless reviewed/hardened |

### Tool-selection prompt

```text
Recommend the smallest tool stack for this milestone.

Milestone:
Users/data/payment/auth involved:
Budget:
Maintenance tolerance:
Team size:
Must avoid:

For each tool, include setup effort, maintenance effort, lock-in risk, hidden cost risk, cheaper alternative, and when to replace it.
Do not recommend tools that are not needed for the next milestone.
```

<!-- VCB:END_SECTION id=vcb.chapter.tool_stack_catalog.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.tool_stack_catalog.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Prevent tool maximalism. Teach tool selection as a cost-benefit and risk exercise.

### Diagnose the human’s stack impulse

Ask:

- What milestone does this tool unlock?
- What happens if we delay it?
- Who maintains it?
- Does Codex need to understand its config?
- What data/secrets/permissions will it receive?
- Is this product capability or setup dopamine?

### Useful metaphor

Tools are kitchen appliances. A professional kitchen has many. A first sandwich does not need all of them.

### Coaching tactics

- Recommend categories before brands.
- Prefer existing project tools unless there is clear pain.
- For production tools, ask about pricing volatility, lock-in, migration, security, and operational burden.
- Route exact pricing to dated pricing snapshots.

### Red flags

- User asks for “the best stack” without milestone constraints.
- User adds auth/payments/analytics/observability before basic app behavior exists.
- User wants multiple AI implementers editing the same repo.
- User wants Codex to integrate a tool whose docs, credentials, or permissions are unclear.

<!-- VCB:END_SECTION id=vcb.chapter.tool_stack_catalog.ai_coach -->

## Shortcut Reality

### The ideal practice

Add tools only when they unlock the next milestone or reduce a repeated operational burden.

### What users often do instead

They buy tools because tutorials mention them, competitors use them, or the dashboard makes the project feel more real.

### When the shortcut may be fine

A rich tool stack is fine for demos, hackathons, and learning when you accept that it may be rebuilt.

### When the shortcut is a bad idea

It is dangerous when tools touch secrets, payments, auth, production deploys, user data, or long-term lock-in without review.

### Risk profile

- Probability of failure: medium.
- Impact if it fails: cost creep, tool sprawl, security exposure, migration pain.
- Ease of recovery: easy before production, hard after data and users accumulate.
- Blast radius: grows with credentials and production integrations.
- Hidden cost: support, invoices, incident debugging, vendor-specific patterns.

### Minimum guardrails

- Add one tool at a time.
- Write why it is needed.
- Prefer fake credentials in prototype.
- Record setup/run/check commands.
- Add source and pricing review dates.
- Keep an exit path.

### Recovery plan

Freeze new tools, list all services with credentials/data/costs, remove unused tools, document required ones, and migrate one category at a time only when needed.

## Budget and Constraint Notes

### Cheapest reliable path

Use fewer tools, platform defaults, existing repo/CI, and manual checks until the milestone proves the need.

### Fastest high-usage path

Use Codex to compare stack options, scaffold integrations, and produce setup docs, but require human approval before adding production dependencies or services.

### Low-attention path

Do not let Codex create accounts, configure billing, or wire credentials unattended. Ask for a report-only stack plan.

### Production-quality path

Require official docs, security review, secrets handling, cost watch, backup/rollback, and ownership for every production service.

## Stable Core

Tools add both capability and complexity. The smallest-stack principle, lock-in risk, setup cost, maintenance cost, and hidden-cost review are durable.

## Volatile Surface

Tool pricing, free tiers, feature packaging, AI integrations, quotas, and reliability change constantly. Exact values belong in dated snapshots or future tool cards.

## Obsolescence Watch

Review monthly. Obsolete when representative tool categories materially change or when a tool’s official capabilities/pricing no longer match its catalog positioning.

## Evidence and Sources

- `openai.codex.best_practices` — official Codex source for using tools only when they unlock workflows
- `vercel.docs.environments` — official vendor source for preview environments and deployment workflow anchors
- `supabase.docs.database` — official vendor source for Supabase/Postgres database positioning
- `stripe.docs.subscriptions` — official vendor source for subscription/payment workflow concepts
- `github.docs.actions_billing` — official GitHub source for CI billing volatility
- `sentry.docs` — official vendor source for error/performance monitoring concepts
- `posthog.pricing` — official vendor source for analytics/session replay pricing volatility

## Related Topics

- `vcb.chapter.cost_benefit_analysis`
- `vcb.chapter.dependency_package_framework_decisions`
- `vcb.chapter.when_to_use_other_ais`
- `tool.ai_coding_tools`
- `tool.repo_and_ci`
- `tool.hosting_and_deployment`
- `tool.databases_and_backend`
- `tool.auth`
- `tool.payments`
- `tool.observability`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.tool_stack_catalog -->
