<!-- VCB:BEGIN_TOPIC id=tool.chatgpt version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-11'
last_reviewed: '2026-06-11'
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
id: tool.chatgpt
title: ChatGPT
name: ChatGPT
type: tool_card
category: planning_explanation
status: active
review_cadence: quarterly
next_review_due: '2026-09-11'
last_pricing_reviewed: '2026-06-11'
pricing_volatility: high
pricing_snapshot_required: false
setup_effort: 'low: the main setup is deciding what context belongs in the chat, project, uploaded files, or connected source'
maintenance_effort: 'medium: projects, saved context, memories, custom GPTs, and tool availability can drift and need periodic cleanup'
debugging_effort: 'medium: wrong output may be caused by missing context, stale sources, hallucination, project-memory confusion, or ambiguous acceptance criteria'
lock_in_risk: 'moderate: project context, saved chats, custom GPT behavior, and planning artifacts can become OpenAI-specific unless exported into repo docs'
hidden_cost_risk: 'medium: repeated deep research, file analysis, image generation, and model-shopping can burn attention and usage without producing shippable evidence'
codex_integration_value: high as a planning, explanation, and review companion before or after Codex execution
best_for:
- product thinking and requirements shaping
- plain-language technical explanation
- planning and acceptance criteria
- research synthesis with source checks
- data-analysis or document-analysis support when the artifact is not a repo patch
not_for:
- direct repository mutation without a review surface
- security approval or production sign-off
- secret-heavy debugging
- choosing the most flattering answer from multiple models
- freezing current model/tool availability into stable docs
integrates_with_codex:
- Codex task planning
- GitHub PR review packets
- prompt-library workflows
- source-backed research
- data-analysis artifacts
hidden_costs:
- long planning loops without implementation
- model-shopping instead of evidence review
- stale project context
- lost decisions that never move into the repo
- privacy review for uploaded files and connected sources
applies_to:
- ChatGPT
- AI coding / AI IDE / AI planning workflows
- Codex-assisted development
stability:
  principle: CORE_ENGINEERING
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.best_of_n_without_review
- vcb.shortcut.cherry_picking_ai_answers
- vcb.shortcut.consensus_as_correctness
- vcb.shortcut.ignoring_model_biases
- vcb.shortcut.model_routing_guesswork
durable_principles:
- Use the smallest tool surface that produces reviewable evidence.
- Separate planning, implementation, review, and approval.
- Treat AI output as a proposal until code, sources, tests, or artifacts verify it.
likely_to_change:
- model routing, plans, pricing, quota behavior, UI labels, integrations, permission defaults, feature names, and context mechanics
obsolete_when:
- ChatGPT is no longer available, no longer documented by its vendor, or no longer serves its stated planning workspace role.
related_topics:
- tool.codex
- tool.github
- vcb.chapter.when_to_use_other_ais
- vcb.chapter.tool_stack_catalog
- vcb.shortcut.model_routing_guesswork
- vcb.shortcut.best_of_n_without_review
- vcb.shortcut.consensus_as_correctness
- vcb.shortcut.ignoring_model_biases
---

# ChatGPT

> Summary:
> ChatGPT is the general-purpose AI workspace for product thinking, explanation, research synthesis, data analysis, writing, planning, and code-oriented reasoning outside the repository editing loop.

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

<!-- VCB:BEGIN_SECTION id=tool.chatgpt.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

ChatGPT is a conversational AI workspace. In vibe coding, its best role is usually product thinking, prompt shaping, requirements explanation, research synthesis, lightweight data analysis, and independent review of plans before Codex or an IDE agent changes files.

### Why it matters

It gives you a thinking surface that is not automatically editing your repo. That separation is useful when the decision is still fuzzy, when the user needs a plain-language explanation, or when the best output is a plan, checklist, acceptance criteria, or critique rather than a patch.

### What good looks like

Use ChatGPT to clarify the goal, compare options, write acceptance criteria, summarize evidence, produce a review checklist, or explain a confusing code concept. Then hand the bounded implementation task to Codex, GitHub, or an IDE tool with the context preserved.

### What bad looks like

Do not treat a persuasive ChatGPT plan as proof that the code works. Do not paste secrets, private user data, or production credentials into a planning chat. Do not bounce among models until one says what you wanted to hear.

### Best-fit cases

- product thinking and requirements shaping
- plain-language technical explanation
- planning and acceptance criteria
- research synthesis with source checks
- data-analysis or document-analysis support when the artifact is not a repo patch

### Not-fit cases

- direct repository mutation without a review surface
- security approval or production sign-off
- secret-heavy debugging
- choosing the most flattering answer from multiple models
- freezing current model/tool availability into stable docs

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | low: the main setup is deciding what context belongs in the chat, project, uploaded files, or connected source |
| Maintenance effort | medium: projects, saved context, memories, custom GPTs, and tool availability can drift and need periodic cleanup |
| Debugging effort | medium: wrong output may be caused by missing context, stale sources, hallucination, project-memory confusion, or ambiguous acceptance criteria |
| Lock-in risk | moderate: project context, saved chats, custom GPT behavior, and planning artifacts can become OpenAI-specific unless exported into repo docs |
| Hidden cost risk | medium: repeated deep research, file analysis, image generation, and model-shopping can burn attention and usage without producing shippable evidence |

### Human checklist

- Define the decision: planning, implementation, review, explanation, or approval.
- Name the artifact that will prove the work: diff, test run, source link, PR, checklist, trace, screenshot, or written decision.
- Keep secrets, production credentials, and sensitive user data out unless the tool/account/environment is explicitly approved for that use.
- Use one implementation owner for overlapping files.
- Re-check official docs before encoding setup, pricing, model, context, or permission mechanics.

<!-- VCB:END_SECTION id=tool.chatgpt.human -->

<!-- VCB:BEGIN_SECTION id=tool.chatgpt.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach `tool.chatgpt` as a planning workspace. The key lesson is tool fit: this tool should be chosen because it produces the right artifact with the right review posture, not because it is familiar or impressive.

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
Use ChatGPT only for the smallest safe role in this task.
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

<!-- VCB:END_SECTION id=tool.chatgpt.ai_coach -->

## Shortcut Reality

### Ideal practice

Choose `tool.chatgpt` only when it is the smallest tool that can produce the required artifact. Keep source checks, diff review, tests, and human approval separate from model fluency.

### What users often do instead

They choose the tool by habit, brand, model preference, or which answer sounds most confident. They may use several AI tools at once, then select the answer that feels best rather than the answer that is verified.

### When the shortcut is acceptable

When the task is analysis, planning, explanation, research triage, or acceptance-criteria writing and no files are being mutated.

### When it becomes a bad trade

When the user uses a fluent plan, estimate, or model agreement as implementation proof.

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

- move durable decisions into the repo or issue tracker
- rerun source checks for current facts
- turn the plan into testable acceptance criteria
- ask Codex or an IDE agent for a small diff only after the task is bounded

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

- `openai.help.chatgpt_capabilities`
- `openai.help.chatgpt_projects`
- `openai.help.chatgpt_data_analysis`
- `openai.help.truthfulness`
- `openai.chatgpt.pricing`
- `vcb.synthesis.stable_engineering_practice`

## Related Topics

- `tool.codex`
- `tool.github`
- `vcb.chapter.when_to_use_other_ais`
- `vcb.chapter.tool_stack_catalog`
- `vcb.shortcut.model_routing_guesswork`
- `vcb.shortcut.best_of_n_without_review`
- `vcb.shortcut.consensus_as_correctness`
- `vcb.shortcut.ignoring_model_biases`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=tool.chatgpt -->
