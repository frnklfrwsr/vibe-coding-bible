<!-- VCB:BEGIN_TOPIC id=vcb.workflow.visual_qa version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
audiences:
- human
- ai_coach
source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: official OpenAI/Codex frontend QA anchors plus Playwright screenshot/visual-comparison
  vendor docs and VCB maintainer synthesis
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
id: vcb.workflow.visual_qa
title: Visual QA and Screenshot Review Workflow with Codex
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Computer Use
- Playwright
- Frontend apps
- Design reviews
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.browser_clicking_without_repro
- vcb.shortcut.eyeballing_ui
- vcb.shortcut.manual_testing_only
- vcb.shortcut.accepting_looks_done
durable_principles:
- visual QA needs a comparison target
- screenshots are evidence but not complete proof
- visual checks must be tied to routes, states, and viewports
likely_to_change:
- Playwright screenshot APIs
- browser automation support
- image-diff thresholds
- design-system tooling
- Codex Computer Use behavior
obsolete_when:
- visual correctness can be inferred reliably from code without rendering or screenshots
related_topics:
- vcb.chapter.frontend_work
- vcb.workflow.frontend_work
- vcb.workflow.accessibility_review
- vcb.workflow.testing
- vcb.codex.computer_use
---

> Summary:
> Visual QA uses screenshots, browser observations, and visual-diff checks to compare what Codex built against the intended UI instead of accepting vague visual confidence.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.visual_qa.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Visual QA means comparing the actual rendered UI against a target: screenshot, design, previous baseline, or written visual requirement.

### Why it matters

A frontend change can pass tests and still be visibly wrong. Visual QA catches spacing, overflow, broken responsive layout, missing states, and generic model-designed UI.

### The mental model

Visual QA is a before-and-after inspection. The code explains how the room was rearranged; the screenshot shows whether the furniture blocks the door.

### What good looks like

Good: “Compare /settings before and after at desktop and mobile widths. Focus on layout, overflow, alignment, missing icons, and button states. Report screenshot evidence and do not rewrite unrelated components.”

### What bad looks like

Bad: “Visually check it” with no target, viewport, route, or acceptance criteria.

### Minimal example

Provide current/target screenshots, route, viewport sizes, states to compare, allowed tolerance, and what not to redesign.

### Checklist

- target image or baseline exists
- route/state/viewport are named
- Codex reports what it opened
- visual findings are separated from functional bugs
- acceptable differences are noted
- unverified states are explicit
<!-- VCB:END_SECTION id=vcb.workflow.visual_qa.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.visual_qa.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to treat screenshots as structured evidence, not decorative attachments.

### Diagnose the human’s current model

- What is the visual source of truth?
- Are we comparing to a target or only judging taste?
- Which viewport matters most?
- Which visual differences are acceptable?
- Does the check cover interaction states?

### Explanation strategy

Convert subjective visual asks into comparison contracts. Require route, viewport, state, observed difference, severity, and recommended fix. Keep visual QA separate from broad redesign.

### Useful metaphor

A screenshot without a target is a mirror; a screenshot with criteria is a measuring tape.

### Coaching tactics

- ask for baseline and target
- label findings by severity
- avoid broad taste rewrites
- separate visual mismatch from functional failure
- turn repeated visual QA into a skill when stable

### Prompt patterns

```text
Open [route]. Compare against [target/baseline] at [viewports]. Check layout, spacing, typography, overflow, icons, focus/hover/disabled states, and long content. Return a table: state, expected, observed, severity, evidence, suggested fix. Do not change code until findings are summarized.
```

### Red flags to call out directly

- Codex redesigns instead of comparing
- only one viewport is checked for responsive work
- visual baseline is stale
- screenshots omit failing state
- image-diff threshold is tuned to ignore real changes

### Exercises

- Ask the human to define acceptable visual differences.
- Have them separate visual, functional, and copy defects from one screenshot.
- Review a screenshot report and find missing states.
<!-- VCB:END_SECTION id=vcb.workflow.visual_qa.ai_coach -->

## Shortcut Reality

### The ideal practice

Use screenshots or browser observations tied to a route, state, viewport, and target.

### What users often do instead

Users eyeball a single happy-path screenshot and accept the work.

### When the shortcut may be fine

Single-screenshot review is fine for rough mockups or a first pass at visual direction.

### When the shortcut is a bad idea

It is a bad trade for responsive layouts, production pages, accessibility-sensitive UI, onboarding, checkout, or changes near design-system primitives.

### Risk profile

- Probability of failure: Medium risk of hidden visual regressions; high risk when multiple breakpoints or states are involved.
- Impact if it fails: Impact ranges from polish debt to blocked user flows and trust loss.
- Ease of recovery: Good if the visual diff is small; poor if many style changes landed without baseline evidence.
- Blast radius: The blast radius is every route/state inheriting the changed style or component.
- Skill needed to recover: Low for screenshot capture; medium for deciding severity; high for fixing layout across breakpoints.
- Hidden cost: Repeated subjective rework, design-system drift, and brittle screenshot baselines.

### Minimum guardrails

- name visual source of truth
- check at least one narrow viewport for responsive UI
- separate report from mutation
- keep thresholds conservative
- record accepted differences

### Recovery plan

- Regenerate before/after screenshots.
- Isolate visual-only diff from behavior changes.
- Revert broad style churn.
- Patch highest-severity visual breaks.
- Add a reusable visual QA prompt or baseline.

## Budget and Constraint Notes

### Cheapest reliable path

Use manual screenshot comparison for one critical route/state/viewport and run the nearest build.

### Fastest high-usage path

Use browser automation or Playwright-style visual checks for repeated screens, but keep reports small and severity-ranked.

### Low-attention path

Low-attention visual QA must be report-only first. It should not auto-accept image diffs or broad restyling.

### Production-quality path

Production visual QA needs baseline/target evidence, responsive checks, severity triage, and human approval for subjective design changes.

### Prototype versus production

Prototype visual QA can use taste and speed. Production and maintenance work need stable baselines and explicit accepted deltas.

### Maintenance phase

In maintenance, screenshot churn is expensive. Prefer stable test data, small baselines, and visual checks only for high-value surfaces.

## Stable Core

- visual QA needs a comparison target
- screenshots are evidence but not complete proof
- visual checks must be tied to routes, states, and viewports

## Volatile Surface

- Playwright screenshot APIs
- browser automation support
- image-diff thresholds
- design-system tooling
- Codex Computer Use behavior

Review volatile details against official sources before freezing commands, UI labels, plan packaging, feature availability, model advice, package metadata, or exact tool behavior.

## Obsolescence Watch

- visual correctness can be inferred reliably from code without rendering or screenshots

## Evidence and Sources

- `openai.codex.use_cases.frontend_designs` — Official OpenAI Codex use case for translating screenshots/design briefs into responsive UI with visual checks.
- `openai.codex.use_cases.qa_computer_use` — Official OpenAI Codex use case for QA passes using Computer Use, structured repro steps, expected/actual results, and severity.
- `playwright.docs.visual_comparisons` — Official Playwright documentation for screenshot visual comparisons.
- `playwright.docs.screenshots` — Official Playwright documentation for screenshot capture.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, and review discipline.

## Related Topics

- `vcb.chapter.frontend_work`
- `vcb.workflow.frontend_work`
- `vcb.workflow.accessibility_review`
- `vcb.workflow.testing`
- `vcb.codex.computer_use`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.visual_qa -->
