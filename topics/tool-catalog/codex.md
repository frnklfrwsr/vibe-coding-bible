<!-- VCB:BEGIN_TOPIC id=tool.codex version=0.1.0 -->
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
id: tool.codex
title: OpenAI Codex
name: OpenAI Codex
type: tool_card
category: first_party_ai_coding_agent
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
last_pricing_reviewed: '2026-06-10'
pricing_volatility: very_high
pricing_snapshot_required: true
pricing_snapshot_ids:
- vcb.pricing_snapshot.openai_codex
setup_effort: 'medium: account, repo access, local/cloud setup, and surface choice'
maintenance_effort: 'medium: docs, models, pricing, permissions, and feature maturity
  change often'
debugging_effort: 'medium: failures can be prompt, context, environment, permissions,
  tests, or product-surface issues'
lock_in_risk: 'moderate: workflows may depend on Codex-specific surfaces, review outputs,
  and config conventions'
hidden_cost_risk: 'high: repeated attempts, long-running tasks, cloud retries, and
  review backlog can dominate apparent tool cost'
codex_integration_value: highest as the orchestration layer that ties prompting, repo
  context, execution, review, and delegation together
best_for:
- repo-aware implementation
- code review and explanation
- bounded cloud delegation
- surface selection for AI-native coding
- risk-managed automation design
not_for:
- unbounded product ownership
- accepting summaries without review
- freezing exact prices, models, limits, or UI mechanics in stable prose
- secrets-heavy production work without explicit controls
integrates_with_codex:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub PR review
- codex exec
hidden_costs:
- usage burn from retries and long contexts
- human review time
- setup and environment drift
- recovery time after broad permissions or unclear scope
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud/Web
- Codex GitHub Review
- codex exec
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.broad_agent_permissions
- vcb.shortcut.skipping_tests
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.model_routing_guesswork
durable_principles:
- Codex works best when task intent, context, constraints, permissions, and acceptance
  evidence are explicit.
- Surface choice should follow task shape and risk, not habit.
- Every mutating result still needs human review proportional to blast radius.
likely_to_change:
- available surfaces, model menus, plan packaging, exact limits, usage economics,
  UI labels, and feature maturity labels
obsolete_when:
- OpenAI replaces Codex with a different first-party coding-agent product family or
  the official docs stop treating Codex surfaces as the primary coding-agent system.
related_topics:
- vcb.chapter.codex_surfaces
- vcb.codex.app
- vcb.codex.cli
- vcb.codex.ide_extension
- vcb.codex.cloud
- vcb.codex.github_review
- vcb.workflow.codex_output_review
---

# OpenAI Codex

> Summary:
> OpenAI Codex is the first-party coding agent family for repo-aware implementation, review, explanation, and delegated work across app, CLI, IDE, cloud, GitHub, and automation surfaces.

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

<!-- VCB:BEGIN_SECTION id=tool.codex.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Codex is the umbrella tool. It is not one button. It is a family of surfaces that can inspect code, propose changes, run commands, review diffs, and hand work between local, cloud, and automation contexts.

### Why it matters

The mistake is treating Codex as a single magic assistant. The useful move is choosing the right surface for the job: local interactive work, editor-context work, terminal work, background cloud work, PR review, or scripted non-interactive work.

### What good looks like

Use Codex for a bounded repo task with a task packet, context, constraints, done-when evidence, and a review path.

### What bad looks like

Ask Codex to own an entire product, skip tests, choose permissions by convenience, and treat the final summary as proof.

### Minimal example

For a small feature, start with a work order, choose App/IDE/CLI/Cloud by context needs, require tests or review evidence, and inspect the diff before merging.

### Best-fit cases

- repo-aware implementation
- code review and explanation
- bounded cloud delegation
- surface selection for AI-native coding
- risk-managed automation design

### Not-fit cases

- unbounded product ownership
- accepting summaries without review
- freezing exact prices, models, limits, or UI mechanics in stable prose
- secrets-heavy production work without explicit controls

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: account, repo access, local/cloud setup, and surface choice |
| Maintenance effort | medium: docs, models, pricing, permissions, and feature maturity change often |
| Debugging effort | medium: failures can be prompt, context, environment, permissions, tests, or product-surface issues |
| Lock-in risk | moderate: workflows may depend on Codex-specific surfaces, review outputs, and config conventions |
| Hidden cost risk | high: repeated attempts, long-running tasks, cloud retries, and review backlog can dominate apparent tool cost |

### Checklist

- choose the smallest Codex surface that fits the task
- confirm permissions before mutation
- require a diff, report, structured output, or check evidence
- keep exact pricing, limits, model availability, and UI mechanics out of stable decisions
- review official OpenAI docs before freezing current product behavior

<!-- VCB:END_SECTION id=tool.codex.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach Codex as an execution system with multiple surfaces. Surface selection is part of risk management, not a preference detail.

### Diagnostic questions

- What surface is the human actually using?
- Does the task need editor context, terminal commands, cloud time, PR review, or a scripted run?
- What evidence must exist before acceptance?
- What permission level and attention level fit the task?

### Coaching tactics

- map task shape to Codex surface before prompting
- separate product facts from stable workflow principles
- route exact pricing, models, limits, and UI labels to official docs or pricing snapshots
- force reviewable artifacts for any mutating work

### Prompt pattern

```text
Choose the Codex surface for this task. Goal: [goal]. Context available: [repo/files/logs]. Constraints: [risk/budget/permissions]. Compare App, CLI, IDE, Cloud, GitHub Review, and codex exec. Recommend the smallest reliable surface and the required evidence before acceptance.
```

### Red flags

- one giant prompt with no surface choice
- exact model/limit/pricing claims in stable prose
- production work with no diff/test/review evidence
- tool selection based on brand feeling instead of task fit

### Intervention rule

When the human asks for a current product detail, exact price, exact limit, model-routing claim, UI label, command flag, or plan-packaging fact, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex.ai_coach -->

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
- `vcb.shortcut.skipping_tests`
- `vcb.shortcut.accepting_looks_done`
- `vcb.shortcut.model_routing_guesswork`

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

- usage burn from retries and long contexts
- human review time
- setup and environment drift
- recovery time after broad permissions or unclear scope

## Stable Core

- Codex works best when task intent, context, constraints, permissions, and acceptance evidence are explicit.
- Surface choice should follow task shape and risk, not habit.
- Every mutating result still needs human review proportional to blast radius.

## Volatile Surface

- available surfaces, model menus, plan packaging, exact limits, usage economics, UI labels, and feature maturity labels

Exact prices, plan packaging, feature availability, commands, flags, model menus, context limits, UI labels, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI replaces Codex with a different first-party coding-agent product family or the official docs stop treating Codex surfaces as the primary coding-agent system.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.overview` — official/synthesis source anchor for this tool card.
- `openai.codex.quickstart` — official/synthesis source anchor for this tool card.
- `openai.codex.best_practices` — official/synthesis source anchor for this tool card.
- `openai.codex.feature_maturity` — official/synthesis source anchor for this tool card.
- `openai.codex.pricing` — official/synthesis source anchor for this tool card.
- `vcb.pricing_snapshot.openai_codex` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `vcb.chapter.codex_surfaces`
- `vcb.codex.app`
- `vcb.codex.cli`
- `vcb.codex.ide_extension`
- `vcb.codex.cloud`
- `vcb.codex.github_review`
- `vcb.workflow.codex_output_review`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex -->
