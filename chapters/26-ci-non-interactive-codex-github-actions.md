<!-- VCB:BEGIN_TOPIC id=vcb.chapter.ci_noninteractive_github_actions version=0.1.0 -->
---
id: vcb.chapter.ci_noninteractive_github_actions
title: "Chapter 26 — CI, Non-Interactive Codex, and GitHub Actions"
type: chapter
chapter_number: 26
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-09-08'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex CLI
- codex exec
- GitHub Actions
- Codex GitHub Action
- CI/CD
- automation
- release notes
- PR reports
- read-only automation

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
- vcb.shortcut.unattended_mutation
- vcb.shortcut.overbroad_ci_permissions
- vcb.shortcut.long_lived_ci_secrets
- vcb.shortcut.unattended_long_runs
- vcb.shortcut.broad_agent_permissions

durable_principles:
- Automation should start read-only and report-only.
- Unattended mutation needs isolation, narrow permissions, explicit outputs, and review gates.
- Secrets in CI are high-value targets; prefer least privilege and short-lived credentials where available.
- CI prompts should be versioned and narrow.

likely_to_change:
- codex exec flags and output options
- Codex GitHub Action inputs and version
- GitHub Actions syntax and runner behavior
- authentication patterns
- API/credit economics
- non-interactive feature maturity

obsolete_when:
- Codex non-interactive mode changes materially or is replaced.
- Codex GitHub Action behavior or safety strategy changes materially.
- GitHub Actions security model changes enough that permissions/secrets advice needs update.

related_topics:
- vcb.chapter.hooks_deterministic_guardrails
- vcb.chapter.security_for_vibe_coders
- vcb.chapter.github_pr_review_with_codex
- vcb.chapter.reviewing_codex_output
- vcb.safety.secrets
- vcb.codex.github_action
- vcb.workflow.ci_noninteractive
- vcb.constraints.usage_burn
---

> Summary:
> CI and non-interactive Codex mean Codex runs from scripts, workflows, or automation instead of a live chat session. In practice, this often means codex exec, a GitHub Actions workflow, or the Codex GitHub Action.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.ci_noninteractive_github_actions.human -->
## 1. For the Human: Plain-Language Concept

### What this means

CI and non-interactive Codex mean Codex runs from scripts, workflows, or automation instead of a live chat session. In practice, this often means `codex exec`, a GitHub Actions workflow, or the Codex GitHub Action.

### Why it matters

Automation is powerful because it runs the same way every time. It is dangerous for the same reason. A bad interactive prompt can annoy you. A bad CI prompt can run on every pull request, expose secrets, comment noise, or mutate code where no human is watching.

Start with reports before mutations.

### The mental model

Use this ladder:

```text
Read-only report -> comment/report artifact -> proposed patch -> branch-only patch -> protected merge/deploy
```

Most teams should start at the left. Move right only when the workflow is narrow, tested, isolated, and reviewed.

### Good automation jobs

Good candidates:

- summarize failing tests;
- produce release-note drafts;
- review PR diffs for risky changes;
- check whether acceptance criteria are present;
- generate migration risk reports;
- inspect dependency changes;
- create structured risk reports for humans.

Bad first automation jobs:

- auto-fix production branches;
- run broad refactors on every PR;
- execute untrusted code with secrets available;
- deploy based on Codex judgment alone;
- mutate large areas without a review gate.

### Secret and permission discipline

CI is not your laptop. It often has tokens, repository access, deployment power, and logs.

Minimum discipline:

- set the smallest `GITHUB_TOKEN` permissions needed;
- avoid job-level API keys when repository-controlled code runs in the same job;
- prefer short-lived cloud credentials through OIDC where appropriate;
- separate read-only analysis from mutation/deployment;
- treat pull-request content and branch names as untrusted input;
- upload artifacts/reports instead of hiding results in logs;
- avoid running broad agent access with secrets.

### What good looks like

A good non-interactive Codex job has:

