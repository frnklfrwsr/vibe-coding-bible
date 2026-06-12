<!-- VCB:BEGIN_TOPIC id=vcb.chapter.understanding_unknown_codebase version=0.1.0 -->
---
id: vcb.chapter.understanding_unknown_codebase
title: "Chapter 11 — Understanding an Unknown Codebase"
type: chapter
chapter_number: 11
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
- unknown repositories
- production repositories
- local development

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
- vcb.shortcut.editing_before_understanding
- vcb.shortcut.context_dumping
- vcb.shortcut.one_big_prompt

durable_principles:
- Understand the real implementation path before changing unfamiliar code.
- Ask for file and symbol evidence, not just architectural summaries.
- Start read-only when the codebase is unfamiliar, risky, or production-adjacent.
- Unknowns should be listed explicitly before edits begin.

likely_to_change:
- Codex codebase-onboarding UI affordances
- built-in repo-map features
- subagent and background exploration mechanics
- exact commands for attaching files or selecting context

obsolete_when:
- Codex can reliably create and verify codebase maps without explicit file/symbol citations or user review.
- Official Codex guidance no longer recommends inspecting relevant code before editing unfamiliar areas.

related_topics:
- vcb.chapter.context_management
- vcb.chapter.plan_first_code_second
- vcb.chapter.git_discipline
- vcb.chapter.four_part_prompt
- vcb.concepts.diff
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.workflow.unknown_codebase
- vcb.prompting.context_management
---

> Summary:
> Understanding an unknown codebase means building a small, evidence-backed map before asking Codex to change it.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.understanding_unknown_codebase.human -->
## 1. For the Human: Plain-Language Concept

### What this means

An unknown codebase is any project where you cannot confidently answer:

- where the feature starts,
- where data enters and leaves,
- what files matter,
- how to run it,
- how to test it,
- what must not break.

Codex can help you understand it quickly, but only if you make it explore before editing. Do not ask for a rewrite when you do not yet know what the existing code is doing.

The first job is not “fix it.” The first job is “show me the map.”

### Why it matters

Unknown codebases hide traps:

- duplicated logic,
- framework conventions,
- old compatibility behavior,
- hidden tests,
- fragile deploy scripts,
- side effects in files that look harmless,
- auth or billing rules that are not obvious from one file.

A vibe coder can move very fast in a new repo. That is useful for exploration and dangerous for production code. Speed without a map creates large diffs that are hard to review and harder to roll back.

### The mental model

Think of the repo like a building you have never entered.

A bad approach is walking in with a sledgehammer because one wall looks ugly.

A better approach is asking Codex to draw the floor plan first:

```text
Start read-only. Find the entrypoints, data flow, commands, tests, and risky areas. Cite exact files and symbols. Do not edit yet.
```

The map does not need to be perfect. It needs to be good enough to avoid changing the wrong thing.

### What Codex should map first

Ask for a compact report:

| Area | What to ask Codex for |
|---|---|
| Entrypoints | app start, routes, CLI commands, API handlers, background jobs |
| Package manager | install command, build command, test command, scripts |
| Data flow | where request/input enters, how it moves, where output is produced |
| State | database, cache, files, browser state, external APIs |
| Tests | test framework, nearest tests, how to run relevant tests |
| Conventions | naming, folder structure, existing patterns |
| Risks | auth, payments, user data, migrations, deployment config, secrets |
| Unknowns | what Codex could not determine from inspection |

### Good first prompt

```text
Read-only codebase tour. Do not edit files.

Goal:
Help me understand how [feature/area] works.

Context:
I am new to this repo. Start at the repo root and inspect only relevant files.

Constraints:
- cite exact files and symbols for every claim,
- distinguish facts from guesses,
- do not propose a broad rewrite,
- do not edit files.

Done when:
Return a compact map with entrypoints, data flow, relevant tests, commands, risks, and unknowns.
```

### Good output from Codex

Good output sounds like:

