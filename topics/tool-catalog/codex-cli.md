<!-- VCB:BEGIN_TOPIC id=tool.codex_cli version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-10'
last_reviewed: '2026-06-10'
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
evidence_scope: official OpenAI/Codex tool documentation plus VCB maintainer synthesis
  for setup, risk, budget, and coaching guidance
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
- major_refactor
- emergency_hotfix
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: tool.codex_cli
title: Codex CLI
name: Codex CLI
type: tool_card
category: codex_terminal_agent
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
last_pricing_reviewed: '2026-06-10'
pricing_volatility: very_high
pricing_snapshot_required: true
pricing_snapshot_ids:
- vcb.pricing_snapshot.openai_codex
setup_effort: 'low to medium: install, authenticate, choose repo root, understand
  config, sandbox, and approval posture'
maintenance_effort: 'medium: CLI commands, flags, maturity labels, config, and auth
  behavior can change'
debugging_effort: 'medium: failures can be shell environment, config, permissions,
  dependencies, or Codex reasoning'
lock_in_risk: 'low to moderate: terminal workflows remain portable, but CLI flags/config
  are Codex-specific'
hidden_cost_risk: 'medium: easy iteration can burn usage and human review time quickly'
codex_integration_value: high for local command/evidence loops and terminal-native
  developers
best_for:
- terminal-first developers
- local command-backed verification
- small patches with tests
- repo inspection and command triage
not_for:
- users who cannot review shell/diff output
- unbounded production runners
- browser/GUI tasks that need rendered state
- long unattended scheduled automation without exec/CI controls
integrates_with_codex:
- local shell
- Git
- tests and linters
- Codex config
- codex exec
- Codex Cloud task commands
hidden_costs:
- failed commands hidden in long terminal logs
- sandbox/approval misconfiguration
- usage burn from repeated retries
- environment-specific behavior
applies_to:
- Codex CLI
- terminal UI
- local repositories
- shell commands
- sandbox and approvals
- CLI review
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.broad_agent_permissions
- vcb.shortcut.full_access_automation
- vcb.shortcut.skipping_tests
- vcb.shortcut.trusting_external_tool_output
durable_principles:
- The CLI is strongest when terminal commands provide executable evidence.
- Sandbox and approval choices are part of the task contract.
- Local shell access should be least-privilege until risk is understood.
likely_to_change:
- CLI flags, command names, maturity labels, sandbox defaults, approval behavior,
  auth, and model menus
obsolete_when:
- OpenAI retires the terminal CLI or replaces it with a materially different local
  execution interface.
related_topics:
- vcb.codex.cli
- vcb.codex.config
- vcb.workflow.testing
- vcb.workflow.ci_triage
- vcb.workflow.ci_noninteractive
- tool.codex_exec
---

# Codex CLI

> Summary:
> Codex CLI is the terminal-native first-party Codex surface for local repository inspection, edits, commands, review, and scripting-oriented workflows.

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

<!-- VCB:BEGIN_SECTION id=tool.codex_cli.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Codex CLI is Codex in the terminal. It is best when your work naturally involves shell commands, logs, tests, Git, and local repo state.

### Why it matters

The CLI matters because many real coding checks happen in the terminal. The risk is giving shell access without understanding sandbox, approval, network, and working-directory boundaries.

### What good looks like

Use the CLI to inspect a repo, make a small patch, run the relevant command, and report exactly what changed.

### What bad looks like

Run it with broad access in a messy directory, approve every command, and skip diff review because the terminal output looked successful.

### Minimal example

Start in the repo root, state the task, allow only the permissions needed, run tests/typecheck/lint as evidence, and inspect `git diff` before acceptance.

### Best-fit cases

- terminal-first developers
- local command-backed verification
- small patches with tests
- repo inspection and command triage

### Not-fit cases

- users who cannot review shell/diff output
- unbounded production runners
- browser/GUI tasks that need rendered state
- long unattended scheduled automation without exec/CI controls

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | low to medium: install, authenticate, choose repo root, understand config, sandbox, and approval posture |
| Maintenance effort | medium: CLI commands, flags, maturity labels, config, and auth behavior can change |
| Debugging effort | medium: failures can be shell environment, config, permissions, dependencies, or Codex reasoning |
| Lock-in risk | low to moderate: terminal workflows remain portable, but CLI flags/config are Codex-specific |
| Hidden cost risk | medium: easy iteration can burn usage and human review time quickly |

