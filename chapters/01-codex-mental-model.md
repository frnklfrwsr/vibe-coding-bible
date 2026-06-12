<!-- VCB:BEGIN_TOPIC id=vcb.chapter.codex_mental_model version=0.1.0 -->
---
id: vcb.chapter.codex_mental_model
title: Chapter 1 — What Codex Actually Is
type: chapter
chapter_number: 1
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
- SDK
- Human software work

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
- emergency_hotfix

attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation

shortcut_profiles:
- vcb.shortcut.one_big_prompt
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.unattended_long_runs
- vcb.shortcut.broad_agent_permissions

durable_principles:
- Codex is an agent loop, not magic autocomplete.
- Repo context, tools, constraints, checks, and feedback make Codex useful.
- Codex output is a patch proposal until the diff and checks support it.
- Vague tasks produce fragile work because the agent must invent missing intent.

likely_to_change:
- current product surfaces
- exact UI entrypoints
- model routing
- app/cloud/IDE/CLI feature names
- plan packaging and access details

obsolete_when:
- Codex no longer operates through inspect, plan, edit, run, review, and revise loops.
- OpenAI materially redefines Codex from a coding agent into a different product class.

related_topics:
- vcb.chapter.how_to_use_this_bible
- vcb.chapter.vibe_coder_advantage_and_risk
- vcb.chapter.codex_surfaces
- vcb.concepts.diff
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.concepts.rollback
- vcb.prompting.four_part_prompt
- vcb.prompting.plan_first
- vcb.workflow.reviewing_diffs
- vcb.safety.sandboxing_and_approvals
---

> Summary:
> Codex is best understood as a repo-aware coding agent: it reads files, edits files, runs tools, inspects feedback, and revises. Treat its work as a fast patch proposal, not as truth.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.codex_mental_model.human -->
## 1. For the Human: Plain-Language Concept

### What Codex is

Codex is a coding agent. That means it can do more than answer questions about code. In the right surface, it can inspect a repository, edit files, run commands, read command output, revise its patch, and report what changed.

A plain ChatGPT answer gives you code in the chat. Codex works closer to the actual project. It can look at the codebase you already have and produce a patch against that codebase.

The practical difference is this:

| Tool shape | What it usually gives you | Main risk |
|---|---|---|
| Chat answer | explanation or code snippet | not grounded in your repo |
| Autocomplete | next lines inside the editor | local context only |
| Codex task | repo-aware patch, commands, and report | larger changes faster, including larger mistakes |
| GitHub review | review signal on a pull request | useful signal, not merge approval |

### The mental model

Think of Codex as a junior engineer with power tools.

A junior engineer needs a clear task, context, constraints, and a definition of done. Power tools matter because Codex can move much faster than a human junior engineer. That speed is useful when the job is bounded. It is dangerous when the task is vague, the project is risky, or the agent has too much authority.

The right question is not “Can Codex write code?” It can. The right question is:

```text
Did I give Codex enough context and boundaries for this patch to be safe, reviewable, and testable?
```

### The agent loop

A good Codex task usually follows this loop:

1. **Intent:** You describe the outcome.
2. **Context:** Codex inspects relevant files, logs, tests, docs, or examples.
3. **Plan:** Codex decides the smallest reasonable change.
4. **Patch:** Codex edits files.
5. **Verification:** Codex runs checks or explains why it could not.
6. **Review:** You inspect the diff, not just the final message.
7. **Recovery:** You keep a branch, commit, rollback path, or other undo plan.
8. **Learning:** Repeated corrections become durable repo guidance later.

Codex is strongest when that loop is visible. It is weakest when you ask for a vague result and accept whatever comes back.

### What Codex is not

Codex is not a mind reader. It does not automatically know your product taste, your user promises, your security requirements, your production risks, or which old behavior must remain compatible.

Codex is also not proof. A confident final message is still a claim. The evidence is the diff, command output, tests, logs, screenshots, and behavior you can inspect.

### What good Codex use looks like

Good Codex use sounds like this:

```text
Goal: Add a small empty-state message to the dashboard.
Context: Use the existing DashboardPage component and design tokens. Do not change data fetching.
Constraints: No new dependencies. Keep behavior unchanged except the empty state.
Done when: The dashboard shows the empty state when there are no projects, existing tests still pass, and the final report lists changed files.
```