```text
The request starts in src/routes/account.ts at updateAccount().
That calls src/services/accounts.ts:updateProfile().
Validation lives in src/validation/account.ts.
The nearest tests are tests/account-update.test.ts.
Unknown: I did not find coverage for failed validation messages.
Risk: this path writes user profile data and touches auth session refresh.
```

Bad output sounds like:

```text
This is a standard React/Express app. I can modernize the architecture.
```

That is a generic guess. It is not a codebase map.

### Checklist before editing

Before asking Codex to modify an unknown repo, require:

- current `git status` understood,
- relevant files identified,
- entrypoint found,
- nearest tests found or absence noted,
- commands known or absence noted,
- risks listed,
- unknowns listed,
- first slice scoped.

If the repo touches real users, data, auth, payments, or deployment, start in read-only mode and get the map first.
<!-- VCB:END_SECTION id=vcb.chapter.understanding_unknown_codebase.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.understanding_unknown_codebase.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to use Codex as a codebase scout before using it as an implementer.

The human should leave this topic knowing that architecture summaries without file evidence are weak, and that exploration should produce a scoped next change.

### Diagnose the human’s current model

Watch for:

- “Just make this work” in a repo the human has never read.
- Requests to refactor before identifying call sites.
- Trusting framework guesses over inspected files.
- Confusing a high-level folder summary with actual data flow.
- Asking Codex to edit in a dirty working tree without knowing existing changes.
- Ignoring tests because the repo is unfamiliar.

### Explanation strategy

Use this sequence:

1. **Freeze edits.** Start read-only.
2. **Map the path.** Entrypoint → call chain → state → output.
3. **Name evidence.** File, symbol, command output, test file.
4. **List unknowns.** Do not let Codex hide uncertainty.
5. **Choose one safe slice.** Move to Chapter 12 only after the map exists.

Do not bury the intervention in politeness. Say:

```text
Do not edit yet. This repo is unknown, so the first deliverable is an evidence-backed map.
```

### Useful metaphors

- **Tour guide before contractor:** you do not renovate a building before finding the load-bearing walls.
- **Trail map:** the repo map is not the hike; it keeps you from walking off a cliff.
- **X-ray before surgery:** inspection comes before cutting.

### Coaching tactics

Ask Codex to produce a table with columns:

```text
Claim | Evidence file/symbol | Confidence | Unknowns | Risk
```

Then coach the human to challenge weak rows.

If the user is budget-constrained, keep exploration narrow:

```text
Inspect only the files needed to explain the checkout route. Do not scan the whole repo unless blocked.
```

If the user is high-throughput and the repo is large, allow parallel read-only exploration only when agents stay read-only and produce cited findings.

### Prompt patterns

#### Unknown feature map

```text
Read-only. Map how [feature] works.
Return:
- entrypoints,
- call/data flow,
- state touched,
- external services,
- nearest tests,
- run commands,
- risks,
- unknowns,
- smallest safe first change.
Cite files and symbols for each factual claim.
```

#### Call-site search

```text
Do not edit. Find every call site for [function/component/API].
Classify each call site as primary path, test, fallback, legacy, or unknown.
Explain what would break if the signature changed.
```

#### Repo onboarding summary

```text
I am new to this repo. Create a one-page onboarding map for this area only.
Avoid generic framework explanation. Ground every claim in inspected files.
```

### Red flags to call out directly

- “Codex did not cite files.”
- “The plan assumes a framework pattern but has not checked this repo.”
- “The proposed change crosses too many boundaries for an unknown codebase.”
- “The repo map does not mention tests, commands, or rollback.”
- “The working tree is dirty; editing now may mix human changes with Codex changes.”

### Exercises

1. Ask Codex to map one feature without editing.
2. Ask it to identify the smallest safe first change.
3. Ask it to state what it does not know.
4. Compare its claims against actual files.
5. Only then move to implementation.
<!-- VCB:END_SECTION id=vcb.chapter.understanding_unknown_codebase.ai_coach -->

## Shortcut Reality

### The ideal practice

Start read-only. Build a cited map. Identify tests and commands. Then make one small change on a branch.

