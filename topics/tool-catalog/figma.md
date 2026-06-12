<!-- VCB:BEGIN_TOPIC id=tool.figma version=0.1.0 -->
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
evidence_scope: official vendor documentation plus VCB maintainer synthesis for setup, risk, budget, and coaching guidance
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
id: tool.figma
title: Figma
name: Figma
type: tool_card
category: design
status: active
review_cadence: quarterly
next_review_due: '2026-09-11'
last_pricing_reviewed: '2026-06-11'
pricing_volatility: very_high
pricing_snapshot_required: false
setup_effort: "low-medium: a design file can start quickly, but libraries, components, prototype flows, dev-ready markings, annotations, permissions, and design-system ownership need decisions"
maintenance_effort: "medium: components, variants, tokens, comments, handoff status, linked tickets, and implementation drift need recurring review"
debugging_effort: "medium: failures often involve stale screens, missing states, component overrides, ambiguous responsive behavior, missing accessibility notes, or implementation mismatch"
lock_in_risk: "moderate: design-system components, tokens, comments, handoff workflow, and team conventions can become durable product process"
hidden_cost_risk: "medium: fast design iteration hides costs for cleanup, component governance, design-review time, seats, handoff accuracy, and implementation reconciliation"
codex_integration_value: 'medium-high: useful as implementation, planning, review, or verification infrastructure, but Codex must still work from explicit artifacts, source docs, tests, diffs, and human-reviewed acceptance criteria'
best_for:
- UI/UX design exploration
- interactive prototypes and user-flow review
- design-system components and variants
- frontend handoff and Dev Mode inspection
- screenshots/specs as review evidence before implementation
not_for:
- accepting a screenshot as proof the shipped UI works
- treating Dev Mode output as implementation approval
- production frontend changes without browser/accessibility evidence
- stale mockups disconnected from tickets or code
- design files with unclear ownership or permissions
integrates_with_codex:
- GitHub PR and branch review
- Codex planning and implementation threads
- Codex output review and hardening passes
- tool-stack and senior-checklist workflows
hidden_costs:
- setup and migration cleanup
- permissions and account-review work
- maintenance and stale-state cleanup
- vendor-specific integration drift
- human review of generated or tool-derived artifacts
applies_to:
- Figma
- Docker/container, design/prototyping, or project-management workflows
- Codex-assisted development
stability:
  principle: CORE_ENGINEERING
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.eyeballing_ui
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.browser_clicking_without_repro
- vcb.shortcut.trusting_external_tool_output
durable_principles:
- Treat tool output as evidence, not approval.
- Keep secrets, production data, money movement, and account authority behind explicit review gates.
- Prefer small reversible changes, clear owners, and observable rollback paths.
- Separate prototype convenience from production ownership and maintenance.
likely_to_change:
- pricing
- plans
- seat limits
- quota limits
- UI labels
- command flags
- setup mechanics
- feature availability
- default permissions
- integration behavior
- and current capability claims
obsolete_when:
- Figma is no longer available, no longer documented by its vendor, or no longer serves its stated role.
related_topics:
- tool.playwright
- tool.v0
- vcb.workflow.frontend_work
- vcb.workflow.visual_qa
- vcb.workflow.accessibility_review
- vcb.failure.ui_taste_gap
- vcb.failure.done_claim_without_evidence
---

# Figma

> Summary:
> Figma is a collaborative design, prototype, component, and developer-handoff tool. Use it to make UI intent explicit and reviewable, not to treat screenshots or specs as proof that implementation is correct.

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

<!-- VCB:BEGIN_SECTION id=tool.figma.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Figma is for design files, components, prototypes, comments, screenshots, annotations, Dev Mode handoff, and frontend/design review evidence. It belongs in the tool stack when that role needs to be explicit, reviewable, and connected to actual project evidence.

Figma is where visual intent can be made concrete: states, flows, components, spacing, responsive expectations, and design comments. It is not where working software is proven.

### Why it matters

This tool can make work faster and more legible, but it can also create false confidence. A clean dashboard, neat ticket, polished design, or running container is not the same thing as reviewed software.

### What good looks like

Good use starts with a clear project phase, a named owner, and the evidence required before trusting the result. Use the tool to produce reviewable artifacts: files, comments, issues, designs, logs, status changes, configs, diffs, or test output.

