<!-- VCB:BEGIN_TOPIC id=vcb.workflow.accessibility_review version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex QA anchors plus W3C/WAI and Playwright accessibility-testing
  documentation with VCB maintainer synthesis
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
id: vcb.workflow.accessibility_review
title: Accessibility Review Workflow with Codex
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Computer Use
- Frontend apps
- Web QA
- Design reviews
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.manual_testing_only
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.checklist_theater
- vcb.shortcut.skipping_tests
durable_principles:
- accessibility is part of product behavior
- automated accessibility checks are useful but incomplete
- keyboard, labels, focus, and contrast need explicit attention
likely_to_change:
- WCAG versions and legal mappings
- framework accessibility patterns
- browser automation support
- axe/integration tooling
- product accessibility requirements
obsolete_when:
- UI frameworks automatically guarantee accessible output for all relevant user flows
related_topics:
- vcb.chapter.frontend_work
- vcb.workflow.frontend_work
- vcb.workflow.visual_qa
- vcb.workflow.testing
- vcb.safety.production_red_lines
---

> Summary:
> Accessibility review uses Codex to check whether UI can be perceived, navigated, understood, and operated by more people without pretending automated checks replace human judgment.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.accessibility_review.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Accessibility review checks whether people can use the interface with different devices, abilities, and assistive tools. Start with basics: semantic elements, labels, keyboard navigation, focus, contrast, errors, and readable copy.

### Why it matters

A UI can look polished and still be unusable for keyboard users, screen-reader users, low-vision users, or people with motor constraints.

### The mental model

Accessibility is not a badge at the end. It is part of whether the feature works.

### What good looks like

Good: “Review this form for accessible labels, keyboard path, focus visibility, error messages, contrast risks, and disabled-state clarity. Report findings by severity before editing.”

### What bad looks like

Bad: “Make it accessible” after the UI is already done, with no target flow and no verification.

### Minimal example

Name the route or component, user task, interactive elements, expected keyboard path, form/error states, and required checks.

### Checklist

- interactive elements have accessible names
- keyboard path reaches controls in logical order
- focus is visible
- form errors are understandable
- color is not the only signal
- contrast and responsive readability are checked
- automated checks do not replace human review
<!-- VCB:END_SECTION id=vcb.workflow.accessibility_review.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.accessibility_review.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to include accessibility in done criteria for UI work, especially forms and flows.

### Diagnose the human’s current model

- Can the flow be completed without a mouse?
- Do buttons and inputs have accessible names?
- Where does focus go after actions and errors?
- Is color carrying information alone?
- Which checks are automated and which are manual?

### Explanation strategy

Start report-only. Classify issues by user impact. Ask Codex to inspect semantics and keyboard flow before style polish. Separate WCAG/source guidance from local project conventions.

### Useful metaphor

Accessibility checks are door-width checks for software. A room can be beautiful and still inaccessible.

### Coaching tactics

- ask for keyboard walkthroughs
- force label and error-state review
- separate automated scan results from human-observed issues
- require severity and reproduction steps
- turn recurring a11y checks into AGENTS.md or a skill

### Prompt patterns

```text
Review [route/component] for accessibility. Report only first. Check keyboard navigation, visible focus, labels/names, form errors, contrast risks, semantic structure, disabled states, and screen-reader-risk areas. Include severity, user impact, evidence, and smallest fix. Do not claim full compliance unless verified by the project’s formal process.
```

### Red flags to call out directly

- Codex claims WCAG compliance from a quick scan
- custom div buttons replace semantic controls
- focus outline is removed
- errors are visual-only
- disabled controls have no explanation

### Exercises

- Ask the human to tab through a form and record failures.
- Have them identify accessible names for each control.
- Compare an automated scan with a manual keyboard pass.
<!-- VCB:END_SECTION id=vcb.workflow.accessibility_review.ai_coach -->

## Shortcut Reality

### The ideal practice

Include accessibility basics in acceptance criteria and review them before merge.

### What users often do instead

Users treat accessibility as optional polish or rely entirely on automated scans.

### When the shortcut may be fine

A narrow automated scan may be enough for an early prototype if the team records that accessibility was not fully reviewed.

### When the shortcut is a bad idea

It is a bad trade for production UI, public products, forms, auth, checkout, healthcare/finance/education flows, or government/regulated contexts.

### Risk profile

- Probability of failure: High risk of omissions when accessibility is not named explicitly.
- Impact if it fails: High because the feature may exclude users or create legal/compliance exposure.
- Ease of recovery: Medium when fixes are local; poor when inaccessible patterns are embedded in shared components.
- Blast radius: The blast radius is every user flow and shared component affected by inaccessible patterns.
- Skill needed to recover: Medium for basics; high for formal audits and assistive-technology-specific diagnosis.
- Hidden cost: Retrofit cost, user harm, legal exposure, and repeated component-level fixes.

### Minimum guardrails

- report-only accessibility pass first
- keyboard walkthrough
- labels/errors/focus checklist
- do not claim compliance casually
- human review for high-impact flows

### Recovery plan

- Identify shared inaccessible primitives.
- Patch keyboard/focus/name failures first.
- Add checks or lint rules where available.
- Document gaps and owner.
- Update reusable UI prompts.

## Budget and Constraint Notes

### Cheapest reliable path

Check keyboard path, labels, visible focus, and obvious contrast risks manually on the changed route.

### Fastest high-usage path

Use automated scanning and Codex triage to find easy issues quickly, then human-review severe findings.

### Low-attention path

Low-attention accessibility work should be report-only unless the flow is low-risk and fixes are local.

### Production-quality path

Production accessibility needs automated checks where useful, manual keyboard review, severity triage, and no casual compliance claims.

### Prototype versus production

Prototypes can note accessibility gaps. Production and maintenance work need to avoid baking inaccessible primitives into the design system.

### Maintenance phase

In maintenance, the cheapest path is fixing shared primitives and adding recurring checks, not patching the same label/focus defects page by page.

## Stable Core

- accessibility is part of product behavior
- automated accessibility checks are useful but incomplete
- keyboard, labels, focus, and contrast need explicit attention

## Volatile Surface

- WCAG versions and legal mappings
- framework accessibility patterns
- browser automation support
- axe/integration tooling
- product accessibility requirements

Review volatile details against official sources before freezing commands, UI labels, plan packaging, feature availability, model advice, package metadata, or exact tool behavior.

## Obsolescence Watch

- UI frameworks automatically guarantee accessible output for all relevant user flows

## Evidence and Sources

- `openai.codex.use_cases.qa_computer_use` — Official OpenAI Codex use case for QA passes using Computer Use, structured repro steps, expected/actual results, and severity.
- `w3c.wcag_overview` — Official W3C/WAI overview for WCAG standards and accessibility guidance.
- `w3c.wai.wcag22_quickref` — Official W3C/WAI quick-reference source for WCAG 2.2 success criteria and techniques.
- `playwright.docs.accessibility_testing` — Official Playwright documentation for accessibility testing with browser automation.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, and review discipline.

## Related Topics

- `vcb.chapter.frontend_work`
- `vcb.workflow.frontend_work`
- `vcb.workflow.visual_qa`
- `vcb.workflow.testing`
- `vcb.safety.production_red_lines`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.accessibility_review -->
