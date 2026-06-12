<!-- VCB:BEGIN_TOPIC id=vcb.codex.cli version=0.1.0 -->
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
id: vcb.codex.cli
title: Codex CLI
type: codex_feature
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex CLI
- Terminal
- Local repositories
- CI/non-interactive workflows
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.broad_agent_permissions
- vcb.shortcut.full_access_automation
- vcb.shortcut.ignoring_lint_typecheck
durable_principles:
- terminal-native agent work should start in the right directory with known commands
- CLI power increases both speed and blast radius
- scripts and non-interactive runs need stricter scope than live supervised sessions
likely_to_change:
- CLI commands and flags
- sandbox and approval option names
- non-interactive output formats
- installation and login flow
obsolete_when:
- Codex CLI is deprecated or official docs no longer support local terminal agent
  workflows
related_topics:
- vcb.chapter.codex_surfaces
- vcb.chapter.ci_noninteractive_github_actions
- vcb.codex.config
- vcb.codex.cloud
- vcb.safety.sandboxing_and_approvals
- vcb.concepts.ci
---

> Summary:
> The Codex CLI is the terminal-native surface for local repo work, command execution, scripting, and automation-like Codex tasks.

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

<!-- VCB:BEGIN_SECTION id=vcb.codex.cli.human -->
## 1. For the Human: Plain-Language Concept

### What this means

The Codex CLI lets you work with Codex from a terminal in a chosen directory. It can inspect files, edit files, and run commands where you are working. This makes it powerful for people who already think in commands, tests, package managers, and scripts.

### Why it matters

The CLI matters because it gives Codex direct contact with the actual repo and command output. That is more reliable than asking for generic code in a chat. It is also riskier: if you point it at the wrong directory or give too much permission, it can move fast in the wrong place.

### The mental model

Use the CLI as a controlled shop tool. It can cut precisely, but only if the workpiece is clamped and the operator knows what command should prove the cut was correct.

### What good looks like

Good use: run the CLI in the repo root, ask for a narrow change, require the smallest relevant test or build command, and inspect Git diff before accepting.

### What bad looks like

Bad use: run the CLI with broad access in a home directory, no Git checkpoint, no known test command, and real secrets nearby.

### Minimal example

Example: from the project root, ask Codex CLI to fix one failing test, explain the root cause, rerun that test, and leave the diff for review.

### Checklist

- Name the task and the Codex surface explicitly.
- Confirm whether the work is prototype, maintenance, production, or emergency work.
- Choose permissions and attention level before starting.
- Require a diff, report, or artifact that proves what changed.
- Review volatile details against official docs before freezing commands or UI instructions.
<!-- VCB:END_SECTION id=vcb.codex.cli.human -->

<!-- VCB:BEGIN_SECTION id=vcb.codex.cli.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the CLI as a high-control local execution surface with explicit scope, permissions, and proof commands.

### Diagnose the human’s current model

- Is the working directory correct?
- Is the working tree clean or intentionally dirty?
- What command proves this task is done?
- Is this live supervised work or scriptable automation?

### Explanation strategy

Start with task/surface fit. Explain what this Codex feature is good at, what it does not prove, and which guardrails become mandatory as blast radius grows. Tie the explanation to the user’s actual repository, risk level, and attention budget.

### Useful metaphors

The CLI is a power tool. It is excellent inside a marked work area and dangerous when waved around the whole garage.

### Coaching tactics

- Ask the user what surface they are actually using before giving feature-specific advice.
- Separate stable workflow principle from volatile product mechanics.
- Convert broad requests into scoped work orders with explicit done-when criteria.
- Escalate hard for production, secrets, auth, payments, migrations, CI credentials, browser state, or unattended mutation.
- Prefer reviewable artifacts over confident summaries.

### Prompt patterns

```text
Using Codex CLI, inspect only the files needed for [task]. Do not add dependencies. Run [specific check] if available. Stop with changed files, command output, and any risks. Ask before destructive Git commands or network installs.
```

### Red flags to call out directly

- unknown working directory
- full access on a machine with secrets
- non-interactive mutation without branch isolation
- package installs from unknown scripts

### Exercises

1. Ask the human to choose this feature for one low-risk task and one high-risk task, then explain what guardrails change.
2. Ask the human to name which part of this feature is stable principle and which part must be rechecked against official docs.
3. Ask the human to write a final-report template for work done through this feature.
<!-- VCB:END_SECTION id=vcb.codex.cli.ai_coach -->

## Shortcut Reality

### The ideal practice

Use the CLI when the task is repo-local, command-verifiable, and benefits from terminal control.

### What users often do instead

Users often reduce approval friction or run broad CLI tasks because the terminal feels precise.

### When the shortcut may be fine

Broad CLI freedom can be fine in a disposable container, fresh VM, or throwaway repo with fake credentials.

### When the shortcut is a bad idea

It is a bad idea on a main machine, in a directory with personal files, or in repos with real secrets, production credentials, or auto-deploy.

### Risk profile

- Probability of failure: Failure probability depends on scope
- Impact if it fails: rises sharply with production data, secrets, real users, payments, auth, CI credentials, or deployment paths.
- Ease of recovery: good only when work is branch-isolated, committed, fake-data backed, and reviewable.
- Blast radius: small for local prototypes; large for shared repos, cloud work, external tools, GUI control, and automated mutation.
- Skill needed to recover: low for small Git-backed diffs; medium/high for secrets, data, deployment, or account-state mistakes.
- Hidden cost: stale configuration, noisy automation, false confidence, usage burn, and future maintenance load.

### Minimum guardrails

- start in the repo root
- commit or stash before broad tasks
- use sandbox/approval modes appropriate to risk
- keep fake credentials in prototypes
- run one relevant command and review the diff

### Recovery plan

Stop the CLI session, inspect Git status and changed files, remove unintended edits with Git, rotate any exposed credentials, and rerun the known check before continuing.

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

- terminal-native agent work should start in the right directory with known commands
- CLI power increases both speed and blast radius
- scripts and non-interactive runs need stricter scope than live supervised sessions

## Volatile Surface

- CLI commands and flags
- sandbox and approval option names
- non-interactive output formats
- installation and login flow

## Obsolescence Watch

- Codex CLI is deprecated or official docs no longer support local terminal agent workflows

## Evidence and Sources

- `openai.codex.cli` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.cli_features` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.cli_reference` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.config_basic` — official source anchor for this card's current Codex feature behavior.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for blast radius, recoverability, workflow fit, and AI-coach intervention guidance.

## Related Topics

- `vcb.chapter.codex_surfaces`
- `vcb.chapter.ci_noninteractive_github_actions`
- `vcb.codex.config`
- `vcb.codex.cloud`
- `vcb.safety.sandboxing_and_approvals`
- `vcb.concepts.ci`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.codex.cli -->
