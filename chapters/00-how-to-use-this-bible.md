<!-- VCB:BEGIN_TOPIC id=vcb.chapter.how_to_use_this_bible version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-08'
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
id: vcb.chapter.how_to_use_this_bible
title: Chapter 0 — How to Use This Bible
type: chapter
chapter_number: 0
next_review_due: '2026-12-08'
source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_profiles:
- vcb.shortcut.one_big_prompt
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.unattended_long_runs
durable_principles:
- retrieve the smallest useful unit
- separate stable principles from volatile product details
- treat AI output as a patch proposal until verified
- route by task, concept, failure mode, budget, and risk
likely_to_change:
- LLM ingestion conventions
- exact Codex documentation map shape
- AI retrieval tooling and product surfaces
obsolete_when:
- the repository no longer uses topic cards, indexes, source registers, and retrieval
  stop markers as the control layer
related_topics:
- vcb.concepts.diff
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.concepts.rollback
- vcb.concepts.git_branch
- vcb.concepts.pull_request
- vcb.index.task
- vcb.index.concept
- vcb.index.ai_coaches
- vcb.register.sources
---

> Summary:
> Use this Bible as an operating manual, not as a linear book. Start from the problem you are facing, retrieve the smallest relevant topic card, apply the guardrails, and stop when the retrieval marker says the topic is complete.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.how_to_use_this_bible.human -->
## 1. For the Human: Plain-Language Concept

### What this Bible is

This is not a normal book. It is a living operating manual for building software with Codex and other AI tools.

A normal book expects you to start at page one and keep reading. This Bible expects you to arrive with a job:

- “Codex changed too much.”
- “I do not understand this diff.”
- “I want to ship fast without breaking production.”
- “I need to know whether skipping tests is acceptable here.”
- “I need my AI coach to explain branches, rollback, or pull requests.”

Start with the task, not the table of contents.

### The mental model

Think of the Bible like a map in a workshop.

You do not read the whole map before picking up a tool. You check the part of the map that tells you where the sharp edges are, what tool fits the job, and how to undo damage if the cut goes wrong.

The Bible has three layers:

1. **Chapters** give you the larger story.
2. **Topic cards** give you the exact concept or workflow.
3. **Indexes and registers** route humans and AI coaches to the right place.

### How to use it while actively building

Use this loop:

1. **Name the job.** What are you trying to do right now?
2. **Pick the smallest route.** Use an index before reading a chapter.
3. **Read the relevant topic card.** Do not over-retrieve.
4. **Apply the guardrail.** Commit, branch, review diff, run a check, or reduce blast radius.
5. **Stop.** Continue only if the topic links to a needed related topic.

### How to cite the Bible to an AI

Use the topic ID. Example:

```text
Use vcb.concepts.diff and vcb.concepts.blast_radius.
Explain this change to me in plain language, then help me decide whether it is safe to accept.
```

The topic ID matters because titles drift, UI labels change, and search can return too much. IDs give the AI a stable target.

### Evidence levels in plain English

| Evidence level | Plain meaning | How to treat it |
|---|---|---|
| `E0_OFFICIAL_DOCS` | Official source | Strongest for product behavior and vendor claims |
| `E1_OFFICIAL_COOKBOOK` | Official example | Useful, but may not fit every repo |
| `E2_REPRODUCED_LOCALLY` | Tested by maintainers | Good local evidence; check scope |
| `E3_EXPERT_REPORT` | Named expert report | Useful, not universal |
| `E4_COMMUNITY_FIELD_REPORT` | User/community report | Treat as anecdote until tested |
| `E5_SPECULATIVE` | Prediction or unverified tactic | Experimental; do not build critical process on it |

### Stable versus volatile guidance

Some advice is durable: use Git, review diffs, reduce blast radius, write down acceptance criteria, and make rollback possible.

Some advice decays: pricing, limits, model names, UI labels, commands, exact feature behavior, and third-party tool plans.

