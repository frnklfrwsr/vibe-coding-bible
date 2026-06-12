<!-- VCB:BEGIN_TOPIC id=vcb.chapter.failure_modes_codex_work version=0.1.0 -->
---
id: vcb.chapter.failure_modes_codex_work
title: "Chapter 32 — Failure Modes: How Codex Work Goes Wrong"
type: chapter
chapter_number: 32
version: 0.1.0
last_verified: '2026-06-09'
next_review_due: '2026-09-09'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub PR review
- security review
- tests
- CI
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
  surface: STABLE
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
- vcb.shortcut.ignoring_failure_mode
- vcb.shortcut.treating_symptom_as_root_cause
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.skipping_tests
- vcb.shortcut.broad_refactor

durable_principles:
- Most Codex failures have recognizable shapes.
- A failure mode should map to a control, not a vague warning.
- The right correction depends on blast radius and recoverability.

likely_to_change:
- model-specific failure rates
- new Codex review/security surfaces
- context window and compaction behavior
- product-specific validation tools

obsolete_when:
- Codex failure patterns materially change or official evaluation guidance replaces this taxonomy.

related_topics:
- vcb.chapter.reviewing_codex_output
- vcb.chapter.debugging_with_reproduction
- vcb.chapter.writing_updating_tests
- vcb.chapter.security_for_vibe_coders
- vcb.chapter.context_management
- vcb.chapter.acceptance_criteria
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
---


> Summary:
> Codex failures are predictable. The goal is not to blame the model or the user; the goal is to recognize the failure shape and apply the right control: context, constraints, tests, review, sandboxing, smaller diffs, durable guidance, or rollback.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.failure_modes_codex_work.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Codex usually does not fail in random ways. It fails in patterns. Once you can name the pattern, you can pick the right guardrail.

A failure mode is a common way work goes wrong. Examples:

- Codex edits more files than intended.
- Codex invents an API that looks real.
- Codex makes tests pass by weakening the test.
- Codex adds a dependency because it is convenient.
- Codex says the work is done before it has proved it.
- Codex changes behavior during a refactor.
- Codex misses security risk because you never gave it a threat model.

The fix is not always "use less AI." The fix is usually: make the task smaller, give better context, add constraints, require checks, review the diff, isolate the work, or update durable guidance.

### Failure-mode table

| Failure mode | What it looks like | Best control |
|---|---|---|
| Scope creep | unrelated files changed | smaller task + file constraints + diff review |
| Hallucinated API | code calls a method/config that does not exist | compile/run/test + vendor docs/source lookup |
| Silent behavior change | refactor passes checks but behavior shifted | characterization tests + public API constraints |
| Weakened tests | assertions deleted, snapshots loosened, mocks hide behavior | test-diff review + failing-test-first workflow |
| Dependency bloat | new package added for a simple need | no-new-dependency first + dependency review |
| Security regression | unsafe auth, validation, upload, redirect, or secrets handling | threat model + security review + explicit red lines |
| UI taste gap | technically works but feels generic or inaccessible | screenshot/reference + state matrix + browser check |
| Context pollution | old task assumptions leak into new work | reset context + summarize current task only |
| Optimistic estimate | Codex says "almost done" before integration | require unknowns, evidence, and remaining checks |
| Summary confidence | final response sounds cleaner than the diff | review changed files and command output |
| Tool sprawl | MCP/hooks/skills/packages added without a real workflow | smallest-tool rule + monthly cleanup |
| Long unattended ambiguity | background task drifts from intent | clear stopping condition + checkpoints + isolation |

### The control loop

A good Codex workflow has a loop:

```text
intent → context → plan → patch → verification → review → recovery → durable learning
```

Most failures are one missing piece of that loop.

If Codex patched before understanding, add context and planning.
If Codex lied by summary, review the diff.
If Codex changed behavior silently, add tests and acceptance criteria.
If Codex damaged too much, reduce blast radius and improve rollback.
If Codex repeats the mistake, update durable guidance.

### What good looks like

Good failure handling sounds like this:

```text
This is not just "Codex messed up." This is scope creep plus weak done criteria.
The control is: restore the unrelated files, rewrite the task with file boundaries,
then ask for a smaller patch and final report with changed files and checks.
```

### What bad looks like

Bad failure handling looks like:

- asking Codex to "try again" with the same vague prompt;
- blaming the model without changing the workflow;
- accepting a second large patch because the first patch failed;
- adding process unrelated to the failure;
- treating a security failure like a normal lint issue.

### Checklist

When something goes wrong, ask:

- What failure mode is this?
- What evidence proves it?
- What was the missing control?
- How far did the damage spread?
- Can we recover from Git, tests, backups, feature flags, or secret rotation?
- Should this become durable guidance?
<!-- VCB:END_SECTION id=vcb.chapter.failure_modes_codex_work.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.failure_modes_codex_work.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to classify Codex failures without blame and to map each failure to a concrete control. The goal is not model criticism. The goal is workflow repair.

### Diagnose the human’s current model

Ask:

- Are they treating all failures as "AI hallucination"?
- Are they rerunning the same prompt after failure?
- Did they inspect the diff or only the final message?
- Did the failure come from missing context, weak constraints, missing tests, broad permissions, or overlarge scope?
- Is recovery easy, or did the failure touch real data/secrets/production?

### Explanation strategy

Use the pattern:

```text
Name the failure → identify the missing control → reduce blast radius → recover → encode the lesson.
```

Avoid vague advice like "be careful." Give a specific control.

### Useful metaphors

