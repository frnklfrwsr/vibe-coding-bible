<!-- VCB:BEGIN_TOPIC id=vcb.workflow.frontend_work version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex frontend and QA anchors plus MDN/Playwright
  vendor documentation and VCB maintainer synthesis
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
id: vcb.workflow.frontend_work
title: Frontend Verification Workflow with Codex
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex IDE Extension
- Codex Cloud
- Computer Use
- Browser QA
- Frontend apps
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.browser_clicking_without_repro
- vcb.shortcut.eyeballing_ui
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.ignoring_lint_typecheck
durable_principles:
- frontend work is not done until visible behavior is checked
- state matrices prevent happy-path-only UI
- browser evidence beats plausible code review for layout work
likely_to_change:
- Codex browser/computer-use availability
- framework commands
- Playwright or visual-check syntax
- design-system conventions
- viewport/device expectations
obsolete_when:
- frontend tooling can prove visual, responsive, state, and accessibility correctness
  automatically for the target project class
related_topics:
- vcb.chapter.frontend_work
- vcb.codex.computer_use
- vcb.workflow.visual_qa
- vcb.workflow.accessibility_review
- vcb.workflow.testing
- vcb.prompting.acceptance_criteria
- vcb.concepts.frontend_backend
---

> Summary:
> Frontend verification uses Codex to implement or review visible UI through states, screen sizes, interaction paths, and browser evidence instead of trusting code that merely compiles.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.frontend_work.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Frontend verification means checking what the user actually sees and touches: layout, text, forms, states, keyboard behavior, mobile layout, loading, empty, error, and success paths.

### Why it matters

Codex can create a screen that compiles and still feels broken. The defect may be spacing, overflow, missing empty states, invisible focus, or a mobile layout that collapses badly.

### The mental model

Treat frontend work like inspecting a staged room. The blueprint matters, but the room still needs a walkthrough under real lighting.

### What good looks like

Good: “Implement this dashboard header using the existing design tokens. Verify desktop and mobile, loading and empty states, keyboard focus, and run the nearest build or test. Report screenshots or observations and gaps.”

### What bad looks like

Bad: “Make it modern” with no target state, no browser check, no state matrix, and no constraint against inventing a new design system.

### Minimal example

Give Codex the route, target screenshot or design notes, existing component examples, forbidden changes, state matrix, viewport requirements, and done-when evidence.

### Checklist

- target route or component is named
- existing components/tokens are reused
- loading/empty/error/success states are checked
- mobile or narrow viewport is checked
- keyboard/focus basics are checked
- build/lint/test evidence is reported when available
<!-- VCB:END_SECTION id=vcb.workflow.frontend_work.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.frontend_work.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to evaluate frontend work by observable behavior, not by diff confidence.

### Diagnose the human’s current model

- What route or component changed?
- Which states matter for this feature?
- What existing component or token should be reused?
- Was a browser opened or only code inspected?
- What was not verified?

### Explanation strategy

Force a state matrix before implementation. Keep style, behavior, data fetching, and routing concerns separate. Require evidence from a browser, test, screenshot, or explicit “not verified” gap.

### Useful metaphor

A UI diff is the recipe; the browser check is tasting the dish.

### Coaching tactics

- ask for state matrix first
- reject generic “modern” language
- separate visual changes from behavior changes
- make Codex report exact route, viewport, and checks
- escalate accessibility/auth/billing flows to human review

### Prompt patterns

```text
Implement or review [route/component]. Reuse existing components/tokens. Cover loading, empty, error, success, disabled, mobile, keyboard, and long-content states. Do not change data fetching or routes unless requested. Run the nearest check and report evidence plus gaps.
```

### Red flags to call out directly

- Codex says “looks good” without route/viewport evidence
- new UI library appears in a visual-only task
- only the happy path was checked
- focus styles disappear
- mobile layout is not mentioned

### Exercises

