<!-- VCB:BEGIN_TOPIC id=vcb.chapter.first_serious_app version=0.1.0 -->
---
id: vcb.chapter.first_serious_app
title: "Chapter 34 — Building Your First Serious App with Codex"
type: chapter
chapter_number: 34
version: 0.1.0
last_verified: '2026-06-09'
next_review_due: '2026-09-09'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- browser checks
- tests
- CI
- security review
- first serious app

source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: CORE_ENGINEERING
  surface: MODERATE
  pricing: VOLATILE

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
- vcb.shortcut.generated_prototype_as_production_foundation
- vcb.shortcut.overbuilding_first_app
- vcb.shortcut.one_big_prompt
- vcb.shortcut.real_secrets_in_prototype
- vcb.shortcut.skipping_security_review

durable_principles:
- Build a vertical slice before expanding scope.
- Use fake data and isolated credentials until security boundaries are real.
- Prototype output is evidence for product direction, not proof of production readiness.

likely_to_change:
- best current app stack
- hosting/product defaults
- auth/database provider details
- pricing/plan economics
- Codex sites or deployment features
- framework-specific commands

obsolete_when:
- dominant app-building stack/product surfaces change materially.
- Codex provides a safer first-app wizard with built-in hardening and source-specific tool cards supersede this chapter.

related_topics:
- vcb.chapter.feature_slicing
- vcb.chapter.four_part_prompt
- vcb.chapter.acceptance_criteria
- vcb.chapter.agents_md_operating_manual
- vcb.chapter.frontend_work
- vcb.chapter.security_for_vibe_coders
- vcb.chapter.dependency_package_framework_decisions
- vcb.chapter.senior_engineer_checklist
---


> Summary:
> A first serious app should be built as a constrained vertical slice, not as a giant generated product. Codex can accelerate every step, but the human owns sequencing, scope, security boundaries, and acceptance criteria.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.first_serious_app.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Your first serious app is not your first toy. It is the first app where bad choices can matter: users may rely on it, data may persist, accounts may exist, payments may happen, or maintenance may become real.

Codex can help you build it faster. That does not mean the right plan is "describe the whole app and accept whatever comes back." The right plan is a controlled sequence:

```text
small product spec
→ architecture sketch
→ clean repo setup
→ AGENTS.md
→ vertical slice
→ tests/checks
→ auth/data carefully
→ UI states
→ review
→ release loop
→ post-launch bug loop
```

A vertical slice is one thin path through the app that proves the stack works end to end. It is not the whole product. Example: user can create one item, save it, see it again, and handle empty/error/loading states.

### Choose a constrained app

Do not start with a platform, marketplace, social network, or fully automated business system. Pick an app with:

- one primary user;
- one core workflow;
- one data model you can explain;
- limited integrations;
- no real payments at first;
- no high-risk personal data at first;
- an obvious manual fallback.

Bad first serious app:

```text
A multi-tenant SaaS with payments, OAuth, AI agents, file uploads, admin dashboard, billing portal, mobile app, analytics, and team roles.
```

Better first serious app:

```text
A private dashboard where one user can create, edit, and mark tasks complete, with login, a database, basic validation, and deployable build checks.
```

### Step 1: write a product spec

Keep the spec short:

- target user;
- problem;
- core workflow;
- non-goals;
- data to store;
- sensitive data to avoid;
- acceptance criteria;
- deployment target if known;
- maintenance tolerance.

Ask Codex to critique scope before building.

### Step 2: ask for architecture before code

Use a plan-only pass:

```text
Plan only. Do not edit files.

Goal:
Build the first serious version of [app].

Return:
- smallest vertical slice,
- repo structure,
- data model,
- routes/screens,
- auth/data/security boundaries,
- test strategy,
- deployment assumptions,
- what not to build yet,
- risks and rollback plan.
```

If the plan is huge, it is already wrong. Cut it down.

### Step 3: set up the repo and operating manual

Before major implementation:

- initialize Git;
- verify package manager and scripts;
- create or update `AGENTS.md`;
- define test/build/lint commands;
- write no-new-dependency and no-real-secret rules;
- define done criteria.

