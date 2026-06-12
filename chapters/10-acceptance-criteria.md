<!-- VCB:BEGIN_TOPIC id=vcb.chapter.acceptance_criteria version=0.1.0 -->
---
id: vcb.chapter.acceptance_criteria
title: "Chapter 10 — Acceptance Criteria: The Difference Between “Looks Done” and Done"
type: chapter
chapter_number: 10
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
- CI
- tests
- manual verification
- production release workflows

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
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.manual_testing_only
- vcb.shortcut.skipping_tests

durable_principles:
- Done must be observable, not just asserted.
- Acceptance criteria define what behavior, checks, states, and constraints must be true before accepting Codex output.
- Command output, tests, diffs, screenshots, and manual repros are evidence; final summaries are claims.
- Acceptance criteria should scale with project risk and recoverability.

likely_to_change:
- Goal mode completion behavior
- native acceptance-check or eval features
- product-specific review UI and command names
- model-specific self-evaluation reliability

obsolete_when:
- Codex can consistently determine production readiness without explicit acceptance criteria, checks, or human review.
- Official Codex guidance no longer requires clear completion criteria or verification for serious tasks.

related_topics:
- vcb.chapter.four_part_prompt
- vcb.chapter.plan_first_code_second
- vcb.chapter.context_management
- vcb.chapter.git_discipline
- vcb.concepts.diff
- vcb.concepts.recoverability
- vcb.prompting.acceptance_criteria
- vcb.workflow.testing
- vcb.workflow.reviewing_diffs
---

> Summary:
> Acceptance criteria turn “looks done” into observable proof: behavior, checks, states, constraints, and final evidence.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.acceptance_criteria.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Acceptance criteria are the conditions that must be true before you accept Codex’s work.

“Looks done” means the output appears plausible. “Done” means the behavior was checked against explicit criteria.

A Codex final message might say:

```text
Implemented the feature and all tests pass.
```

That is not enough. You need evidence:

- What files changed?
- What behavior changed?
- What tests or checks ran?
- What command output proves it?
- What did not get tested?
- What risks remain?

### The mental model

Acceptance criteria are the finish line. Without a finish line, Codex may stop when the code looks plausible, not when the product works.

Use this sentence:

```text
Done is not a mood. Done is a set of observable facts.
```

### Types of acceptance criteria

| Type | Example |
|---|---|
| Behavioral | “A user can reset a password with a valid token and cannot reuse the token.” |
| Technical | “`pnpm test auth` and `pnpm typecheck` pass.” |
| UX state | “Loading, empty, error, success, disabled, and mobile states exist.” |
| Security | “No secret is logged; invalid tokens fail safely.” |
| Performance | “The page does not add an extra request per row in the table.” |
| Compatibility | “Existing API response shape is unchanged.” |
| Negative constraint | “Do not add dependencies or change billing calculation logic.” |
| Evidence/report | “Final report lists files changed, checks run, known gaps, and risks.” |

### Bad acceptance criteria versus better criteria

Bad:

```text
Make checkout work.
```

Better:

```text
Done when:
- successful card payment creates exactly one order,
- failed payment shows a safe error and creates no order,
- duplicate webhook delivery does not double-charge or duplicate the order,
- existing checkout tests pass,
- no secret values appear in logs,
- final report includes files changed and checks run.
```

The better criteria are stricter because checkout has real money and user trust attached.

### Acceptance criteria by risk level

| Project context | Minimum reasonable criteria |
|---|---|
| Throwaway prototype | launches locally and demonstrates the intended behavior |
| Personal tool | exact path manually checked and changes committed |
| MVP | critical flows manually checked; build/typecheck/test if available |
| Public app | automated checks, manual critical path, diff review, rollback path |
| Auth/payment/data-sensitive | tests, security review, no real-secret exposure, rollback/backout plan, monitoring expectations |

### Final report expectations

Ask Codex to end with:

```text
Final report:
- Summary of behavior changed
- Files changed
- Tests/checks run with command output summary
- Manual checks performed
- Known gaps
- Risks or follow-up work
- Rollback notes
```

If Codex says something passed, ask for the command and result. If it did not run a check, it should say so.

### Acceptance criteria are not all automated

Some things need human judgment: UI taste, copy, accessibility nuance, user flow, and product fit. That does not mean “vibes only.” It means you need observable human checks: screenshot comparison, state matrix, keyboard navigation, or manual repro steps.
<!-- VCB:END_SECTION id=vcb.chapter.acceptance_criteria.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.acceptance_criteria.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to define “done” before accepting Codex output and to treat final summaries as claims that require evidence.

### Diagnose the human’s current model

Watch for:

- “It works” without saying what was tested.
- “Codex said tests passed” without command output.
- “Looks good” for production UI with no state checks.
- “Ship it” after a broad diff.
- “Done” before reviewing changed files.
- Criteria that only cover the happy path.

### Explanation strategy

Turn vague completion into an evidence contract.

Ask:

```text
What must be true for a user?
What must not change?
What command or manual flow proves it?
What failure states must be handled?
What evidence should Codex report at the end?
```

Then write those as acceptance criteria.

### Useful metaphors

- **Finish line:** the runner does not decide the race is over because they feel tired.
- **Inspection checklist:** the building is not done until it passes inspection.
- **Receipt versus evidence:** Codex’s final message is a receipt; checks and diff are the evidence.

### Coaching tactics

When the user says “done,” ask for evidence:

```text
What changed, what check proved it, and what remains unverified?
```

If the user is trying to accept a risky patch without checks:

```text
This touches a high-blast-radius area. Accepting “looks done” is not a good trade. Define the critical checks and run at least the smallest relevant one before accepting.
```

