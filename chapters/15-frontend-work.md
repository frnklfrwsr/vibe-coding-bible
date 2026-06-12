<!-- VCB:BEGIN_TOPIC id=vcb.chapter.frontend_work version=0.1.0 -->
---
id: vcb.chapter.frontend_work
title: "Chapter 15 — Frontend Work: Screenshots, Browser Checks, and Taste"
type: chapter
chapter_number: 15
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-09-08'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex IDE Extension
- Codex CLI
- Codex Cloud
- Computer Use
- Browser checks
- Frontend UI
- Design systems

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
  surface: MODERATE
  pricing: STABLE

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
- emergency_hotfix

attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation

shortcut_profiles:
- vcb.shortcut.eyeballing_ui
- vcb.shortcut.vague_prompt
- vcb.shortcut.manual_testing_only
- vcb.shortcut.accepting_looks_done

durable_principles:
- Frontend quality is judged through visible behavior, not code alone.
- Screenshots and browser checks turn taste into evidence.
- UI work needs state coverage, not only the happy path.
- Visual changes should reuse existing components, tokens, and interaction patterns unless a redesign is explicit.

likely_to_change:
- Codex browser and Computer Use capabilities
- Codex UI-iteration surfaces and model-specific frontend behavior
- screenshot attachment mechanics
- browser automation integrations
- accessibility tooling and framework conventions

obsolete_when:
- Codex can reliably perform visual QA, responsive checks, accessibility checks, and state-matrix verification without explicit human constraints.
- Official Codex frontend workflows no longer rely on screenshots, browser checks, or user-specified visual constraints.

related_topics:
- vcb.chapter.acceptance_criteria
- vcb.chapter.feature_slicing
- vcb.chapter.context_management
- vcb.chapter.writing_updating_tests
- vcb.concepts.diff
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.workflow.frontend_work
- vcb.failure.ui_taste_gap
---

> Summary:
> Frontend work is not done because the code compiles. It is done when the visible behavior matches the target across important states, screen sizes, and interaction paths.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.frontend_work.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Frontend work is the part of software that people see and touch: pages, buttons, forms, spacing, colors, loading states, error messages, mobile layouts, and keyboard behavior.

Codex can write frontend code quickly. That does not mean it has taste. It can produce a working screen that is generic, misaligned, inaccessible, or inconsistent with the rest of your app.

For frontend work, the diff is not enough. You need visual evidence.

Think of UI as a conversation with the user. Copy is the words. Layout is the sentence structure. Spacing is grammar. If the grammar is bad, the user feels friction even if every button technically works.

### Why screenshots matter

A screenshot is a concrete target. Without one, “make this modern” usually becomes whatever pattern Codex has seen most often.

Useful inputs include:

- target screenshot,
- current screenshot,
- Figma frame or design export,
- existing component examples,
- design tokens,
- route or page URL,
- mobile and desktop expectations,
- loading, empty, error, success, disabled, and hover/focus states.

Bad input:

```text
Make this dashboard look modern.
```

Better input:

```text
Goal:
Improve the dashboard header so it looks closer to the attached screenshot.

Context:
- Current route: /dashboard
- Existing components: components/Card.tsx, components/Button.tsx
- Use existing spacing and color tokens from styles/theme.ts
- Target screenshot attached

Constraints:
- Do not change data fetching or routes
- Do not add new UI libraries
- Keep keyboard focus visible
- Preserve mobile layout

Done when:
- Header matches the screenshot direction
- Desktop and mobile screenshots are provided or described
- Loading, empty, and error states still render
- npm run build passes if available
```

### The state matrix

A state matrix is a checklist of what the UI must handle.

| State | Question |
|---|---|
| Loading | What does the user see before data arrives? |
| Empty | What if there is no data yet? |
| Error | What if the request fails? |
| Success | What does the normal path look like? |
| Disabled | Which actions are blocked and why? |
| Mobile | Does it work on a narrow screen? |
| Keyboard | Can a keyboard user reach and use controls? |
| Long content | What happens with long names, many cards, or overflowing text? |

For production UI, do not accept a screenshot of only the perfect happy path.

### Browser checks

Frontend changes need a browser check because layout bugs often hide from static code review.

Minimum browser check:

1. Start or reuse the dev server.
2. Open the changed route.
3. Check the changed state.
4. Check one narrow viewport.
5. Check one error or empty state if relevant.
6. Capture or describe what was verified.

When Codex cannot actually use a browser, it must say so. A claim like “visually verified” is not enough unless it includes what was opened and what changed.

