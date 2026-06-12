<!-- VCB:BEGIN_TOPIC id=vcb.chapter.installing_and_configuring_codex version=0.1.0 -->
---
id: vcb.chapter.installing_and_configuring_codex
title: Chapter 4 — Installing and Configuring Codex Without Creating a Mess
type: chapter
chapter_number: 4
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
- Local development environments
- Git repositories

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
- vcb.shortcut.using_existing_local_setup
- vcb.shortcut.skipping_setup
- vcb.shortcut.unofficial_tools

durable_principles:
- Bad setup produces bad Codex output.
- Codex should start from the right repository root with known commands and dependencies.
- User defaults, project config, profiles, and repo guidance have different jobs.
- Deterministic setup saves both human attention and agent usage.

likely_to_change:
- exact install commands
- supported operating systems and package managers
- config file keys
- configuration precedence details
- IDE settings labels
- project trust behavior
- profile syntax

obsolete_when:
- Codex no longer uses local install/config layers for CLI or IDE workflows.
- OpenAI materially changes Codex configuration discovery or project-trust behavior.
- Official install/config guidance conflicts with this chapter's setup model.

related_topics:
- vcb.chapter.codex_surfaces
- vcb.chapter.sandboxing_and_approvals
- vcb.chapter.git_discipline
- vcb.codex.cli
- vcb.codex.config
- vcb.codex.agents_md
- vcb.safety.permissions
- vcb.workflow.unknown_codebase
- vcb.concepts.git_branch
- vcb.concepts.diff
---

> Summary:
> Installing Codex is the easy part. The real setup is making sure Codex is pointed at the right repo, can run the right commands, understands the project rules, and is not wasting tokens on a broken or ambiguous environment.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.installing_and_configuring_codex.human -->
## 1. For the Human: Plain-Language Concept

### Setup is not just installation

Installing Codex gives you the tool. Configuring Codex gives it a usable workplace.

A bad setup makes Codex look dumb even when the model is capable. If Codex is in the wrong folder, missing dependencies, using the wrong package manager, unable to run tests, or following stale project instructions, it will make confident changes against a distorted version of reality.

Think of setup like giving a contractor the right house key, blueprint, tool list, and safety rules. If you hand them the wrong address, the problem is not their hammer.

### The clean setup target

A clean Codex setup answers these questions before serious editing starts:

| Question | Why it matters |
|---|---|
| What is the repository root? | Codex needs the real project boundary, not a random subfolder. |
| What package manager is used? | `npm`, `pnpm`, `yarn`, `pip`, `uv`, `cargo`, `go`, and others imply different commands and lockfiles. |
| How do you install dependencies? | Missing dependencies make tests and builds fail for the wrong reason. |
| How do you run the app? | Codex needs a way to verify behavior, not just change files. |
| How do you run checks? | Tests, lint, typecheck, and build commands turn claims into evidence. |
| What should Codex avoid? | Production config, secrets, generated files, migrations, and vendor directories often need boundaries. |

### Pick only the surfaces you need

Do not install every Codex surface just because it exists.

- Use the **IDE extension** when the work lives near open files and you want close steering.
- Use the **CLI** when terminal commands, local repo state, and exact shell control matter.
- Use the **app or cloud surfaces** when the task can be isolated, delegated, and reviewed later.

The surface choice is covered in Chapter 3. The setup rule here is simpler: install the surface that matches the work you actually do.

### Current official setup facts to re-check

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Official OpenAI docs currently describe Codex CLI as a local terminal coding agent that can read, change, and run code in a selected directory, and they describe shared local configuration layers for the CLI and IDE extension. The exact install commands, supported platforms, settings labels, config keys, and package options are volatile. Re-check official OpenAI Codex docs before copying commands into a real setup guide.
<!-- VCB:END_VOLATILE_INFO -->

### User config, project config, and profiles

Use this mental model:

| Layer | Plain meaning | Good use |
|---|---|---|
| User config | Your personal defaults | preferred approval style, default provider/model, common local tool settings |
| Project config | Rules for one repo | project-specific sandbox, commands, MCP, hooks, or workflow defaults |
| Profile | Named mode for a workflow | prototype mode, review mode, strict production mode, low-friction local mode |
| AGENTS.md | Written instructions to Codex | repo layout, conventions, commands, done criteria, do-not-touch rules |

Do not shove everything into one place. Config should control behavior. AGENTS.md should explain how to work in the project. A profile should switch modes without rewriting your defaults.

### The minimum useful setup file

A production-grade project will eventually deserve precise config and AGENTS.md. For early work, the minimum useful setup note is:

