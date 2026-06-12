<!-- VCB:BEGIN_TOPIC id=vcb.codex.cloud version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
audiences:
- human
- ai_coach
source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: official OpenAI product behavior anchors plus VCB maintainer synthesis
  for risk, workflow, and coaching guidance
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
id: vcb.codex.cloud
title: Codex Cloud / Web
type: codex_feature
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex Cloud
- Codex Web
- GitHub repositories
- Cloud environments
- Pull requests
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.unattended_cloud_delegation
- vcb.shortcut.cloud_task_without_context
- vcb.shortcut.cloud_work_with_real_secrets
- vcb.shortcut.parallel_agents_edit_same_files
durable_principles:
- cloud delegation works best when the task can be isolated, reviewed, and merged
  later
- cloud environments need explicit setup and external-access boundaries
- background work is useful only when final evidence is reviewable
likely_to_change:
- cloud environment setup behavior
- GitHub connection and PR flow
- internet access controls
- remote connection behavior
- usage economics
obsolete_when:
- official docs no longer support background cloud tasks or GitHub-connected Codex
  work
related_topics:
- vcb.chapter.cloud_delegation_parallel_work
- vcb.codex.app
- vcb.codex.github_review
- vcb.codex.automations
- vcb.concepts.git_branch
- vcb.concepts.pull_request
---

> Summary:
> Codex Cloud/Web is the background delegation surface for scoped repo tasks that can run away from your local session and return as a reviewable result.

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

<!-- VCB:BEGIN_SECTION id=vcb.codex.cloud.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Codex Cloud lets Codex work on repository tasks in a cloud environment, including background and parallel work. You give it a bounded job, it works away from your local hands, and you review what it returns.

### Why it matters

Cloud delegation matters when a task needs time, exploration, or parallel attempts. It is not magic autonomy. It needs the right repo, setup, environment, secrets policy, internet policy, and review path.

### The mental model

Cloud Codex is a remote contractor with a branch. It can make progress while you do something else, but it still needs a work order, safe tools, and final inspection.

### What good looks like

Good use: delegate a scoped bug investigation or feature slice in a branch, require tests and a final report, then review the PR or diff before merging.

### What bad looks like

Bad use: ask for an ambiguous production refactor, enable broad internet/tool access, include real secrets, then leave it unattended.

### Minimal example

Example: ask Cloud to implement one API endpoint in a branch, using existing patterns, with no new dependencies and a final report listing files changed and checks run.

### Checklist

- Name the task and the Codex surface explicitly.
- Confirm whether the work is prototype, maintenance, production, or emergency work.
- Choose permissions and attention level before starting.
- Require a diff, report, or artifact that proves what changed.
- Review volatile details against official docs before freezing commands or UI instructions.
<!-- VCB:END_SECTION id=vcb.codex.cloud.human -->

<!-- VCB:BEGIN_SECTION id=vcb.codex.cloud.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach cloud delegation as isolated, review-later work with explicit setup and a high-quality done-when contract.

### Diagnose the human’s current model

- Is all needed context in the remote repo/environment?
- Can the task finish without uncommitted local state?
- Does it need internet access or secrets, and why?
- How will the user review the result?

### Explanation strategy

Start with task/surface fit. Explain what this Codex feature is good at, what it does not prove, and which guardrails become mandatory as blast radius grows. Tie the explanation to the user’s actual repository, risk level, and attention budget.

### Useful metaphors

Cloud delegation is sending a task to a workshop across town. If you forgot the blueprint or gave it unsafe keys, distance makes the mistake harder to notice.

### Coaching tactics

- Ask the user what surface they are actually using before giving feature-specific advice.
- Separate stable workflow principle from volatile product mechanics.
- Convert broad requests into scoped work orders with explicit done-when criteria.
- Escalate hard for production, secrets, auth, payments, migrations, CI credentials, browser state, or unattended mutation.
- Prefer reviewable artifacts over confident summaries.

### Prompt patterns

