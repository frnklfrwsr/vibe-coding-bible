<!-- VCB:BEGIN_TOPIC id=tool.docker version=0.1.0 -->
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
id: tool.docker
title: Docker
name: Docker
type: tool_card
category: local_dev_containers
status: active
review_cadence: quarterly
next_review_due: '2026-09-11'
last_pricing_reviewed: '2026-06-11'
pricing_volatility: very_high
pricing_snapshot_required: false
setup_effort: "medium: Docker itself can be quick to install, but Dockerfiles, Compose files, volumes, ports, user permissions, networking, image provenance, and host resource settings need explicit review"
maintenance_effort: "medium-high: base images, package versions, build cache, volumes, Compose services, secrets, exposed ports, and local/CI drift need recurring maintenance"
debugging_effort: "medium-high: failures may involve image layers, package managers, build cache, DNS/networking, port conflicts, file mounts, platform architecture, volumes, or host permissions"
lock_in_risk: "moderate: Dockerfiles, Compose service names, image registries, volume layout, and dev-env assumptions can become part of the project architecture"
hidden_cost_risk: "medium-high: local convenience can hide onboarding, storage, cache, CPU/RAM, image security, CI runtime, registry, and licensing review costs"
codex_integration_value: 'medium-high: useful as implementation, planning, review, or verification infrastructure, but Codex must still work from explicit artifacts, source docs, tests, diffs, and human-reviewed acceptance criteria'
best_for:
- reproducible local databases and services
- dev onboarding without hand-built host setup
- containerized build/test environments
- CI parity for service-dependent workflows
- isolated experiments that must be easy to reset
not_for:
- treating containers as a complete security boundary
- shipping images without dependency/base-image review
- hiding secrets in Dockerfiles, images, or Compose files
- claiming production parity without testing the production target
- using Docker to mask dependency or environment confusion
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
- Docker
- Docker/container, design/prototyping, or project-management workflows
- Codex-assisted development
stability:
  principle: CORE_ENGINEERING
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.default_config_forever
- vcb.shortcut.real_secrets_in_prototype
- vcb.shortcut.skipping_tests
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
- Docker is no longer available, no longer documented by its vendor, or no longer serves its stated role.
related_topics:
- tool.github
- tool.github_actions
- tool.npm
- tool.playwright
- vcb.workflow.testing
- vcb.workflow.dependency_decisions
- vcb.concepts.environment_variable
---

# Docker

> Summary:
> Docker is a container, image, and local-service orchestration tool for making development environments more reproducible. Use it to make runtime assumptions explicit, not to pretend local containers are the same as production.

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

<!-- VCB:BEGIN_SECTION id=tool.docker.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Docker is for local development containers, repeatable service stacks, image-based packaging, Compose-based multi-service apps, and CI/parity evidence. It belongs in the tool stack when that role needs to be explicit, reviewable, and connected to actual project evidence.

Docker helps you define the app runtime instead of relying on whatever happens to be installed on a laptop. It is strongest when the repo contains reviewable files that say what services exist, what images are built, what ports are exposed, and what data is persistent.

### Why it matters

This tool can make work faster and more legible, but it can also create false confidence. A clean dashboard, neat ticket, polished design, or running container is not the same thing as reviewed software.

### What good looks like

Good use starts with a clear project phase, a named owner, and the evidence required before trusting the result. Use the tool to produce reviewable artifacts: files, comments, issues, designs, logs, status changes, configs, diffs, or test output.

### What bad looks like

Bad Docker use is a pile of containers that only one person understands. Worse: secrets baked into images, production-like labels on non-production stacks, or Compose files that mutate real databases by accident.

### Best-fit cases

- reproducible local databases and services
- dev onboarding without hand-built host setup
- containerized build/test environments
- CI parity for service-dependent workflows
- isolated experiments that must be easy to reset

### Not-fit cases

- treating containers as a complete security boundary
- shipping images without dependency/base-image review
- hiding secrets in Dockerfiles, images, or Compose files
- claiming production parity without testing the production target
- using Docker to mask dependency or environment confusion

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: Docker itself can be quick to install, but Dockerfiles, Compose files, volumes, ports, user permissions, networking, image provenance, and host resource settings need explicit review |
| Maintenance effort | medium-high: base images, package versions, build cache, volumes, Compose services, secrets, exposed ports, and local/CI drift need recurring maintenance |
| Debugging effort | medium-high: failures may involve image layers, package managers, build cache, DNS/networking, port conflicts, file mounts, platform architecture, volumes, or host permissions |
| Lock-in risk | moderate: Dockerfiles, Compose service names, image registries, volume layout, and dev-env assumptions can become part of the project architecture |
| Hidden cost risk | medium-high: local convenience can hide onboarding, storage, cache, CPU/RAM, image security, CI runtime, registry, and licensing review costs |

### Human checklist

- State whether this is a throwaway prototype, MVP, production build, or maintenance change.
- Identify what the tool can touch: files, local services, designs, comments, tickets, users, secrets, databases, payments, deployments, or third-party accounts.
- Define the evidence before trusting the result: diff, config, test output, screenshot, prototype, issue link, project status, trace, dashboard, or rollback note.
- Keep exact pricing, limits, quotas, setup mechanics, UI labels, command flags, and default permissions source-checked instead of memorized.
- Decide the exit path: keep, harden, replace, migrate, roll back, archive, or discard.

<!-- VCB:END_SECTION id=tool.docker.human -->

<!-- VCB:BEGIN_SECTION id=tool.docker.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach `tool.docker` as a reproducibility and isolation aid, not as proof that the application is secure, production-ready, or deployment-equivalent.

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
Use `tool.docker` only as a bounded tool in this project. First identify what it can touch, what evidence proves it is configured or used correctly, what can be rolled back, and what must not be changed without human approval. Do not rely on remembered pricing, limits, UI labels, commands, or setup mechanics; route those to current vendor docs.
```

<!-- VCB:END_SECTION id=tool.docker.ai_coach -->

## Shortcut Reality

### The shortcut people take

They add Docker because it seems to solve a whole category quickly, then accept the default setup, polished artifact, dashboard status, or generated integration as proof.

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

- `docker.docs.overview` — official Docker documentation anchor for containers, images, Docker Desktop, Docker client/daemon, registries, and lifecycle framing.
- `docker.docs.compose` — official Docker documentation anchor for multi-container application orchestration and Compose surface volatility.
- `docker.docs.dockerfile` — official Docker reference anchor for Dockerfile mechanics, image-building syntax, and build behavior volatility.
- `docker.docs.security` — official Docker security anchor for container isolation, daemon/host risk, and security posture.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for stable engineering control loops, risk framing, and coaching guidance.

## Related Topics

- `tool.github`
- `tool.github_actions`
- `tool.npm`
- `tool.playwright`
- `vcb.workflow.testing`
- `vcb.workflow.dependency_decisions`
- `vcb.concepts.environment_variable`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" -->
<!-- VCB:END_TOPIC id=tool.docker -->
