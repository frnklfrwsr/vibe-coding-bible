<!-- VCB:BEGIN_TOPIC id=tool.cursor version=0.1.0 -->
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
id: tool.cursor
title: Cursor
name: Cursor
type: tool_card
category: ai_ide
status: active
review_cadence: quarterly
next_review_due: '2026-09-11'
last_pricing_reviewed: '2026-06-11'
pricing_volatility: very_high
pricing_snapshot_required: false
setup_effort: 'medium: repository rules, privacy posture, terminal permissions, model/tool settings, and review workflow need explicit choices'
maintenance_effort: 'medium: rules, integrations, model access, usage pools, security settings, and IDE behavior drift over time'
debugging_effort: 'medium-high: failures may involve repo context, generated diff scope, terminal commands, model selection, ignored files, or stale rules'
lock_in_risk: 'moderate-high: editor workflows, rules, context habits, and team conventions can become Cursor-specific'
hidden_cost_risk: 'high: fast multi-file work can create review debt, usage burn, broad diffs, and local-environment coupling'
codex_integration_value: medium as an alternate implementation surface; high as an IDE-side review/planning companion when Codex is not the editor owner
best_for:
- AI IDE-native coding assistance
- repo-aware planning and implementation
- local multi-file edits with human review
- diff review inside the editor
- bug fixing with terminal/check evidence
not_for:
- unbounded autonomous rewrites
- secret-heavy production operations
- accepting all suggestions blindly
- parallel agents editing the same files
- stable prose about current model or plan packaging
integrates_with_codex:
- GitHub PR workflow
- local test runners
- Codex plan comparison
- AGENTS.md-style repo guidance
- MCP/tooling where source-checked
hidden_costs:
- reviewing large IDE-generated diffs
- terminal-command side effects
- local setup drift
- rules and memories cleanup
- cross-tool conflict when Codex also edits files
applies_to:
- Cursor
- AI coding / AI IDE / AI planning workflows
- Codex-assisted development
stability:
  principle: CORE_ENGINEERING
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.many_ais_same_files
- vcb.shortcut.parallel_agents_edit_same_files
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.skipping_tests
- vcb.shortcut.model_routing_guesswork
durable_principles:
- Use the smallest tool surface that produces reviewable evidence.
- Separate planning, implementation, review, and approval.
- Treat AI output as a proposal until code, sources, tests, or artifacts verify it.
likely_to_change:
- model routing, plans, pricing, quota behavior, UI labels, integrations, permission defaults, feature names, and context mechanics
obsolete_when:
- Cursor is no longer available, no longer documented by its vendor, or no longer serves its stated AI IDE / coding agent role.
related_topics:
- tool.codex_ide_extension
- tool.github
- tool.github_actions
- tool.playwright
- vcb.shortcut.parallel_agents_edit_same_files
- vcb.shortcut.many_ais_same_files
- vcb.workflow.reviewing_diffs
---

# Cursor

> Summary:
> Cursor is an AI editor and coding-agent environment for repo-aware planning, editing, reviewing, and shipping inside an IDE-style workflow.

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

<!-- VCB:BEGIN_SECTION id=tool.cursor.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Cursor is an AI IDE / coding-agent surface. It can be a strong fit when the work needs editor context, plan-before-code behavior, multi-file edits, reviewable diffs, and human supervision close to the code.

### Why it matters

An AI IDE shortens the loop between question, code, terminal, and diff. That speed is useful only if the task has boundaries, tests, and review discipline. Otherwise the same speed creates broad unreviewed changes.

### What good looks like

Use Cursor for scoped local repo work: understand the codebase, plan the patch, apply a small diff, run checks, and review the result before committing.

### What bad looks like

Do not let an IDE agent roam through unrelated files. Do not rely on a plan or screenshot instead of tests and diffs. Do not give broad local access to secrets or production credentials by default.

### Best-fit cases

- AI IDE-native coding assistance
- repo-aware planning and implementation
- local multi-file edits with human review
- diff review inside the editor
- bug fixing with terminal/check evidence

### Not-fit cases

- unbounded autonomous rewrites
- secret-heavy production operations
- accepting all suggestions blindly
- parallel agents editing the same files
- stable prose about current model or plan packaging

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: repository rules, privacy posture, terminal permissions, model/tool settings, and review workflow need explicit choices |
| Maintenance effort | medium: rules, integrations, model access, usage pools, security settings, and IDE behavior drift over time |
| Debugging effort | medium-high: failures may involve repo context, generated diff scope, terminal commands, model selection, ignored files, or stale rules |
| Lock-in risk | moderate-high: editor workflows, rules, context habits, and team conventions can become Cursor-specific |
| Hidden cost risk | high: fast multi-file work can create review debt, usage burn, broad diffs, and local-environment coupling |

### Human checklist

- Define the decision: planning, implementation, review, explanation, or approval.
- Name the artifact that will prove the work: diff, test run, source link, PR, checklist, trace, screenshot, or written decision.
- Keep secrets, production credentials, and sensitive user data out unless the tool/account/environment is explicitly approved for that use.
- Use one implementation owner for overlapping files.
- Re-check official docs before encoding setup, pricing, model, context, or permission mechanics.

<!-- VCB:END_SECTION id=tool.cursor.human -->

<!-- VCB:BEGIN_SECTION id=tool.cursor.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach `tool.cursor` as a AI IDE / coding agent. The key lesson is tool fit: this tool should be chosen because it produces the right artifact with the right review posture, not because it is familiar or impressive.

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
Use Cursor only for the smallest safe role in this task.
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

<!-- VCB:END_SECTION id=tool.cursor.ai_coach -->

## Shortcut Reality

### Ideal practice

Choose `tool.cursor` only when it is the smallest tool that can produce the required artifact. Keep source checks, diff review, tests, and human approval separate from model fluency.

### What users often do instead

They choose the tool by habit, brand, model preference, or which answer sounds most confident. They may use several AI tools at once, then select the answer that feels best rather than the answer that is verified.

### When the shortcut is acceptable

When Cursor owns a bounded local task, the human can review the diff, and test/check evidence is available.

### When it becomes a bad trade

When Cursor and another agent mutate overlapping files, or when the human accepts multi-file changes because the IDE experience feels fluid.

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

- stop the agent
- inspect the diff file by file
- reset unrelated changes
- run targeted checks
- move the final patch into a small branch/PR

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

- `cursor.docs.agent_overview`
- `cursor.docs.plan_mode`
- `cursor.docs.agent_review`
- `cursor.security`
- `vcb.synthesis.stable_engineering_practice`

## Related Topics

- `tool.codex_ide_extension`
- `tool.github`
- `tool.github_actions`
- `tool.playwright`
- `vcb.shortcut.parallel_agents_edit_same_files`
- `vcb.shortcut.many_ais_same_files`
- `vcb.workflow.reviewing_diffs`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=tool.cursor -->