- narrow prompt committed in the repo;
- explicit working directory;
- read-only or workspace-limited sandbox;
- minimal token permissions;
- no unnecessary secrets;
- structured output or report file;
- clear pass/fail behavior;
- human review before mutation/merge/deploy;
- logging that does not leak secrets.

### Checklist

Before adding Codex to CI:

- Is the job read-only first?
- What exact event triggers it?
- What permissions does it need?
- What secrets can it access?
- Can untrusted code run in the same job?
- Where does output go?
- What does failure mean?
- Who reviews results?
- What prevents auto-mutation of protected branches?

<!-- VCB:END_SECTION id=vcb.chapter.ci_noninteractive_github_actions.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.ci_noninteractive_github_actions.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that CI automation amplifies both good workflow and bad assumptions. Start narrow, read-only, and least-privilege.

### Diagnose the human’s current model

Ask:

- “Do you want a report, a proposed patch, or an automatic mutation?”
- “What event triggers this job?”
- “What secrets and tokens are available?”
- “Could untrusted PR code read those secrets?”
- “What permissions does `GITHUB_TOKEN` need?”
- “Where is the prompt versioned?”
- “What output is machine-readable?”

### Explanation strategy

Route automation by risk:

- Report-only: safest default.
- Comment on PR: moderate; avoid spam and secrets.
- Generate patch on branch: needs sandbox, branch isolation, and review.
- Commit/push automatically: high risk; only for narrow maintenance tasks.
- Deploy: highest risk; needs standard release controls.

Make the user state the automation level before writing YAML.

### Useful metaphors

- CI is a robot with a badge. Decide which rooms its badge opens.
- Non-interactive Codex is a night shift worker: useful when the checklist is precise, risky when the job is vague.
- Report-only automation is a scout; auto-mutation is a bulldozer.

### Coaching tactics

- Start with read-only `codex exec` or report-only GitHub Action flows.
- Keep prompts in versioned files.
- Require explicit output schema or report fields for downstream use.
- Avoid exposing API keys to jobs that run repo-controlled code.
- Make permissions visible in the workflow.
- Use separate jobs for analysis and posting feedback when possible.
- Escalate hard around pull-request workflows, secrets, deployment credentials, and full access.

### Prompt patterns

```text
Design a read-only Codex CI job.
Goal: [goal]
Trigger: [event]
Output: [comment/artifact/json]
Constraints:
- do not mutate code,
- no secrets unless justified,
- least GITHUB_TOKEN permissions,
- no network unless necessary,
- explain failure behavior.
Return the plan first, not YAML.
```

```text
Review this GitHub Actions workflow for security.
Focus on secrets, GITHUB_TOKEN permissions, untrusted PR input, checkout behavior, third-party actions, cache use, and whether Codex can mutate code.
Return blockers first.
```


### Red flags to call out directly

- “Do not auto-mutate production branches from a vague prompt.”
- “Do not expose API keys to untrusted code.”
- “Set token permissions explicitly.”
- “A CI agent with secrets and full access is a high-blast-radius setup.”
- “Read-only report first.”

### Exercises

1. Pick one CI idea and classify it as report, comment, patch, or deploy.
2. Write the minimum permissions.
3. Remove all unnecessary secrets.
4. Define output fields.
5. Run it manually before scheduling or triggering broadly.

<!-- VCB:END_SECTION id=vcb.chapter.ci_noninteractive_github_actions.ai_coach -->

## Shortcut Reality

### The ideal practice

Build narrow, versioned, read-only Codex automation first; add mutation only behind isolation, least privilege, branch protection, and human review.

### What users often do instead

They add a workflow that runs broad prompts, exposes secrets, uses default permissions, and comments or mutates on every PR before the job is proven useful.

### When the shortcut may be fine

A quick CI experiment may be fine in a private throwaway repo with no secrets, read-only permissions, manual trigger, and report-only output.

### When the shortcut is a bad idea

Unattended mutation is a bad idea when the job has write tokens, deployment credentials, production branches, untrusted PR code, broad network access, or vague prompts.

