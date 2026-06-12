<!-- VCB:BEGIN_TOPIC id=tool.bolt version=0.1.0 -->
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
evidence_scope: official vendor documentation plus VCB maintainer synthesis for setup,
  risk, budget, and coaching guidance
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
id: tool.bolt
title: Bolt
name: Bolt
type: tool_card
category: app_builder
status: active
review_cadence: quarterly
next_review_due: '2026-09-11'
last_pricing_reviewed: '2026-06-11'
pricing_volatility: very_high
pricing_snapshot_required: false
setup_effort: 'low-medium: a prompt can start the project quickly, but publish target,
  repo handoff, dependencies, tokens, and integrations need explicit choices'
maintenance_effort: 'medium: project dependencies, generated structure, token usage,
  integrations, and publish settings need cleanup as the app grows'
debugging_effort: 'medium-high: failures may involve generated code, package installs,
  browser preview state, backend/database assumptions, mobile packaging, or hosting
  behavior'
lock_in_risk: 'moderate: browser-builder workflow and hosted project history can shape
  how the team edits, deploys, and reasons about the app'
hidden_cost_risk: 'high: token usage, generated-code review, dependency drift, and
  prototype hardening costs can exceed the initial time saved'
codex_integration_value: 'medium: useful for fast sketching; Codex can later inspect
  the repo, isolate risky diffs, write tests, or produce hardening plans'
best_for:
- browser-based full-stack prototyping
- website and app sketching
- MVP demos with review owner
- mobile-app prototype exploration
- fast iteration before formal repo workflow
not_for:
- secret-heavy production apps
- unreviewed dependency additions
- regulated workflows without governance
- accepting generated output without file/diff review
- stable prose about current token or hosting limits
integrates_with_codex:
- GitHub/code review handoff
- npm dependency review
- Playwright/browser evidence
- Codex review/hardening
- CI workflow after repo migration
hidden_costs:
- token burn from repeated prompting
- dependency cleanup
- prototype-to-repo migration
- generated file review
- mobile/web publishing rework
applies_to:
- Bolt
- browser-dev / app-builder / UI-generation workflows
- Codex-assisted development
stability:
  principle: CORE_ENGINEERING
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.tool_sprawl
- vcb.shortcut.real_secrets_in_prototype
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.skipping_tests
- vcb.shortcut.trusting_external_tool_output
durable_principles:
- Use app builders for bounded product learning, not implicit production approval.
- Require code, diff, browser, dependency, and security evidence before trusting generated
  apps.
- Separate prototype speed from ownership, deployment, testing, and maintenance responsibility.
- Keep secrets and real customer data out of disposable prototypes unless explicitly
  approved.
likely_to_change:
- pricing
- plans
- quota behavior
- model availability
- UI labels
- deployment mechanics
- export behavior
- integrations
- default stacks
- hosting/runtime limits
- and current capability claims
obsolete_when:
- Bolt is no longer available, no longer documented by its vendor, or no longer serves
  its stated browser-dev / app-builder / UI-generation role.
related_topics:
- tool.github
- tool.npm
- tool.playwright
- tool.github_actions
- vcb.workflow.dependency_decisions
- vcb.shortcut.adding_dependencies_fast
- vcb.shortcut.real_secrets_in_prototype
- vcb.failure.dependency_bloat

---

# Bolt

> Summary:
> Bolt is an AI-powered browser builder for turning ideas into websites, web apps, and mobile-app prototypes with a chat-first build loop.

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

<!-- VCB:BEGIN_SECTION id=tool.bolt.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Bolt is a browser-based app-builder. It is useful when the goal is to build a working prototype quickly, explore a website/app idea, or generate a first version that can be reviewed and iterated.

### Why it matters

It is optimized for speed from prompt to working product. That speed is useful for discovery, but it can create token burn, broad generated changes, dependency ambiguity, and false confidence in unreviewed full-stack behavior.

### What good looks like

Use Bolt for short prototype loops, MVP demos, website/app sketches, and first-pass flows where the human inspects generated files, dependencies, integration boundaries, and publish/deploy posture.

### What bad looks like

Do not let Bolt become the production source of truth without code review, dependency review, tests, secrets policy, and deployment ownership.

### Best-fit cases

- browser-based full-stack prototyping
- website and app sketching
- MVP demos with review owner
- mobile-app prototype exploration
- fast iteration before formal repo workflow

### Not-fit cases

