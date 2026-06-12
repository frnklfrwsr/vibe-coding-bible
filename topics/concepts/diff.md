<!-- VCB:BEGIN_TOPIC id=vcb.concepts.diff version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-08'
review_cadence: annual
audiences:
- human
- ai_coach
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- Human software work
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
id: vcb.concepts.diff
title: Diff
type: concept
next_review_due: '2027-06-08'
source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
stability:
  principle: CORE_ENGINEERING
  surface: STABLE
  pricing: STABLE
shortcut_profiles:
- vcb.shortcut.accepting_diff_without_review
durable_principles:
- the diff is the evidence of what changed
- final AI summaries are claims until checked
- review changed files before accepting AI-generated code
likely_to_change:
- diff UI presentation in Codex, GitHub, IDEs, and CLI tools
- exact commands or labels used to display diffs
obsolete_when:
- software changes stop being represented as inspectable file-level patches
related_topics:
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.concepts.git_branch
- vcb.concepts.pull_request
- vcb.workflow.reviewing_diffs
- vcb.failure.done_claim_without_evidence
---

> Summary:
> A diff is the exact set of code changes between two versions. It is the first thing to inspect before trusting Codex output.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.diff.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A **diff** is the exact list of changes between two versions of your code. It shows which lines were added, removed, or changed.

Think of it like **tracked changes in Google Docs**, but for code.

In many diff views:

- Lines starting with `+` were added.
- Lines starting with `-` were removed.
- Nearby unchanged lines are shown so you can understand context.

### Why it matters

Codex’s final message is a summary. The diff is the evidence.

A final message can say “I only updated the button style.” The diff might show that Codex also changed validation logic, removed a test, added a dependency, or edited deployment config.

You do not review Codex by reading its final message. You review Codex by reading the diff.

### The mental model

Codex is handing you a proposed patch. The diff is the receipt and the bag of groceries at the same time: it tells you what you paid for and what you actually got.

Check the bag.

### What good looks like

Good diff review asks:

- Which files changed?
- Is the diff small enough to understand?
- Does every changed file belong to the task?
- Were tests added, removed, or weakened?
- Did dependencies, config, auth, deployment, or database code change?
- Does the diff match the requested behavior?

### What bad looks like

Bad diff review sounds like:

```text
Codex said it fixed it, so I accepted everything.
```

That is not review. That is trusting the label on the box without opening the box.

### Minimal example

```diff
- if user.is_admin:
+ if user:
    show_admin_panel()
```

That diff looks tiny. It is also dangerous. It changes “only admins can see this” into “any logged-in user can see this.” Small diffs can have large blast radius.

### Checklist

Before accepting a Codex diff:

- Read the changed file list.
- Scan for unrelated files.
- Look for removed checks, removed tests, and broad rewrites.
- Search the diff for auth, permissions, secrets, payments, migrations, deletion, deployment, and dependencies.
- Run the smallest relevant verification you can afford.
- Commit only after the diff and checks match the task.
<!-- VCB:END_SECTION id=vcb.concepts.diff.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.diff.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Get the human to treat the diff as primary evidence. The final assistant message is a claim; the diff is the artifact to inspect.

### Diagnose the human’s current model

Ask:

- Are you looking at the changed files or only the summary?
- Can you name the riskiest file in the diff?
- Did Codex remove or weaken tests?
- Did any file change outside the requested area?
- Does the diff touch auth, data, config, dependencies, or deployment?

### Explanation strategy

Start simple: “A diff is tracked changes for code.” Then immediately connect it to trust: “This is how you verify what Codex really did.”

### Useful metaphors

- Final summary = receipt.
- Diff = groceries in the bag.
- Review = checking the bag before leaving the store.

### Coaching tactics

When the user wants to accept a diff quickly, ask for a changed-file list and risk classification. For large diffs, split review by file category: UI, tests, data, auth/security, config, dependencies.

### Prompt patterns

