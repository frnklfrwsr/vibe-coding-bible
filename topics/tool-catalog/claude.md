<!-- VCB:BEGIN_TOPIC id=tool.claude version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-11'
last_reviewed: '2026-06-11'
audiences:
- human
- ai_coach
source_status:
  official_openai: false
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: official vendor/OpenAI documentation plus VCB maintainer synthesis for setup, risk, budget, and coaching guidance
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
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: tool.claude
title: Claude
name: Claude
type: tool_card
category: alternate_ai_review
status: active
review_cadence: quarterly
next_review_due: '2026-09-11'
last_pricing_reviewed: '2026-06-11'
pricing_volatility: high
pricing_snapshot_required: false
setup_effort: 'medium: useful review depends on clear artifacts, code context, evidence packets, and boundaries'
maintenance_effort: 'medium: model behavior, Claude Code surfaces, integrations, plans, and permissions are volatile'
debugging_effort: 'medium: errors may come from missing repo context, stale assumptions, plausible but false citations, or overbroad agent permissions'
lock_in_risk: 'moderate: workflows, instructions, memories, and Claude Code conventions can become Anthropic-specific'
hidden_cost_risk: 'medium: alternate review can become answer-shopping or duplicate implementation effort if the review question is not bounded'
codex_integration_value: high as an independent planning and review companion for Codex work when evidence is supplied
best_for:
- alternate AI review and critique
- architecture and product tradeoff analysis
- long-form explanation
- codebase reasoning when context is supplied
- review checklists before implementation
not_for:
- approval without evidence
- secret-heavy debugging in a general chat
- best-of-N answer shopping
- repo mutation without branch/diff review
- freezing model names or capabilities into stable guidance
integrates_with_codex:
- Codex plan review
- GitHub PR review packets
- architecture decision records
- dependency review checklists
- multi-AI comparison workflows
hidden_costs:
- second-model review loops
- context packaging time
- conflicting recommendations
- review fatigue
- cross-tool privacy review
applies_to:
- Claude
- AI coding / AI IDE / AI planning workflows
- Codex-assisted development
stability:
  principle: CORE_ENGINEERING
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.consensus_as_correctness
- vcb.shortcut.best_of_n_without_review
- vcb.shortcut.cherry_picking_ai_answers
- vcb.shortcut.ignoring_model_biases
- vcb.shortcut.many_ais_same_files
durable_principles:
- Use the smallest tool surface that produces reviewable evidence.
- Separate planning, implementation, review, and approval.
- Treat AI output as a proposal until code, sources, tests, or artifacts verify it.
likely_to_change:
- model routing, plans, pricing, quota behavior, UI labels, integrations, permission defaults, feature names, and context mechanics
obsolete_when:
- Claude is no longer available, no longer documented by its vendor, or no longer serves its stated alternate AI review workspace role.
related_topics:
- tool.chatgpt
- tool.codex
- tool.github
- vcb.chapter.when_to_use_other_ais
- vcb.shortcut.consensus_as_correctness
- vcb.shortcut.best_of_n_without_review
- vcb.shortcut.many_ais_same_files
---

# Claude

> Summary:
> Claude is an Anthropic AI assistant and coding ecosystem useful for alternate reasoning, architecture critique, long-form explanation, and independent review when outputs are source-checked.

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

<!-- VCB:BEGIN_SECTION id=tool.claude.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Claude is an AI assistant and, through Claude Code, an agentic coding tool. In this Bible, its safest role is independent planning, architecture review, codebase explanation, or alternate critique rather than unquestioned second-opinion authority.

### Why it matters

A second model can reveal blind spots, but it can also repeat plausible mistakes. Claude is useful when you ask it to inspect evidence, argue against a plan, identify missing tests, or produce a review checklist that a human can verify.

### What good looks like

Use Claude to challenge a Codex plan, review an architecture decision, explain a complex module, compare tradeoffs, or produce a risk checklist. Keep the final implementation tied to a branch, diff, test, or PR.

### What bad looks like

