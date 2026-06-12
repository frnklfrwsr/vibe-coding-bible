<!-- VCB:BEGIN_TOPIC id=vcb.codex.computer_use version=0.1.0 -->
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
id: vcb.codex.computer_use
title: Codex Computer Use
type: codex_feature
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Computer Use
- Browser work
- GUI tasks
- Desktop apps
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.computer_use_without_scope
- vcb.shortcut.exposing_sensitive_screen_context
- vcb.shortcut.logged_in_gui_control
- vcb.shortcut.browser_clicking_without_repro
durable_principles:
- use visual control only when files/APIs are insufficient
- scope GUI tasks tightly and stay present for sensitive actions
- prefer structured tools over GUI control when available
likely_to_change:
- OS permission behavior
- browser and Chrome extension support
- remote/locked-use behavior
- approval prompts and sensitive-action rules
obsolete_when:
- Codex no longer supports Computer Use or GUI/browser behavior is replaced by safer
  structured APIs
related_topics:
- vcb.chapter.computer_use_browser_gui_tasks
- vcb.codex.app
- vcb.codex.cloud
- vcb.safety.security_review
- vcb.concepts.observability
---

> Summary:
> Computer Use lets Codex inspect or operate graphical apps and browser flows when code, logs, and APIs are not enough.

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

<!-- VCB:BEGIN_SECTION id=vcb.codex.computer_use.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Computer Use means Codex can look at and interact with an app or browser the way a user would. It is useful for GUI-only bugs, visual verification, local app flows, and settings screens that are hard to inspect from files alone.

### Why it matters

GUI work matters because not every bug is visible in code. A page can compile and still be broken, ugly, inaccessible, or wrong. Computer Use gives Codex eyes and hands, so it also needs stronger boundaries.

### The mental model

Computer Use is letting Codex borrow your screen. Do not hand over screens that show secrets, production consoles, payment flows, or personal accounts unless the task is tightly controlled and supervised.

### What good looks like

Good use: ask Codex to reproduce a local onboarding bug in a test account, observe the UI, make a minimal fix, and rerun the same flow.

### What bad looks like

Bad use: let Codex operate a logged-in production admin console unattended with broad permissions.

### Minimal example

Example: use Computer Use to verify a local checkout mock flow with fake data and collect screenshots of the failing step.

### Checklist

- Name the task and the Codex surface explicitly.
- Confirm whether the work is prototype, maintenance, production, or emergency work.
- Choose permissions and attention level before starting.
- Require a diff, report, or artifact that proves what changed.
- Review volatile details against official docs before freezing commands or UI instructions.
<!-- VCB:END_SECTION id=vcb.codex.computer_use.human -->

<!-- VCB:BEGIN_SECTION id=vcb.codex.computer_use.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach GUI access as high-context and high-exposure. Prefer structured integrations when possible and scope visual control tightly.

### Diagnose the human’s current model

- Does this require visual inspection, or would logs/tests/API calls be safer?
- What app/site is allowed?
- Is the account fake/staging/production?
- Will the user stay present for sensitive actions?

### Explanation strategy

Start with task/surface fit. Explain what this Codex feature is good at, what it does not prove, and which guardrails become mandatory as blast radius grows. Tie the explanation to the user’s actual repository, risk level, and attention budget.

### Useful metaphors

Computer Use is handing Codex the mouse. A mouse can click the right button or the wrong button very quickly.

### Coaching tactics

- Ask the user what surface they are actually using before giving feature-specific advice.
- Separate stable workflow principle from volatile product mechanics.
- Convert broad requests into scoped work orders with explicit done-when criteria.
- Escalate hard for production, secrets, auth, payments, migrations, CI credentials, browser state, or unattended mutation.
- Prefer reviewable artifacts over confident summaries.

### Prompt patterns

```text
Use Computer Use only for [specific app/site/flow]. Use fake or staging data. Do not enter credentials, change billing, delete data, or perform admin actions. Stop before any sensitive or irreversible action and report screenshots/observations.
```

### Red flags to call out directly

- logged-in production UI
- real customer data on screen
- payment or account settings
- unattended GUI mutation
- browser history or personal account exposure

### Exercises

1. Ask the human to choose this feature for one low-risk task and one high-risk task, then explain what guardrails change.
2. Ask the human to name which part of this feature is stable principle and which part must be rechecked against official docs.
3. Ask the human to write a final-report template for work done through this feature.
<!-- VCB:END_SECTION id=vcb.codex.computer_use.ai_coach -->

## Shortcut Reality

### The ideal practice

Use Computer Use for narrow visual observation or repeatable GUI verification, preferably in local or staging environments.

### What users often do instead

Users often let Codex click around because it feels like real QA.

### When the shortcut may be fine

It can be fine on a local app, fake account, or disposable browser profile.

### When the shortcut is a bad idea

It is a bad idea with real production consoles, payment actions, secrets, personal email, customer records, or irreversible UI operations.

### Risk profile

- Probability of failure: Medium to high failure probability when tasks are vague
- Impact if it fails: rises sharply with production data, secrets, real users, payments, auth, CI credentials, or deployment paths.
- Ease of recovery: good only when work is branch-isolated, committed, fake-data backed, and reviewable.
- Blast radius: small for local prototypes; large for shared repos, cloud work, external tools, GUI control, and automated mutation.
- Skill needed to recover: low for small Git-backed diffs; medium/high for secrets, data, deployment, or account-state mistakes.
- Hidden cost: stale configuration, noisy automation, false confidence, usage burn, and future maintenance load.

### Minimum guardrails

- use fake/staging accounts
- scope to one app and flow
- stay present for sensitive steps
- prefer structured tools/MCP/API when available
- capture observations before mutating

### Recovery plan

Stop the task, revoke session access if needed, audit actions taken, undo changes in the app, rotate exposed credentials, and rerun in a safer environment.

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

- use visual control only when files/APIs are insufficient
- scope GUI tasks tightly and stay present for sensitive actions
- prefer structured tools over GUI control when available

## Volatile Surface

- OS permission behavior
- browser and Chrome extension support
- remote/locked-use behavior
- approval prompts and sensitive-action rules

## Obsolescence Watch

- Codex no longer supports Computer Use or GUI/browser behavior is replaced by safer structured APIs

## Evidence and Sources

- `openai.codex.app_computer_use` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.app_browser` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.chrome_extension` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.remote_connections` — official source anchor for this card's current Codex feature behavior.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for blast radius, recoverability, workflow fit, and AI-coach intervention guidance.

## Related Topics

- `vcb.chapter.computer_use_browser_gui_tasks`
- `vcb.codex.app`
- `vcb.codex.cloud`
- `vcb.safety.security_review`
- `vcb.concepts.observability`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.codex.computer_use -->