Bad Codex use sounds like this:

```text
Build me a SaaS app. Make it good.
```

That prompt may produce something impressive. It will also force Codex to invent product requirements, architecture, security posture, styling, billing rules, and data model assumptions.

### The key shift for vibe coders

Vibe coding is not “let AI do everything.” It is fast product-driven building. Codex gives you leverage, but leverage needs a control loop.

Use Codex for speed. Use diffs, checks, constraints, and rollback to stop speed from becoming accidental damage.

<!-- VCB:END_SECTION id=vcb.chapter.codex_mental_model.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.codex_mental_model.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Move the human from “AI writes code” to “Codex proposes repo-aware patches inside an engineering control loop.” The important teaching target is not syntax. It is task framing, evidence, and risk control.

### Diagnose the human’s current model

Ask or infer:

- Are they treating Codex like autocomplete, chat, or an autonomous engineer?
- Did they provide goal, context, constraints, and done-when criteria?
- Are they asking for a patch or a product fantasy?
- Does the task touch production, auth, payments, secrets, migrations, or user data?
- Is there a clean Git checkpoint or branch?
- Do they plan to review the diff?

### Explanation strategy

Use this sequence:

1. **Name the agent loop.** “Codex reads, edits, runs, checks, and revises.”
2. **Separate claim from evidence.** “The final summary is a claim; the diff and checks are evidence.”
3. **Calibrate by risk.** Small prototype: lightweight guardrail. Production/auth/data: strict guardrail.
4. **Convert vague asks into observable tasks.** Force a done-when condition.
5. **Avoid overexplaining product surfaces.** Surface mechanics belong in `vcb.chapter.codex_surfaces`; setup/config belongs later.

### Useful metaphors

- **Junior engineer with power tools:** helpful, fast, but needs scope and review.
- **Patch proposal, not verdict:** Codex submits work; the repo and checks judge it.
- **Slot machine versus workshop:** vague prompts pull a lever; scoped prompts use tools.

### Coaching tactics

When the human says “Codex built it,” ask:

```text
What changed, what evidence says it works, and how do we undo it if it is wrong?
```

When the human says “It says it passed,” ask:

```text
Which command passed, and did the output come from the current repo state?
```

When the human asks for a giant build, respond with:

```text
That is too broad for a safe first patch. I will split it into a product sketch, a technical plan, and the smallest vertical slice.
```

### Prompt patterns

```text
Before editing, inspect the repo and summarize the existing pattern.
Then propose the smallest patch.
Do not add dependencies.
Run the smallest relevant check.
Report changed files, check results, assumptions, and remaining risks.
```

```text
Treat this as a patch proposal, not a final answer.
After you edit, give me:
- the diff summary,
- risky files touched,
- checks run,
- what you did not verify,
- rollback steps.
```

### Red flags to call out directly

- The task is broad and has no acceptance criteria.
- The user wants to skip diff review on a large change.
- Codex added packages without explaining why.
- Codex changed auth, billing, migrations, deployment, or secrets as a side effect.
- The user is using unattended work for an ambiguous production change.
- The user is trusting a final summary without evidence.

### Exercises

1. Take a vague app request and rewrite it into goal/context/constraints/done-when.
2. Ask the human to classify a task by blast radius and recoverability before using Codex.
3. Have the human inspect one Codex diff and identify one change the final summary did not mention.

<!-- VCB:END_SECTION id=vcb.chapter.codex_mental_model.ai_coach -->

## Shortcut Reality

### The ideal practice

The ideal practice is to give Codex a scoped task with relevant context, explicit constraints, a clear done-when condition, and a verification plan. Then review the diff before accepting or merging.

### What users often do instead

Users ask Codex to “build the thing,” “fix everything,” or “make it better,” then trust the final message because the output looks professional.

### When the shortcut may be fine

A broad prompt can be fine when:

- the project is disposable,
- the repo is new or throwaway,
- no real users, money, secrets, or persistent data are involved,
- the output is treated as a sketch,
- the human expects to rebuild or heavily revise it.

