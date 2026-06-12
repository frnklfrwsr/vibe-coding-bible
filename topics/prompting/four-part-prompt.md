<!-- VCB:BEGIN_TOPIC id=vcb.prompting.four_part_prompt version=0.1.0 -->
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
evidence_scope: official OpenAI Codex prompting/workflow anchors plus VCB maintainer synthesis
  for risk, budget, and coaching guidance
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
- emergency_hotfix
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.prompting.four_part_prompt
title: Four-Part Prompt
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- ChatGPT coding conversations
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.vague_prompt
- vcb.shortcut.one_big_prompt
- vcb.shortcut.accepting_looks_done
durable_principles:
- clear prompts reduce hidden assumptions
- constraints are part of the task, not decoration
- done-when criteria turn a request into a verifiable contract
likely_to_change:
- Codex prompt UI affordances
- available context attachments
- surface-specific prompt shortcuts
- model behavior around ambiguity
obsolete_when:
- official Codex guidance no longer recommends explicit goals, context, constraints, and success
  criteria for coding tasks
related_topics:
- vcb.chapter.four_part_prompt
- vcb.prompting.acceptance_criteria
- vcb.prompting.context_management
- vcb.prompting.plan_first
- vcb.codex.app
- vcb.codex.cli
- vcb.codex.ide_extension
- vcb.codex.cloud
---

> Summary:
> A four-part prompt gives Codex a goal, context, constraints, and done-when criteria so it can work like a teammate instead of guessing like autocomplete.

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

<!-- VCB:BEGIN_SECTION id=vcb.prompting.four_part_prompt.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A four-part prompt is a coding request with four explicit parts: the goal, the context, the constraints, and the definition of done. It tells Codex what you want, what it should look at, what it must not do, and how both of you will know the work is finished.

### Why it matters

Most bad Codex sessions fail before the model writes code. The user asks for a vague result, Codex guesses missing context, and the final diff looks plausible while solving the wrong problem. The four-part prompt prevents that by turning intention into a work order.

### The mental model

Treat the prompt like a ticket for a competent developer who has not lived inside your head. The ticket does not need to be long. It needs to remove the dangerous guesses.

### What good looks like

Good: “Goal: add server-side validation for signup email. Context: follow `app/auth/signup.ts` and existing tests in `auth.test.ts`. Constraints: no new validation library, keep public API unchanged. Done when: invalid emails fail tests, valid signup still passes, and you list checks run.”

### What bad looks like

Bad: “Fix signup.” That prompt hides the goal, the relevant files, the forbidden changes, and the proof required.

### Minimal example

Use this skeleton: Goal: [one outcome]. Context: [files, issue, logs, user flow]. Constraints: [do not change, dependencies, risk boundaries]. Done when: [tests, behavior, diff report, manual check].

### Checklist

- one primary outcome is named
- relevant files, logs, docs, or commands are provided
- dangerous or unwanted changes are ruled out
- done-when evidence is executable or reviewable
- the request is small enough to inspect in one diff
<!-- VCB:END_SECTION id=vcb.prompting.four_part_prompt.human -->

<!-- VCB:BEGIN_SECTION id=vcb.prompting.four_part_prompt.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to prompt Codex as a scoped operator: outcome first, context second, boundaries third, proof last.

### Diagnose the human’s current model

- Can the user state the outcome in one sentence?
- Can Codex see the files or logs needed to decide?
- What must not change?
- What evidence would convince a reviewer the task is complete?
- Is this one task or a bundle of unrelated tasks?

### Explanation strategy

Rewrite vague prompts into four labeled blocks. Do not merely “improve wording.” Force the missing operating contract into the prompt. If the task is too broad, split it before asking Codex to implement.

### Useful metaphor

The four-part prompt is a runway. Without it, the agent may still take off, but it is guessing direction, payload, and landing conditions.

### Coaching tactics

- ask for missing context before code
- turn adjectives such as “clean” or “better” into measurable acceptance criteria
- include negative constraints when a shortcut would be risky
- require Codex to report checks run and files changed
- use the same skeleton across App, CLI, IDE, and Cloud surfaces

### Prompt patterns

```text
Goal: [single outcome]. Context: [files/logs/issue]. Constraints: [boundaries]. Done when: [tests/checks/report].
Before editing, restate the goal, assumptions, touched files, and verification plan. Ask if any critical context is missing.
Implement only [slice]. Do not refactor unrelated code. Done when [specific test/check] passes and you summarize the diff.
```