### Good frontend work looks like

Good Codex frontend work:

- reuses existing components,
- follows existing design tokens,
- changes one visual concern at a time,
- keeps behavior and data flow unchanged unless requested,
- checks responsive layout,
- handles empty/loading/error states,
- runs a relevant build or lint check,
- reports what it could and could not verify.

Bad frontend work:

- adds a new component library without asking,
- rewrites layout architecture to fix spacing,
- hardcodes random colors and pixel values,
- only checks one browser width,
- ignores keyboard focus,
- deletes loading or error states,
- calls a UI “polished” without showing evidence.

### Minimal prompt: one visual change

```text
Make one focused UI change.

Change:
Increase the spacing between pricing cards and align their CTA buttons along the bottom.

Constraints:
- Do not change pricing logic or routes.
- Reuse existing Button and Card components.
- Do not add dependencies.
- Keep mobile stacking behavior.

Done when:
- Browser check confirms desktop and mobile layout.
- Report changed files and any visual states not checked.
```

### Checklist

Before accepting frontend work, ask:

- Did I provide a visual target or concrete visual constraints?
- Did Codex use existing components and tokens?
- Did it check the browser or clearly say it could not?
- Did it cover loading, empty, error, success, disabled, and mobile where relevant?
- Did it avoid new dependencies unless approved?
- Did I review the diff for unrelated behavior changes?

<!-- VCB:END_SECTION id=vcb.chapter.frontend_work.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.frontend_work.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that frontend acceptance is evidence-based. The goal is not “pretty enough”; the goal is “matches the intended visual behavior across the states that matter.”

### Diagnose the human’s current model

Ask:

- Do they have a screenshot, design, existing component, or target example?
- Are they asking for “modern,” “clean,” or “better” without constraints?
- Is this prototype UI, production UI, conversion-critical UI, or accessibility-sensitive UI?
- Are they checking only one happy path?
- Does Codex have access to a browser, screenshot attachment, or visual QA tool?

### Explanation strategy

Use this sequence:

1. Convert visual preference into concrete constraints.
2. Identify the UI states that matter.
3. Keep the patch small.
4. Require a browser or screenshot check.
5. Review the diff for unintended behavior changes.

Do not over-police throwaway prototypes. Do push hard on production flows, auth forms, checkout, onboarding, dashboards with real customers, and accessibility requirements.

### Useful metaphors

- **UI is a conversation.** Layout controls pacing; copy controls tone; states handle interruptions.
- **Spacing is grammar.** Bad spacing makes the page feel wrong even if every sentence is technically there.
- **A screenshot is the measuring stick.** Without it, Codex guesses what “modern” means.
- **The state matrix is weather testing.** Sunny-day UI is not enough; test rain, wind, and darkness.

### Coaching tactics

When the user says “make it look better,” respond with a narrowing move:

```text
That request is underspecified. Give Codex a visual target. Minimum useful target: one screenshot, the changed route, which components to reuse, and which states must still work.
```

When the user wants speed:

```text
Do one visual note per patch. That keeps the diff reviewable and makes browser checks cheaper.
```

When the work touches production:

```text
Require a state matrix, browser evidence, build/lint if available, and a final report that names unchecked states.
```

### Prompt patterns

#### Screenshot-to-implementation prompt

```text
Use the attached screenshot as the visual target.

Inspect the existing UI patterns first.
Then implement the smallest patch that moves this route toward the screenshot.

Constraints:
- reuse existing components and tokens,
- no new UI dependency,
- do not change API/data behavior,
- preserve mobile behavior,
- keep focus states visible.

Done when:
- browser check covers desktop and mobile,
- changed files are listed,
- unchecked states are listed,
- build/lint result is reported if available.
```

#### State-matrix prompt

```text
Before editing, list the frontend states this screen must support:
loading, empty, error, success, disabled, mobile, keyboard, and long-content cases.
Then patch only the states relevant to this change.
```

### Red flags to call out directly

- “Make it modern” with no visual target.
- New UI library for a small styling problem.
- One giant redesign diff.
- No browser evidence.
- Loading/error states disappeared.
- Hardcoded colors instead of tokens.
- Accessibility dismissed as polish.
- Mobile not checked.

### Exercises

1. Ask the human to provide one screenshot and one current route, then turn that into a four-part prompt.
2. Ask the human to name three states beyond the happy path.
3. Review a UI diff and mark every line that changes behavior rather than presentation.

<!-- VCB:END_SECTION id=vcb.chapter.frontend_work.ai_coach -->

