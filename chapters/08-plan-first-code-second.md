<!-- VCB:BEGIN_TOPIC id=vcb.chapter.plan_first_code_second version=0.1.0 -->
---
id: vcb.chapter.plan_first_code_second
title: 'Chapter 8 — Plan First, Code Second'
type: chapter
chapter_number: 8
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-12-08'
review_cadence: semiannual

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- AI coach workflows

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
- major_refactor
- emergency_hotfix

attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation

shortcut_profiles:
- vcb.shortcut.skipping_plan
- vcb.shortcut.one_big_prompt

durable_principles:
- Complex or risky tasks should be planned before editing files.
- A useful plan names files, milestones, risks, checks, and rollback strategy.
- Planning should reduce uncertainty, not become performative delay.
- Small safe edits can skip formal planning when the blast radius is tiny.

likely_to_change:
- Plan mode UI and keyboard shortcuts
- execution-plan file conventions
- model-specific planning quality
- future native planning or project-management features

obsolete_when:
- Codex can reliably perform broad, ambiguous, risky implementation work without an explicit plan and still produce reviewable diffs and safe rollback paths.
- Official Codex planning guidance materially changes away from planning before complex or ambiguous tasks.

related_topics:
- vcb.chapter.four_part_prompt
- vcb.chapter.context_management
- vcb.chapter.acceptance_criteria
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.chapter.git_discipline
- vcb.prompting.plan_first
- vcb.shortcut.skipping_plan
---

> Summary:
> Planning first turns broad Codex work into inspectable milestones. It is most valuable when the task is ambiguous, multi-file, risky, or hard to undo.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.plan_first_code_second.human -->
## 1. For the Human: Plain-Language Concept

### What this means

“Plan first, code second” means Codex should inspect and propose the route before it starts changing files.

You are not asking for a philosophical essay. You are asking for an implementation map:

- which files are likely involved,
- what the current behavior is,
- what the smallest safe milestone is,
- what risks exist,
- what checks will prove the change,
- what rollback path exists,
- what should cause Codex to stop.

A plan is a map before a hike. You can still change the route when you see the terrain, but starting without a map is a bad idea when the trail crosses cliffs.

### When to plan first

Plan first when the task is:

| Task shape | Why planning matters |
|---|---|
| Broad | The diff can become too large to review. |
| Ambiguous | Codex will guess product intent. |
| Multi-file | Changes can cross hidden boundaries. |
| Risky | Auth, payments, data, secrets, migrations, or deploy config can fail badly. |
| Unfamiliar codebase | Codex needs to inspect before estimating or editing. |
| Long-running | Codex needs checkpoints and stop rules. |
| Low-attention | You need stronger boundaries before leaving it alone. |

For a spelling fix, a small copy change, or one obvious CSS tweak, a formal plan is overkill. Use judgment.

### What a good plan includes

A good Codex plan is specific enough to review before code exists.

```text
Plan only. Do not edit files.

Goal:
[task]

Your plan must include:
- files likely affected,
- current data flow or behavior,
- implementation steps in small milestones,
- risks and assumptions,
- tests/checks to run,
- rollback strategy,
- questions only if truly blocked.
```

Bad plan:

```text
1. Update the frontend.
2. Add backend logic.
3. Test everything.
```

Better plan:

```text
1. Inspect `app/settings/page.tsx`, `components/forms/ProfileForm.tsx`, and `lib/user.ts`.
2. Confirm how profile updates currently call the API.
3. Add validation only inside the existing form component.
4. Preserve the API payload shape.
5. Add or update a form validation test.
6. Run the profile-form test and typecheck.
7. Roll back by reverting this branch if validation changes break existing updates.
```

The better plan tells you where the work will happen and how to judge it.

### How to review a plan

Before approving implementation, ask:

- Does the plan start by inspecting real files?
- Does it name specific files or areas?
- Does it preserve behavior that must not change?
- Does it split the work into reviewable milestones?
- Does it identify risky areas?
- Does it define tests or checks?
- Does it have a rollback path?
- Is it too broad for one diff?

If a plan is generic, reject it. Generic plans create false confidence.

### Turn plans into milestones

A milestone is one reviewable step. It should have a check attached.

```text
Milestone 1: Add server-side validation only.
Check: existing API tests pass.

Milestone 2: Show validation errors in UI.
Check: manual form flow and component tests pass.

Milestone 3: Add empty/error/loading states.
Check: screenshot or browser verification.
```

This makes Codex work like a careful builder, not a gambler.

### Plans do not replace judgment

A plan can be wrong. It is still useful because it exposes assumptions early. If Codex’s plan ignores auth, data migration, rollback, tests, or existing patterns, you caught the problem before it edited files.
<!-- VCB:END_SECTION id=vcb.chapter.plan_first_code_second.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.plan_first_code_second.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to request a plan before risky edits and to reject vague plans. The goal is bounded implementation, not planning theater.

### Diagnose the human’s current model

The human may think planning is slow. Reframe it as speed control. A short plan can prevent a long cleanup.

Watch for these phrases:

- “Just build it.”
- “Refactor this whole thing.”
- “Can Codex handle this while I’m away?”
- “Migrate us to X.”
- “Fix all the tests.”
- “Clean up the architecture.”

Those are plan-first triggers.

### Explanation strategy

Use the risk gate:

```text
Small, obvious, reversible: code first is acceptable.
Broad, ambiguous, irreversible, or production-sensitive: plan first.
```

Teach that planning is not a universal virtue. It is a tool for reducing uncertainty before the model can create a large diff.

### Useful metaphors

- **Measure twice, cut once:** planning is cheaper than recutting every board.
- **Flight checklist:** routine when risk is high; unnecessary for tying your shoes.
- **Construction permit:** the point is not paperwork; the point is avoiding hidden structural damage.