- secret-heavy production apps
- unreviewed dependency additions
- regulated workflows without governance
- accepting generated output without file/diff review
- stable prose about current token or hosting limits

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | low-medium: a prompt can start the project quickly, but publish target, repo handoff, dependencies, tokens, and integrations need explicit choices |
| Maintenance effort | medium: project dependencies, generated structure, token usage, integrations, and publish settings need cleanup as the app grows |
| Debugging effort | medium-high: failures may involve generated code, package installs, browser preview state, backend/database assumptions, mobile packaging, or hosting behavior |
| Lock-in risk | moderate: browser-builder workflow and hosted project history can shape how the team edits, deploys, and reasons about the app |
| Hidden cost risk | high: token usage, generated-code review, dependency drift, and prototype hardening costs can exceed the initial time saved |

### Human checklist

- State whether this is a sketch, prototype, MVP, or production-bound artifact.
- Name the proof artifact before trusting output: source code, diff, browser recording, trace, screenshot, test, PR, or deployment checklist.
- Keep real secrets, production databases, customer data, and payment credentials out unless the tool/account/environment is explicitly approved.
- Review generated dependencies, integration settings, environment variables, and hosting/deployment assumptions.
- Decide the exit path: discard, export, rewrite, harden, or maintain.

<!-- VCB:END_SECTION id=tool.bolt.human -->

<!-- VCB:BEGIN_SECTION id=tool.bolt.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach `tool.bolt` as a bounded app-builder/browser-dev/UI-generation surface. The human should use it to accelerate product learning, not to bypass engineering ownership.

### Diagnostic questions

- Is the requested output a disposable demo, a stakeholder prototype, an MVP candidate, or production-bound code?
- What data, credentials, integrations, accounts, and deployment targets can the tool touch?
- What artifact will prove the generated result: diff, tests, browser evidence, trace, PR, dependency review, or security review?
- Who owns the code after generation: the app-builder project, a GitHub repo, Codex, or a human maintainer?
- What would make this unsafe: real users, secrets, payments, production data, broad dependencies, or misleading visual polish?

### Coaching tactics

- push the user to name prototype versus production before choosing the tool
- require fake data and staging credentials for first demos
- convert impressive output into reviewable artifacts before claiming progress
- route UI/browser proof to `tool.playwright` when behavior or screenshots matter
- route repo ownership to `tool.github`, dependency review to `tool.npm`, and security review to `vcb.safety.security_review` or `tool.codex_security` when relevant

### Prompt pattern

```text
Use Bolt only for the smallest safe role in this task.
Goal: [prototype / MVP sketch / UI variant / stakeholder demo]
Data boundary: [fake/staging/production/no sensitive data]
Allowed authority: [generate only / edit project / publish demo / create PR]
Required evidence: [diff / browser screenshot / trace / test / PR / review checklist]
Exit path: [discard / export / rewrite / harden / maintain]
Give the tool-fit recommendation, guardrails, and review path before generating or shipping anything.
```

### Red flags

- The user says “it deployed” as if deployment proves correctness.
- The user wants to use real credentials or customer data in a prototype.
- The app has auth, payments, admin actions, or sensitive data but no security owner.
- Generated dependencies or integrations are accepted without inspection.
- Visual polish is being used as a substitute for state, accessibility, and browser evidence.

<!-- VCB:END_SECTION id=tool.bolt.ai_coach -->

## Shortcut Reality

### Ideal practice

Choose `tool.bolt` when its output matches the task shape and review budget. Use it to produce a bounded app, UI, or prototype artifact, then inspect the code, dependencies, data boundaries, and deployment path before relying on it.

### What users often do instead

They prompt until the app looks impressive, publish a demo, and treat the running preview as proof that the architecture, security, dependencies, accessibility, and maintenance posture are solved.

### When the shortcut is acceptable

The shortcut is acceptable when the output is a disposable prototype or reviewable starting point with no real secrets/users/money and clear stopping criteria.

### When it becomes a bad trade

It becomes a bad trade when the team keeps prompting until something looks finished, then ships without dependency, browser, security, or ownership review.

### Risk profile

| Risk dimension | Practical read |
|---|---|
| Probability | High: app-builder speed encourages users to skip ownership and review decisions. |
| Impact | Medium to high: impact rises with real users, credentials, databases, payments, dependencies, and deployment authority. |
| Recoverability | Moderate: recovery is easiest when the project is isolated, fake-data-only, versioned, and has a clear export/rewrite path. |

