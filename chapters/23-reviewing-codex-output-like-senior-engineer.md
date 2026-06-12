<!-- VCB:BEGIN_TOPIC id=vcb.chapter.reviewing_codex_output version=0.1.0 -->
---
id: vcb.chapter.reviewing_codex_output
title: "Chapter 23 — Reviewing Codex Output Like a Senior Engineer"
type: chapter
chapter_number: 23
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-09-08'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- pull requests
- local diffs
- code review

source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: AGENTIC_PRINCIPLE
  surface: VOLATILE
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
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.broad_refactor
- vcb.shortcut.adding_dependencies_fast

durable_principles:
- Review the diff and checks, not the agent summary.
- Risk determines review depth.
- A small patch with evidence can be accepted quickly; a large patch touching security, data, or dependencies needs slower review.
- Review should classify blocking risks separately from style preferences.

likely_to_change:
- review UI labels and commands
- Codex local review presets
- Codex app review-pane behavior
- model-specific review quality
- GitHub review integration behavior

obsolete_when:
- Codex produces verifiable proof that makes human diff review unnecessary for most production changes.
- Review surfaces change enough that the current workflow advice misroutes users.
- A future editor splits this chapter into separate diff-review and security-review workflow cards.

related_topics:
- vcb.concepts.diff
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.chapter.git_discipline
- vcb.chapter.acceptance_criteria
- vcb.chapter.github_pr_review_with_codex
- vcb.chapter.security_for_vibe_coders
- vcb.workflow.reviewing_diffs
- vcb.failure.unreviewed_large_diffs
---

> Summary:
> Reviewing Codex output like a senior engineer means treating every Codex change as a patch proposal. It might be good. It might be almost good. It might be plausible trash. You do not know until you inspect evidence.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.reviewing_codex_output.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Reviewing Codex output like a senior engineer means treating every Codex change as a patch proposal. It might be good. It might be almost good. It might be plausible trash. You do not know until you inspect evidence.

### Why it matters

Codex can make changes faster than you can understand them. That is useful only if your review loop keeps up.

The review target is not the final message. The final message is a claim. The diff, tests, logs, screenshots, and command output are the evidence.

Use this order:

1. What files changed?
2. What behavior changed?
3. What checks ran?
4. What risky areas were touched?
5. What did Codex not prove?
6. Can you roll back?

### The mental model

Think of Codex like a contractor handing you renovation work. The invoice may say “fixed the kitchen.” You still inspect the sink, stove, wiring, and floor before paying.

For code:

```text
Codex summary = invoice
Diff = actual work
Tests/checks = inspection tools
Rollback = insurance
```

A senior review does not mean reading every line with panic. It means knowing which lines can hurt you.

### What good looks like

A good review checks:

- changed file list;
- deleted code and deleted tests;
- new dependencies;
- auth, authorization, payments, secrets, user data, uploads, redirects, migrations, deployment config;
- error/loading/empty states;
- tests that prove behavior rather than only implementation;
- whether the patch stayed inside the requested scope;
- whether the final report includes checks run and known gaps.

For a tiny CSS tweak, this can take one minute. For auth or billing, it may be the main work.

### What bad looks like

Bad review habits:

- accepting because the app “seems fine”;
- reading only Codex’s final summary;
- ignoring deleted assertions;
- letting Codex add packages without justification;
- asking Codex to self-review and treating that as approval;
- merging a huge diff because it is too tiring to inspect;
- approving a production change with no rollback path.

If the diff is too large to review, the task was too large or the review strategy is wrong.

### Minimal review checklist

Before accepting:

- I inspected the changed file list.
- I searched the diff for risky words: auth, token, secret, env, migration, payment, permission, redirect, upload, eval, exec, dependency.
- I checked deleted tests and weakened assertions.
- I looked for unexpected files.
- I verified at least one relevant check or exact manual path.
- I know what to revert if this is wrong.

<!-- VCB:END_SECTION id=vcb.chapter.reviewing_codex_output.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.reviewing_codex_output.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to treat Codex output as evidence-bearing work, not as a trustworthy story. Your job is to calibrate review depth to risk, not to turn every change into ceremony.

### Diagnose the human’s current model

Ask:

- “Have you looked at the diff yet?”
- “What files changed that you did not expect?”
- “What check proves the behavior?”
- “Did tests get weaker or narrower?”
- “Does this touch auth, secrets, data, payments, deploy config, or dependencies?”
- “Can we revert this cleanly?”

### Explanation strategy

Use the risk ladder:

- Small local cosmetic change: file list + visual check may be enough.
- Feature slice: diff review + focused test/manual check.
- Refactor: behavior-preservation check + test review.
- Dependency/config change: package/lockfile review + build/test.
- Security/data/payment/auth: threat-focused review + independent signal + rollback plan.

Do not let the user hide behind “Codex said it ran tests.” Ask for command output or a final report that names the checks.

### Useful metaphors

- The summary is the receipt; the diff is the bag of groceries.
- Review is a smoke alarm plus a building inspection; different risks need different tools.
- A large diff is a fog bank. Split it until you can see.