If no tests exist, do not pretend they do:

```text
There may be no automated tests here. The minimum criteria are a manual exact-flow check, build/typecheck if available, and a small diff review.
```

### Prompt patterns

Acceptance block:

```text
Done when:
- [observable behavior]
- [negative case]
- [state or edge case]
- [test/check command]
- [no-change constraint]
- final report includes files changed, checks run, gaps, and risks.
```

Evidence-demand prompt:

```text
Do not just say the task is done.
Show:
- changed files,
- checks run and results,
- behavior verified,
- what you did not verify,
- remaining risks.
```

Acceptance-criteria repair prompt:

```text
Convert this vague request into acceptance criteria before implementation.
Include behavior, edge cases, do-not-change rules, checks, and final report requirements.
```

### Red flags to call out directly

- Criteria only say “works.”
- Criteria have no negative cases.
- Criteria omit tests/checks for production paths.
- Criteria omit UI states for user-facing work.
- Criteria omit security/privacy constraints for auth, payments, files, or data.
- Codex reports success without proof.
- The user wants unattended work but has no stopping rule.

### Exercises

Take these requests and write acceptance criteria:

1. “Improve onboarding.”
2. “Fix webhook retries.”
3. “Make it mobile friendly.”
4. “Add delete account.”
5. “Speed up the dashboard.”

For each, include at least one negative case and one verification method.
<!-- VCB:END_SECTION id=vcb.chapter.acceptance_criteria.ai_coach -->

## Shortcut Reality

### The ideal practice

Define acceptance criteria before implementation and verify against them before accepting Codex output.

### What users often do instead

They accept the patch because it looks plausible, compiles once, or matches Codex’s final summary.

### When the shortcut may be fine

Accepting “looks done” may be fine for:

- throwaway demos,
- local-only prototypes,
- visual sketches,
- tiny copy or styling changes,
- work that will be reviewed later before real use.

### When the shortcut is a bad idea

It is a bad trade for:

- production code,
- auth, payments, webhooks, migrations, data deletion,
- user-facing flows with failure states,
- security-sensitive changes,
- broad diffs,
- unattended agent work.

### Risk profile

- Probability of failure: medium; high when only happy path was checked.
- Impact if it fails: low for demos, high for real users/data/money.
- Ease of recovery: high with a branch/checkpoint; low after deployment or data changes.
- Blast radius: hidden until edge cases appear.
- Skill needed to recover: medium to high for production regressions.
- Hidden cost: latent bugs, customer trust loss, rework, and false confidence.

### Minimum guardrails

- Define at least one observable behavior criterion.
- Add one negative/edge case.
- Run the smallest relevant check.
- Review changed file names and diff scope.
- Ask Codex to list unverified items.
- Do not skip stronger checks for auth, payments, migrations, secrets, or data deletion.

### Recovery plan

If “looks done” failed later:

1. Reproduce the failure.
2. Identify which acceptance criterion was missing.
3. Add that criterion to the task.
4. Patch with a regression check if feasible.
5. Update durable guidance if this class of miss repeats.

### AI coach guidance

Do not argue abstractly. Name the missing proof:

```text
This may be done, but we have not proved it. The minimum proof is the exact user flow plus the smallest relevant command check. For this risk level, accepting the summary alone is not enough.
```

## Budget and Constraint Notes

### Cheapest reliable path

Use one or two critical acceptance criteria and the smallest relevant check. For low-risk work, a manual exact-flow check plus diff review can be enough.

### Fastest high-usage path

Let Codex generate a full criteria list, implement, run checks, and self-review against the criteria. For hard tasks, use a second agent to review whether the evidence actually satisfies the criteria.

### Low-attention path

Low-attention work must have explicit stop rules and evidence requirements. Codex should not continue indefinitely under “make it better.” It should report progress, blockers, checks, and gaps.

### Production-quality path

Production criteria should include behavior, failure cases, security/privacy constraints, compatibility, tests/checks, monitoring/rollback expectations, and final review before merge or deploy.

## Stable Core

- Done must be observable.
- Final summaries are claims, not proof.
- Acceptance criteria should include positive behavior, edge/negative cases, constraints, and evidence.
- The strength of criteria should scale with blast radius and recoverability.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-12-08 source_required=true -->

Volatile items:

- Goal mode,
- native completion criteria features,
- product-specific review commands,
- model self-evaluation reliability,
- CI/test integration behavior.

Use official OpenAI docs before writing exact current product instructions.

<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when:

- OpenAI changes official guidance around goals, completion criteria, testing, review, or stopping rules,
- Codex adds native acceptance-check features,
- product surfaces change how command output, diff review, or completion reports are displayed,
- future evidence workflows replace manual final-report patterns.

## Evidence and Sources

- `openai.codex.best_practices` — official current anchor for tests, checks, confirming behavior, and reviewing diffs before accepting work.
- `openai.codex.prompting` — official current anchor for goal text acting as both starting prompt and completion criteria.
- `openai.codex.follow_goals` — official current anchor for validation, stopping conditions, checkpoints, and proof of progress.
- `openai.codex.iterate_difficult_problems` — official current anchor for evals, explicit stopping rules, running logs, and artifact inspection in harder loops.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for acceptance criteria categories, evidence contracts, and harm-reduction review posture.

## Related Topics

- `vcb.chapter.four_part_prompt`
- `vcb.chapter.plan_first_code_second`
- `vcb.chapter.context_management`
- `vcb.chapter.git_discipline`
- `vcb.concepts.diff`
- `vcb.concepts.recoverability`
- `vcb.prompting.acceptance_criteria`
- `vcb.workflow.testing`
- `vcb.workflow.reviewing_diffs`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.acceptance_criteria -->
