<!-- VCB:BEGIN_TOPIC id=vcb.concepts.build_step version=0.1.0 -->
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
id: vcb.concepts.build_step
title: Build Step
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
- vcb.shortcut.ignoring_lint_typecheck
- vcb.shortcut.accepting_looks_done
durable_principles:
- builds catch integration/config errors before deployment
- build output is not source truth but deployable artifact
- Codex should run the relevant build when changing compiled/bundled code
likely_to_change:
- framework build commands
- bundler behavior
- deployment platform build settings
obsolete_when:
- all code becomes directly deployable without transformation
related_topics:
- vcb.concepts.typecheck
- vcb.concepts.lint
- vcb.concepts.ci
- vcb.chapter.ci_noninteractive_github_actions
---

> Summary:
> A build step transforms source code into something runnable or deployable, often bundling, compiling, optimizing, or type-checking first.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.build_step.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A build step turns your source code into the version your app can actually run or deploy. It may bundle files, compile TypeScript, optimize assets, generate routes, or fail if code/config does not fit together.

### Why it matters

“It works in one file” is not enough. Codex can make changes that look fine but fail at build time because imports, types, assets, routes, or environment variables are wrong.

### The mental model

A build step is the kitchen pass: every dish must fit together before it leaves for the dining room.

### What good looks like

- known build command exists
- build runs after changes that affect compiled/deployed code
- errors are fixed instead of ignored
- build artifacts are not confused with source

### What bad looks like

- deploy fails because build was skipped
- Codex edits generated output instead of source
- build warnings ignored as noise
- env-specific build behavior not checked

### Minimal example

A React app may run locally in dev mode but fail production build because a server-only module was imported into browser code.

### Checklist

- Know the build command.
- Run build for production-sensitive changes.
- Do not edit generated artifacts unless that is the project convention.
- Treat build errors as evidence.
<!-- VCB:END_SECTION id=vcb.concepts.build_step.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.build_step.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach build as integration proof and prevent “looks done” acceptance without deployable output.

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
Identify the project build command and run it after this change. Report exact failures and do not edit generated files unless the repo expects it.
```

```text
Explain this build error in plain language and trace it to the source file/config that caused it.
```

### Red flags to call out directly

- generated files edited as source
- build skipped before deploy
- dev server success treated as production proof
- warnings/errors waved away

### Exercises

- Ask the human to find one real example in their repo.
- Ask them what would break if this concept were wrong.
<!-- VCB:END_SECTION id=vcb.concepts.build_step.ai_coach -->

## Shortcut Reality

### The ideal practice

Run the smallest relevant build/check for deployable code.

### What users often do instead

Users rely on the dev server or screenshot only.

### When the shortcut may be fine

Visual prototype or local script that is not deployed.

### When the shortcut is a bad idea

Production deploys, packages, CI-gated repos, environment-sensitive code, or frontend bundling changes.

### Risk profile

- Probability of failure: medium
- Impact if it fails: deployment/blocker
- Ease of recovery: high before deploy
- Blast radius: CI/deploy pipeline
- Skill needed to recover: build-tool debugging
- Hidden cost: deploy surprises

### Minimum guardrails

- Run build.
- Do not edit generated output blindly.
- Keep env variables clear.
- Separate old warnings from new failures.

### Recovery plan

Revert generated-output edits, run build locally/CI, fix source/config, and add build command guidance to README/AGENTS.md if missing.

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

- builds catch integration/config errors before deployment
- build output is not source truth but deployable artifact
- Codex should run the relevant build when changing compiled/bundled code

## Volatile Surface

- framework build commands
- bundler behavior
- deployment platform build settings

## Obsolescence Watch

Obsolete or review this topic when:

- all code becomes directly deployable without transformation

## Evidence and Sources

- `vite.docs.build` — source anchor for this concept.
- `webpack.docs.concepts` — source anchor for this concept.
- `npm.docs.scripts` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.typecheck
- vcb.concepts.lint
- vcb.concepts.ci
- vcb.chapter.ci_noninteractive_github_actions

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.build_step -->