```text
Project root:
Package manager:
Install command:
Dev command:
Test command:
Typecheck/lint/build command:
Files/directories Codex should avoid:
Production-sensitive areas:
Definition of done for normal patches:
```

Put that information where Codex can see it: in your prompt, a repo guidance file, or a future AGENTS.md card when that topic is authored.

### What good setup looks like

Good setup looks boring:

- Codex starts in the correct repository root.
- Dependencies are installed or the missing install step is known.
- The app can run locally or the reason it cannot is documented.
- There is at least one meaningful check: test, typecheck, lint, build, or exact manual flow.
- Generated files, secrets, build artifacts, and vendor directories are identified.
- Repeated rules are encoded once instead of pasted into every prompt.

### What bad setup looks like

Bad setup usually looks like motion:

- Codex edits from the wrong directory.
- It guesses package-manager commands.
- It adds a second lockfile.
- It cannot run tests and proceeds anyway without saying why.
- It follows stale docs or ignores project conventions.
- It spends a long run rediscovering obvious setup facts.
- It changes config to make errors disappear instead of fixing the real cause.

### Minimal setup prompt

```text
Before changing code, inspect this repository setup.

Report:
- repo root,
- package manager and lockfiles,
- install/dev/test/typecheck/lint/build commands if discoverable,
- project guidance files such as AGENTS.md or .codex/config.toml,
- obvious setup risks,
- the smallest check you can run after the change.

Do not edit files yet.
```

<!-- VCB:END_SECTION id=vcb.chapter.installing_and_configuring_codex.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.installing_and_configuring_codex.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that setup quality is part of output quality. The goal is not “install Codex.” The goal is “make the project legible, runnable, and bounded enough for Codex to work safely.”

### Diagnose the current setup model

Ask or infer:

- Is the user inside the actual repo root?
- Is the working tree clean before Codex starts?
- Does the project have one obvious package manager or multiple conflicting lockfiles?
- Are dependencies installed?
- Is there a test, typecheck, lint, or build command?
- Is there durable project guidance such as AGENTS.md?
- Is project-local config trusted and appropriate?
- Is the user asking for production-quality work before the environment is reproducible?

### Explanation strategy

Use this line when the user is frustrated with poor Codex output:

```text
Codex can only work from the project reality it can see. Right now the setup is blurry, so it is guessing. First make the repo root, commands, dependencies, and boundaries explicit.
```

### Useful metaphors

- **Wrong address:** starting Codex in the wrong folder is sending a contractor to the wrong house.
- **Checklist before takeoff:** setup is the preflight check; skipping it saves minutes and can waste hours.
- **Kitchen labels:** config and guidance label where the knives, fire extinguisher, and recipes are.

### Coaching tactics

For a new repo:

```text
Before implementation, ask Codex to identify the package manager, commands, app entrypoints, and current test surface. Then do one small change and run one small check.
```

For an existing repo:

```text
Do not let Codex start with broad edits. First ask for a read-only setup audit and file map. Then write the smallest task-specific prompt.
```

For a user who wants speed:

```text
Setup is not process theater. A 5-minute setup audit prevents burning usage on wrong commands, missing dependencies, and changes that cannot be verified.
```

### Prompt patterns

#### Setup audit before editing

```text
Read-only setup audit. Do not edit files.

Find:
- repo root,
- package manager,
- lockfiles,
- dev command,
- test command,
- typecheck/lint/build commands,
- project instruction files,
- config layers,
- likely generated files,
- risky areas to avoid.

End with the smallest safe verification command for a normal code change.
```

#### Create durable setup guidance

```text
Create a concise project guidance draft for Codex.

Include:
- project layout,
- package manager,
- commands,
- coding conventions visible in the repo,
- tests/checks to run,
- files/directories to avoid,
- done criteria.

Do not invent rules. Cite the files or commands you used as evidence.
```

### Red flags to call out directly

- Codex is not in the repository root.
- It wants to add or switch package managers without a reason.
- It cannot run a check and tries to proceed silently.
- The user has no rollback path and wants broad setup changes.
- Project config is being loaded from an untrusted repository without review.
- The task touches production config before local setup is understood.

### Exercises

1. Ask Codex for a read-only setup audit of a small repo.
2. Have the human identify the repo root and package manager before Codex does.
3. Turn repeated setup facts into a short project guidance file.
4. Compare one vague implementation prompt with one prompt that includes setup facts and done criteria.

<!-- VCB:END_SECTION id=vcb.chapter.installing_and_configuring_codex.ai_coach -->

## Shortcut Reality

### The ideal practice

