<!-- VCB:BEGIN_TOPIC id=tool.windsurf version=0.1.0 -->
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
id: tool.windsurf
title: Windsurf / Devin Desktop
name: Windsurf / Devin Desktop
type: tool_card
category: ai_ide
status: active
review_cadence: quarterly
next_review_due: '2026-09-11'
last_pricing_reviewed: '2026-06-11'
pricing_volatility: very_high
pricing_snapshot_required: false
setup_effort: 'medium: install, account/team settings, privacy controls, plugin selection, repo rules, and command permissions need explicit review'
maintenance_effort: 'medium-high: product naming, feature toggles, plugins, privacy controls, rules, hooks, and model surfaces are volatile'
debugging_effort: 'medium-high: failures may involve IDE context, Cascade tool calls, checkpoints, linter integration, ignored files, plugin behavior, or team controls'
lock_in_risk: 'moderate-high: team rules, memories, skills/plugins, and agent workflows can become vendor-specific'
hidden_cost_risk: 'high: agentic IDE speed can create broad diffs, review backlog, plugin policy work, hidden usage burn, and privacy-review overhead'
codex_integration_value: medium as an alternate IDE implementation surface; high as a comparison point when Codex is used for planning or review instead of same-file edits
best_for:
- agentic IDE workflows
- multi-file local coding with review checkpoints
- code explanation and targeted fixes
- plugin-based AI coding assistance
- team-controlled editor adoption
not_for:
- unbounded autonomous rewrites
- secrets-heavy or account-authority work without controls
- production mutation without review
- parallel overlapping agents
- stable claims about current feature names or plan mechanics
integrates_with_codex:
- GitHub review workflow
- local lint/test runners
- plugin ecosystem
- Codex plan comparison
- team AI IDE policy
hidden_costs:
- reviewing broad agentic edits
- checkpoint/revert confusion
- team privacy and feature-control review
- plugin governance
- cross-agent file conflicts
applies_to:
- Windsurf / Devin Desktop
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
- vcb.shortcut.subagent_swarm
- vcb.shortcut.broad_agent_permissions
durable_principles:
- Use the smallest tool surface that produces reviewable evidence.
- Separate planning, implementation, review, and approval.
- Treat AI output as a proposal until code, sources, tests, or artifacts verify it.
likely_to_change:
- model routing, plans, pricing, quota behavior, UI labels, integrations, permission defaults, feature names, and context mechanics
obsolete_when:
- Windsurf / Devin Desktop is no longer available, no longer documented by its vendor, or no longer serves its stated AI IDE / agentic coding surface role.
related_topics:
- tool.cursor
- tool.github
- tool.github_actions
- tool.codex_ide_extension
- vcb.shortcut.parallel_agents_edit_same_files
- vcb.shortcut.subagent_swarm
- vcb.workflow.reviewing_diffs
---

# Windsurf / Devin Desktop

> Summary:
> Windsurf / Devin Desktop is an AI IDE and agentic coding surface centered on Cascade-style planning, editing, command use, checkpoints, and plugin-based coding assistance.

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

<!-- VCB:BEGIN_SECTION id=tool.windsurf.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Windsurf, now documented through Devin Desktop and Windsurf plugin docs, is an AI IDE / agentic coding surface. Its core value is local editor context, agentic code changes, plans, tool use, checkpoints, and plugin/IDE workflows.

### Why it matters

A fast agentic IDE can make exploratory coding feel frictionless. That is useful when paired with checkpoints, scoped prompts, review owners, and tests. It is risky when broad agent authority replaces diff review.

### What good looks like

Use Windsurf for bounded IDE work where Cascade can plan, edit, run checks, and produce reviewable changes. Keep checkpoints, branch state, terminal output, and screenshots/traces tied to acceptance criteria.

### What bad looks like

Do not treat checkpoints as full rollback guarantees. Do not let an agentic IDE touch secrets or production systems casually. Do not use simultaneous agent runs on overlapping files without clear ownership.

### Best-fit cases

- agentic IDE workflows
- multi-file local coding with review checkpoints
- code explanation and targeted fixes
- plugin-based AI coding assistance
- team-controlled editor adoption

### Not-fit cases

- unbounded autonomous rewrites
- secrets-heavy or account-authority work without controls
- production mutation without review
- parallel overlapping agents
- stable claims about current feature names or plan mechanics

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: install, account/team settings, privacy controls, plugin selection, repo rules, and command permissions need explicit review |
| Maintenance effort | medium-high: product naming, feature toggles, plugins, privacy controls, rules, hooks, and model surfaces are volatile |
| Debugging effort | medium-high: failures may involve IDE context, Cascade tool calls, checkpoints, linter integration, ignored files, plugin behavior, or team controls |
| Lock-in risk | moderate-high: team rules, memories, skills/plugins, and agent workflows can become vendor-specific |
| Hidden cost risk | high: agentic IDE speed can create broad diffs, review backlog, plugin policy work, hidden usage burn, and privacy-review overhead |

### Human checklist

- Define the decision: planning, implementation, review, explanation, or approval.
- Name the artifact that will prove the work: diff, test run, source link, PR, checklist, trace, screenshot, or written decision.
- Keep secrets, production credentials, and sensitive user data out unless the tool/account/environment is explicitly approved for that use.
- Use one implementation owner for overlapping files.
- Re-check official docs before encoding setup, pricing, model, context, or permission mechanics.

<!-- VCB:END_SECTION id=tool.windsurf.human -->

<!-- VCB:BEGIN_SECTION id=tool.windsurf.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach `tool.windsurf` as a AI IDE / agentic coding surface. The key lesson is tool fit: this tool should be chosen because it produces the right artifact with the right review posture, not because it is familiar or impressive.

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
Use Windsurf / Devin Desktop only for the smallest safe role in this task.
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

<!-- VCB:END_SECTION id=tool.windsurf.ai_coach -->

## Shortcut Reality

### Ideal practice

Choose `tool.windsurf` only when it is the smallest tool that can produce the required artifact. Keep source checks, diff review, tests, and human approval separate from model fluency.

### What users often do instead

They choose the tool by habit, brand, model preference, or which answer sounds most confident. They may use several AI tools at once, then select the answer that feels best rather than the answer that is verified.

### When the shortcut is acceptable

When Windsurf owns a bounded IDE task with checkpoints, branch isolation, test evidence, and human review.

### When it becomes a bad trade

When the tool is used as a broad always-on coding agent across important files, secrets, or production-adjacent workflows without review controls.

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

- stop active agent runs
- use checkpoints and git diff together
- reset unrelated changes
- rerun tests/lint
- create a small PR with evidence

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

- `windsurf.docs.getting_started`
- `windsurf.docs.cascade`
- `windsurf.docs.plugins`
- `windsurf.docs.admin_controls`
- `windsurf.docs.cascade_hooks`
- `vcb.synthesis.stable_engineering_practice`

## Related Topics

- `tool.cursor`
- `tool.github`
- `tool.github_actions`
- `tool.codex_ide_extension`
- `vcb.shortcut.parallel_agents_edit_same_files`
- `vcb.shortcut.subagent_swarm`
- `vcb.workflow.reviewing_diffs`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=tool.windsurf -->
