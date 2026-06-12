<!-- VCB:BEGIN_TOPIC id=vcb.chapter.sandboxing_and_approvals version=0.1.0 -->
---
id: vcb.chapter.sandboxing_and_approvals
title: Chapter 5 — Sandboxes, Approvals, and Why Full Access Is Usually a Bad Default
type: chapter
chapter_number: 5
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
- local commands
- package managers
- MCP tools
- repositories with secrets or production access

source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: CODEX_FEATURE
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
- vcb.shortcut.broad_agent_permissions
- vcb.shortcut.unattended_long_runs
- vcb.shortcut.unofficial_tools

durable_principles:
- Sandboxes define technical boundaries; approvals decide when Codex must ask before crossing them.
- More access is not automatically more productive; it increases blast radius.
- Broad permissions are acceptable only when isolation, fake data, and rollback make damage recoverable.
- Real secrets, production data, money movement, and destructive commands require harder boundaries.

likely_to_change:
- exact sandbox mode names
- approval policy syntax
- auto-review behavior
- permission-profile schema
- OS-specific sandbox enforcement
- protected path rules
- MCP approval handling

obsolete_when:
- Codex no longer uses sandbox and approval controls for local commands.
- OpenAI materially changes permission defaults or approval semantics.
- official docs replace sandbox/approval concepts with a new permission model.

related_topics:
- vcb.chapter.installing_and_configuring_codex
- vcb.chapter.git_discipline
- vcb.chapter.codex_surfaces
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.concepts.rollback
- vcb.safety.permissions
- vcb.safety.secrets
- vcb.safety.sandboxing_and_approvals
- vcb.shortcut.broad_agent_permissions
---

> Summary:
> Sandboxes and approvals are how you give Codex useful autonomy without handing it your whole machine. The right default is bounded access, not maximum access.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.sandboxing_and_approvals.human -->
## 1. For the Human: Plain-Language Concept

### The simple distinction

A **sandbox** is the fence.

An **approval policy** is the gatekeeper.

The sandbox controls what Codex can do by itself: which files it can modify, whether commands can reach the network, and whether commands can operate outside the project boundary. The approval policy controls when Codex must stop and ask before crossing a boundary.

Official OpenAI docs currently describe these controls as working together: the sandbox creates technical boundaries, and approvals decide when Codex must ask before going beyond them.

### Why full access is usually the wrong default

Full access feels fast because Codex stops asking questions. The problem is that it can also make the wrong thing happen faster.

A dangerous setup is:

```text
broad filesystem access + network access + real secrets + no approvals + vague task
```

That combination gives Codex enough room to damage code, leak credentials, modify files outside the repo, install unreviewed packages, or run destructive commands before you notice.

A safer setup is:

```text
project-limited access + approvals for boundary-crossing actions + clean Git checkpoint + no real secrets in reach
```

That still lets Codex work. It just keeps the blast radius legible.

### What Codex might need permission to do

Codex work often involves more than file edits:

- read files,
- write files,
- run tests,
- run package managers,
- install dependencies,
- access the network,
- call MCP tools,
- invoke shell commands,
- touch Git state,
- edit config files,
- run database migrations.

Not all actions have the same risk. Reading a local source file is not the same as running a shell script from the internet. Running unit tests is not the same as applying a production migration.

### Current official permission model is volatile

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Official OpenAI docs currently document sandboxing, approval policies, protected paths, network controls, auto-review behavior, and permission-profile configuration. Exact mode names, flags, defaults, OS behavior, and config syntax are volatile and must be rechecked before writing operational instructions.
<!-- VCB:END_VOLATILE_INFO -->

### Permission choice by project risk

| Project situation | Better default |
|---|---|
| Throwaway prototype with fake data | broader permissions may be acceptable if isolated |
| Personal local tool | project-limited write access; ask for network/package installs |
| Shared repo | branch/worktree isolation; approvals for risky commands |
| Public app | strict boundaries, reviews, tests, rollback path |
| Auth/payment/data-sensitive system | least privilege, fake/staging data, no broad no-approval runs |
| Main personal machine with secrets | do not use broad full access as the default |

### The clean mental model

Codex should be able to move freely inside the safe work area and stop at the edge.

That edge should become stricter when the task touches:

- secrets and `.env` files,
- production credentials,
- user data,
- payments and billing,
- auth and authorization,
- database migrations,
- deployment config,
- package installs,
- destructive Git commands,
- unknown shell scripts.