### What bad looks like

Bad Figma use is approving a UI because it looks good in one frame. Missing states, stale components, untested keyboard paths, and design-code drift still create real bugs.

### Best-fit cases

- UI/UX design exploration
- interactive prototypes and user-flow review
- design-system components and variants
- frontend handoff and Dev Mode inspection
- screenshots/specs as review evidence before implementation

### Not-fit cases

- accepting a screenshot as proof the shipped UI works
- treating Dev Mode output as implementation approval
- production frontend changes without browser/accessibility evidence
- stale mockups disconnected from tickets or code
- design files with unclear ownership or permissions

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | low-medium: a design file can start quickly, but libraries, components, prototype flows, dev-ready markings, annotations, permissions, and design-system ownership need decisions |
| Maintenance effort | medium: components, variants, tokens, comments, handoff status, linked tickets, and implementation drift need recurring review |
| Debugging effort | medium: failures often involve stale screens, missing states, component overrides, ambiguous responsive behavior, missing accessibility notes, or implementation mismatch |
| Lock-in risk | moderate: design-system components, tokens, comments, handoff workflow, and team conventions can become durable product process |
| Hidden cost risk | medium: fast design iteration hides costs for cleanup, component governance, design-review time, seats, handoff accuracy, and implementation reconciliation |

### Human checklist

- State whether this is a throwaway prototype, MVP, production build, or maintenance change.
- Identify what the tool can touch: files, local services, designs, comments, tickets, users, secrets, databases, payments, deployments, or third-party accounts.
- Define the evidence before trusting the result: diff, config, test output, screenshot, prototype, issue link, project status, trace, dashboard, or rollback note.
- Keep exact pricing, limits, quotas, setup mechanics, UI labels, command flags, and default permissions source-checked instead of memorized.
- Decide the exit path: keep, harden, replace, migrate, roll back, archive, or discard.

<!-- VCB:END_SECTION id=tool.figma.human -->

<!-- VCB:BEGIN_SECTION id=tool.figma.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach `tool.figma` as a design-intent and handoff-evidence tool. It should trigger browser, accessibility, and implementation checks, not replace them.

### Diagnostic questions

- What is the smallest project outcome that needs this tool?
- What exact files, accounts, designs, issues, local services, workflows, or external systems can it affect?
- What proof will show the tool is configured or used correctly?
- What would be expensive or irreversible if the tool is wrong?
- Who owns review, rollback, access control, billing, cleanup, and long-term maintenance?

### Coaching tactics

- Force a phase label: prototype, MVP, production build, or maintenance.
- Ask for a real artifact before trust: config diff, test output, design link, issue link, comment thread, container output, workflow status, or project note.
- Convert tool enthusiasm into a risk matrix: data touched, users affected, reversibility, owner, and rollback path.
- Route exact setup mechanics, limits, feature availability, and pricing to current official vendor docs.

### Red flags

- The human says the tool proves the app is safe, ready, or complete.
- Real secrets, production data, payments, or user accounts are involved before review.
- Tool output is accepted without logs, diffs, tests, review, or owner assignment.
- The tool has broad account permissions but no revocation or ownership path.
- Pricing, quota, retention, setup, or default behavior is described from memory.

### Prompt pattern

```text
Use `tool.figma` only as a bounded tool in this project. First identify what it can touch, what evidence proves it is configured or used correctly, what can be rolled back, and what must not be changed without human approval. Do not rely on remembered pricing, limits, UI labels, commands, or setup mechanics; route those to current vendor docs.
```

<!-- VCB:END_SECTION id=tool.figma.ai_coach -->

## Shortcut Reality

### The shortcut people take

They add Figma because it seems to solve a whole category quickly, then accept the default setup, polished artifact, dashboard status, or generated integration as proof.

### When the shortcut is acceptable

It is acceptable for a bounded prototype, learning task, or low-risk review spike where fake data is used, permissions are limited, and the output will be reviewed before promotion.

### When it becomes a bad trade

It becomes a bad trade when real users, secrets, payments, production data, account authority, release gates, or team commitments depend on settings or artifacts nobody reviewed.

### Risk profile