- **Failure mode:** a recurring pothole on the road.
- **Control:** the guardrail or speed limit for that pothole.
- **Diff review:** checking the bag, not the receipt.
- **Regression test:** a tripwire for the bug returning.
- **AGENTS.md update:** putting the lesson on the wall.

### Coaching tactics

- If the user says "Codex broke everything," ask for `git status`, changed files, and the symptom.
- If the diff is huge, stop feature work and recover scope first.
- If tests were changed, review test intent before implementation details.
- If secrets or user data were exposed, move immediately to containment and rotation.
- If the same failure happened twice, propose a durable rule.

### Prompt patterns

```text
Classify this Codex failure.
Inputs:
- what I asked for:
- what changed:
- what failed:
- files changed:
- checks run:

Return:
1. likely failure mode,
2. missing control,
3. recovery path,
4. smallest workflow change to prevent recurrence.
```

```text
Before editing, inspect the current diff and classify risks:
- scope creep,
- behavior changes,
- weakened tests,
- new dependencies,
- security-sensitive changes,
- missing checks.
Then recommend whether to proceed, split, or revert.
```

### Red flags to call out directly

- The human wants a bigger prompt after a broad failure.
- The human treats passing tests as proof without reviewing whether tests were weakened.
- The human keeps running Codex on an ambiguous background task.
- The human wants to patch a security issue without a threat model.
- The human accepts a summary that contradicts the diff.

### Exercises

Take one previous bad Codex result and classify it in the failure-mode table. Then write one prevention rule and one recovery rule.
<!-- VCB:END_SECTION id=vcb.chapter.failure_modes_codex_work.ai_coach -->

## Shortcut Reality

### The ideal practice

When Codex work goes wrong, classify the failure, recover safely, and improve the workflow.

### What users often do instead

Users often rerun the same vague prompt, ask for a complete rewrite, or blame the model without identifying the missing control.

### When the shortcut may be fine

If the project is disposable and the failure is local, it may be fine to reset the branch and try a cleaner prompt.

### When the shortcut is a bad idea

Do not "just try again" when the failure touched auth, payments, user data, production config, migrations, secrets, CI credentials, or large refactors.

### Risk profile

- Probability of failure: high if the same workflow is repeated unchanged.
- Impact if it fails: low in throwaway prototypes; severe in production/security contexts.
- Ease of recovery: high with clean Git checkpoints; low with data loss or secret exposure.
- Blast radius: depends on permissions, branch isolation, and affected systems.
- Skill needed to recover: increases sharply with migrations, deployments, and security incidents.
- Hidden cost: repeated rework and false confidence.

### Minimum guardrails

- Identify the changed files before retrying.
- Preserve or restore a clean Git checkpoint.
- Name the failure mode.
- Reduce task scope before the next attempt.
- Add one missing control: context, constraints, tests, review, sandbox, or rollback.

### Recovery plan

Stop new edits. Inspect `git status` and diff. Separate intended changes from accidental changes. Restore unrelated files. Add missing checks. Only then rerun Codex with a smaller prompt.

### AI coach guidance

Do not let the user treat failure as a vibe. Make it diagnosable.

## Budget and Constraint Notes

### Cheapest reliable path

Use the failure table to pick one guardrail, not every guardrail. For example: scope creep → file constraints and diff review; weak tests → test review and one behavior check.

### Fastest high-usage path

Run a fresh review agent to classify the failure while the main thread pauses. Use parallel analysis, not parallel mutation, until recovery is clear.

### Low-attention path

Low-attention recovery requires report-only work first. Codex may inspect and propose recovery, but should not mutate until the human approves the recovery path.

### Production-quality path

Production failures need containment, rollback, incident notes, test additions, durable guidance, and review. Security-sensitive failures may require secret rotation, audit logs, and external review.

## Stable Core

- Failure modes are useful because they map to controls.
- The diff and command output matter more than Codex’s confidence.
- Tests can be weak; review what they prove.
- Security and data failures require containment, not just another patch.
- Repeated failures should become durable guidance.

## Volatile Surface

- Model-specific failure frequency.
- Current Codex review/security features.
- Context compaction behavior.
- Exact commands/UI used to inspect diffs, checks, and work logs.
- New official failure-detection tools.

## Obsolescence Watch

Review this chapter if official OpenAI guidance materially changes around hallucinations, Codex validation, security review, or long-running agent behavior. Also review when recurring project failures reveal a missing failure mode.

## Evidence and Sources

- `openai.help.truthfulness` — official OpenAI source that models can produce incorrect or misleading outputs and may sound confident when wrong.
- `openai.hallucinations` — OpenAI research-facing source on hallucination and incentives around guessing versus uncertainty.
- `openai.codex.prompting` — official OpenAI source for context, task loop, goal mode, and success criteria.
- `openai.codex.workflows` — official OpenAI source for verification, context notes, bug repros, tests, and workflow recipes.
- `openai.codex.guide_ai_native_engineering_team` — official OpenAI source for AI-native testing/review/agentic SDLC changes.
- `openai.codex.security` — official OpenAI source for Codex Security and security-review limitations.
- `openai.codex.cloud_internet_access` — official OpenAI source for prompt-injection, exfiltration, dependency, and external-content risks.
- Maintainer synthesis: failure taxonomy derived from prior VCB chapters and stable engineering practice.

## Related Topics

- `vcb.chapter.reviewing_codex_output`
- `vcb.chapter.debugging_with_reproduction`
- `vcb.chapter.writing_updating_tests`
- `vcb.chapter.security_for_vibe_coders`
- `vcb.chapter.context_management`
- `vcb.chapter.acceptance_criteria`
- `vcb.concepts.blast_radius`
- `vcb.concepts.recoverability`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.failure_modes_codex_work -->
