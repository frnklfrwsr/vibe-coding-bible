<!-- VCB:BEGIN_TOPIC id=vcb.failure.ui_taste_gap version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex anchors, relevant vendor or named expert anchors
  where cited, and VCB maintainer synthesis for failure-mode control loops
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
id: vcb.failure.ui_taste_gap
title: UI Taste Gap
type: failure_mode
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex IDE Extension
- Computer Use
- Frontend apps
- Design systems
- Browser QA
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.eyeballing_ui
- vcb.shortcut.browser_clicking_without_repro
- vcb.shortcut.manual_testing_only
- vcb.shortcut.accepting_looks_done
durable_principles:
- frontend quality includes feel, state coverage, responsiveness, and accessibility
- browser evidence is stronger than compile success
- design-system reuse prevents visual drift
likely_to_change:
- Codex frontend use-case guidance
- browser automation tooling
- visual-regression tooling
- design-system conventions
- framework UI APIs
obsolete_when:
- agents can consistently infer product taste and verify visual quality across devices
  without explicit references
related_topics:
- vcb.workflow.frontend_work
- vcb.workflow.visual_qa
- vcb.workflow.accessibility_review
- vcb.concepts.frontend_backend
- vcb.failure.done_claim_without_evidence
---

> Summary:
> UI taste gap happens when generated frontend code technically works but feels generic, inconsistent, inaccessible, off-brand, poorly spaced, or incomplete across states and breakpoints.

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

<!-- VCB:BEGIN_SECTION id=vcb.failure.ui_taste_gap.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A UI can build and still be bad. Buttons can work while spacing feels wrong, empty states are missing, mobile breaks, loading states jump, or the design ignores the product’s visual language.

### Why it matters

Codex can produce usable UI quickly, but it may default to common patterns unless you give specific references, design-system rules, states, and browser evidence.

### The mental model

Frontend quality is not only “does it render?” It is “does it feel intentional in the real app?”

### What good looks like

Good: “Use existing design tokens and components. Match this screenshot’s hierarchy, check mobile/tablet/desktop, and report differences instead of inventing a new style.”

### What bad looks like

Bad: accepting a page because it compiles and has roughly the right fields.

### Minimal example

Ask Codex to name the evidence it used, the assumption it is making, the files it changed, and the verification that would catch this failure mode if it were wrong.

### Checklist

- existing components reused
- states covered
- responsive breakpoints checked
- visual reference compared
- accessibility basics reviewed
<!-- VCB:END_SECTION id=vcb.failure.ui_taste_gap.human -->

<!-- VCB:BEGIN_SECTION id=vcb.failure.ui_taste_gap.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to review frontend output against product feel, not just compile success.

### Diagnose the human’s current model

- What visual target exists?
- Which design tokens/components should be reused?
- What states are missing?
- Which breakpoints were checked?
- Is keyboard/accessibility behavior acceptable?

### Explanation strategy

Make Codex compare implementation against screenshots, component conventions, breakpoints, and state inventory. Require visual differences to be named.

### Useful metaphor

Frontend quality is not only “does it render?” It is “does it feel intentional in the real app?”

### Coaching tactics

- slow the human down at the first unsupported assumption
- ask for artifact-backed evidence instead of a verbal assurance
- separate read-only diagnosis from mutation
- require a smaller diff when review quality drops
- turn repeated misses into durable guidance only after the pattern is verified

### Prompt patterns

```text
Implement this UI using the repo’s existing component layer and tokens. Cover loading, empty, error, long-content, and mobile states. Run or describe browser checks at key breakpoints. Compare against the reference and list remaining visual differences.
```

### Red flags to call out directly

- new ad-hoc CSS duplicates tokens
- only happy path is implemented
- mobile layout untested
- accessibility language is vague
- screenshot comparison is replaced by “looks good”

### Exercises

- Ask the human to compare a generated UI against a reference and list hierarchy, spacing, state, and accessibility gaps.
- Ask the human to write one “stop condition” that would make Codex pause instead of pushing through.
- Review a previous agent diff and classify which evidence was missing.
<!-- VCB:END_SECTION id=vcb.failure.ui_taste_gap.ai_coach -->

## Shortcut Reality

### The ideal practice

Use real browser evidence, design-system reuse, state inventory, and screenshot or reference comparison.

### What users often do instead

Users eyeball the first render or accept a screenshot from the agent.

### When the shortcut may be fine

A rough UI is fine for internal prototypes when visual polish is explicitly out of scope.

### When the shortcut is a bad idea

It is a bad trade for customer-facing flows, onboarding, checkout, dashboards, accessibility-sensitive interfaces, or brand-critical pages.

### Risk profile

- Probability of failure: High for greenfield UI and vague design prompts.
- Impact if it fails: Medium to high: users may distrust or fail to use a technically working interface.
- Ease of recovery: Good with isolated components; poor when ad-hoc styling spreads.
- Blast radius: User trust, conversion, accessibility, responsive behavior, and design-system consistency.
- Skill needed to recover: Medium; recovery requires visual judgment and frontend architecture awareness.
- Hidden cost: Polish passes, design debt, duplicate components, and manual QA churn.

### Minimum guardrails

- visual target
- design-system rules
- state checklist
- breakpoint checks
- accessibility review

### Recovery plan

- Capture actual screenshots.
- Compare against target and tokens.
- List state/breakpoint gaps.
- Patch one component or state at a time.
- Add visual or browser checks where useful.

## Budget and Constraint Notes

### Cheapest reliable path

Ask for state inventory and one real browser screenshot before paying for repeated style passes.

### Fastest high-usage path

High-throughput users can iterate visually with browser tooling, but each pass needs a concrete difference list.

### Low-attention path

Low-attention UI work should be limited to drafts unless screenshots and state coverage are returned.

### Production-quality path

Production frontend work needs design-system reuse, browser evidence, state coverage, accessibility checks, and human visual review.

### Prototype versus production

Prototype UI may be generic. Production UI must match product language and critical user states.

### Maintenance phase

In maintenance, taste gaps become component debt. Fold repeated fixes back into shared components and tokens.

## Stable Core

- frontend quality includes feel, state coverage, responsiveness, and accessibility
- browser evidence is stronger than compile success
- design-system reuse prevents visual drift

## Volatile Surface

- Codex frontend use-case guidance
- browser automation tooling
- visual-regression tooling
- design-system conventions
- framework UI APIs

Review volatile details against official sources before freezing commands, UI labels, plan packaging, feature availability, model advice, package metadata, or exact tool behavior.

## Obsolescence Watch

- agents can consistently infer product taste and verify visual quality across devices without explicit references

## Evidence and Sources

- `openai.codex.use_cases.frontend_designs` — Official OpenAI Codex use case for screenshot/design context, design-system reuse, responsive checks, and browser verification.
- `openai.codex.use_cases.make_granular_ui_changes` — Official OpenAI Codex use case for targeted UI changes and browser-backed iteration.
- `playwright.docs.visual_comparisons` — Official Playwright documentation for screenshot/visual comparison behavior and caveats.
- `w3c.wai.web_accessibility_intro` — Official W3C WAI source for accessibility barriers and inclusive design framing.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable failure-mode, risk, review, budget, and recovery discipline.

## Related Topics

- `vcb.workflow.frontend_work`
- `vcb.workflow.visual_qa`
- `vcb.workflow.accessibility_review`
- `vcb.concepts.frontend_backend`
- `vcb.failure.done_claim_without_evidence`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.failure.ui_taste_gap -->