### What good looks like

Good permission design looks like this:

- the repo is isolated,
- Codex has enough access to edit intended files,
- risky commands require approval,
- secrets are not available unless strictly needed,
- package installs are reviewed,
- migrations are explicit and staged,
- broad autonomy runs only in branches/worktrees/containers/VMs,
- final output is reviewed through diff and checks.

### What bad looks like

Bad permission design looks like this:

- Codex can see your whole home directory,
- `.env` files contain real secrets in the workspace,
- network access is open for vague tasks,
- package installs run without review,
- production databases are reachable,
- destructive commands run without a human seeing them,
- the user says “just do whatever it takes.”

That last sentence is not a productivity strategy. It is an incident waiting for a trigger.

<!-- VCB:END_SECTION id=vcb.chapter.sandboxing_and_approvals.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.sandboxing_and_approvals.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach bounded autonomy. The user should understand that the goal is not to block Codex. The goal is to let Codex work inside a boundary where mistakes are recoverable.

### Diagnose the permission risk

Ask:

- Is this project disposable, personal, shared, public, or production?
- Are real secrets present in the workspace?
- Can Codex reach production services?
- Does the task require network access?
- Does it require package installs?
- Does it touch migrations, auth, billing, deployment, or data deletion?
- Will the user supervise continuously or review later?
- Is there a Git checkpoint or branch?

### Explanation strategy

Do not say “never use full access.” That is too blunt and false. Say what is true:

```text
Full access is a bad default on a normal machine with secrets. It can be reasonable inside a disposable environment with fake credentials and a clean rollback path.
```

### Useful metaphors

- **Fenced yard:** Codex can run freely inside the fence; it asks before leaving.
- **Workshop key:** give access to the workshop, not the whole building.
- **Firebreak:** isolation keeps one mistake from spreading into production, credentials, or personal files.

### Coaching tactics

For prototype work:

```text
You can loosen permissions if this is a disposable repo with fake data. Keep it isolated and commit first.
```

For production work:

```text
Do not use broad no-approval access here. This touches real users/data/money. Use least privilege, require approvals for boundary-crossing commands, and keep a rollback plan.
```

For package installs:

```text
Before approving this install, ask why the dependency is needed, whether an existing package can do it, and what files/lockfiles will change.
```

For network access:

```text
Network access is not just a convenience. It can fetch untrusted scripts, leak data, or change dependency behavior. Approve only the specific need.
```

### Prompt patterns

#### Permission selection prompt

```text
Help me choose safe Codex permissions for this task.

Project type:
Data/secrets present:
Task goal:
Commands likely needed:
Network needed? yes/no/unknown
Package installs needed? yes/no/unknown
Production systems reachable? yes/no
Human attention: continuous / periodic / review later
Rollback path:

Recommend the least permissive setup that still lets the task progress.
List what should require approval.
```

#### Broad-permission harm-reduction prompt

```text
I want a low-friction run. Help me reduce blast radius.

Assume I may use broader permissions, but require:
- isolated repo/worktree/container/VM,
- fake credentials,
- no production services,
- clean Git checkpoint,
- final diff summary,
- list of commands run,
- no package installs or migrations without explicit approval.
```

### Red flags to call out directly

- The user wants no approvals while real secrets are present.
- Codex can access production credentials or production databases.
- The task is vague and broad but permissions are also broad.
- Codex asks to run a remote install script without explanation.
- Codex wants to modify deployment config, auth policy, billing logic, or migrations without a plan.
- A low-attention run is combined with high blast radius.

### Exercises

1. Classify five commands by risk: test command, package install, `curl | sh`, migration, delete command.
2. Ask the human to draw the sandbox boundary in words: “Codex can touch X but not Y.”
3. Convert a risky broad-access request into an isolated run with fake credentials.
4. Practice saying no to a permission request and asking Codex for a safer path.

<!-- VCB:END_SECTION id=vcb.chapter.sandboxing_and_approvals.ai_coach -->

## Shortcut Reality

### The ideal practice

Use the least permission needed for the task, escalate only when necessary, keep secrets out of reach, and use branches/worktrees or disposable environments for broad autonomy.

### What users often do instead

They disable prompts or grant broad access because approvals feel annoying.

### When the shortcut may be fine

Broad permissions may be acceptable when:

- the environment is disposable,
- credentials are fake,
- no production systems are reachable,
- no personal files are in scope,
- the task is recoverable,
- a Git checkpoint or snapshot exists,
- the final diff and command list will be reviewed.

### When the shortcut is a bad idea

Broad permissions are a bad trade when:

- real secrets are present,
- user data or production services are reachable,
- the task is ambiguous,
- the human will not supervise,
- Codex may run package installs, migrations, or deployment commands,
- the machine contains personal files outside the repo.

### Risk profile

- Probability of failure: medium; higher when permissions and task scope are both broad.
- Impact if it fails: potentially severe because failure can leave the project boundary.
- Ease of recovery: high in disposable environments; low if secrets leak or production data changes.
- Blast radius: controlled by filesystem, network, credentials, production access, and Git isolation.
- Skill needed to recover: low for a bad local patch; high for credential leaks or data incidents.
- Hidden cost: cleanup, credential rotation, dependency audit, incident response, and lost trust.

### Minimum guardrails

- Use a disposable VM/container/worktree for broad runs.
- Remove or fake `.env` secrets.
- Disable production service access.
- Commit or snapshot first.
- Require approval for package installs, network, migrations, destructive Git commands, and deployment changes.
- Review changed files and commands run.

### Recovery plan

If broad access causes trouble:

1. Stop Codex immediately.
2. Disconnect production credentials or network if relevant.
3. Inspect changed files and command history.
4. Revert local code changes from Git where possible.
5. Rotate any exposed credentials.
6. Audit package/dependency changes.
7. Check whether data or deployment state changed.
8. Add a stricter permission profile before retrying.

### AI coach guidance

```text
I will not pretend broad permissions never help. They do reduce friction. But this environment has real secrets and production reach, so the blast radius is too large. Use an isolated workspace with fake credentials, or keep approvals on for boundary-crossing actions.
```

## Budget and Constraint Notes

### Cheapest reliable path

Use stricter defaults and approve only specific requests. This spends more human attention but avoids costly cleanup and wasted usage.

### Fastest high-usage path

Use broader autonomy only in isolated branches/worktrees/containers where the user can review later. Spend usage on progress, not on incident recovery.

### Low-attention path

Low-attention work requires isolation. Do not combine low attention with production credentials, real user data, or broad network/filesystem access.

### Production-quality path

Use least privilege, explicit approvals, clean Git checkpoints, no real secrets in local agent reach unless required, staged migrations, and independent review for sensitive areas.

## Stable Core

- Boundaries make autonomy safer.
- More access increases blast radius.
- Secrets and production data change the risk category.
- Isolation converts some high-risk shortcuts into recoverable experiments.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Codex sandbox modes, approval-policy names, permission-profile syntax, auto-review behavior, OS enforcement details, protected paths, and MCP/tool approval mechanisms are volatile. Re-check official OpenAI sandbox, agent approvals/security, permissions, rules, and changelog docs before writing exact operational steps.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when:

- OpenAI changes sandbox defaults, mode names, or approval policies.
- permission profiles replace or materially change older sandbox settings.
- auto-review behavior changes.
- OS-level sandbox support changes.
- Codex gains new tool or network capabilities that alter blast radius.

## Evidence and Sources

- `openai.codex.sandboxing` — Official source for sandbox boundaries and relationship to approvals.
- `openai.codex.agent_approvals_security` — Official source for approval behavior, protected paths, and broad/no-approval caution anchors.
- `openai.codex.permissions` — Official source for permission profile compatibility and configuration caveats.
- `openai.codex.rules` — Official source for rules and allow-list behavior.
- `openai.codex.auto_review` — Official source for auto-review as approval reviewer swap, not a permission expansion.
- `openai.codex.windows` — Official source for Windows sandbox notes and safer automation guidance.
- `openai.codex.changelog` — Official source for sandbox/approval changes.
- `vcb.synthesis.stable_engineering_practice` — VCB synthesis for least-privilege and blast-radius framing; not a product-behavior source.

## Related Topics

- `vcb.chapter.installing_and_configuring_codex`
- `vcb.chapter.git_discipline`
- `vcb.chapter.codex_surfaces`
- `vcb.concepts.blast_radius`
- `vcb.concepts.recoverability`
- `vcb.concepts.rollback`
- `vcb.safety.permissions`
- `vcb.safety.secrets`
- `vcb.safety.sandboxing_and_approvals`
- `vcb.shortcut.broad_agent_permissions`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.sandboxing_and_approvals -->
