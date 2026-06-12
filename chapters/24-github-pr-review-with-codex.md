<!-- VCB:BEGIN_TOPIC id=vcb.chapter.github_pr_review_with_codex version=0.1.0 -->
---
id: vcb.chapter.github_pr_review_with_codex
title: "Chapter 24 — GitHub PR Review with Codex"
type: chapter
chapter_number: 24
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-09-08'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- GitHub
- Codex Cloud
- Codex GitHub integration
- pull requests
- AGENTS.md review guidelines
- automatic reviews

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
- vcb.shortcut.skipping_pr_review
- vcb.shortcut.accepting_codex_review_as_approval
- vcb.shortcut.accepting_diff_without_review

durable_principles:
- Codex PR review is an additional review signal, not merge approval.
- Review prompts should focus on risk areas, not broad nitpicking.
- Repository review guidance belongs in durable project instructions when repeated.
- Humans still own merge decisions.

likely_to_change:
- trigger phrase and UI behavior
- automatic review settings
- review severity labels
- GitHub integration prerequisites
- Codex permission and cloud-task behavior

obsolete_when:
- Codex GitHub review is replaced by a different PR-review workflow.
- GitHub integration behavior changes so materially that trigger and automatic-review guidance is wrong.
- Native PR review becomes strong enough that this chapter should split into team-policy and human-triage cards.

related_topics:
- vcb.concepts.pull_request
- vcb.concepts.diff
- vcb.chapter.reviewing_codex_output
- vcb.chapter.agents_md_operating_manual
- vcb.chapter.security_for_vibe_coders
- vcb.workflow.github_pr_review
- vcb.safety.production_red_lines
---

> Summary:
> GitHub PR review with Codex means asking Codex to review a pull request as another reviewer. It can inspect the PR diff, use repository guidance, and leave findings in the PR workflow.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.github_pr_review_with_codex.human -->
## 1. For the Human: Plain-Language Concept

### What this means

GitHub PR review with Codex means asking Codex to review a pull request as another reviewer. It can inspect the PR diff, use repository guidance, and leave findings in the PR workflow.

### Why it matters

PRs are where real code gets accepted. Codex can help catch regressions, missing tests, and risky changes before merge. But Codex review is not magic approval. It is one signal.

The practical rule:

```text
Codex review = another reviewer
Human merge = ownership
```

If Codex says nothing, that does not prove the PR is safe. If Codex flags something, triage it before asking for a fix.

### The mental model

A PR review is a checkpoint at the border between “someone tried a change” and “we accept this change into shared history.”

Codex can be useful because it is not the tired implementer staring at the same code. It can read the diff with a fresh prompt: security, tests, missing states, or risky behavior changes.

### What good looks like

Good Codex PR review usage:

- the PR is small enough to understand;
- the review prompt names risk areas;
- AGENTS.md contains durable review guidelines;
- Codex findings are triaged by severity;
- humans distinguish blockers from nice-to-haves;
- fixes are requested only after deciding the finding is real;
- Codex review complements tests and human review.

Good review guidance is specific:

```text
Focus on auth middleware, PII logging, missing tests, permission changes, and risky dependency changes. Ignore formatting unless it changes behavior.
```

### What bad looks like

Bad usage:

- asking Codex to review a huge vague PR and accepting silence as proof;
- using Codex review as merge approval;
- asking Codex to fix every comment without triage;
- setting automatic review without review guidelines;
- using PR review to replace tests;
- mixing feature requests, refactors, dependencies, and migrations in one PR.

### Checklist

Before requesting review:

- Is the PR focused?
- Are checks passing or is failure explained?
- Did you include review focus if risk is specific?
- Does AGENTS.md include durable review rules?
- Is a human responsible for final merge?

After review:

- Classify findings as blocker, worth-fixing, noise, or needs more evidence.
- Ask for fixes only for real findings.
- Rerun relevant checks after fixes.
- Do not merge solely because Codex approved or stayed quiet.

<!-- VCB:END_SECTION id=vcb.chapter.github_pr_review_with_codex.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.github_pr_review_with_codex.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to use Codex PR review as a focused independent signal inside GitHub, not as a substitute for ownership.

### Diagnose the human’s current model

Ask:

- “What risk do you want Codex to review for?”
- “Is this PR small enough to review?”
- “Are you treating no comments as proof of safety?”
- “Do you have review guidance in AGENTS.md?”
- “Are you asking Codex to fix before verifying the finding?”

### Explanation strategy

Separate the PR workflow into stages:

1. Human or agent opens PR.
2. CI/checks create evidence.
3. Codex review searches for prioritized risks.
4. Human triages findings.
5. Fixes are applied if real.
6. Human merges when the evidence is acceptable.

Codex fits stage 3 and sometimes stage 5. It does not own stage 6.

### Useful metaphors

- Codex is a second set of eyes, not the judge.
- Automatic review is a smoke detector, not a building inspector.
- AGENTS.md review guidelines are the reviewer brief.

