<!-- VCB:BEGIN_TOPIC id=tool.codex_exec version=0.1.0 -->
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
id: tool.codex_exec
title: codex exec
name: codex exec
type: tool_card
category: codex_noninteractive_cli
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
last_pricing_reviewed: '2026-06-10'
pricing_volatility: very_high
pricing_snapshot_required: true
pricing_snapshot_ids:
- vcb.pricing_snapshot.openai_codex
setup_effort: 'medium: CLI auth, runner isolation, prompt/stdin contract, sandbox/approval
  flags, and output parsing'
maintenance_effort: 'high: flags, auth, JSON event shapes, sandbox defaults, and CI
  integration patterns are volatile'
debugging_effort: 'high: failures can involve shell quoting, stdin, runner permissions,
  auth, sandbox, schema, or downstream parsers'
lock_in_risk: 'moderate: scripts can be portable, but flags/events/auth behavior are
  Codex-specific'
hidden_cost_risk: 'high: scheduled retries, broad logs, and unattended mutation can
  create usage and recovery cost quickly'
codex_integration_value: high for bounded automation that emits auditable reports
  or structured outputs
best_for:
- CI/log summaries
- release-note drafts from verified inputs
- read-only repo reports
- isolated scripted repair attempts
not_for:
- open-ended product work
- unreviewed auto-fixes on protected branches
- secret-heavy runners
- tasks needing interactive clarification
integrates_with_codex:
- Codex CLI
- CI pipelines
- shell scripts
- structured output schemas
- GitHub Actions patterns
hidden_costs:
- credential exposure
- irreversible automation side effects
- schema drift
- quiet failures in pipelines
- usage burn from scheduled retries
applies_to:
- codex exec
- non-interactive mode
- scripts
- CI jobs
- JSONL output
- structured output schemas
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.automation_mutation_without_review
- vcb.shortcut.full_access_automation
- vcb.shortcut.overbroad_ci_permissions
- vcb.shortcut.long_lived_ci_secrets
durable_principles:
- Non-interactive automation needs stronger permission and output contracts than supervised
  work.
- Read-only report generation is safer than unattended mutation.
- Structured output is useful only when downstream steps validate it.
likely_to_change:
- codex exec flags, maturity labels, JSONL event types, auth modes, sandbox defaults,
  Git checks, and CI guidance
obsolete_when:
- OpenAI retires `codex exec` or replaces non-interactive Codex automation with a
  different execution surface.
related_topics:
- vcb.workflow.ci_noninteractive
- vcb.workflow.ci_triage
- vcb.codex.cli
- vcb.shortcut.automation_mutation_without_review
- vcb.shortcut.full_access_automation
- vcb.safety.secrets
---

# codex exec

> Summary:
> codex exec is the non-interactive Codex CLI mode for scripts, CI-style runs, machine-readable output, and bounded automation.

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

<!-- VCB:BEGIN_SECTION id=tool.codex_exec.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

`codex exec` runs Codex without the interactive terminal UI. It is for scripts, pipelines, scheduled jobs, and command chains where the input, permissions, and output format are already defined.

### Why it matters

It matters because automation magnifies mistakes. Non-interactive Codex can be useful for triage or report generation, but mutating runs need hard permission boundaries and evidence output.

### What good looks like

Use `codex exec` for read-only summaries, CI log triage, structured reports, or carefully scoped workspace-write fixes in isolated runners.

### What bad looks like

Run non-interactive Codex with full access, broad credentials, no Git checkpoint, and no human review.

### Minimal example

Pipe CI logs into `codex exec` for a read-only failure summary, then decide manually whether to create a fix branch.

### Best-fit cases

- CI/log summaries
- release-note drafts from verified inputs
- read-only repo reports
- isolated scripted repair attempts

### Not-fit cases

- open-ended product work
- unreviewed auto-fixes on protected branches
- secret-heavy runners
- tasks needing interactive clarification

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: CLI auth, runner isolation, prompt/stdin contract, sandbox/approval flags, and output parsing |
| Maintenance effort | high: flags, auth, JSON event shapes, sandbox defaults, and CI integration patterns are volatile |
| Debugging effort | high: failures can involve shell quoting, stdin, runner permissions, auth, sandbox, schema, or downstream parsers |
| Lock-in risk | moderate: scripts can be portable, but flags/events/auth behavior are Codex-specific |
| Hidden cost risk | high: scheduled retries, broad logs, and unattended mutation can create usage and recovery cost quickly |

### Checklist

- choose the smallest Codex surface that fits the task
- confirm permissions before mutation
- require a diff, report, structured output, or check evidence
- keep exact pricing, limits, model availability, and UI mechanics out of stable decisions
- review official OpenAI docs before freezing current product behavior

<!-- VCB:END_SECTION id=tool.codex_exec.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_exec.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach non-interactive mode as automation infrastructure. It must have explicit stdin/prompt contracts, least privilege, structured output, and a recovery path.

### Diagnostic questions

- Is the run read-only or mutating?
- What sandbox and approval settings apply?
- Is the runner isolated from secrets and production state?
- Does downstream automation parse structured output safely?

### Coaching tactics

- default to read-only for reports
- use workspace-write only inside isolated branches/runners
- avoid job-level API keys when repo-controlled code can read env vars
- prefer JSONL/schema output for downstream automation

### Prompt pattern

```text
Run non-interactively. Mode: [read-only/report or workspace-write isolated]. Input: [logs/diff/files]. Output: [schema/report]. Constraints: no deploys, no secrets, no network unless stated, no changes outside scope. Evidence required: [fields/checks].
```

### Red flags

- danger/full-access in shared runner
- API keys exposed to repository-controlled scripts
- automation mutates files and pushes without review
- stdout parsed as truth without schema or validation

### Intervention rule

When the human asks for a current product detail, exact price, exact limit, model-routing claim, UI label, command flag, or plan-packaging fact, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_exec.ai_coach -->

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

- `vcb.shortcut.automation_mutation_without_review`
- `vcb.shortcut.full_access_automation`
- `vcb.shortcut.overbroad_ci_permissions`
- `vcb.shortcut.long_lived_ci_secrets`

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

- credential exposure
- irreversible automation side effects
- schema drift
- quiet failures in pipelines
- usage burn from scheduled retries

## Stable Core

- Non-interactive automation needs stronger permission and output contracts than supervised work.
- Read-only report generation is safer than unattended mutation.
- Structured output is useful only when downstream steps validate it.

## Volatile Surface

- codex exec flags, maturity labels, JSONL event types, auth modes, sandbox defaults, Git checks, and CI guidance

Exact prices, plan packaging, feature availability, commands, flags, model menus, context limits, UI labels, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI retires `codex exec` or replaces non-interactive Codex automation with a different execution surface.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.noninteractive` — official/synthesis source anchor for this tool card.
- `openai.codex.cli_reference` — official/synthesis source anchor for this tool card.
- `openai.codex.cli_features` — official/synthesis source anchor for this tool card.
- `openai.codex.agent_approvals_security` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `vcb.workflow.ci_noninteractive`
- `vcb.workflow.ci_triage`
- `vcb.codex.cli`
- `vcb.shortcut.automation_mutation_without_review`
- `vcb.shortcut.full_access_automation`
- `vcb.safety.secrets`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_exec -->
