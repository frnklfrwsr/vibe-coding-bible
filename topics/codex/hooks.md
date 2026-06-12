<!-- VCB:BEGIN_TOPIC id=vcb.codex.hooks version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
audiences:
- human
- ai_coach
source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: official OpenAI product behavior anchors plus VCB maintainer synthesis
  for risk, workflow, and coaching guidance
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
id: vcb.codex.hooks
title: Codex Hooks
type: codex_feature
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex CLI
- Codex IDE Extension
- Project configuration
- Deterministic guardrails
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: STABLE
shortcut_profiles:
- vcb.shortcut.brittle_hooks
- vcb.shortcut.hook_overreach
- vcb.shortcut.accepting_looks_done
durable_principles:
- hooks are deterministic guardrails, not complete security boundaries
- slow or flaky hooks become workflow tax
- hooks should enforce narrow rules that are hard for prompts alone to guarantee
likely_to_change:
- hook events and payloads
- trust/review behavior
- managed hook support
- config feature flags and aliases
obsolete_when:
- Codex hook framework is deprecated or event semantics change materially
related_topics:
- vcb.chapter.hooks_deterministic_guardrails
- vcb.codex.config
- vcb.codex.mcp
- vcb.safety.permissions
- vcb.chapter.ci_noninteractive_github_actions
---

> Summary:
> Hooks are deterministic scripts that run during the Codex lifecycle to log, scan, validate, or enforce narrow workflow rules.

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

<!-- VCB:BEGIN_SECTION id=vcb.codex.hooks.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A hook is a script Codex runs at a specific point in its workflow. You can use hooks to scan prompts, log activity, run validation, or enforce policy that should not depend on Codex remembering to do it.

### Why it matters

Hooks matter because prompts are soft rules. Hooks are harder rules. But hooks are not magic security walls; they can be incomplete, brittle, slow, or too broad.

### The mental model

A hook is a turnstile or checklist stamp. It can stop or record certain actions, but it is not a full security team.

### What good looks like

Good use: block obvious secret pastes, log high-risk tool use, or run a narrow validation check after a turn.

### What bad looks like

Bad use: build a giant fragile hook system that tries to replace tests, review, CI, sandboxing, and judgment.

### Minimal example

Example: use a hook to scan user prompts for accidentally pasted API keys before the prompt enters the agent loop.

### Checklist

- Name the task and the Codex surface explicitly.
- Confirm whether the work is prototype, maintenance, production, or emergency work.
- Choose permissions and attention level before starting.
- Require a diff, report, or artifact that proves what changed.
- Review volatile details against official docs before freezing commands or UI instructions.
<!-- VCB:END_SECTION id=vcb.codex.hooks.human -->

<!-- VCB:BEGIN_SECTION id=vcb.codex.hooks.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach hooks as deterministic guardrails with limits. Do not let users over-trust them.

### Diagnose the human’s current model

- What exact rule should be deterministic?
- Can this be a test or CI check instead?
- Will the hook be fast and reliable?
- What happens when the hook fails or misses a path?

### Explanation strategy

Start with task/surface fit. Explain what this Codex feature is good at, what it does not prove, and which guardrails become mandatory as blast radius grows. Tie the explanation to the user’s actual repository, risk level, and attention budget.

### Useful metaphors

Hooks are guardrails on a road, not autopilot. They reduce certain crashes; they do not make reckless driving safe.

### Coaching tactics

- Ask the user what surface they are actually using before giving feature-specific advice.
- Separate stable workflow principle from volatile product mechanics.
- Convert broad requests into scoped work orders with explicit done-when criteria.
- Escalate hard for production, secrets, auth, payments, migrations, CI credentials, browser state, or unattended mutation.
- Prefer reviewable artifacts over confident summaries.

### Prompt patterns

```text
Design a narrow Codex hook for [policy]. It must state the lifecycle point, inputs inspected, allow/deny behavior, failure mode, performance limit, and what it does not protect against.
```

### Red flags to call out directly

- hooks treated as a complete security boundary
- hook code that mutates too much
- slow hooks skipped by users
- policy hidden from the repo team

### Exercises

1. Ask the human to choose this feature for one low-risk task and one high-risk task, then explain what guardrails change.
2. Ask the human to name which part of this feature is stable principle and which part must be rechecked against official docs.
3. Ask the human to write a final-report template for work done through this feature.
<!-- VCB:END_SECTION id=vcb.codex.hooks.ai_coach -->

## Shortcut Reality

### The ideal practice

Use hooks for small deterministic rules that prevent repeated risky behavior or create useful audit trails.

### What users often do instead

Users often skip hooks until a team has repeated problems, or overbuild hooks to solve every risk.

### When the shortcut may be fine

Skipping hooks is fine for small prototypes. A minimal hook is enough when one repeated failure is clear.

### When the shortcut is a bad idea

Relying on hooks alone is bad for secrets, production data, auth, payments, or any path requiring tests, review, and least privilege.

### Risk profile

- Probability of failure: Medium failure probability if hooks are brittle or incomplete
- Impact if it fails: rises sharply with production data, secrets, real users, payments, auth, CI credentials, or deployment paths.
- Ease of recovery: good only when work is branch-isolated, committed, fake-data backed, and reviewable.
- Blast radius: small for local prototypes; large for shared repos, cloud work, external tools, GUI control, and automated mutation.
- Skill needed to recover: low for small Git-backed diffs; medium/high for secrets, data, deployment, or account-state mistakes.
- Hidden cost: stale configuration, noisy automation, false confidence, usage burn, and future maintenance load.

### Minimum guardrails

- keep hooks narrow
- document what they cover and do not cover
- run fast
- review and trust project-local hooks
- keep CI/tests/review in place

### Recovery plan

Disable broken hooks, inspect what they allowed or blocked, restore normal tests/review, then rebuild the hook around one enforceable rule.

### AI coach guidance

Do not moralize the shortcut. Name the tradeoff, reduce blast radius, improve recoverability, and require the smallest guardrail that changes the risk profile.

## Budget and Constraint Notes

### Cheapest reliable path

Use this feature for one narrow task with curated context, conservative permissions, and one relevant check. Do not spend usage exploring broad unknowns unless the task is important enough to justify it.

### Fastest high-usage path

Use this feature aggressively only with branch/worktree isolation, clear acceptance criteria, structured final reports, and independent review for risky diffs.

### Low-attention path

Low-attention work requires stronger isolation, report-only or read-only posture when possible, fake credentials, and a final report that names files changed, checks run, unresolved risks, and review needs.

### Production-quality path

Use least privilege, clear done-when criteria, Git checkpoints, tests/build/lint where relevant, diff review, source-register discipline, and a rollback plan before accepting work.

## Stable Core

- hooks are deterministic guardrails, not complete security boundaries
- slow or flaky hooks become workflow tax
- hooks should enforce narrow rules that are hard for prompts alone to guarantee

## Volatile Surface

- hook events and payloads
- trust/review behavior
- managed hook support
- config feature flags and aliases

## Obsolescence Watch

- Codex hook framework is deprecated or event semantics change materially

## Evidence and Sources

- `openai.codex.hooks` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.config_basic` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.best_practices` — official source anchor for this card's current Codex feature behavior.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for blast radius, recoverability, workflow fit, and AI-coach intervention guidance.

## Related Topics

- `vcb.chapter.hooks_deterministic_guardrails`
- `vcb.codex.config`
- `vcb.codex.mcp`
- `vcb.safety.permissions`
- `vcb.chapter.ci_noninteractive_github_actions`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.codex.hooks -->