### Blast radius

The blast radius includes generated dependency risk, unreviewed auth/data flows, misleading UI polish, leaked secrets, fragile deployment assumptions, product expectations set by demos, and maintenance work hidden behind a fast first build.

### Minimum guardrails

- use fake or staging data for prototypes
- keep one source of truth for the code after generation
- review generated dependencies and integration boundaries
- require browser/state/accessibility evidence for UI claims
- require security review before real auth, payments, or sensitive data
- define the exit path before the demo becomes the roadmap

### Recovery plan

- stop adding features
- export or inspect the generated code and project settings
- rotate any exposed secrets
- list dependencies, integrations, data stores, and deployment targets
- move production-bound work into a reviewed repo/branch/PR
- add tests, browser evidence, and security review before real users

## Budget and Constraint Notes

| Constraint profile | Cheapest reliable path | Fastest high-usage path | Low-attention path | Production-quality path |
|---|---|---|---|---|
| Individual / constrained usage | Use it for one bounded prototype with fake data and a written exit path. | Batch related UI/app questions, then freeze scope and review the generated code. | Use report/demo mode only; do not publish or connect real services unattended. | Move production-bound work into a repo with tests, dependency review, and owner review. |
| Team / shared budget | Define when the team may use app builders versus Codex, GitHub, or manual implementation. | Use a template for prototype review packets. | Route non-urgent ideas to demo-first, review-later artifacts. | Track setup, review, security, migration, and maintenance cost, not just tool subscription cost. |
| Prototype | Accept rough scaffolding if no real users, money, secrets, or production data are involved. | Use it to compare product flows quickly. | Keep the artifact disposable unless explicitly promoted. | Add acceptance criteria before converting to MVP work. |
| Production / maintenance | Prefer narrow UI or proof-of-concept tasks, not broad app ownership. | Use only with branch/repo isolation and reviewable diffs. | Use report-only or demo-only posture unless an owner can inspect the result. | Require rollback, security review, browser/test evidence, and source-checked volatile details. |

Do not freeze exact prices, plan limits, quota limits, model availability, hosting/runtime limits, UI labels, deployment mechanics, integration limits, export behavior, command flags, or current capability claims in stable guidance. Put exact values in dated pricing snapshots or source-checked volatile notes.

## Stable Core

- App builders are acceleration surfaces, not approval surfaces.
- A running preview proves only that something runs in that context.
- Production use requires ownership of code, data, secrets, dependencies, deployment, tests, and rollback.
- UI generation must still cover loading, empty, error, success, mobile, keyboard, and accessibility states.
- Browser evidence is useful only when tied to exact repro steps and expected/actual behavior.
- Token speed is not free if it creates review debt.
- Generated app structure must be inspected before it becomes the repo standard.

## Volatile Surface

- current pricing, plan limits, quota systems, credits, and usage accounting
- model availability, generation quality, and context behavior
- current UI labels, export paths, deployment mechanics, hosting/runtime limits, and integration catalogs
- default frameworks, package versions, generated project structure, and dependency behavior
- publishing, privacy, team/workspace, governance, and enterprise controls
- API, automation, MCP, GitHub, database, auth, storage, and third-party integration behavior

## Obsolescence Watch

Review this card when:

- the vendor changes product positioning, pricing, availability, or generation/deployment behavior
- the tool adds or removes repo export, GitHub, database, auth, hosting, or app-publishing capabilities
- team policy changes what tools may touch source code, secrets, customer data, or production accounts
- a more specific VCB tool card exists for the actual surface being used
- generated-output quality or default stack changes enough to alter review expectations

## Evidence and Sources

Evidence level: `E0_OFFICIAL_DOCS` plus `VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE` for tool-fit, risk, budget, and coaching guidance.

Source IDs:

- `bolt.docs.intro`
- `bolt.docs.quickstart`
- `bolt.docs.plan_app`
- `bolt.docs.tokens`
- `bolt.docs.glossary`
- `vcb.synthesis.stable_engineering_practice`

## Related Topics

- `tool.github`
- `tool.npm`
- `tool.playwright`
- `tool.github_actions`
- `vcb.workflow.dependency_decisions`
- `vcb.shortcut.adding_dependencies_fast`
- `vcb.shortcut.real_secrets_in_prototype`
- `vcb.failure.dependency_bloat`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=tool.bolt -->