### Coaching tactics

- Ask Codex to summarize the diff by risk area, then verify against the actual diff.
- Ask for a fresh-agent review when the patch is non-trivial.
- Use a targeted review prompt: security, tests, behavior changes, dependency impact.
- Separate blockers from nits.
- If the user is fatigued, recommend splitting or reverting rather than rubber-stamping.

### Prompt patterns

```text
Review this diff as a senior engineer.
Focus only on blocking issues:
- unintended behavior changes,
- deleted or weakened tests,
- auth/security/data/payment risks,
- new dependencies,
- migration/deploy/config risk,
- missing checks.
Return P0/P1/P2 findings with file references and evidence.
Do not comment on style unless it creates real risk.
```

```text
Before I accept this Codex patch, compare the final summary to the actual diff.
List any claim in the summary that the diff or command output does not support.
```


### Red flags to call out directly

- “You are reviewing the story, not the patch.”
- “This diff is too large to accept blind.”
- “A self-review by the same agent is not an independent review.”
- “The tests pass claim needs command output.”
- “This touched auth/data/deploy config; use a higher bar.”

### Exercises

1. Pick a recent Codex diff.
2. Classify each changed file as expected, suspicious, or unrelated.
3. Identify one behavior-level check.
4. Identify one rollback path.
5. Ask a fresh agent for P0/P1 review and compare findings to your own.

<!-- VCB:END_SECTION id=vcb.chapter.reviewing_codex_output.ai_coach -->

## Shortcut Reality

### The ideal practice

Review the actual diff, run or inspect relevant checks, and accept only changes whose behavior and risk you understand.

### What users often do instead

They read Codex’s final message, skim the app, and accept the patch because it “looks done.”

### When the shortcut may be fine

Accepting quickly may be fine for disposable prototypes, cosmetic tweaks, or local scripts when the diff is tiny, the blast radius is small, and rollback is easy.

### When the shortcut is a bad idea

Blind acceptance is a bad idea when the diff is large, touches real users, changes auth/authorization, handles secrets or payments, changes migrations, adds dependencies, changes deploy config, or deletes tests.

### Risk profile

- Probability of failure: medium; higher when diff is large or repo is unfamiliar.
- Impact if it fails: low for prototypes, high for production/security/data.
- Ease of recovery: high with clean branch and small commit; low after deploy/migration/secret exposure.
- Blast radius: from one file to all users.
- Skill needed to recover: low for simple revert; high for data/security incidents.
- Hidden cost: confidence debt; you do not know what changed.

### Minimum guardrails

- Inspect changed file list.
- Review diff around risky areas.
- Run at least one relevant check or exact manual flow.
- Ask for checks run and known gaps.
- Commit before accepting into a larger branch.
- Use fresh-agent review for non-trivial changes.

### Recovery plan

1. Stop merging further changes.
2. Inspect `git diff` and `git status`.
3. Revert the smallest bad commit or restore specific files.
4. Rerun the failing path.
5. Add a regression check if the failure mattered.
6. Add or update project guidance if Codex repeated a bad pattern.

### AI coach guidance

Do not shame the user for moving fast. Move them up one guardrail: file list, risky-area diff, one check, or fresh review.

## Budget and Constraint Notes

### Cheapest reliable path

Use a tight review checklist and one focused check. Do not ask for broad reviews unless risk demands it.

### Fastest high-usage path

Use a fresh Codex review pass plus human triage. Spend extra agent usage on independent risk detection, not cosmetic opinions.

### Low-attention path

Require structured final reports: files changed, checks run, risks, known gaps. Avoid unattended broad patches without fresh review.

### Production-quality path

Use branch/PR review, tests/CI, security-focused review for risky code, dependency review, rollback plan, and deployment monitoring.

## Stable Core

- Review the diff, not the final message.
- Match review depth to blast radius and recoverability.
- Checks are evidence; claims are not evidence.
- Large unreviewable diffs should be split.
- Fresh independent review catches different failures.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Codex review panes, local review commands, GitHub integration behavior, review severity labels, automatic review settings, and model-specific review quality are volatile. Verify current official docs before teaching exact commands or UI flows.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when Codex review surfaces change, official review severity behavior changes, or the repo adds dedicated topic cards for diff review, security review, test review, or dependency review.

## Evidence and Sources

- `openai.codex.best_practices` — official Codex source for validation, review, and using Codex as more than a code generator.
- `openai.codex.app_review` — official Codex source for the app review pane and Git-backed change inspection.
- `openai.codex.cli_features` — official Codex source for local review presets and diff-focused review behavior.
- `github.docs.pull_requests` — official GitHub source for PR review surfaces such as commits, checks, files changed, and merge status.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis: review depth should track blast radius, recoverability, and evidence quality.

## Related Topics

- vcb.concepts.diff
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.chapter.git_discipline
- vcb.chapter.acceptance_criteria
- vcb.chapter.github_pr_review_with_codex
- vcb.chapter.security_for_vibe_coders
- vcb.workflow.reviewing_diffs
- vcb.failure.unreviewed_large_diffs

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.reviewing_codex_output -->