## Shortcut Reality

### The ideal practice

Provide a target screenshot or design reference, define the state matrix, make a small patch, verify in a browser, and review the diff.

### What users often do instead

They ask Codex to “make it modern,” accept the first version that looks okay, and skip mobile, error, loading, empty, disabled, and keyboard states.

### When the shortcut may be fine

Eyeballing UI may be acceptable for:

- disposable prototypes,
- throwaway landing pages,
- internal sketches,
- personal demos,
- early design exploration with fake data.

### When the shortcut is a bad idea

Eyeballing is not enough for:

- production onboarding,
- checkout/payment flows,
- auth flows,
- accessibility-sensitive products,
- conversion-critical pages,
- design-system components,
- enterprise or regulated UI,
- mobile-heavy products.

### Risk profile

- Probability of failure: medium.
- Impact if it fails: low in prototypes; high in production flows.
- Ease of recovery: medium if committed and scoped; low if a broad redesign lands without checkpoints.
- Blast radius: one route if scoped; whole app if shared components or tokens are changed carelessly.
- Skill needed to recover: low for CSS tweaks; medium/high for component architecture or design-system regressions.
- Hidden cost: repeated “almost right” iterations can burn more usage than a precise screenshot and state matrix.

### Minimum guardrails

- Commit or branch before the UI pass.
- Provide one visual target.
- Limit Codex to specific files or components when possible.
- Require desktop and mobile check.
- Name unchecked states.
- Do not add UI dependencies without approval.
- Do not change data flow unless requested.

### Recovery plan

If the UI pass goes wrong:

1. Inspect the diff for shared component, token, route, and data-flow changes.
2. Revert or isolate broad component changes first.
3. Keep only the smallest useful visual patch.
4. Re-run the changed route in the browser.
5. Add a clearer visual target and state matrix before retrying.

### AI coach guidance

Do not argue about taste in abstract terms. Convert taste into evidence: screenshots, tokens, states, browser checks, and before/after comparisons.

## Budget and Constraint Notes

### Cheapest reliable path

Use one screenshot or one route, one focused visual change, and one browser check. Avoid broad redesign prompts and avoid new dependencies.

### Fastest high-usage path

Run a short design exploration in an isolated branch, then choose one direction and ask Codex to harden it with browser checks and state coverage.

### Low-attention path

Low-attention frontend work must return artifacts: changed route, screenshots or browser-check notes, state matrix status, checks run, and known gaps. Do not let low-attention UI work mutate shared components broadly.

### Production-quality path

Require responsive checks, state coverage, accessibility basics, no unintended behavior changes, diff review, and staging or preview validation for critical flows.

## Stable Core

- Visual acceptance criteria beat vague aesthetic requests.
- Reuse project patterns before inventing new UI systems.
- Browser checks catch bugs code review misses.
- State coverage prevents happy-path-only UI.
- Accessibility and keyboard behavior are functionality, not decoration.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
- exact screenshot attachment mechanics,
- Codex browser/Computer Use capabilities,
- current frontend-specific models or UI-iteration features,
- live preview and pop-out-window behavior,
- browser automation integrations,
- plan access to any fast UI iteration surface.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when:

- Codex frontend workflows change materially,
- Computer Use/browser verification changes,
- official docs introduce native state-matrix or accessibility review features,
- current fast-UI model or surface advice changes,
- screenshot and Figma ingestion mechanics change.

## Evidence and Sources

- Official OpenAI Codex web-development and workflow docs currently support using screenshots, visual references, browser verification, and small focused UI iteration: `openai.codex.use_cases.web_development`, `openai.codex.use_cases.frontend_designs`, `openai.codex.use_cases.make_granular_ui_changes`, `openai.codex.workflows`.
- Official OpenAI Computer Use QA guidance supports browser/flow testing that returns repro steps, expected result, actual result, severity, and triage summary: `openai.codex.use_cases.qa_computer_use`.
- The state-matrix, taste, and accessibility framing is maintainer synthesis from stable frontend engineering practice: `vcb.synthesis.stable_engineering_practice`.

## Related Topics

- `vcb.chapter.acceptance_criteria`
- `vcb.chapter.context_management`
- `vcb.chapter.feature_slicing`
- `vcb.chapter.writing_updating_tests`
- `vcb.concepts.diff`
- `vcb.concepts.blast_radius`
- `vcb.concepts.recoverability`
- `vcb.workflow.frontend_work`
- `vcb.failure.ui_taste_gap`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.frontend_work -->