This prevents Codex from guessing the project’s operating system.

### Step 4: build one vertical slice

Ask for one slice only:

```text
Implement milestone 1 only:
A user can create [object], save it, and see it listed again.

Constraints:
- fake/local credentials only;
- no payment flow;
- no production data;
- no extra dependencies without approval;
- include loading, empty, error, and success states if applicable;
- keep diff reviewable.

Done when:
- app builds/runs;
- one relevant test or manual flow passes;
- final report lists changed files, checks, and gaps.
```

### Step 5: add hard parts deliberately

Do not add auth, database writes, file uploads, payments, email, and background jobs all at once.

Sequence them:

1. local data or fake data;
2. real database schema with migration plan;
3. auth with clear session/authorization behavior;
4. validation and error states;
5. tests for core behavior;
6. deploy preview;
7. monitoring/logging basics;
8. payment or sensitive flows only after review.

### Step 6: review like it matters

Before launch:

- inspect the diff;
- run build/lint/typecheck/tests where available;
- test the main flow manually;
- check empty/error/loading states;
- review dependencies;
- review auth/security/data behavior;
- write rollback notes;
- commit clean checkpoints.

### What good looks like

A good first serious app is boring in the right ways. It has fewer features, clearer behavior, fewer dependencies, obvious commands, and one core workflow that actually works.

### What bad looks like

Bad first serious apps usually fail because they try to look complete before they are reliable. They have many screens, vague data rules, unclear auth behavior, no tests, no rollback path, and a giant generated diff nobody understands.
<!-- VCB:END_SECTION id=vcb.chapter.first_serious_app.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.first_serious_app.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Coach the human through sequence and restraint. The main enemy is not lack of code. It is uncontrolled scope, hidden security/data risk, and accepting a prototype as production foundation.

### Diagnose the human’s current model

Ask:

- Is this still a prototype or a real app?
- Will real users, accounts, money, secrets, or persistent data be involved?
- Can the core workflow be explained in one sentence?
- Is the first slice small enough to test manually?
- Does the human want the full app before proving the slice?

### Explanation strategy

Use the vertical-slice model. Do not let the user build layers in isolation forever, and do not let them build everything at once.

A useful phrasing:

```text
We are not building the whole restaurant. We are proving one order can be placed, cooked, served, and paid for safely. Then we expand the menu.
```

### Useful metaphors

- **Vertical slice:** one elevator shaft from lobby to roof.
- **Prototype:** concept car.
- **Production foundation:** car you let your family drive.
- **AGENTS.md:** site foreman notes.
- **Tests:** smoke alarms.

### Coaching tactics

- Shrink the app idea before first implementation.
- Force non-goals into the prompt.
- Add real auth/data/payment only after fake/local behavior works.
- Insist on branch/Git checkpoints before major milestones.
- Turn repeated decisions into `AGENTS.md` only after they stabilize.
- Push hard against real secrets in early prototypes.

### Prompt patterns

```text
Act as a senior engineer scoping my first serious app.
Given this idea, reduce it to the smallest useful vertical slice.
Return:
- what to build first,
- what not to build yet,
- data model,
- risks,
- acceptance criteria,
- how to test it.
```

```text
Review this first-app plan for overreach.
Flag anything that adds unnecessary dependencies, external services, auth/payment complexity, production data risk, or unclear maintenance burden.
Return a smaller plan.
```

### Red flags to call out directly

- The user wants real payments before one local flow works.
- The user wants social/team/roles/admin/settings all in version one.
- The user wants to paste production API keys into a prototype.
- The user wants Codex to choose the whole stack without constraints.
- The generated diff is too large for the human to review.

### Exercises

Ask the human to write their app idea in one sentence, then turn it into one vertical slice and three explicit non-goals.
<!-- VCB:END_SECTION id=vcb.chapter.first_serious_app.ai_coach -->

## Shortcut Reality

### The ideal practice

Build a small, reviewable, testable vertical slice and expand only after the core loop works.

### What users often do instead