### Coaching tactics

When the user asks for broad implementation, respond with a plan-only step before code:

```text
This is too broad to edit safely in one pass. First ask Codex for a plan-only pass with files, risks, checks, and rollback. Then approve the first milestone only.
```

If the user is budget-constrained, keep the plan short:

```text
Give a compact plan in 10 bullets or fewer. Do not edit files yet.
```

If the user wants unattended work, require checkpoints:

```text
Work in milestones. After each milestone, run the named check and update a short progress log. Stop if a check fails twice, if you need secrets, or if the diff expands outside the named files.
```

### Prompt patterns

Plan-only prompt:

```text
Plan only. Do not edit files.
Inspect the relevant files first.
Return:
1. current behavior,
2. files likely affected,
3. smallest safe milestone,
4. implementation steps,
5. risks and unknowns,
6. tests/checks,
7. rollback path.
```

Plan critique prompt:

```text
Review this plan before implementation.
Call out vague steps, missing files, missing checks, hidden risk, dependency creep, and rollback gaps.
Then rewrite it as smaller milestones.
```

### Red flags to call out directly

- The plan says “test everything” but names no checks.
- The plan starts editing before inspecting.
- The plan touches many domains at once.
- The plan adds dependencies without justification.
- The plan omits rollback for migrations or deployment changes.
- The plan is longer than the task but less specific than the codebase.

### Exercises

Give the human three tasks and ask whether each needs a plan:

1. Fix a typo in a label.
2. Add password reset.
3. Replace the ORM.

Then ask what changes the answer: project phase, real users, tests, rollback, and attention level.
<!-- VCB:END_SECTION id=vcb.chapter.plan_first_code_second.ai_coach -->

## Shortcut Reality

### The ideal practice

Plan before complex, ambiguous, high-risk, or multi-file edits.

### What users often do instead

They skip the plan because planning feels slower than asking Codex to start coding.

### When the shortcut may be fine

Skipping the plan can be fine for:

- tiny low-risk edits,
- local-only prototypes,
- disposable experiments,
- one-file changes with obvious behavior,
- supervised sessions where the human will stop bad scope creep quickly.

### When the shortcut is a bad idea

Skipping the plan is a bad trade for:

- migrations,
- auth or payments,
- production bugs,
- large refactors,
- unknown codebases,
- long unattended work,
- changes touching persistent data or secrets.

### Risk profile

- Probability of failure: low for small edits; high for broad ambiguous work.
- Impact if it fails: grows with project risk and diff size.
- Ease of recovery: high with branch/checkpoint; low with mixed unrelated edits.
- Blast radius: often unknown until Codex has already changed files.
- Skill needed to recover: medium to high if architecture/data changes are involved.
- Hidden cost: generic plans, duplicated work, and fragile patches.

### Minimum guardrails

If skipping a formal plan:

- make the diff small,
- commit first,
- name forbidden files/areas,
- require Codex to stop before sensitive changes,
- run at least one relevant check,
- ask for a final risk list.

### Recovery plan

If skipping the plan caused a messy diff:

1. Stop implementation.
2. Ask Codex to summarize the current diff by intent.
3. Revert unrelated or speculative edits.
4. Ask for a plan-only pass from the cleanest recoverable state.
5. Re-implement one milestone at a time.

### AI coach guidance

Do not say “always plan.” Say:

```text
This task is broad enough that code-first is likely to produce an unreviewable diff. The fast version is not no-plan; it is a short plan and then the first milestone only.
```

## Budget and Constraint Notes

### Cheapest reliable path

Use one compact plan-only pass. Do not ask for multiple alternatives unless the choice is genuinely important. Approve only the smallest safe milestone.

### Fastest high-usage path

Run one implementation plan and one independent plan critique, then choose the smallest coherent path. Parallel planning can be useful when the cost of a bad path is high.

### Low-attention path

Do not leave Codex alone without a plan. Require checkpoints, stop rules, forbidden areas, and a progress log.

### Production-quality path

Production planning should name affected systems, compatibility constraints, test strategy, deployment/rollback path, observability, and review steps. A production plan that lacks rollback is incomplete.

## Stable Core

- Planning is most valuable when uncertainty, blast radius, or irreversibility is high.
- A useful plan contains file-level specificity, risks, checks, and rollback.
- Generic plans should be rejected before implementation.
- Planning should scale down for small low-risk work.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-12-08 source_required=true -->

Volatile items:

- Codex Plan mode mechanics,
- keyboard shortcuts and UI controls,
- execution-plan templates,
- model planning quality,
- future Codex project-management features.

Use official OpenAI docs before writing exact command or UI instructions.

<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when:

- official Codex planning guidance changes,
- Plan mode behavior or controls change,
- execution-plan docs change,
- Codex starts enforcing milestones or acceptance criteria natively.

## Evidence and Sources

- `openai.codex.best_practices` — official current anchor for planning first on complex, ambiguous, or hard-to-describe tasks.
- `openai.codex.prompting` — official current anchor for using planning when a goal is hard to define up front.
- `openai.codex.follow_goals` — official current anchor for defining objective, validation, checkpoints, and stopping conditions.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for milestone planning, risk gating, and plan review heuristics.

## Related Topics

- `vcb.chapter.four_part_prompt`
- `vcb.chapter.context_management`
- `vcb.chapter.acceptance_criteria`
- `vcb.concepts.blast_radius`
- `vcb.concepts.recoverability`
- `vcb.chapter.git_discipline`
- `vcb.prompting.plan_first`
- `vcb.shortcut.skipping_plan`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.plan_first_code_second -->
