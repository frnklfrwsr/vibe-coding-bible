<!-- VCB:BEGIN_TOPIC id=vcb.chapter.when_to_use_other_ais version=0.1.0 -->
---
id: vcb.chapter.when_to_use_other_ais
title: "Chapter 44 — When to Use Other AIs With Codex"
type: chapter
chapter_number: 44
version: 0.1.0
last_verified: '2026-06-09'
next_review_due: '2026-07-09'
review_cadence: monthly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- all project types

source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: AGENTIC_PRINCIPLE
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE

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
- disposable_prototype

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

shortcut_profiles:
- vcb.shortcut.many_ais_same_files
- vcb.shortcut.cherry_picking_ai_answers
- vcb.shortcut.tool_sprawl
- vcb.shortcut.buying_tools_as_progress

durable_principles:
- Use one primary implementer, optional reviewer, and optional planner.
- Independent perspectives help only when roles are separated.
- Do not let multiple agents mutate the same files without integration discipline.

likely_to_change:
- product packaging
- current pricing and limits
- model-specific behavior

obsolete_when:
- Codex product behavior or pricing model materially changes.

related_topics:
- vcb.chapter.tool_stack_catalog
- vcb.chapter.reviewing_codex_output
- vcb.chapter.subagents_parallel_thinking
- vcb.chapter.field_notes_unofficial_practices
---

> Summary:
> Other AIs can be useful with Codex when each has a clear role. They become harmful when they duplicate work, fight over files, or let the user cherry-pick the most pleasing answer.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.when_to_use_other_ais.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Codex does not have to be the only AI in your workflow. It should usually be the repo-aware implementer: it reads files, edits code, runs checks, and reports diffs.

Other AIs can help when they play a different role.

### Useful roles

| Role | Good use | Bad use |
|---|---|---|
| Planner / product thinker | clarify product intent, user flows, tradeoffs | invent implementation details without repo context |
| Repo implementer | Codex edits files and runs checks | multiple tools edit same files blindly |
| Fresh reviewer | independent critique of diff, risks, architecture | rubber-stamp or style nitpicks only |
| Explainer/tutor | teach concepts and jargon | replace actual repo inspection |
| UI/prototype generator | rough visual direction or scaffold | production code without review/hardening |
| IDE autocomplete | small local assistance | autonomous broad refactors without control loop |

### Good multi-AI workflow

```text
ChatGPT or planner AI: clarify product spec.
Codex: inspect repo, implement slice, run checks.
Fresh reviewer AI/Codex: review diff and risks.
Human: decide what ships.
```

### Bad multi-AI workflow

```text
Ask five tools the same vague question.
Pick the answer that sounds easiest.
Paste code between them.
Let two tools edit the same files.
Ship because they agree vaguely.
```

Agreement is not proof. Evidence is proof: diff, tests, screenshots, logs, and behavior.

### Multi-AI prompt

```text
You are not the implementer. Your job is independent review.

Review this plan/diff for:
- missing assumptions,
- security risks,
- test gaps,
- dependency risk,
- simpler alternatives.

Do not suggest rewriting unless the current approach cannot meet the goal.
Separate blockers from nice-to-have feedback.
```

<!-- VCB:END_SECTION id=vcb.chapter.when_to_use_other_ais.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.when_to_use_other_ais.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Help the human use other AIs as role-separated perspectives, not as a swarm of conflicting implementers.

### Diagnostic questions

- What role is each AI playing?
- Which tool has actual repo context?
- Which tool is allowed to mutate files?
- Is the user seeking better evidence or a more pleasing answer?
- Are two tools touching the same files?

### Useful metaphor

A good team has roles: product lead, implementer, reviewer, tester. A bad team has five people grabbing the keyboard at once.

### Coaching tactics

- Assign one implementer.
- Assign one reviewer if risk justifies it.
- Use planning tools before Codex, not after a confusing diff.
- Convert external AI advice into Codex prompts only after checking repo reality.
- Demand evidence when AIs disagree.

### Red flags

- “Claude said it was fine, Codex said it was fine, so ship it.”
- “Let Cursor, Codex, and an app builder all edit the repo.”
- “I asked many tools until one said no tests needed.”
- “This AI knows the framework better than our actual code.”

<!-- VCB:END_SECTION id=vcb.chapter.when_to_use_other_ais.ai_coach -->

## Shortcut Reality

### The ideal practice

Use one primary implementer and optional independent reviewer/planner roles.

### What users often do instead

They ask many tools the same question, paste outputs around, and cherry-pick the answer that sounds fastest.

### When the shortcut may be fine

Multi-AI brainstorming is fine before code exists, or when comparing product ideas without committing files.

### When the shortcut is a bad idea

It is bad when multiple tools edit the same repo, make incompatible architecture assumptions, or touch production/auth/payments/secrets without one integration owner.

### Risk profile

- Probability of failure: medium/high with file mutation.
- Impact if it fails: conflicting architecture, context pollution, unreviewable diffs.
- Ease of recovery: high if advice-only, lower if multiple tools wrote files.
- Blast radius: grows with shared files and production config.
- Hidden cost: subscription drag and decision fatigue.

### Minimum guardrails

- Assign one implementer.
- Keep others read-only/review-only.
- Route all changes through Git diff.
- Record which advice was accepted and why.
- Never let multiple tools fight over the same files.

### Recovery plan

If tools conflict, stop edits, inspect diff, revert ambiguous changes, write one accepted plan, and let a single implementer apply the next slice.

## Budget and Constraint Notes

### Cheapest reliable path

Use one AI implementer and one lightweight planning/review pass only for high-value ambiguity.

### Fastest high-usage path

Use parallel independent reviewers for architecture/security/tests, but keep mutation serialized through Codex and Git.

### Low-attention path

Do not leave several tools running independently. Use report-only outputs and one integration owner.

### Production-quality path

Require clear roles, source-backed claims, diffs, tests, review, and human approval.

## Stable Core

The stable principle is role separation. Independent perspectives can reduce blind spots; uncoordinated mutation creates chaos.

## Volatile Surface

AI product capabilities, prices, context windows, model strengths, integrations, and file-editing behavior change quickly.

## Obsolescence Watch

Review monthly or when major AI coding tools change their autonomous-editing or review capabilities. Obsolete if one platform reliably provides role-separated planning, implementation, review, testing, and integration with strong evidence controls.

## Evidence and Sources

- `openai.codex.overview` — official OpenAI source for Codex as coding agent
- `openai.codex.best_practices` — official Codex source for workflow, validation, tools, and durable guidance
- `openai.help.truthfulness` — official OpenAI source for critical verification of model outputs
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for multi-AI role separation

## Related Topics

- `vcb.chapter.tool_stack_catalog`
- `vcb.chapter.reviewing_codex_output`
- `vcb.chapter.subagents_parallel_thinking`
- `vcb.chapter.field_notes_unofficial_practices`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.when_to_use_other_ais -->