### When the shortcut is a bad idea

The shortcut is a bad trade when:

- the system is already in production,
- the task touches auth, payments, data deletion, migrations, deployment, or secrets,
- the diff is too large to review,
- the user cannot explain what changed,
- rollback is unclear.

### Risk profile

- Probability of failure: medium for vague tasks; higher when the repo is unfamiliar.
- Impact if it fails: low in prototypes; high in production or data-sensitive systems.
- Ease of recovery: high with a branch and clean checkpoint; low without Git or backups.
- Blast radius: depends on files, permissions, and deployment coupling.
- Skill needed to recover: low for isolated UI changes; high for data/security incidents.
- Hidden cost: cleanup, dependency removal, architecture repair, and false confidence.

### Minimum guardrails

- Start from a clean Git state.
- Use a branch or isolated worktree for broad tasks.
- Ask for a plan before editing.
- Forbid auth, payments, secrets, deployment config, and migrations unless explicitly in scope.
- Require changed-files summary and checks run.
- Review the diff before accepting.

### Recovery plan

If the shortcut goes wrong:

1. Stop new edits.
2. Inspect `git status` and changed files.
3. Separate intended changes from accidental changes.
4. Keep useful isolated pieces if possible.
5. Restore or revert unsafe changes.
6. Rewrite the task as a smaller patch with explicit constraints.

### AI coach guidance

Do not moralize about the shortcut. Name the tradeoff.

```text
This broad prompt may be fine as a prototype sketch. It is not safe as a production patch. The minimum safer version is: put it on a branch, forbid sensitive areas, ask for a plan first, and review the diff afterward.
```

## Budget and Constraint Notes

### Cheapest reliable path

Spend human attention to save agent usage. Think through the task first, provide only relevant context, ask for the smallest patch, and run the smallest meaningful check.

### Fastest high-usage path

Use Codex for planning, implementation, and review in separate passes when the work is recoverable. Run parallel attempts only when branches/worktrees isolate the changes and the human will review the winner.

### Low-attention path

Low attention is acceptable only when the task is isolated, reversible, and has clear stop conditions. Use branches/worktrees, no secrets, no production settings, and a required final report.

### Production-quality path

Use plan-first, branch/worktree isolation, tests or checks, diff review, independent review for risky changes, and a rollback path. Spend both usage and human attention.

## Stable Core

- Codex works best with context, constraints, tools, and verification.
- The diff is the evidence; the final summary is a claim.
- Small scoped tasks are more reviewable than large vague tasks.
- Risk is controlled by blast radius, recoverability, and check quality.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Current Codex product surfaces, feature names, platform support, plan packaging, model routing, and exact UI flows are volatile. Use official OpenAI docs and the Codex changelog before writing surface-specific instructions.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when:

- OpenAI changes the official definition or positioning of Codex.
- Codex surfaces merge, split, or gain materially different autonomy defaults.
- Codex verification, review, or sandbox behavior changes enough to alter the agent-loop model.
- Model reliability changes enough that current risk advice needs recalibration.

## Evidence and Sources

- `openai.codex.overview` — Official OpenAI source for Codex as a coding agent and high-level capability framing.
- `openai.codex.best_practices` — Official OpenAI source for context, reusable guidance, validation, and review practices.
- `openai.codex.llms_txt` — Official OpenAI source-map pattern for Codex documentation.
- `openai.help.truthfulness` — Official OpenAI caveat that language models can produce confident incorrect output.
- `openai.hallucinations` — Official OpenAI research framing for hallucination and guessing incentives.
- `vcb.synthesis.stable_engineering_practice` — VCB synthesis layer for durable engineering control-loop framing; not a product-behavior source.

## Related Topics

- `vcb.chapter.how_to_use_this_bible`
- `vcb.chapter.vibe_coder_advantage_and_risk`
- `vcb.chapter.codex_surfaces`
- `vcb.concepts.diff`
- `vcb.concepts.blast_radius`
- `vcb.concepts.recoverability`
- `vcb.concepts.rollback`
- `vcb.prompting.four_part_prompt`
- `vcb.workflow.reviewing_diffs`
- `vcb.safety.sandboxing_and_approvals`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.codex_mental_model -->