### Red flags to call out directly

- “fix it” prompt
- multiple features in one request
- no done-when clause
- no forbidden changes
- production task with no review plan

### Exercises

- Have the human convert three vague requests into four-part prompts.
- Ask the human to delete any prompt line Codex does not need, then add any missing constraint.
- Give the human a bad diff and trace the missing prompt part that allowed it.
<!-- VCB:END_SECTION id=vcb.prompting.four_part_prompt.ai_coach -->

## Shortcut Reality

### The ideal practice

Use a compact four-part prompt for every non-trivial Codex task.

### What users often do instead

Users often write a one-line wish and rely on Codex to infer everything else.

### When the shortcut may be fine

A one-line prompt can be fine for tiny read-only questions, formatting nits, or throwaway experiments where failure is cheap.

### When the shortcut is a bad idea

It is a bad trade for production code, auth, data, migrations, dependency changes, broad refactors, or anything you will merge without deep review.

### Risk profile

- Probability of failure: Medium failure probability on normal tasks; high when the repo is unfamiliar or the request is ambiguous.
- Impact if it fails: Small for disposable prototypes; large for production code, shared APIs, data behavior, or security boundaries.
- Ease of recovery: Good when changes are small and Git-backed; poor when the vague request caused broad edits across many files.
- Blast radius: The blast radius grows with each missing part: no context causes wrong files, no constraints cause unrelated changes, and no done-when causes false completion.
- Skill needed to recover: Low to medium for prompt repair; medium for diff cleanup after broad agent changes.
- Hidden cost: Extra review time, wasted usage, noisy diffs, and future bug hunts from plausible but wrong assumptions.

### Minimum guardrails

- use the four labels even when brief
- limit one outcome per prompt
- include at least one verification requirement
- forbid unrelated refactors by default
- review the diff rather than the summary

### Recovery plan

- Stop the session before accepting more changes.
- Ask Codex to summarize assumptions it made.
- Reset or branch the diff if it is too broad.
- Rewrite the request using the four-part skeleton.
- Re-run with narrower scope and explicit proof.

## Budget and Constraint Notes

### Cheapest reliable path

Spend one minute writing the skeleton. It is cheaper than paying for a long correction loop.

### Fastest high-usage path

Use a saved prompt template and fill the four blanks. High-usage users should standardize it across surfaces.

### Low-attention path

Do not use low-attention delegation unless the done-when clause is concrete and the task is branch-isolated.

### Production-quality path

Production prompts must include constraints, tests/checks, and a reviewable final report. The prompt is part of the audit trail.

### Prototype versus production

For prototypes, a thinner prompt is acceptable if you expect to throw code away. For production, the prompt must survive review and maintenance.

## Stable Core

- agents need explicit intent, context, constraints, and verification
- short prompts are fine only when they still contain the needed contract
- a prompt that cannot be reviewed usually creates a diff that cannot be trusted

## Volatile Surface

- Codex UI prompt affordances
- context attachment limits
- model behavior around ambiguity
- surface-specific prompt examples
- availability of plan or prompt modes

Review volatile details against official sources before freezing commands, UI labels, model advice, plan packaging, context limits, or feature availability.

## Obsolescence Watch

- official Codex guidance changes its recommended prompt structure
- Codex surfaces start enforcing structured task fields natively
- model behavior becomes reliable enough with underspecified prompts that the risk profile changes

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for prompt structure, planning, review, and verification.
- `openai.codex.prompting` — Official OpenAI Codex prompting guidance for goals, context, success criteria, and interaction patterns.
- `openai.codex.workflows` — Official OpenAI Codex workflow examples for explicit context, done definitions, bug fixes, and tests.
- `vcb.synthesis.prompting_operator_practice` — VCB maintainer synthesis for prompt operating patterns, guardrails, and coaching tactics.

## Related Topics

- `vcb.chapter.four_part_prompt`
- `vcb.prompting.acceptance_criteria`
- `vcb.prompting.context_management`
- `vcb.prompting.plan_first`
- `vcb.codex.app`
- `vcb.codex.cli`
- `vcb.codex.ide_extension`
- `vcb.codex.cloud`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.prompting.four_part_prompt -->