### Risk profile

- Probability of failure: medium; higher with broad triggers and secrets.
- Impact if it fails: medium for noisy comments, severe for secret exposure or bad deploys.
- Ease of recovery: high for report-only jobs; low for leaked credentials or automated production mutation.
- Blast radius: repo, organization, cloud account, production users.
- Skill needed to recover: high for CI/security incidents.
- Hidden cost: noisy automation, billable usage, secret rotation, broken trust.

### Minimum guardrails

- Manual trigger or narrow event first.
- Report-only before mutation.
- Explicit minimal `GITHUB_TOKEN` permissions.
- No job-level API keys around untrusted code.
- Use short-lived cloud credentials/OIDC where appropriate.
- Store prompts in versioned files.
- Upload artifacts or structured reports.
- Human review before merge/deploy.

### Recovery plan

1. Disable the workflow.
2. Revoke/rotate exposed tokens or API keys.
3. Delete sensitive logs if needed.
4. Revert bad automated commits.
5. Narrow triggers, permissions, secrets, and prompt scope.
6. Re-enable in report-only mode.

### AI coach guidance

Default to “report/propose, do not mutate.” Only recommend automatic mutation when the task is narrow, isolated, repeatable, and guarded by branch protection or equivalent review.

## Budget and Constraint Notes

### Cheapest reliable path

Use manual `codex exec` or a manually triggered read-only workflow for summaries and risk reports. Avoid always-on automation until the value is proven.

### Fastest high-usage path

Use Codex GitHub Action or `codex exec` for PR review reports, release prep, and failing-test triage, but keep mutation branch-scoped and review-gated.

### Low-attention path

Low-attention CI must be read-only or branch-isolated. Do not combine low attention with secrets, full access, and auto-merge.

### Production-quality path

Use least privilege, OIDC where appropriate, protected environments, pinned/reviewed actions, clear artifacts, branch protection, human approval, and rollback/deploy controls.

## Stable Core

- Automation amplifies workflow quality and mistakes.
- Read-only reports are safer than unattended patches.
- Secrets and broad permissions make CI high blast radius.
- Prompts should be versioned and narrow.
- Output should be structured enough for humans or downstream tools to inspect.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Codex exec flags, GitHub Action inputs/version, output-schema behavior, authentication choices, runner support, GitHub Actions event semantics, token permission defaults, and API/usage economics are volatile. Verify official docs before giving executable workflow snippets.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when OpenAI changes non-interactive mode, Codex GitHub Action behavior, authentication guidance, or GitHub changes token/secret/OIDC/security guidance.

## Evidence and Sources

- `openai.codex.noninteractive` — official OpenAI Codex source for `codex exec`, scripts/CI use, sandbox defaults, output behavior, and automation auth guidance.
- `openai.codex.github_action` — official OpenAI Codex source for the GitHub Action, CI/CD usage, prerequisites, and prompt-file workflows.
- `openai.codex.agent_approvals_security` — official OpenAI source for sandbox/approval combinations and non-interactive safety posture.
- `github.docs.actions_secure_use` — official GitHub source for secure GitHub Actions workflow practices and least-privilege guidance.
- `github.docs.github_token` — official GitHub source for `GITHUB_TOKEN` authentication and permission control.
- `github.docs.actions_oidc` — official GitHub source for OIDC-based cloud-provider authentication without long-lived secrets.
- `github.docs.actions_secrets` — official GitHub source for repository, environment, and organization secrets.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis: report-only automation is safer than unattended mutation.

## Related Topics

- vcb.chapter.hooks_deterministic_guardrails
- vcb.chapter.security_for_vibe_coders
- vcb.chapter.github_pr_review_with_codex
- vcb.chapter.reviewing_codex_output
- vcb.safety.secrets
- vcb.codex.github_action
- vcb.workflow.ci_noninteractive
- vcb.constraints.usage_burn

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.ci_noninteractive_github_actions -->
