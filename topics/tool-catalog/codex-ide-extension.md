<!-- VCB:BEGIN_TOPIC id=tool.codex_ide_extension version=0.1.0 -->
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
id: tool.codex_ide_extension
title: Codex IDE Extension
name: Codex IDE Extension
type: tool_card
category: codex_ide_agent
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
last_pricing_reviewed: '2026-06-10'
pricing_volatility: very_high
pricing_snapshot_required: true
pricing_snapshot_ids:
- vcb.pricing_snapshot.openai_codex
setup_effort: 'low to medium: install extension, authenticate, configure IDE settings,
  learn context and approval controls'
maintenance_effort: 'medium: editor support, settings, command palette commands, model
  controls, and cloud handoff behavior are volatile'
debugging_effort: 'medium: failures may be context selection, extension settings,
  local env, or cloud handoff state'
lock_in_risk: 'moderate: editor workflows can become dependent on extension-specific
  context and command behavior'
hidden_cost_risk: 'medium: low-friction edits can multiply attempts and review debt'
codex_integration_value: high when precise editor context reduces prompt noise and
  speeds focused edits
best_for:
- focused edits from selected code
- code explanation with visible context
- small refactors inside known files
- IDE-to-cloud handoff with context
not_for:
- whole-repo audits without explicit file discovery
- headless automation
- tasks where terminal checks are the main interface
- accepting unverified frontend behavior
integrates_with_codex:
- IDE files and selections
- local project context
- Codex Cloud
- model/reasoning controls
- approval settings
hidden_costs:
- missing-file blind spots
- editor-context staleness
- cloud/local handoff confusion
- review debt from fast inline edits
applies_to:
- Codex IDE Extension
- open files
- selections
- '@file references'
- approval modes
- cloud delegation from IDE
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.context_dumping
- vcb.shortcut.broad_refactor
- vcb.shortcut.parallel_agents_edit_same_files
- vcb.shortcut.accepting_looks_done
durable_principles:
- Editor context is useful only when the relevant files are actually included or discoverable.
- Small local patches still need tests, typechecks, or manual review evidence.
- Cloud handoff from IDE should preserve task boundaries and review expectations.
likely_to_change:
- extension commands, editor support, context mechanics, approval modes, cloud handoff,
  model/reasoning controls
obsolete_when:
- OpenAI retires the IDE extension or changes it so it no longer provides editor-context
  Codex workflows.
related_topics:
- vcb.codex.ide_extension
- vcb.prompting.context_management
- vcb.workflow.frontend_work
- vcb.workflow.refactoring
- vcb.shortcut.context_dumping
---

# Codex IDE Extension

> Summary:
> Codex IDE Extension is the editor-integrated first-party surface for using open files, selections, file references, approval modes, and cloud handoff inside an IDE workflow.

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

<!-- VCB:BEGIN_SECTION id=tool.codex_ide_extension.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

The IDE extension is Codex inside your editor. It is useful when the task depends on the files you already have open, selected code, or an edit loop where you want to keep coding context visible.

### Why it matters

The IDE extension matters because editor context can reduce prompt bulk. The risk is confusing nearby visible code with full project understanding.

### What good looks like

Use it for a focused change where open files, selections, and file references make the instruction precise.

### What bad looks like

Assume the extension understands the whole repo because a few files are open, then accept a cross-cutting change without tests.

### Minimal example

Select the component or failing function, reference the test file, state the acceptance behavior, and ask for a small patch plus checks.

### Best-fit cases

- focused edits from selected code
- code explanation with visible context
- small refactors inside known files
- IDE-to-cloud handoff with context

### Not-fit cases

- whole-repo audits without explicit file discovery
- headless automation
- tasks where terminal checks are the main interface
- accepting unverified frontend behavior

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | low to medium: install extension, authenticate, configure IDE settings, learn context and approval controls |
| Maintenance effort | medium: editor support, settings, command palette commands, model controls, and cloud handoff behavior are volatile |
| Debugging effort | medium: failures may be context selection, extension settings, local env, or cloud handoff state |
| Lock-in risk | moderate: editor workflows can become dependent on extension-specific context and command behavior |
| Hidden cost risk | medium: low-friction edits can multiply attempts and review debt |

### Checklist

- choose the smallest Codex surface that fits the task
- confirm permissions before mutation
- require a diff, report, structured output, or check evidence
- keep exact pricing, limits, model availability, and UI mechanics out of stable decisions
- review official OpenAI docs before freezing current product behavior

<!-- VCB:END_SECTION id=tool.codex_ide_extension.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_ide_extension.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the IDE extension as context-efficient local coaching/editing, not a proof that the model has inspected every relevant dependency.

### Diagnostic questions

- Is the selected/open context sufficient?
- Which file references need to be named explicitly?
- Should this remain local or be delegated to cloud?
- Which approval mode is appropriate?

### Coaching tactics

- prefer selections and @file references over broad context dumps
- ask for a plan when cross-file impact is unknown
- apply cloud handoff only after local context is explicit
- require local test/review before finishing

### Prompt pattern

```text
In the IDE extension, use the selected code plus these referenced files: [files]. Goal: [goal]. Constraints: [constraints]. First identify any missing context, then make the smallest patch and list checks to run.
```

### Red flags

- open-file context treated as whole-repo context
- cloud handoff started from a vague editor chat
- approval mode escalated for convenience
- visual/frontend work accepted without browser evidence

### Intervention rule

When the human asks for a current product detail, exact price, exact limit, model-routing claim, UI label, command flag, or plan-packaging fact, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_ide_extension.ai_coach -->

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

- `vcb.shortcut.context_dumping`
- `vcb.shortcut.broad_refactor`
- `vcb.shortcut.parallel_agents_edit_same_files`
- `vcb.shortcut.accepting_looks_done`

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

- missing-file blind spots
- editor-context staleness
- cloud/local handoff confusion
- review debt from fast inline edits

## Stable Core

- Editor context is useful only when the relevant files are actually included or discoverable.
- Small local patches still need tests, typechecks, or manual review evidence.
- Cloud handoff from IDE should preserve task boundaries and review expectations.

## Volatile Surface

- extension commands, editor support, context mechanics, approval modes, cloud handoff, model/reasoning controls

Exact prices, plan packaging, feature availability, commands, flags, model menus, context limits, UI labels, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI retires the IDE extension or changes it so it no longer provides editor-context Codex workflows.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.ide` — official/synthesis source anchor for this tool card.
- `openai.codex.ide_features` — official/synthesis source anchor for this tool card.
- `openai.codex.ide_settings` — official/synthesis source anchor for this tool card.
- `openai.codex.best_practices` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `vcb.codex.ide_extension`
- `vcb.prompting.context_management`
- `vcb.workflow.frontend_work`
- `vcb.workflow.refactoring`
- `vcb.shortcut.context_dumping`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_ide_extension -->
