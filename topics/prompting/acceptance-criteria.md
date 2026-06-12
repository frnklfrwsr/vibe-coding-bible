<!-- VCB:BEGIN_TOPIC id=vcb.prompting.acceptance_criteria version=0.1.0 -->
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
id: vcb.prompting.acceptance_criteria
title: Acceptance Criteria / Done-When
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- Pull requests
- Testing workflows
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.skipping_tests
durable_principles:
- done is a claim that needs evidence
- acceptance criteria must be observable by humans or machines
- ambiguous success criteria produce ambiguous diffs
likely_to_change:
- test runner commands
- CI checks
- Codex final-report formatting
- surface-specific verification buttons
obsolete_when:
- software work no longer requires observable completion evidence before merge or release
related_topics:
- vcb.chapter.acceptance_criteria
- vcb.prompting.four_part_prompt
- vcb.workflow.testing
- vcb.workflow.bug_repro
- vcb.concepts.test
- vcb.concepts.ci
---

> Summary:
> Acceptance criteria are the observable conditions that prove a Codex task is finished instead of merely plausible.

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

<!-- VCB:BEGIN_SECTION id=vcb.prompting.acceptance_criteria.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Acceptance criteria are the conditions that must be true before you call the work done. In vibe coding, “done” should mean behavior changed, checks passed, and the diff is reviewable—not “Codex said it is fixed.”

### Why it matters

Codex can produce convincing explanations and still miss the target. Acceptance criteria give you a scoreboard before the work starts.

### The mental model

Acceptance criteria are the finish line painted on the track. Without the line, everyone keeps running and argues later about who won.

### What good looks like

Good: “Done when a logged-out user is redirected to `/login`, the existing authenticated route test still passes, a new unauthenticated test fails before the fix and passes after, and no unrelated route files are changed.”

### What bad looks like

Bad: “Make auth better.” That has no observable finish line.

### Minimal example

Done when: [specific behavior]. Evidence: [test, command, screenshot, log, or manual step]. Boundaries: [files or behavior that must not change]. Report: [what Codex must summarize].

### Checklist

- user-visible behavior is named
- machine check or manual verification step is named
- negative case is included when relevant
- forbidden regressions are named
- final evidence is small enough to inspect
<!-- VCB:END_SECTION id=vcb.prompting.acceptance_criteria.human -->

<!-- VCB:BEGIN_SECTION id=vcb.prompting.acceptance_criteria.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to make “done” observable before implementation starts.

### Diagnose the human’s current model

- What behavior should change?
- What behavior must stay the same?
- How can the result be tested?
- What would make you reject the diff?
- Can a reviewer verify this without trusting Codex’s summary?

### Explanation strategy

Translate vague outcomes into testable conditions. Separate acceptance criteria from implementation instructions. If the human cannot define done, pause and scope the task.

### Useful metaphor

Acceptance criteria are a receipt. They do not guarantee the product is perfect, but they show what was bought and how it was checked.

### Coaching tactics

- ask for one positive and one negative example
- force the user to name the verification artifact
- prefer behavior criteria over implementation criteria
- include non-regression criteria for risky areas
- make Codex report evidence, not confidence

### Prompt patterns

```text
Done when: [behavior] is true, [regression] remains false, [test/check] passes, and the diff only touches [scope].
Before coding, propose acceptance criteria and wait for confirmation.
After coding, map each changed file to one acceptance criterion and list checks run.
```

### Red flags to call out directly

- done when “it works”
- no negative case
- test added after implementation without failure-first check
- criteria hidden in a long prompt paragraph
- criteria based on internal implementation only

### Exercises

- Ask the human to write reject conditions before accept conditions.
- Turn a user story into three done-when bullets.
- Compare a Codex final report against the original criteria and mark unsupported claims.
<!-- VCB:END_SECTION id=vcb.prompting.acceptance_criteria.ai_coach -->

## Shortcut Reality

### The ideal practice

Define done-when criteria before Codex changes code.

### What users often do instead

Users often inspect the final summary and decide by vibes whether the task is done.

### When the shortcut may be fine

Loose done-when can be acceptable for throwaway spikes, visual sketches, or exploratory reading tasks.

### When the shortcut is a bad idea

It is a bad trade for mergeable code, bug fixes, tests, production behavior, data changes, or security-sensitive flows.

### Risk profile

- Probability of failure: Medium probability of false completion when criteria are vague; high for bugs without a repro or UI work without expected states.
- Impact if it fails: Small for disposable exploration; high for regressions that reach users because the task looked done.
- Ease of recovery: Good if criteria are added before merge; poor after broad changes land without evidence.
- Blast radius: The blast radius is the set of behaviors users assume were checked but were not.
- Skill needed to recover: Low for writing criteria; medium for reconstructing evidence after the fact.
- Hidden cost: False confidence, missing tests, review fatigue, and repeated prompts to fix symptoms.

### Minimum guardrails

- write done-when bullets separately from implementation advice
- include one verification artifact
- require Codex to map results to criteria
- treat unchecked criteria as not done
- do not merge based only on summary text

### Recovery plan

- Freeze the diff.
- Write acceptance criteria retroactively.
- Ask Codex to map current changes to each criterion.
- Run or create missing checks.
- Reject, narrow, or revert unsupported changes.

## Budget and Constraint Notes

### Cheapest reliable path

Use two to five criteria. More is not better if it hides the important proof.

### Fastest high-usage path

High-throughput users should use default done-when templates for bugs, features, tests, and refactors.

### Low-attention path

Low-attention tasks need stricter criteria, not looser ones, because you are not watching the work unfold.

### Production-quality path

Production work needs executable evidence where possible plus human review of the diff.

### Prototype versus production

Prototype criteria can focus on visible behavior. Production criteria must include regressions, tests, and maintainability boundaries.

## Stable Core

- done must be observable
- criteria should be written before implementation
- verification evidence is stronger than agent confidence

## Volatile Surface

- available test commands
- CI setup
- Codex report format
- surface-specific test-running support
- UI screenshot or browser capabilities

Review volatile details against official sources before freezing commands, UI labels, model advice, plan packaging, context limits, or feature availability.

## Obsolescence Watch

- Codex surfaces begin enforcing task-level acceptance criteria
- official Codex docs change verification recommendations
- team workflow moves from prompt criteria to formal issue templates or agent policy files

## Evidence and Sources

- `openai.codex.prompting` — Official OpenAI Codex prompting guidance for goals, context, success criteria, and interaction patterns.
- `openai.codex.workflows` — Official OpenAI Codex workflow examples for explicit context, done definitions, bug fixes, and tests.
- `openai.codex.use_cases.follow_goals` — Official OpenAI Codex use case for goal-following, constraints, validation, stopping, checkpoints, and proof.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable software-engineering practice, risk, and review discipline.

## Related Topics

- `vcb.chapter.acceptance_criteria`
- `vcb.prompting.four_part_prompt`
- `vcb.workflow.testing`
- `vcb.workflow.bug_repro`
- `vcb.concepts.test`
- `vcb.concepts.ci`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.prompting.acceptance_criteria -->