- Ask the human to write a state matrix for a login page.
- Have them mark which states are production-blocking.
- Review a UI diff and identify hidden behavior changes.
<!-- VCB:END_SECTION id=vcb.workflow.frontend_work.ai_coach -->

## Shortcut Reality

### The ideal practice

Use a state matrix, browser verification, and targeted checks before accepting frontend work.

### What users often do instead

Users accept a screenshot, a summary, or code that compiles.

### When the shortcut may be fine

A shallow check is fine for throwaway prototypes, style experiments, or internal mockups with no merge path.

### When the shortcut is a bad idea

It is a bad trade for production UI, auth, checkout, onboarding, accessibility-sensitive flows, or anything where users can get blocked.

### Risk profile

- Probability of failure: Medium risk of visible regressions and high risk of missed edge states when verification is shallow.
- Impact if it fails: High when a broken screen blocks signup, purchase, support, or data entry.
- Ease of recovery: Good with small diffs and screenshots; poor when many UI changes stack without visual checkpoints.
- Blast radius: The blast radius is the set of routes, states, devices, and users affected by the unchecked UI.
- Skill needed to recover: Low for state matrices; medium for browser QA; high for diagnosing CSS/layout regressions in complex apps.
- Hidden cost: Future polish debt, accessibility fixes, support friction, and churn from subjective rework.

### Minimum guardrails

- state matrix
- route and viewport evidence
- no new UI dependency without approval
- nearest build/lint/test
- explicit verification gaps

### Recovery plan

- List changed routes/components.
- Capture current screenshots or observations.
- Check critical states and viewport.
- Revert unrelated style churn.
- Add a durable frontend checklist or prompt snippet.

## Budget and Constraint Notes

### Cheapest reliable path

Use one route, one narrow viewport, one happy path, and one failure/empty path. Run the cheapest local check that catches obvious breakage.

### Fastest high-usage path

High-throughput users can let Codex iterate with browser tooling, but require a compact evidence table per route/state.

### Low-attention path

Low-attention UI work is acceptable only for isolated branches and non-sensitive flows. It must return screenshots/observations, checks run, and gaps.

### Production-quality path

Production UI needs state coverage, browser evidence, relevant tests/builds, and human review for copy, accessibility, auth, billing, and data-loss flows.

### Prototype versus production

Prototype UI can optimize for learning and speed. Production and maintenance UI need regression awareness, design-system consistency, and repeatable checks.

### Maintenance phase

In maintenance, the main cost is not building the screen; it is keeping future changes from breaking old states. Prefer small UI diffs and reusable state-check prompts.

## Stable Core

- frontend work is not done until visible behavior is checked
- state matrices prevent happy-path-only UI
- browser evidence beats plausible code review for layout work

## Volatile Surface

- Codex browser/computer-use availability
- framework commands
- Playwright or visual-check syntax
- design-system conventions
- viewport/device expectations

Review volatile details against official sources before freezing commands, UI labels, plan packaging, feature availability, model advice, package metadata, or exact tool behavior.

## Obsolescence Watch

- frontend tooling can prove visual, responsive, state, and accessibility correctness automatically for the target project class

## Evidence and Sources

- `openai.codex.use_cases.frontend_designs` — Official OpenAI Codex use case for translating screenshots/design briefs into responsive UI with visual checks.
- `openai.codex.use_cases.qa_computer_use` — Official OpenAI Codex use case for QA passes using Computer Use, structured repro steps, expected/actual results, and severity.
- `openai.codex.use_cases.web_development` — Official OpenAI Codex web-development collection for responsive UI and browser verification workflows.
- `mdn.css.media_queries` — Official MDN documentation for media queries and responsive design conditions.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, and review discipline.

## Related Topics

- `vcb.chapter.frontend_work`
- `vcb.codex.computer_use`
- `vcb.workflow.visual_qa`
- `vcb.workflow.accessibility_review`
- `vcb.workflow.testing`
- `vcb.prompting.acceptance_criteria`
- `vcb.concepts.frontend_backend`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.frontend_work -->