Do not use Claude agreement as correctness. Do not ask Claude to approve a patch it cannot inspect. Do not use independent model output to bypass tests, code review, or dependency/source checks.

### Best-fit cases

- alternate AI review and critique
- architecture and product tradeoff analysis
- long-form explanation
- codebase reasoning when context is supplied
- review checklists before implementation

### Not-fit cases

- approval without evidence
- secret-heavy debugging in a general chat
- best-of-N answer shopping
- repo mutation without branch/diff review
- freezing model names or capabilities into stable guidance

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: useful review depends on clear artifacts, code context, evidence packets, and boundaries |
| Maintenance effort | medium: model behavior, Claude Code surfaces, integrations, plans, and permissions are volatile |
| Debugging effort | medium: errors may come from missing repo context, stale assumptions, plausible but false citations, or overbroad agent permissions |
| Lock-in risk | moderate: workflows, instructions, memories, and Claude Code conventions can become Anthropic-specific |
| Hidden cost risk | medium: alternate review can become answer-shopping or duplicate implementation effort if the review question is not bounded |

### Human checklist

- Define the decision: planning, implementation, review, explanation, or approval.
- Name the artifact that will prove the work: diff, test run, source link, PR, checklist, trace, screenshot, or written decision.
- Keep secrets, production credentials, and sensitive user data out unless the tool/account/environment is explicitly approved for that use.
- Use one implementation owner for overlapping files.
- Re-check official docs before encoding setup, pricing, model, context, or permission mechanics.

<!-- VCB:END_SECTION id=tool.claude.human -->

<!-- VCB:BEGIN_SECTION id=tool.claude.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach `tool.claude` as a alternate AI review workspace. The key lesson is tool fit: this tool should be chosen because it produces the right artifact with the right review posture, not because it is familiar or impressive.

### Diagnostic questions

- Is the human asking for planning, editing, review, explanation, or proof?
- What source material can the tool inspect, and what source material is missing?
- Will the tool mutate files, create branches, call external tools, or only produce analysis?
- What is the human's review budget for the output?
- What would make this output unsafe: secrets, production data, auth, payments, broad diffs, or unreviewed dependency changes?

### Coaching tactics

- route tool-choice questions to the smallest active tool card before chapter fallbacks
- ask for evidence, not confidence
- separate alternate-model critique from approval
- force one implementation owner when tools can edit overlapping files
- move durable instructions, decisions, and acceptance criteria into repo artifacts after the chat

### Prompt pattern

```text
Use Claude only for the smallest safe role in this task.
Goal: [goal]
Current evidence: [files/PR/logs/sources/tests]
Allowed authority: [plan only / edit files / review only / create PR]
Risk: [secrets/users/money/production/dependencies]
Required artifact: [diff/checklist/test/source-backed decision]
Give the tool-fit recommendation, minimum guardrails, and review step before any implementation.
```

### Red flags

- The user says “the other AI agreed” as if agreement is verification.
- The user wants broad edits without a branch, diff, or test plan.
- The user asks for current pricing, models, limits, or feature availability without source checks.
- The user wants to paste secrets or production data into a general planning surface.
- Multiple tools are being asked to edit the same files at the same time.

<!-- VCB:END_SECTION id=tool.claude.ai_coach -->

## Shortcut Reality

### Ideal practice

Choose `tool.claude` only when it is the smallest tool that can produce the required artifact. Keep source checks, diff review, tests, and human approval separate from model fluency.

### What users often do instead

They choose the tool by habit, brand, model preference, or which answer sounds most confident. They may use several AI tools at once, then select the answer that feels best rather than the answer that is verified.

### When the shortcut is acceptable

When Claude is asked to critique evidence, propose tests, explain tradeoffs, or serve as a second reviewer with clear source artifacts.

### When it becomes a bad trade

When agreement between Claude and another model is treated as proof, or when two agents edit the same files without ownership boundaries.

### Risk profile