```text
Delegate this as a cloud task on a separate branch. Goal: [goal]. Context: [files/issues/logs]. Constraints: no production secrets, no new dependencies unless justified, no unrelated refactors. Done when: [checks/report/PR].
```

### Red flags to call out directly

- uncommitted local-only context
- real secrets in cloud setup
- internet access enabled without allowlist or purpose
- parallel tasks touching the same files
- ambiguous task with low attention

### Exercises

1. Ask the human to choose this feature for one low-risk task and one high-risk task, then explain what guardrails change.
2. Ask the human to name which part of this feature is stable principle and which part must be rechecked against official docs.
3. Ask the human to write a final-report template for work done through this feature.
<!-- VCB:END_SECTION id=vcb.codex.cloud.ai_coach -->

## Shortcut Reality

### The ideal practice

Use cloud for independent, branch-isolated, reviewable tasks where background work saves human attention.

### What users often do instead

Users often delegate broad work to cloud because they want progress without supervision.

### When the shortcut may be fine

This can be fine for read-only audits, docs updates, low-risk prototypes, or isolated branches with no real secrets.

### When the shortcut is a bad idea

It is a bad trade for unclear production changes, migrations, auth/payments, or any work needing local-only context the cloud cannot see.

### Risk profile

- Probability of failure: Medium to high failure probability when context is missing
- Impact if it fails: rises sharply with production data, secrets, real users, payments, auth, CI credentials, or deployment paths.
- Ease of recovery: good only when work is branch-isolated, committed, fake-data backed, and reviewable.
- Blast radius: small for local prototypes; large for shared repos, cloud work, external tools, GUI control, and automated mutation.
- Skill needed to recover: low for small Git-backed diffs; medium/high for secrets, data, deployment, or account-state mistakes.
- Hidden cost: stale configuration, noisy automation, false confidence, usage burn, and future maintenance load.

### Minimum guardrails

- scope one task per cloud job
- use a branch/worktree
- avoid real secrets or restrict them tightly
- require final evidence
- review diff/PR before merge

### Recovery plan

Cancel or pause the cloud task, revoke exposed credentials if needed, inspect the branch diff, close bad PRs, and rerun with narrower context and safer environment settings.

### AI coach guidance

Do not moralize the shortcut. Name the tradeoff, reduce blast radius, improve recoverability, and require the smallest guardrail that changes the risk profile.

## Budget and Constraint Notes

### Cheapest reliable path

Use this feature for one narrow task with curated context, conservative permissions, and one relevant check. Do not spend usage exploring broad unknowns unless the task is important enough to justify it.

### Fastest high-usage path

Use this feature aggressively only with branch/worktree isolation, clear acceptance criteria, structured final reports, and independent review for risky diffs.

### Low-attention path

Low-attention work requires stronger isolation, report-only or read-only posture when possible, fake credentials, and a final report that names files changed, checks run, unresolved risks, and review needs.

### Production-quality path

Use least privilege, clear done-when criteria, Git checkpoints, tests/build/lint where relevant, diff review, source-register discipline, and a rollback plan before accepting work.

## Stable Core

- cloud delegation works best when the task can be isolated, reviewed, and merged later
- cloud environments need explicit setup and external-access boundaries
- background work is useful only when final evidence is reviewable

## Volatile Surface

- cloud environment setup behavior
- GitHub connection and PR flow
- internet access controls
- remote connection behavior
- usage economics

## Obsolescence Watch

- official docs no longer support background cloud tasks or GitHub-connected Codex work

## Evidence and Sources

- `openai.codex.cloud` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.cloud_environments` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.cloud_internet_access` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.remote_connections` — official source anchor for this card's current Codex feature behavior.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for blast radius, recoverability, workflow fit, and AI-coach intervention guidance.

## Related Topics

- `vcb.chapter.cloud_delegation_parallel_work`
- `vcb.codex.app`
- `vcb.codex.github_review`
- `vcb.codex.automations`
- `vcb.concepts.git_branch`
- `vcb.concepts.pull_request`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.codex.cloud -->