Users ask Codex to build the whole app from one prompt, accept a large scaffold, add real services early, and then try to harden the result after it is already tangled.

### When the shortcut may be fine

A one-prompt generated prototype is useful for product discovery, demos, or deciding whether an idea feels worth building.

### When the shortcut is a bad idea

It is a bad idea when you plan to keep the generated output as production foundation without review, tests, dependency review, auth/security review, data modeling, and rollback.

### Risk profile

- Probability of failure: medium/high if scope is broad.
- Impact if it fails: low for demos; high with users, data, payments, or auth.
- Ease of recovery: medium with Git and fake data; low after real users/data/services enter.
- Blast radius: grows with external services, secrets, and production deployment.
- Skill needed to recover: architecture, debugging, security, data modeling, deployment.
- Hidden cost: maintaining a messy prototype as if it were a product.

### Minimum guardrails

- New branch or repo.
- Fake credentials and fake data first.
- One vertical slice.
- No real payments or sensitive data in the first pass.
- No new dependencies without justification.
- Build/run/test or manual core-flow check.
- Final report with changed files, checks, gaps, and risks.

### Recovery plan

If the first app becomes too broad, stop implementation. Save useful product learnings. Start a fresh branch/repo with a smaller vertical slice. Copy ideas, not the entire generated codebase, unless it passes review.

### AI coach guidance

Do not optimize for impressiveness. Optimize for a core loop the human can understand, verify, and maintain.

## Budget and Constraint Notes

### Cheapest reliable path

Use Codex for planning, one feature slice, and one check at a time. Avoid subagents, broad cloud delegation, and new tools until the core loop works.

### Fastest high-usage path

Use cloud/worktrees for alternative implementations only after the vertical slice is defined. Compare diffs, not summaries. Use fresh-agent review before merging.

### Low-attention path

Low-attention first-app building should be branch-only, fake-data-only, with final reports and no real secrets. Do not leave Codex unattended with production services.

### Production-quality path

Add tests, PR review, dependency review, auth/security review, deployment checklist, rollback notes, monitoring basics, and post-launch bug workflow before calling it production.

## Stable Core

- Serious apps are built by sequencing risk.
- Vertical slices beat giant scaffolds.
- Fake data and fake credentials come before real secrets.
- Prototype code is not automatically production foundation.
- The human owns product scope, security boundaries, and acceptance criteria.

## Volatile Surface

- Current recommended stacks and frameworks.
- Codex app/site/deployment workflows.
- Plan-specific usage economics.
- Auth/database/hosting provider details.
- Exact commands for build/deploy/test in any given stack.

## Obsolescence Watch

Review this chapter when Codex first-app/app-building surfaces materially change, or when tool-catalog chapters add more current stack-specific guidance.

## Evidence and Sources

- `openai.codex.best_practices` — official OpenAI source for context, planning, reusable guidance, and validation habits.
- `openai.codex.workflows` — official OpenAI source for practical codebase, bug, test, and prototype workflows with verification.
- `openai.codex.use_cases.follow_goals` — official OpenAI source for long-running first-version/prototype work with clear stopping conditions and checkpoints.
- `openai.codex.use_cases.idea_to_proof_of_concept` — official OpenAI source for turning rough ideas into the smallest useful prototype and verifying in a browser.
- `openai.codex.use_cases.build_and_deploy_internal_apps` — official OpenAI source for focused internal-app workflows and testing the main flow before deploy.
- `openai.codex.security` — official OpenAI source for security review positioning and limitations.
- Maintainer synthesis: vertical-slice and production-hardening sequence based on stable engineering practice.

## Related Topics

- `vcb.chapter.feature_slicing`
- `vcb.chapter.four_part_prompt`
- `vcb.chapter.acceptance_criteria`
- `vcb.chapter.agents_md_operating_manual`
- `vcb.chapter.frontend_work`
- `vcb.chapter.security_for_vibe_coders`
- `vcb.chapter.dependency_package_framework_decisions`
- `vcb.chapter.senior_engineer_checklist`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.first_serious_app -->