| Risk dimension | Practical read |
|---|---|
| Probability | Medium: tool-choice mistakes are common when the task is ambiguous. |
| Impact | Medium to high: impact depends on whether the output changes files, dependencies, secrets, production behavior, or team decisions. |
| Recoverability | Moderate: recovery is easiest when work is isolated in a chat, branch, checkpoint, or PR; harder when broad changes were accepted without evidence. |

### Blast radius

The blast radius includes wrong plans, broad diffs, stale context, leaked sensitive context, duplicated implementation effort, conflicting agent edits, and tool-specific workflows that later become hard to migrate.

### Minimum guardrails

- decide whether the tool is allowed to plan, edit, review, or approve
- keep implementation on a branch or isolated workspace when files can change
- require a proof artifact before accepting claims
- do not treat model agreement as source verification
- record durable decisions outside the vendor chat or IDE state

### Recovery plan

- ask for source-linked objections, not approval
- merge only through a reviewed diff
- assign one tool as implementation owner
- record unresolved disagreements and test them

## Budget and Constraint Notes

| Constraint profile | Cheapest reliable path | Fastest high-usage path | Low-attention path | Production-quality path |
|---|---|---|---|---|
| Individual / constrained usage | Use the tool for one bounded role, then move the result into a durable artifact. | Batch related questions but require a decision log. | Use it for report-first planning only; do not allow unattended mutation. | Require source checks, small diffs, tests, and explicit review ownership. |
| Team / shared budget | Define when the team uses this tool versus Codex, GitHub, or CI. | Use templates for repeatable review packets. | Route non-urgent tasks to review-later artifacts. | Track setup, review, recovery, and policy-maintenance cost, not just subscription cost. |
| Prototype | Accept rough planning if no production data or user-facing risk is involved. | Use the tool to explore alternatives quickly. | Keep notes disposable unless promoted to the repo. | Convert the winning plan into tests and acceptance criteria before build. |
| Production / maintenance | Prefer narrow review and evidence generation. | Use only with branch isolation and checks. | Use report-only mode unless the owner can inspect diffs. | Require rollback, ownership, security review when relevant, and source-checked volatile details. |

Do not freeze exact prices, plan limits, model names, context-window values, feature names, command flags, default permissions, or UI labels in stable guidance. Put exact values in dated pricing snapshots or source-checked volatile notes.

## Stable Core

- Tool selection is about artifact fit, authority, and review posture.
- Planning tools should produce plans, criteria, and critiques; implementation tools should produce bounded diffs; review tools should produce evidence packets.
- Independent AI review is useful only when it inspects evidence and names uncertainty.
- AI IDE speed increases both productivity and review debt.
- The durable handoff should live in the repo, PR, issue tracker, test artifact, or decision record, not only inside a vendor chat.

## Volatile Surface

- current model availability and routing
- plan packaging, pricing, quotas, usage pools, and limits
- IDE extension behavior, command flags, UI labels, and permission prompts
- context-window behavior, memory/project mechanics, and file-upload constraints
- enterprise/admin controls, privacy defaults, and data-retention posture
- integrations with GitHub, CI, MCP, browser surfaces, and external tools

## Obsolescence Watch

Review this card when:

- the vendor substantially changes product positioning, pricing, plans, or feature availability
- a tool adds or removes file-editing, agentic, repository, or browser/account authority
- model-routing or context behavior changes the safe-use boundary
- team policy changes what may be pasted, uploaded, indexed, or edited
- the repository has an active smaller card for a more specific surface

## Evidence and Sources

Evidence level: `E0_OFFICIAL_DOCS` plus `VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE` for tool-fit, risk, and coaching guidance.

Source IDs:

- `anthropic.docs.claude_intro`
- `anthropic.docs.claude_code_overview`
- `anthropic.docs.prompt_engineering_overview`
- `anthropic.support.claude_projects`
- `vcb.synthesis.stable_engineering_practice`

## Related Topics

- `tool.chatgpt`
- `tool.codex`
- `tool.github`
- `vcb.chapter.when_to_use_other_ais`
- `vcb.shortcut.consensus_as_correctness`
- `vcb.shortcut.best_of_n_without_review`
- `vcb.shortcut.many_ais_same_files`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=tool.claude -->