```text
Review this diff before I accept it.
Group changes by file.
Call out unrelated edits, removed tests, new dependencies, auth/security/data risks, and anything that does not match the original request.
```

```text
Explain this diff in plain language.
Separate behavior changes from refactors, formatting, tests, and configuration changes.
```

### Red flags to call out directly

- “Looks good” without file-level evidence.
- Deleted tests or weakened assertions.
- New dependency added for a small task.
- Large formatting change mixed with behavior change.
- Auth, payment, data deletion, secrets, migration, or deployment changes hidden in a broad diff.

### Exercises

Give the human a small diff and ask them to identify:

1. What behavior changed.
2. What could break.
3. What check would prove the change works.
4. Whether they would accept, reject, or ask Codex to narrow it.
<!-- VCB:END_SECTION id=vcb.concepts.diff.ai_coach -->

## Shortcut Reality

### The ideal practice

Review every non-trivial diff before accepting it. Use tests and command output as supporting evidence.

### What users often do instead

Users often read Codex’s final message, see that the app appears to run, and accept the entire patch.

### When the shortcut may be fine

Accepting a diff after only a light scan may be fine for disposable prototypes, throwaway branches, small visual tweaks, or learning exercises.

### When the shortcut is a bad idea

It is a bad idea when the diff is large, hard to understand, touches production paths, changes auth/payment/data behavior, removes tests, adds dependencies, or edits deployment/config files.

### Risk profile

- Probability of failure: medium for AI-generated diffs; higher when the diff is large.
- Impact if it fails: low for local prototypes; high for real users, data, money, auth, or deployment.
- Ease of recovery: high if committed on a branch; low if accepted into production without rollback.
- Blast radius: depends on changed files, not line count.
- Skill needed to recover: low for a CSS typo; high for data/security changes.
- Hidden cost: review debt accumulates when bad changes are accepted quietly.

### Minimum guardrails

- Inspect the changed file list.
- Read any removed lines carefully.
- Search for risky domains: auth, payments, deletion, secrets, migrations, config, deployment.
- Run the smallest relevant check.
- Commit only after review.

### Recovery plan

If you accepted a bad diff, stop adding new changes. Inspect `git status` and recent commits, identify which files belong to the bad change, and use `vcb.concepts.rollback` before asking Codex for more edits.

### AI coach guidance

Do not say “trust the diff” as a slogan. Teach the human what to look for: changed files, removed logic, hidden risk areas, test quality, and mismatch between requested work and actual patch.

## Budget and Constraint Notes

### Cheapest reliable path

Ask Codex for a changed-file summary, then manually inspect only the riskiest files and run one targeted check.

### Fastest high-usage path

Ask a fresh agent to review the diff after implementation. Use this for broad changes, not for every tiny edit.

### Low-attention path

Low-attention work requires a final report with changed files, checks run, and known risks. Do not merge without later human or independent review.

### Production-quality path

Use diff review plus tests, CI, independent review for sensitive areas, and rollback planning.

## Stable Core

- Diff review is the control point for AI-generated code.
- Changed lines are stronger evidence than final summaries.
- Small diffs can still create large damage.

## Volatile Surface

- Exact diff UI in Codex, IDEs, GitHub, and Git clients.
- Commands and shortcuts for viewing diffs.
- Native AI review features.

## Obsolescence Watch

Review this topic if AI coding systems stop producing inspectable patches or if Codex/GitHub introduces a materially different review artifact that replaces file-level diffs.

## Evidence and Sources

- `git.docs.diff`: official Git documentation for showing changes between working tree, index, commits, trees, blobs, and files.
- `openai.codex.best_practices`: official OpenAI guidance for validation and review practices.
- `vcb.blueprint.v1`: durable framing that Codex output is a patch proposal, not truth.

## Related Topics

- `vcb.concepts.blast_radius`
- `vcb.concepts.recoverability`
- `vcb.concepts.rollback`
- `vcb.concepts.pull_request`
- `vcb.workflow.reviewing_diffs`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.diff -->