Do not treat volatile product details as timeless rules. The Bible separates them so future AI coaches can update the changing parts without corrupting the stable engineering ideas.

### What good use looks like

Good use:

```text
I am about to accept a Codex change.
I will read vcb.concepts.diff, check the file list, look for risky areas, and then decide whether I need vcb.concepts.rollback.
```

Bad use:

```text
I asked Codex to build the whole app. Its final message says it is done. I will ship it.
```

That is not confidence. That is skipping the control loop.

### Checklist

Before using any advice from this Bible, ask:

- Is this a prototype, MVP, production build, maintenance task, or emergency hotfix?
- Does this touch real users, money, secrets, auth, deployment, or persistent data?
- Can I undo the change quickly?
- Is the source official, field practice, local reproduction, or speculation?
- Is the claim stable, or does it need current verification?
<!-- VCB:END_SECTION id=vcb.chapter.how_to_use_this_bible.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.how_to_use_this_bible.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to use the Bible as a retrieval-and-control system. Do not force a linear reading path. Route to the smallest useful topic, apply the relevant guardrail, and stop when the topic is complete.

### Source precedence

Use this precedence order:

1. **Local repo evidence** for what this project actually does.
2. **Official OpenAI documentation** for current Codex behavior.
3. **Official vendor documentation** for Git, GitHub, hosting, databases, auth, payments, and pricing.
4. **Maintainer local reproduction** for tested Bible claims.
5. **Expert and community field reports** as labeled tactics, not official truth.
6. **Speculation** only as watchlist material.

Do not let a community trick override official product behavior. Do not let official product docs override what the local repo demonstrably does.

### Retrieval strategy

Use exact topic IDs. Prefer topic cards over chapters when the user has a narrow problem.

Examples:

| User behavior | Route first |
|---|---|
| Trusting Codex’s final message | `vcb.concepts.diff` |
| Wanting to move fast | `vcb.concepts.blast_radius`, `vcb.concepts.recoverability` |
| Asking “can I undo this?” | `vcb.concepts.rollback`, `vcb.concepts.recoverability` |
| Working directly on main | `vcb.concepts.git_branch` |
| Asking whether to merge | `vcb.concepts.pull_request`, `vcb.concepts.diff` |

### Adapt to skill level

For a beginner, translate jargon immediately. A diff is “tracked changes for code.” A branch is “a parallel timeline.” A pull request is “a proposed change with review.”

For an experienced developer, skip the metaphor sooner and focus on failure modes: scope creep, hidden side effects, test weakening, migration risk, credential exposure, and rollback path.

### Diagnostic questions

Ask these before giving process-heavy advice:

- What are you trying to change?
- Is this local-only, staging, or production?
- Is there a clean Git checkpoint?
- What would be expensive or impossible to undo?
- What evidence do we have besides Codex’s final summary?
- Is the user usage-constrained or optimizing for speed?
- Will the human supervise continuously, check periodically, or review later?

### Red flags to call out directly

- The user wants to accept a large diff without reading it.
- The task touches auth, payments, production data, secrets, migrations, deployment, or user deletion.
- The user wants long unattended work but has no branch/worktree/isolation.
- The user treats a final summary as proof.
- The user asks for current pricing, limits, model behavior, or UI steps without verification.

### Prompt patterns

```text
Use only the smallest relevant VCB topic card for this situation.
Explain the concept first, then give me the minimum guardrail and recovery plan.
Stop when the topic reaches VCB:STOP_RETRIEVAL unless a related topic is necessary.
```

```text
I am usage-constrained.
Route me to the cheapest reliable workflow.
Prefer one targeted topic card over a broad chapter.
```

```text
I want to move fast.
Classify blast radius and recoverability first.
Then tell me the smallest guardrail that makes this shortcut less dangerous.
```

### Coaching stance

