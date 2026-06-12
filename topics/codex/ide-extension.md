<!-- VCB:BEGIN_TOPIC id=vcb.codex.ide_extension version=0.1.0 -->
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
id: vcb.codex.ide_extension
title: Codex IDE Extension
type: codex_feature
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex IDE Extension
- VS Code-compatible editors
- JetBrains IDEs
- Local repositories
- Codex Cloud
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.context_dumping
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.vague_prompt
durable_principles:
- IDE context is useful when open files and selections are relevant
- near-code conversations should still end in diffs and checks
- local IDE work and cloud delegation need different review expectations
likely_to_change:
- supported editors and platforms
- commands, slash commands, and settings
- model/approval UI
- cloud handoff behavior
obsolete_when:
- official docs no longer describe IDE extension as a supported Codex surface
related_topics:
- vcb.chapter.codex_surfaces
- vcb.codex.app
- vcb.codex.cli
- vcb.codex.cloud
- vcb.prompting.context_management
- vcb.concepts.diff
---

> Summary:
> The Codex IDE extension is the side-by-side coding surface for tasks where open files, selected code, local editor context, and quick iteration matter.

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

<!-- VCB:BEGIN_SECTION id=vcb.codex.ide_extension.human -->
## 1. For the Human: Plain-Language Concept

### What this means

The IDE extension lets Codex work beside your code editor. It can use the files you have open, selected code, and file references to answer or edit in context. It is best when you are actively looking at the relevant code and want help close to the change.

### Why it matters

The IDE extension matters because context quality is often better when the editor already has the right files open. It also reduces friction for small fixes and explanation tasks. But the same closeness can create overtrust: nearby suggestions still need diff review and checks.

### The mental model

Use the IDE extension like a pair programmer sitting next to your open files. It sees what you point at, but it does not automatically know every production risk around that code.

### What good looks like

Good use: select a function, ask Codex to explain it, ask for a small change, run the nearby test, and inspect the resulting diff.

### What bad looks like

Bad use: ask a broad repo-wide change from the IDE without plan, branch, or acceptance criteria because the relevant file happens to be open.

### Minimal example

Example: highlight a component and ask Codex to add an empty/error state using existing patterns, then run the relevant story or test and review the changed files.

### Checklist

- Name the task and the Codex surface explicitly.
- Confirm whether the work is prototype, maintenance, production, or emergency work.
- Choose permissions and attention level before starting.
- Require a diff, report, or artifact that proves what changed.
- Review volatile details against official docs before freezing commands or UI instructions.
<!-- VCB:END_SECTION id=vcb.codex.ide_extension.human -->

<!-- VCB:BEGIN_SECTION id=vcb.codex.ide_extension.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach IDE work as context-rich, supervised, and diff-backed. Avoid letting open-file convenience become scope creep.

### Diagnose the human’s current model

- Are the currently open files actually the right context?
- Is the task small enough for live IDE supervision?
- Should this be delegated to cloud instead?
- What local check proves the edit?

### Explanation strategy

Start with task/surface fit. Explain what this Codex feature is good at, what it does not prove, and which guardrails become mandatory as blast radius grows. Tie the explanation to the user’s actual repository, risk level, and attention budget.

### Useful metaphors

The IDE extension is a microscope. It is excellent for close inspection, but it can make the user forget the rest of the organism exists.

### Coaching tactics

- Ask the user what surface they are actually using before giving feature-specific advice.
- Separate stable workflow principle from volatile product mechanics.
- Convert broad requests into scoped work orders with explicit done-when criteria.
- Escalate hard for production, secrets, auth, payments, migrations, CI credentials, browser state, or unattended mutation.
- Prefer reviewable artifacts over confident summaries.

### Prompt patterns

```text
Use the currently open files and this selection as context. Make the smallest change that satisfies [done when]. Do not touch unrelated files. Before editing, name the files you expect to change. After editing, tell me the exact check to run.
```

### Red flags to call out directly

- the user expects open files to substitute for acceptance criteria
- the edit touches project-wide behavior
- Codex wants to add dependencies without asking
- the IDE task should be a cloud/worktree task instead

### Exercises

1. Ask the human to choose this feature for one low-risk task and one high-risk task, then explain what guardrails change.
2. Ask the human to name which part of this feature is stable principle and which part must be rechecked against official docs.
3. Ask the human to write a final-report template for work done through this feature.
<!-- VCB:END_SECTION id=vcb.codex.ide_extension.ai_coach -->

## Shortcut Reality

### The ideal practice

Use the IDE extension for local, supervised, context-rich code explanation, small edits, and targeted iteration.

### What users often do instead

Users often ask the IDE extension to infer too much from whatever file is open.

### When the shortcut may be fine

This is acceptable for explanations, local prototypes, or tiny edits where the open file fully contains the behavior.

### When the shortcut is a bad idea

It fails when the change depends on routing, backend contracts, auth, database state, or shared components not open in the editor.

### Risk profile

- Probability of failure: Medium failure probability for multi-file tasks, low impact for local edits, higher impact when hidden dependencies or shared components are involved.
- Impact if it fails: rises sharply with production data, secrets, real users, payments, auth, CI credentials, or deployment paths.
- Ease of recovery: good only when work is branch-isolated, committed, fake-data backed, and reviewable.
- Blast radius: small for local prototypes; large for shared repos, cloud work, external tools, GUI control, and automated mutation.
- Skill needed to recover: low for small Git-backed diffs; medium/high for secrets, data, deployment, or account-state mistakes.
- Hidden cost: stale configuration, noisy automation, false confidence, usage burn, and future maintenance load.

### Minimum guardrails

- name the intended files
- include done-when criteria
- ask for plan-only if multiple files are involved
- run the nearest test/build
- review the actual diff

### Recovery plan

Revert the IDE diff if scope expanded, reopen with explicit files and constraints, and move broad work into a branch/worktree or cloud task.

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

- IDE context is useful when open files and selections are relevant
- near-code conversations should still end in diffs and checks
- local IDE work and cloud delegation need different review expectations

## Volatile Surface

- supported editors and platforms
- commands, slash commands, and settings
- model/approval UI
- cloud handoff behavior

## Obsolescence Watch

- official docs no longer describe IDE extension as a supported Codex surface

## Evidence and Sources

- `openai.codex.ide` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.ide_features` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.ide_settings` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.prompting` — official source anchor for this card's current Codex feature behavior.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for blast radius, recoverability, workflow fit, and AI-coach intervention guidance.

## Related Topics

- `vcb.chapter.codex_surfaces`
- `vcb.codex.app`
- `vcb.codex.cli`
- `vcb.codex.cloud`
- `vcb.prompting.context_management`
- `vcb.concepts.diff`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.codex.ide_extension -->