### What users often do instead

They open an unfamiliar repo, paste a vague feature request, and let Codex edit before anyone understands the code path.

### When the shortcut may be fine

Editing before understanding may be acceptable when:

- the repo is disposable,
- the change is tiny and local,
- the file is obvious,
- the working tree is clean,
- no real users, data, secrets, payments, auth, or deploy config are involved,
- recovery is a simple revert.

Example: changing text in a throwaway demo page.

### When the shortcut is a bad idea

It is a bad trade when:

- the repo is production or shared,
- the task touches auth, payments, data deletion, migrations, or secrets,
- the change spans multiple packages,
- Codex proposes a rewrite before tracing current behavior,
- tests are missing or unknown,
- deployment is automatic from the edited branch.

### Risk profile

- Probability of failure: medium in small repos, high in large unfamiliar repos.
- Impact if it fails: low in throwaway prototypes, high in production systems.
- Ease of recovery: medium if committed first; poor if changes mix with human edits.
- Blast radius: grows with cross-boundary edits and persistent data.
- Skill needed to recover: low for one-file changes; high for data, auth, or deploy regressions.
- Hidden cost: debugging time caused by changing the wrong abstraction.

### Minimum guardrails

- Commit or stash current work first.
- Ask for a read-only map.
- Require file/symbol citations.
- Scope the first edit to one behavior path.
- Run the smallest relevant check.
- Ask Codex to list unknowns before editing.

### Recovery plan

If Codex edited too soon:

1. Stop new edits.
2. Inspect `git status` and changed files.
3. Ask Codex to classify each change as intended, accidental, or uncertain.
4. Revert accidental changes.
5. Build the missing codebase map.
6. Restart with a smaller scoped prompt.

### AI coach guidance

Do not shame the human for moving fast. Move them one guardrail up:

```text
We can still move quickly, but this repo is unknown. First get a cited map, then edit one slice. That preserves speed without turning the whole repo into the blast radius.
```

## Budget and Constraint Notes

### Cheapest reliable path

Ask for a narrow read-only map of only the relevant feature area. Do not pay for broad repo exploration unless the first map finds ambiguity.

### Fastest high-usage path

Use parallel read-only exploration for independent areas, then merge findings into one implementation plan. Keep implementation separate from exploration.

### Low-attention path

Low-attention unknown-repo work requires read-only exploration, a branch/worktree, no secrets, and a final map with file citations. Do not let Codex perform broad edits unattended.

### Production-quality path

Require a map, risk list, tests/checks, branch or PR, diff review, and rollback notes. For data/auth/payment work, add security and migration review before patching.

## Stable Core

- Understand before changing.
- File evidence beats generic architecture claims.
- Unknowns are part of the deliverable.
- The first implementation slice should follow the real code path, not the framework stereotype.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
- Exact Codex repo-exploration features.
- UI affordances for file references, selections, and codebase maps.
- Subagent visibility and default availability.
- Cloud versus local context-handling mechanics.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when Codex adds or removes codebase-onboarding workflows, built-in code maps, read-only exploration agents, or repo-analysis summaries that change how users inspect unfamiliar code.

## Evidence and Sources

- `openai.codex.use_cases.codebase_onboarding` — official current anchor for using Codex to map unfamiliar codebases, modules, data flow, and next files to read before editing.
- `openai.codex.workflows` — official current anchor for explicit context, relevant files, and verification in Codex workflows.
- `openai.codex.prompting` — official current anchor for prompts, context, file references, and task loop behavior.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for codebase exploration, evidence-backed claims, and risk-first sequencing.

## Related Topics

- `vcb.chapter.context_management`
- `vcb.chapter.plan_first_code_second`
- `vcb.chapter.git_discipline`
- `vcb.chapter.feature_slicing`
- `vcb.concepts.diff`
- `vcb.concepts.blast_radius`
- `vcb.concepts.recoverability`
- `vcb.workflow.unknown_codebase`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.chapter.understanding_unknown_codebase -->