### Checklist

- choose the smallest Codex surface that fits the task
- confirm permissions before mutation
- require a diff, report, structured output, or check evidence
- keep exact pricing, limits, model availability, and UI mechanics out of stable decisions
- review official OpenAI docs before freezing current product behavior

<!-- VCB:END_SECTION id=tool.codex_cli.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_cli.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the CLI as a high-leverage local agent that must be bounded by directory, sandbox, approval mode, and command evidence.

### Diagnostic questions

- What directory is the CLI allowed to read/write?
- Which commands are necessary evidence?
- What sandbox and approval policy match the task?
- Does this need interactive TUI or non-interactive exec?

### Coaching tactics

- start with read-only or workspace-scoped work for unfamiliar repos
- turn broad shell work into plan-first when risk is unclear
- require command transcript and diff summary
- use non-interactive exec only when the task is scriptable and bounded

### Prompt pattern

```text
In the Codex CLI, work only in this repo. Goal: [goal]. Constraints: [sandbox/approval/no-new-deps/no broad refactor]. Evidence required: [tests/typecheck/lint/diff]. Stop and ask before touching [danger zones].
```

### Red flags

- danger/full-access before the repo is understood
- commands run outside the intended root
- network access used without purpose
- scripted CI-like work attempted through an interactive-only process

### Intervention rule

When the human asks for a current product detail, exact price, exact limit, model-routing claim, UI label, command flag, or plan-packaging fact, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_cli.ai_coach -->

## Shortcut Reality

### The ideal practice

Use this tool only after the task, context, permissions, evidence, and review path are clear.

### What users often do instead

Users often pick the most convenient surface, then retrofit the safety controls after the tool has already produced output.

### When the shortcut may be acceptable

The shortcut can be acceptable for disposable prototypes, read-only inspection, docs work, small branches, or reports where rollback is trivial and no secrets or production state are exposed.

### When it becomes a bad trade

It becomes a bad trade when the tool can mutate broad code, touch secrets, make production changes, create noisy automation, hide environment assumptions, or return a polished summary without verifiable evidence.

### Relevant shortcut cards

- `vcb.shortcut.broad_agent_permissions`
- `vcb.shortcut.full_access_automation`
- `vcb.shortcut.skipping_tests`
- `vcb.shortcut.trusting_external_tool_output`

### Minimum guardrails

- one bounded task per run/thread/job
- explicit permissions and forbidden zones
- Git checkpoint or isolated branch/worktree for mutation
- evidence packet before acceptance
- human review before merge, deploy, credential use, or production action

### Recovery plan

Stop the tool, preserve logs/transcripts/output, inspect the diff or generated artifact, revert or isolate unsafe changes, rotate exposed secrets if needed, and restart with a smaller task packet.

## Budget and Constraint Notes

### Cheapest reliable path

Use the narrowest surface, smallest context packet, and cheapest reviewable workflow that can produce the needed evidence. Avoid retry loops caused by vague prompts.

### Fastest high-usage path

Use parallel or automated surfaces only when work is independent, review capacity exists, and integration cost is budgeted.

### Low-attention path

Low-attention use requires isolation, stop conditions, and a final review packet. It does not justify broad mutation or production access.

### Production-quality path

Production use requires explicit scope, least privilege, checks, security review where relevant, and human acceptance based on artifacts rather than summaries.

### Hidden costs to watch

- failed commands hidden in long terminal logs
- sandbox/approval misconfiguration
- usage burn from repeated retries
- environment-specific behavior

## Stable Core

- The CLI is strongest when terminal commands provide executable evidence.
- Sandbox and approval choices are part of the task contract.
- Local shell access should be least-privilege until risk is understood.

## Volatile Surface

- CLI flags, command names, maturity labels, sandbox defaults, approval behavior, auth, and model menus

Exact prices, plan packaging, feature availability, commands, flags, model menus, context limits, UI labels, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI retires the terminal CLI or replaces it with a materially different local execution interface.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.cli` — official/synthesis source anchor for this tool card.
- `openai.codex.cli_features` — official/synthesis source anchor for this tool card.
- `openai.codex.cli_reference` — official/synthesis source anchor for this tool card.
- `openai.codex.agent_approvals_security` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `vcb.codex.cli`
- `vcb.codex.config`
- `vcb.workflow.testing`
- `vcb.workflow.ci_triage`
- `vcb.workflow.ci_noninteractive`
- `tool.codex_exec`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_cli -->