Use official install instructions, start Codex in the right repo root, verify dependencies and project commands, review project config, and encode repeated guidance in durable files.

### What users often do instead

They install the tool, open a folder that “looks close enough,” ask for a feature, and let Codex discover the setup by trial and error.

### When the shortcut may be fine

Using an existing messy local setup may be fine when:

- the project is a throwaway prototype,
- the change is small and local,
- no real data, secrets, deployment, auth, or payments are involved,
- the human will supervise continuously,
- there is a clean Git checkpoint.

### When the shortcut is a bad idea

The shortcut is a bad trade when:

- onboarding to a production repo,
- multiple package managers or lockfiles are present,
- tests/builds are failing for unknown reasons,
- Codex needs to run migrations, install packages, or edit deployment config,
- the user wants low-attention or unattended work,
- the repo contains secrets or production credentials.

### Risk profile

- Probability of failure: medium; high if repo structure or commands are unclear.
- Impact if it fails: low in prototypes; high in production or shared repos.
- Ease of recovery: high with a clean checkpoint; lower if setup changes are scattered.
- Blast radius: can expand from one feature to package manager, config, build, and CI behavior.
- Skill needed to recover: low for wrong-folder mistakes; higher for dependency/config damage.
- Hidden cost: wasted usage, duplicated lockfiles, brittle local commands, and false verification.

### Minimum guardrails

- Confirm the repo root.
- Run or identify `git status` before changes.
- Identify package manager and lockfile.
- Ask for commands before implementation.
- Forbid package-manager switches unless explicitly requested.
- Require Codex to report checks it could and could not run.

### Recovery plan

If setup goes wrong:

1. Stop implementation edits.
2. Inspect `git status` and changed files.
3. Revert accidental package-manager/config changes first.
4. Re-establish the repo root and commands.
5. Run the smallest known check.
6. Restart the task with setup facts included.

### AI coach guidance

```text
The shortcut is not “bad,” but it is now costing us reliability. Before more edits, we need a setup audit: repo root, package manager, commands, guidance files, and one meaningful check.
```

## Budget and Constraint Notes

### Cheapest reliable path

Invest a small amount of human attention up front. A constrained user should avoid long exploratory Codex runs caused by missing setup facts.

### Fastest high-usage path

Let Codex perform a setup audit and propose durable guidance, then run implementation in separate bounded tasks. Do not combine “figure out setup” and “make broad product changes” unless the repo is disposable.

### Low-attention path

Low-attention work requires stronger setup, not weaker setup. Codex must know the repo root, commands, boundaries, and stop conditions before the human walks away.

### Production-quality path

Use official install/config docs, reviewed project config, AGENTS.md or equivalent guidance, known verification commands, Git checkpoints, and explicit sensitive-area boundaries.

## Stable Core

- Deterministic environments matter.
- Codex needs the right working directory and project commands.
- Repeated setup instructions should become durable guidance.
- Clear setup reduces wasted usage and review debt.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Exact Codex installation commands, config keys, supported operating systems, IDE menu labels, project-trust behavior, and profile syntax are volatile. Use official OpenAI Codex CLI, config, advanced config, Windows, and AGENTS.md docs for current instructions.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when:

- Codex install methods or supported platforms change.
- configuration precedence or project-trust behavior changes.
- CLI/IDE config layers split or merge.
- official guidance changes for AGENTS.md, profiles, rules, or project-local config.
- setup becomes primarily cloud-managed rather than local/repo-root based.

## Evidence and Sources

- `openai.codex.cli` — Official Codex CLI setup and local terminal surface anchor.
- `openai.codex.config_basic` — Official source for user config, project config, profile precedence, and shared CLI/IDE configuration layers.
- `openai.codex.config_advanced` — Official source for project-root detection and advanced config behavior.
- `openai.codex.agents_md` — Official source for persistent project guidance and AGENTS.md discovery.
- `openai.codex.windows` — Official Windows setup and sandbox caveat anchor.
- `openai.codex.rules` — Official source for rules loaded from active config layers.
- `vcb.synthesis.stable_engineering_practice` — VCB synthesis for deterministic setup and control-loop framing; not a product-behavior source.

## Related Topics

- `vcb.chapter.codex_surfaces`
- `vcb.chapter.sandboxing_and_approvals`
- `vcb.chapter.git_discipline`
- `vcb.codex.cli`
- `vcb.codex.config`
- `vcb.codex.agents_md`
- `vcb.safety.permissions`
- `vcb.workflow.unknown_codebase`
- `vcb.concepts.diff`
- `vcb.concepts.git_branch`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.installing_and_configuring_codex -->
