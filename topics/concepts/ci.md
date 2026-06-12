<!-- VCB:BEGIN_TOPIC id=vcb.concepts.ci version=0.1.0 -->
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
id: vcb.concepts.ci
title: CI
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
- vcb.shortcut.unattended_mutation
- vcb.shortcut.overbroad_ci_permissions
durable_principles:
- CI makes checks repeatable
- CI is a gate, not a substitute for review
- CI automation must use least privilege around secrets and deploys
likely_to_change:
- provider UI and syntax
- runner images
- billing and quota details
obsolete_when:
- teams stop needing repeatable automated checks
related_topics:
- vcb.concepts.test
- vcb.concepts.lint
- vcb.concepts.typecheck
- vcb.concepts.build_step
- vcb.chapter.ci_noninteractive_github_actions
---

> Summary:
> CI is a robot checkpoint that runs checks like tests, lint, typecheck, and builds when code changes, usually before merge or deploy.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.ci.human -->
## 1. For the Human: Plain-Language Concept

### What this means

CI means **continuous integration**. In practice, it is the robot that runs your project’s checks when you open a pull request, push a branch, or prepare a deploy.

### Why it matters

CI protects you from accepting Codex changes that only worked on the agent’s machine or only on the happy path. It also turns “please remember to run checks” into automatic feedback.

### The mental model

CI is a bouncer at the merge door. It does not know everything, but it can refuse obvious trouble before it enters.

### What good looks like

- checks are relevant and not theatrical
- CI runs on PRs or key branches
- permissions and secrets are scoped
- failures are investigated instead of bypassed

### What bad looks like

- CI red but merged anyway
- workflow has broad write permissions for no reason
- tests are weak but green
- Codex changes CI YAML without security review

### Minimal example

A simple CI job might install dependencies, run lint, run tests, and build before a PR can merge.

### Checklist

- Know what CI checks run.
- Treat failures as evidence.
- Keep automation permissions narrow.
- Avoid long-lived secrets when possible.
- Do not let CI auto-mutate production branches casually.
<!-- VCB:END_SECTION id=vcb.concepts.ci.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.ci.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach CI as repeatable verification and least-privilege automation.

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
Inspect the CI workflow and summarize triggers, permissions, secrets, commands, and artifacts. Do not edit yet.
```

```text
Add the narrowest CI check for this project. It should run tests/build on PRs and use the least permissions necessary.
```

### Red flags to call out directly

- workflow grants write-all permissions
- secrets exposed to untrusted code
- CI failure ignored as “flaky” without proof
- Codex edits deploy workflow and app code together

### Exercises

- Ask the human to find one real example in their repo.
- Ask them what would break if this concept were wrong.
<!-- VCB:END_SECTION id=vcb.concepts.ci.ai_coach -->

## Shortcut Reality

### The ideal practice

Use CI for repeatable checks with narrow permissions.

### What users often do instead

Users run checks manually or disable CI to get a merge through.

### When the shortcut may be fine

Tiny solo prototype with no shared deploy path.

### When the shortcut is a bad idea

Shared repo, production deploys, packages, CI secrets, release automation, or external contributions.

### Risk profile

- Probability of failure: medium
- Impact if it fails: high for deploy/security automation
- Ease of recovery: medium
- Blast radius: repo, deploys, secrets, releases
- Skill needed to recover: CI/security/debugging
- Hidden cost: false confidence from weak green checks

### Minimum guardrails

- Require PR checks.
- Limit token permissions.
- Avoid secrets on untrusted code.
- Prefer report-only Codex automation first.
- Review workflow diffs.

### Recovery plan

Disable risky workflow, rotate exposed secrets, restore known-good CI config, re-run checks, and add branch protections or permission constraints.

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

- CI makes checks repeatable
- CI is a gate, not a substitute for review
- CI automation must use least privilege around secrets and deploys

## Volatile Surface

- provider UI and syntax
- runner images
- billing and quota details

## Obsolescence Watch

Obsolete or review this topic when:

- teams stop needing repeatable automated checks

## Evidence and Sources

- `github.docs.actions_ci` — source anchor for this concept.
- `github.docs.actions_overview` — source anchor for this concept.
- `github.docs.actions_secure_use` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.test
- vcb.concepts.lint
- vcb.concepts.typecheck
- vcb.concepts.build_step
- vcb.chapter.ci_noninteractive_github_actions

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.ci -->