| Dimension | Rating |
|---|---|
| Probability of misuse | medium |
| Impact of misuse | medium-high for shared or production-bound work; high when secrets, data, money, account authority, or release state are involved |
| Recoverability | medium when isolated; low after real data, customer-visible state, money movement, or broad team process drift |
| Blast radius | project files, local environment, team process, account permissions, customer evidence, and vendor lock-in |

### Minimum guardrails

- Use fake data and restricted accounts until the tool is explicitly production-approved.
- Keep secrets in approved secret stores, not prompts, screenshots, design files, tickets, logs, or generated config.
- Require a rollback, archive, or disable path before using the tool as part of a release path.
- Record owners for configuration, billing, access, review, and maintenance.
- Review current official vendor docs before exact setup or limit-sensitive decisions.

### Recovery plan

1. Freeze further changes and identify what the tool touched.
2. Revoke risky permissions, rotate exposed secrets, and isolate affected environments or accounts.
3. Roll back config, design, ticket, container, workflow, or release-state changes where possible.
4. Reconstruct evidence from logs, diffs, links, comments, dashboards, account history, and review notes.
5. Add the missing guardrail: test, owner, approval gate, cleanup policy, or rollback checklist.

## Budget and Constraint Notes

### Cheapest reliable path

Use the smallest supported surface, fake data, limited permissions, and manual review. Avoid paid, seat-sensitive, or usage-sensitive features until the tool's role is justified.

### Fastest high-usage path

Use the tool only with explicit owner assignment, review artifacts, usage/billing watch, and a stop condition. Speed is acceptable only when rollback and evidence are already defined.

### Low-attention path

Use read-only, report-only, or planning-only workflows where possible. Do not let low-attention operation mutate production infrastructure, user accounts, money, source-of-truth tickets, or customer data without a human checkpoint.

### Production-quality path

Production use requires source-checked setup, review artifacts, tests/checks where relevant, privacy/security review, owner map, and operational maintenance plan. Exact pricing, quotas, limits, defaults, and feature availability belong in volatile/source review, not stable prose.

### Prototype vs production

Prototype use can optimize for speed and learning. Production use must optimize for ownership, auditability, reversibility, support, and user safety.

### Build vs maintenance

During build, use the tool to clarify architecture, design, workflow, or environment assumptions. During maintenance, use it to reduce incident time, stale-state drift, and regression risk without adding hidden tool sprawl.

## Stable Core

- Tool choice should follow project risk, data sensitivity, reversibility, and evidence needs.
- A working integration, design, issue status, or running service is not proof of correctness.
- Tools that shape development environments, design intent, or team workflow require explicit owners.
- Vendor dashboards and AI summaries are evidence sources, not decision-makers.
- Production-bound systems need rollback, monitoring, and review before launch.

## Volatile Surface

Review current vendor docs before relying on:

- exact pricing, plan limits, seats, quotas, or retention windows;
- current UI labels, setup steps, command flags, SDK names, or default permissions;
- container/runtime defaults, design handoff mechanics, workflow/status mechanics, integrations, automation behavior, and feature availability;
- export/import behavior, account permissions, admin controls, and current capability claims.

## Obsolescence Watch

Re-check this card when:

- the vendor changes docs, pricing, product packaging, setup mechanics, or limits;
- the project moves from prototype to production;
- real users, secrets, money, production data, or regulated data enter scope;
- the tool becomes a source of incidents, hidden costs, stale work, or lock-in;
- a smaller active VCB card supersedes this tool for the user intent.

## Evidence and Sources

- `figma.docs.design` — official Figma design product anchor for collaborative design, prototyping, and product-development positioning.
- `figma.help.prototyping` — official Figma help anchor for interactive prototype flows and stakeholder/user feedback posture.
- `figma.help.components` — official Figma help anchor for reusable components, instances, libraries, and design-system consistency.
- `figma.help.dev_mode` — official Figma help anchor for Dev Mode inspection, ready-for-development surfaces, annotations, linked tickets, and volatile handoff mechanics.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for stable engineering control loops, risk framing, and coaching guidance.

## Related Topics

- `tool.playwright`
- `tool.v0`
- `vcb.workflow.frontend_work`
- `vcb.workflow.visual_qa`
- `vcb.workflow.accessibility_review`
- `vcb.failure.ui_taste_gap`
- `vcb.failure.done_claim_without_evidence`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" -->
<!-- VCB:END_TOPIC id=tool.figma -->