### Coaching tactics

- Use one-off review focus in the PR comment for special risk.
- Promote repeated review focus into AGENTS.md.
- Push back on giant PRs.
- Ask for file-specific evidence in findings.
- Keep Codex review focused on P0/P1 issues where possible.
- Do not let the human chase every low-value suggestion.

### Prompt patterns

```text
@codex review for security regressions, missing tests, risky behavior changes, and unexpected dependency or config changes.
```

```text
@codex review this PR as a production-risk review.
Focus on auth, authorization, PII, payments, migrations, deploy config, and test weakening.
Ignore style unless it creates real risk.
```

```text
Triage these Codex review findings.
For each one, classify: real blocker, real non-blocker, likely false positive, or needs evidence.
Do not change code until the triage is complete.
```


### Red flags to call out directly

- “Codex review is not approval.”
- “A silent review does not prove safety.”
- “This PR is too broad for high-signal review.”
- “Do not ask Codex to fix a finding you have not triaged.”
- “If review guidance matters every time, put it in AGENTS.md.”

### Exercises

1. Take one PR and write a one-sentence risk focus.
2. Ask Codex for review.
3. Triage each finding before fixing.
4. Convert any repeated review concern into AGENTS.md review guidance.

<!-- VCB:END_SECTION id=vcb.chapter.github_pr_review_with_codex.ai_coach -->

## Shortcut Reality

### The ideal practice

Use Codex PR review as an independent signal alongside human review, tests, CI, and project-specific review guidelines.

### What users often do instead

They skip PR review on solo work, or they turn on automated review and treat it as approval.

### When the shortcut may be fine

Skipping PR review is usually fine for throwaway prototypes, local-only experiments, docs drafts, or tiny changes on branches with no real users.

### When the shortcut is a bad idea

Skipping independent review is a bad idea when the PR touches auth, permissions, user data, billing, deployments, migrations, security-sensitive dependencies, public APIs, or large refactors.

Treating Codex review as approval is also a bad idea. It can miss issues and can be noisy in the wrong areas.

### Risk profile

- Probability of failure: medium when PRs are broad or risky.
- Impact if it fails: high for production and security-sensitive code.
- Ease of recovery: high before merge; lower after deploy, migration, or data exposure.
- Blast radius: shared repo, production, users.
- Skill needed to recover: medium to high.
- Hidden cost: false confidence from a clean automated review.

### Minimum guardrails

- Keep PRs small.
- Request focused Codex review for risky areas.
- Keep durable review guidance in AGENTS.md.
- Treat findings as candidates, not truth.
- Require human triage before merge.
- Re-run checks after fixes.

### Recovery plan

1. If a bad PR merged, stop follow-up merges.
2. Identify the merged commit and affected files.
3. Revert or hotfix based on blast radius.
4. Ask Codex for a post-merge risk review with concrete symptoms.
5. Add review guidance or tests for the missed issue.

### AI coach guidance

Use Codex PR review to add a second signal, not to lower the acceptance bar. Push hardest when the human wants to skip review on high-blast-radius code.

## Budget and Constraint Notes

### Cheapest reliable path

Request targeted PR review only on risky PRs. Use concise AGENTS.md review guidelines to avoid restating the same criteria.

### Fastest high-usage path

Use automatic reviews plus targeted follow-up reviews for security/tests/dependencies, but triage findings before fixes.

### Low-attention path

Automatic review can help, but low attention needs narrower PRs and structured final evidence. Do not merge automatically from Codex review.

### Production-quality path

Require CI, human review, Codex review for risky surfaces, branch protection, and explicit merge ownership.

## Stable Core

- PR review is a review signal, not approval.
- A focused review prompt gets better signal than “review this.”
- AGENTS.md should hold durable review guidance.
- Findings need triage before fixes.
- Human merge responsibility does not disappear.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Triggers, automatic-review settings, severity labels, GitHub UI, cloud-task follow-up behavior, and plan access are volatile. Verify official OpenAI and GitHub docs before giving exact setup steps.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when OpenAI changes GitHub review behavior, severity focus, automatic review configuration, or when GitHub changes PR review/check surfaces.

## Evidence and Sources

- `openai.codex.github_review` — official OpenAI Codex source for GitHub code review setup, `@codex review`, automatic reviews, and AGENTS.md review guidelines.
- `openai.codex.use_cases.github_code_reviews` — official OpenAI use-case source for PR reviews focused on regressions, missing tests, and risky changes.
- `github.docs.pull_requests` — official GitHub source for pull request review surfaces and merge context.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis: automated review is a signal; humans own merge risk.

## Related Topics

- vcb.concepts.pull_request
- vcb.concepts.diff
- vcb.chapter.reviewing_codex_output
- vcb.chapter.agents_md_operating_manual
- vcb.chapter.security_for_vibe_coders
- vcb.workflow.github_pr_review
- vcb.safety.production_red_lines

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.github_pr_review_with_codex -->