Be direct. Do not moralize. Shortcuts are sometimes rational. The intervention is not “never do that.” The intervention is: identify blast radius, improve recoverability, set the minimum guardrail, and define the recovery plan.
<!-- VCB:END_SECTION id=vcb.chapter.how_to_use_this_bible.ai_coach -->

## Shortcut Reality

### The ideal practice

The ideal practice is to use the right index, retrieve the smallest applicable topic, check source status, apply the guardrail, and update durable project guidance when a lesson repeats.

### What users often do instead

Users often ask an AI for “the answer,” paste a large chunk of context, accept a confident summary, and skip the topic card that would have told them what to verify.

### When the shortcut may be fine

This may be fine for disposable prototypes, learning projects, and local-only experiments where the cost of being wrong is low and recovery is easy.

### When the shortcut is a bad idea

It is a bad idea when the work affects real users, secrets, auth, payments, production data, deployment, database migrations, or long-lived architecture.

### Risk profile

- Probability of failure: medium when users skip retrieval and verification.
- Impact if it fails: low for throwaway work; high for production systems.
- Ease of recovery: high when Git checkpoints and branches exist; low when production data or secrets are involved.
- Blast radius: determined by project context, not by how confident Codex sounds.
- Skill needed to recover: low for small local diffs; high for migrations, security mistakes, or production incidents.
- Hidden cost: stale or overbroad guidance can waste usage and human attention.

### Minimum guardrails

- Use an index instead of asking for the whole Bible.
- Prefer topic cards over broad chapters.
- Check evidence level and review date.
- Treat volatile claims as requiring current verification.
- Stop at `VCB:STOP_RETRIEVAL` unless a related topic is needed.

### Recovery plan

If the Bible or AI coach routed you poorly, name the actual task, pick a narrower index route, and retrieve only one topic card. If a shortcut failed, move to `vcb.concepts.rollback` and `vcb.concepts.recoverability` before asking for more code.

### AI coach guidance

If the user is overloaded, reduce the Bible to one action. Example: “Review the diff first. Everything else is secondary until you know what changed.”

## Budget and Constraint Notes

### Cheapest reliable path

Use one topic card and one guardrail. Avoid broad research, broad repo scans, and multi-agent reviews unless the risk justifies them.

### Fastest high-usage path

Route by task, let Codex or the AI coach inspect related cards, then use independent review for non-trivial diffs.

### Low-attention path

Low-attention use requires stricter boundaries: branch/worktree, clear done criteria, final report, changed-file list, checks run, and review-before-merge.

### Production-quality path

Use topic cards as a control layer, not motivational reading. Combine stable engineering topics with current official sources for product-specific behavior.

## Stable Core

- Retrieve the smallest useful unit.
- Use evidence, not summaries, to judge AI work.
- Separate stable engineering principles from volatile product facts.
- Treat field practice as labeled practice, not official truth.
- Align workflow with budget, attention, project phase, blast radius, and recoverability.

## Volatile Surface

- Exact LLM ingestion formats.
- Codex documentation map conventions.
- Current feature names, UI labels, limits, pricing, and model routing.
- Third-party tool capabilities and pricing.

## Obsolescence Watch

Review this chapter if:

- Codex documentation changes its LLM ingestion/export pattern.
- The repository changes from topic-card retrieval to another source architecture.
- New official OpenAI guidance changes how Codex should consume project instructions or source maps.

## Evidence and Sources

- `vcb.blueprint.v1`: governing architecture, chunking, section, and retrieval requirements.
- `openai.codex.llms_txt`: official source-map pattern for Codex documentation.
- `openai.codex.best_practices`: official guidance anchor for planning, context, constraints, done criteria, verification, and reusable guidance.

## Related Topics

- `vcb.concepts.diff`
- `vcb.concepts.blast_radius`
- `vcb.concepts.recoverability`
- `vcb.concepts.rollback`
- `vcb.concepts.git_branch`
- `vcb.concepts.pull_request`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.how_to_use_this_bible -->
