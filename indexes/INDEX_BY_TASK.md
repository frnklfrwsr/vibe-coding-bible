---
id: vcb.index.by_task
title: INDEX_BY_TASK
artifact_type: index
version: 0.41.0-draft.chunk40
status: chunk_40_updated
created_on: '2026-06-08'
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: quarterly
---

<!-- VCB:BEGIN_INDEX id=vcb.index.by_task version=0.41.0-draft.chunk40 -->

# INDEX_BY_TASK

> Status: Current routing index. Entries marked active have authored source files; entries marked planned are future routes.

## Orient yourself and choose a Codex surface
- `tool.codex` → active: primary surface-selection hub for deciding between App, CLI, IDE extension, Cloud, GitHub Review, and codex exec
- `tool.codex_app` → active: supervised desktop/local project work
- `tool.codex_cli` → active: terminal and command-backed local work
- `tool.codex_ide_extension` → active: editor-context work
- `tool.codex_cloud` → active: isolated cloud/background delegation
- `tool.codex_github_review` → active: GitHub PR review signal
- `tool.codex_exec` → active: non-interactive scripts, CI-style reports, and automation runs
- `vcb.chapter.how_to_use_this_bible` → active
- `vcb.chapter.codex_mental_model` → active
- `vcb.chapter.codex_surfaces` → active
- `vcb.chapter.vibe_coder_advantage_and_risk` → active

## Set up Codex safely
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_agents_md` → active: durable repo/project guidance for repeated setup expectations and local conventions

- `vcb.shortcut.skipping_setup` → active: inspect setup before allowing edits
- `vcb.shortcut.default_config_forever` → active: review config at phase/risk changes
- `vcb.shortcut.skipping_agents_md` → active: add durable guidance after repeated mistakes
- `vcb.shortcut.overstuffing_agents_md` → active: keep AGENTS.md concise and durable
- `vcb.shortcut.stale_agents_md` → active: prune outdated project guidance
- `vcb.shortcut.always_allow_sensitive_apps` → active: avoid persistent sensitive app/site approvals
- `vcb.shortcut.full_access_automation` → active: avoid full-access automation defaults
- `vcb.chapter.installing_and_configuring_codex` → active
- `vcb.chapter.sandboxing_and_approvals` → active
- `vcb.chapter.git_discipline` → active
- `vcb.safety.sandboxing_and_approvals` → planned
- `vcb.codex.config` → active
- `vcb.shortcut.broad_agent_permissions` → active: shortcut risk: excessive filesystem, command, network, or tool permissions

## Prompt, plan, context, and done criteria
- `vcb.chapter.four_part_prompt` → active
- `vcb.chapter.plan_first_code_second` → active
- `vcb.chapter.context_management` → active
- `vcb.chapter.acceptance_criteria` → active
- `vcb.prompting.four_part_prompt` → active: work-order prompt structure
- `vcb.prompting.plan_first` → active: plan-before-editing gate
- `vcb.prompting.context_management` → active: task-shaped context packet
- `vcb.prompting.acceptance_criteria` → active: done-when evidence boundary
- `vcb.failure.context_pollution` → active: stale, irrelevant, or contradictory context control
- `vcb.failure.done_claim_without_evidence` → active: done claim without artifact evidence
- `vcb.shortcut.vague_prompt` → active: convert underspecified requests into goal/context/constraints/done-when work orders
- `vcb.shortcut.skipping_plan` → active: require files, checks, risks, and rollback before risky mutation
- `vcb.shortcut.one_big_prompt` → active: slice oversized prompts into reviewable milestones
- `vcb.shortcut.context_dumping` → active: shortcut risk: stale, excessive, or contradictory context
- `vcb.shortcut.accepting_looks_done` → active: shortcut risk: polished done claims without evidence

## Bootstrap a new project
- new project bootstrap playbook → use the smallest active tool card below before chapter fallbacks
- `tool.docker` → active when reproducible local services, containerized setup, Compose, or dev-environment parity matters
- `tool.cloudflare` → active companion when DNS/CDN/edge/Workers/Pages setup is part of bootstrap
- `tool.netlify` → active companion when deploy previews/functions/site deployment are part of bootstrap
- `tool.neon` → active companion when a serverless Postgres or branchable preview database is part of bootstrap
- `tool.resend` → active companion when transactional email or notifications are part of bootstrap
- `tool.github` → active companion for repository source of truth
- `tool.npm` → active companion for package manifests, scripts, lockfiles, installs, and audit evidence
- `tool.github_actions` → active companion when CI/checks are part of bootstrap
- `tool.linear` → active companion when project planning, issue ownership, or team handoff is part of bootstrap
- `tool.figma` → active companion when UI/design flow or handoff is part of bootstrap
- `tool.codex_agents_md` → active companion when durable repo guidance is needed
- `vcb.chapter.codex_playbooks` → active fallback
- `vcb.chapter.installing_and_configuring_codex` → active fallback
- `vcb.chapter.agents_md_operating_manual` → active fallback
- `vcb.chapter.first_serious_app` → active fallback

## Understand an unknown codebase
- `vcb.chapter.understanding_unknown_codebase` → active
- `vcb.chapter.context_management` → active
- `vcb.chapter.plan_first_code_second` → active
- `vcb.workflow.unknown_codebase` → active: read-only repo tour and first safe slice
- `vcb.prompting.context_management` → active: context packet for repo exploration
- `vcb.prompting.plan_first` → active: plan before mutating unfamiliar code

## Build a feature in small slices
- `vcb.chapter.feature_slicing` → active
- `vcb.chapter.four_part_prompt` → active
- `vcb.chapter.acceptance_criteria` → active
- `vcb.chapter.git_discipline` → active
- `vcb.workflow.feature_slicing` → active: smallest vertical slice workflow
- `vcb.prompting.four_part_prompt` → active: scope the feature work order
- `vcb.prompting.acceptance_criteria` → active: define slice evidence

## Debug a bug from reproduction
- `vcb.chapter.debugging_with_reproduction` → active
- `vcb.chapter.understanding_unknown_codebase` → active
- `vcb.chapter.writing_updating_tests` → active
- `vcb.workflow.bug_repro` → active: reproduce-root-cause-patch-rerun loop
- `vcb.workflow.testing` → active: regression and nearest-check guidance
- `vcb.prompting.acceptance_criteria` → active: expected/actual done boundary
- `vcb.shortcut.debugging_without_repro` → active: preserve expected/actual evidence before patching
- `vcb.failure.hallucinated_apis` → active: fake API and invented contract diagnosis
- `vcb.failure.weakened_tests` → active: test weakening and false fix diagnosis
- `vcb.failure.done_claim_without_evidence` → active: summary needs task-specific evidence

## Write or update tests
- `tool.playwright` → active: browser/end-to-end tests, screenshots, traces, and UI verification evidence
- `tool.vitest` → active: Vite-native unit/component tests, watch-mode feedback, and JavaScript/TypeScript test evidence
- `tool.github_actions` → active: CI workflows, check evidence, secrets, token permissions, and repository automation
- `vcb.chapter.writing_updating_tests` → active
- `vcb.chapter.debugging_with_reproduction` → active
- `vcb.chapter.acceptance_criteria` → active
- `vcb.workflow.testing` → active: executable acceptance evidence
- `vcb.prompting.acceptance_criteria` → active: specify what tests must prove
- `vcb.failure.weakened_tests` → active: preserve or strengthen test meaning
- `vcb.failure.ci_false_confidence` → active: green checks are only conditional evidence
- `vcb.shortcut.skipping_tests` → active: shortcut risk: skipped verification and hidden regressions
- `vcb.shortcut.manual_testing_only` → active: convert repeated manual checks into repeatable verification where feasible
- `vcb.shortcut.ignoring_lint_typecheck` → active: separate old static-check failures from failures introduced by changed files

## Improve frontend UI

- `tool.figma` → active: design files, components, prototype flows, Dev Mode handoff, screenshots, and design-intent evidence
- `tool.storybook` → active: component workshop, isolated UI states, component docs, interaction tests, and design-handoff evidence
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points
- `tool.playwright` → active: browser/end-to-end tests, screenshots, traces, and UI verification evidence
- `tool.replit` → active companion: browser-hosted prototype preview and quick demo loop
- `tool.lovable` → active companion: full-stack app sketch when UI flow depends on backend/auth/storage behavior
- `tool.bolt` → active companion: browser-based app prototype when generated frontend and backend need review
- `vcb.workflow.frontend_work` → active companion: frontend state and browser verification workflow
- `vcb.workflow.visual_qa` → active companion: screenshot and visual-regression review workflow
- `vcb.workflow.accessibility_review` → active companion: accessibility review workflow for keyboard, labels, and semantics
- `vcb.chapter.frontend_work` → active fallback
- `vcb.chapter.context_management` → active fallback
- `vcb.chapter.acceptance_criteria` → active fallback
- `vcb.chapter.computer_use_browser_gui_tasks` → active fallback
- `vcb.failure.ui_taste_gap` → active: generated UI is functional but generic, inconsistent, or unverified
- `vcb.failure.done_claim_without_evidence` → active: UI summary needs screenshot/browser evidence

## Refactor safely
- `vcb.workflow.refactoring` → active: behavior-preserving refactor workflow
- `vcb.chapter.refactoring_without_breaking_everything` → active
- `vcb.chapter.writing_updating_tests` → active
- `vcb.chapter.reviewing_codex_output` → active
- `vcb.failure.broad_refactor_drift` → active: cleanup drifts into behavior change, migration, or rewrite
- `vcb.failure.weakened_tests` → active: tests weakened to make refactor pass
- `vcb.failure.done_claim_without_evidence` → active: refactor summary needs diff and check evidence
- `vcb.shortcut.broad_refactor` → active: shortcut risk: cleanup drifting into behavior change

## Choose dependencies, packages, or frameworks
- `tool.npm` → active: JavaScript package manifests, scripts, lockfiles, installs, and audit evidence
- `tool.github_dependabot` → active: dependency alerts, security update PRs, version update PRs, and dependency-maintenance queue
- `tool.openssf_scorecard` → active: supply-chain health signals, repository hardening checks, and dependency-adoption risk review
- `vcb.workflow.dependency_decisions` → active: dependency/package/framework decision workflow
- `vcb.chapter.dependency_package_framework_decisions` → active
- `vcb.chapter.security_for_vibe_coders` → active
- `vcb.chapter.sandboxing_and_approvals` → active
- `vcb.failure.dependency_bloat` → active: dependency addition outpaces maintenance value
- `vcb.failure.hallucinated_apis` → active: verify package APIs and SDK capabilities before relying on them
- `vcb.shortcut.adding_dependencies_fast` → active: shortcut risk: package bloat and supply-chain drag

## Review Codex output or a PR

- `tool.claude` → active companion: alternate AI review and architecture critique when source artifacts are supplied
- `tool.chatgpt` → active companion: plain-language review checklist and evidence-packet explanation
- `tool.github_copilot` → active companion: GitHub/IDE-native review assistance when repository context matters
- `tool.github` → active: repository collaboration, pull requests, branch protection, issues, and code-review source of truth
- `tool.github_actions` → active: CI workflows, check evidence, secrets, token permissions, and repository automation
- `tool.codex_security` → active: security-specific review/findings route when PR output changes trust boundaries, auth, secrets, payments, or user data

- `tool.codex_github_review` → active: GitHub PR review tool card; review signal, not merge authority
- `vcb.shortcut.accepting_looks_done` → active: completion evidence before acceptance
- `vcb.shortcut.accepting_diff_without_review` → active: changed-file review before accepting generated patches
- `vcb.shortcut.reviewing_cloud_summary_only` → active: inspect diff/check artifacts, not only summaries
- `vcb.chapter.reviewing_codex_output` → active
- `vcb.chapter.github_pr_review_with_codex` → active
- `vcb.concepts.diff` → active
- `vcb.workflow.codex_output_review` → active
- `vcb.workflow.reviewing_diffs` → active
- `vcb.workflow.github_pr_review` → active
- `vcb.shortcut.coding_on_main` → active: branch/worktree isolation before mutating shared or deploying code
- `vcb.failure.hallucinated_apis` → active: fake API contracts hidden in plausible code
- `vcb.failure.weakened_tests` → active: tests weakened in the patch
- `vcb.failure.broad_refactor_drift` → active: broad cleanup drift in review
- `vcb.failure.done_claim_without_evidence` → active: verify summaries against diff, tests, and logs

## Do security-sensitive work
- `tool.codex_security` → active: Codex Security plugin/cloud scans, security diff review, finding validation, threat-model-informed triage, and reviewed fix preparation

- `vcb.shortcut.real_secrets_in_prototype` → active: keep real credentials out of prototype and agent context
- `vcb.shortcut.cloud_work_with_real_secrets` → active: avoid real secrets in delegated cloud work
- `vcb.shortcut.production_console_computer_use` → active: treat production GUI actions as human-owned
- `vcb.chapter.security_for_vibe_coders` → active
- `vcb.chapter.sandboxing_and_approvals` → active
- `vcb.chapter.ci_noninteractive_github_actions` → active
- `vcb.safety.security_review` → active
- `vcb.safety.production_red_lines` → active

## Run Codex Security scan or review findings

- `tool.codex_security` → active: Codex Security plugin/cloud scans, security diff review, finding validation, threat-model-informed triage, and reviewed fix preparation
- `vcb.safety.security_review` → active: companion workflow for trust-boundary, auth, data, and exploitability review
- `vcb.safety.secrets` → active: companion secret-handling route
- `tool.codex_github_review` → active: companion PR-review signal route

## Run CI or non-interactive Codex
- `tool.github_actions` → active: CI workflows, check evidence, secrets, token permissions, and repository automation
- `tool.openssf_scorecard` → active: supply-chain health signals, repository hardening checks, and dependency-adoption risk review
- `tool.codex_exec` → active: non-interactive Codex tool card for scripts, CI-style reports, structured output, sandboxing, and credential guardrails
- `vcb.shortcut.automation_mutation_without_review` → active: non-interactive mutation must be report/propose or branch-only with human review
- `vcb.shortcut.automation_spam` → active: scheduled/non-interactive output must be actionable and deduplicated
- `vcb.shortcut.overbroad_ci_permissions` → active: narrow CI token/workflow permissions
- `vcb.shortcut.long_lived_ci_secrets` → active: replace or scope persistent CI secrets
- `vcb.shortcut.full_access_automation` → active: separate read-only automation from mutation
- `vcb.chapter.ci_noninteractive_github_actions` → active
- `vcb.chapter.security_for_vibe_coders` → active
- `vcb.chapter.reviewing_codex_output` → active
- `vcb.workflow.ci_triage` → active
- `vcb.workflow.ci_noninteractive` → active
- `vcb.failure.ci_false_confidence` → active: CI or agent summary creates unsupported confidence
- `vcb.failure.weakened_tests` → active: green build may reflect weakened test meaning
- `vcb.failure.done_claim_without_evidence` → active: CI/result summary must map to acceptance criteria
- `vcb.constraints.usage_burn` → active: usage-aware non-interactive and API-key workflow budgeting
- `vcb.constraints.production_quality` → active: production-quality gate for automated or CI-assisted work

## Make guidance durable
- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

- `vcb.chapter.agents_md_operating_manual` → active
- `vcb.chapter.codex_config_defaults` → active
- `vcb.chapter.skills_reusable_workflows` → active
- `vcb.chapter.hooks_deterministic_guardrails` → active
- `vcb.codex.agents_md` → active
- `vcb.codex.skills` → active
- `vcb.shortcut.skipping_agents_md` → active: add minimal durable AGENTS.md guidance after repeated mistakes
- `vcb.shortcut.overstuffing_agents_md` → active: keep AGENTS.md concise and durable
- `vcb.shortcut.stale_agents_md` → active: audit stale instructions and commands

## Add external tools or recurring workflows
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior

- `tool.codex_automations` → active: recurring/report-first Codex automation tool card
- `vcb.shortcut.automation_spam` → active: recurring automations need silence/archive and duplicate-suppression rules
- `vcb.shortcut.automation_mutation_without_review` → active: recurring mutation needs human review gates and audit evidence
- `vcb.shortcut.broad_agent_permissions` → active: permission scope for external tools and recurring workflows
- `vcb.shortcut.unattended_long_runs` → active: checkpoints for recurring or background automation
- `vcb.chapter.mcp_external_tools` → active
- `vcb.chapter.automations_recurring_work` → active
- `vcb.chapter.cloud_delegation_parallel_work` → active
- `vcb.codex.mcp` → active
- `vcb.codex.automations` → active
- `vcb.shortcut.unofficial_tools` → active: vet external tools before enabling them
- `vcb.shortcut.hook_overreach` → active: keep hooks narrow and deterministic
- `vcb.shortcut.trusting_external_tool_output` → active: verify tool output provenance and freshness

## Use cloud, subagents, browser, or GUI surfaces
- `tool.codex_cloud` → active: cloud/background delegation surface for isolated review-later tasks
- `tool.codex_worktrees` → active: worktree isolation for parallel local/app tasks and automation change separation
- `tool.codex_subagents` → active: parallel specialist agents for bounded analysis and disjoint work
- `tool.codex_automations` → active: recurring/report-first Codex background work
- `tool.codex_computer_use` → active: desktop GUI operation with app permissions and human supervision
- `tool.codex_browser` → active: in-app rendered-page preview, comments, screenshots, and browser verification
- `tool.codex_chrome_extension` → active: signed-in Chrome browser workflows with website approvals and account-risk controls
- `tool.codex_app` → active: app/browser/GUI-adjacent local orchestration surface where human supervision and review panes matter
- `vcb.shortcut.unattended_cloud_delegation` → active: unattended cloud work needs branch/worktree isolation, stop conditions, and review packet
- `vcb.shortcut.ambiguous_cloud_task` → active: vague cloud tasks should plan before editing
- `vcb.shortcut.cloud_task_without_context` → active: cloud tasks need delegation packet and context-gap checks
- `vcb.shortcut.parallel_cloud_sprawl` → active: parallel cloud work needs task matrix and one integrator
- `vcb.shortcut.conflicting_parallel_agents` → active: parallel write agents need file ownership and integration rules
- `vcb.shortcut.browser_clicking_without_repro` → active: browser/GUI tasks need exact repro and before/after evidence
- `vcb.shortcut.logged_in_browser_secrets` → active: signed-in browser/GUI tasks require fake/staging accounts or human-present boundaries
- `vcb.shortcut.unattended_mutation` → active: isolate write-capable unattended work
- `vcb.shortcut.always_allow_sensitive_apps` → active: avoid persistent sensitive app/site approvals
- `vcb.shortcut.production_console_computer_use` → active: use production GUI surfaces in report-only or human-present mode
- `vcb.shortcut.unattended_long_runs` → active: shortcut card for bounded background work and stop conditions
- `vcb.shortcut.reviewing_cloud_summary_only` → active: shortcut card for cloud task review
- `vcb.chapter.cloud_delegation_parallel_work` → active
- `vcb.chapter.subagents_parallel_thinking` → active
- `vcb.chapter.computer_use_browser_gui_tasks` → active

## Turn prompts into team workflow
- `tool.linear` → active: promote repeated work into issues, projects, workflow status, ownership, cycles, or team execution hygiene when process needs a source of truth
- `tool.codex_agents_md` → active: promote repeated repo guidance and review expectations into durable project instructions
- `tool.codex_config` → active: promote repeated approval, sandbox, profile, or MCP defaults into source-checked configuration
- `tool.codex_skills` → active: promote repeated workflows into reusable skill packages only after the workflow is proven
- `tool.codex_hooks` → active: promote objective recurring checks into deterministic lifecycle guardrails
- `tool.codex_mcp` → active: add external context/tool access only when source, auth, scope, and provenance are clear
- `vcb.chapter.prompt_library_to_team_workflow` → active fallback
- `vcb.chapter.agents_md_operating_manual` → active fallback
- `vcb.chapter.skills_reusable_workflows` → active fallback
- `vcb.chapter.hooks_deterministic_guardrails` → active fallback

## Diagnose Codex work going wrong
- `vcb.chapter.failure_modes_codex_work` → active
- `vcb.chapter.reviewing_codex_output` → active
- `vcb.chapter.debugging_with_reproduction` → active
- `vcb.concepts.recoverability` → active
- `vcb.failure.hallucinated_apis` → active: hallucinated APIs and fake interface contracts
- `vcb.failure.context_pollution` → active: stale, noisy, excessive, or contradictory context
- `vcb.failure.weakened_tests` → active: tests changed to pass without proving behavior
- `vcb.failure.broad_refactor_drift` → active: refactor work drifting into behavior change or rewrite
- `vcb.failure.dependency_bloat` → active: unnecessary dependencies and supply-chain drag
- `vcb.failure.ui_taste_gap` → active: frontend work that renders but lacks state, responsive, accessibility, or polish evidence
- `vcb.failure.ci_false_confidence` → active: green CI mistaken for complete verification
- `vcb.failure.done_claim_without_evidence` → active: done claim without artifact evidence

## Use a Codex playbook
- `vcb.chapter.codex_playbooks` → active
- `vcb.chapter.feature_slicing` → active
- `vcb.chapter.debugging_with_reproduction` → active
- `vcb.chapter.writing_updating_tests` → active
- `vcb.chapter.ci_noninteractive_github_actions` → active

## Generate release notes
- `vcb.workflow.release_notes` → active: release-note drafting from verified change sources
- `vcb.chapter.codex_playbooks` → active
- `vcb.chapter.prompt_library_to_team_workflow` → active
- `vcb.chapter.automations_recurring_work` → active

## Investigate production errors

- `tool.sentry` → active: error, tracing, performance, release, and session-context evidence for production debugging
- `tool.posthog` → active companion: user-behavior, feature-flag, replay, and funnel context around incidents
- `tool.vercel` → active companion: deployment, runtime, logs, preview/production environment, and promotion context
- `tool.github_actions` → active companion: release/check artifact context
- `vcb.chapter.codex_playbooks` → active fallback
- `vcb.chapter.debugging_with_reproduction` → active fallback
- `vcb.chapter.security_for_vibe_coders` → active fallback
- `vcb.chapter.senior_engineer_checklist` → active fallback

## Add an API endpoint

- `tool.supabase` → active: backend/database/function/API-adjacent data layer when Postgres/RLS/functions are in scope
- `tool.auth0` → active: API authorization/resource-server and OAuth/OIDC access-token posture
- `tool.clerk` → active: session/user/org context for app APIs when Clerk owns identity
- `tool.stripe` → active companion when the API handles payment, subscription, or webhook state
- `tool.sentry` → active companion for API error/tracing evidence
- `vcb.chapter.codex_playbooks` → active fallback
- `vcb.chapter.feature_slicing` → active fallback
- `vcb.chapter.security_for_vibe_coders` → active fallback
- `vcb.workflow.feature_slicing` → active fallback
- `vcb.failure.hallucinated_apis` → active: fake routes, clients, fields, or response shapes
- `vcb.failure.done_claim_without_evidence` → active: endpoint summary needs contract and test evidence

## Migrate a dependency
- `tool.github_dependabot` → active: dependency alerts, security update PRs, version update PRs, and dependency-maintenance queue
- `tool.npm` → active: JavaScript package manifests, scripts, lockfiles, installs, and audit evidence
- `tool.openssf_scorecard` → active: supply-chain health signals, repository hardening checks, and dependency-adoption risk review
- `vcb.workflow.dependency_update_review` → active: dependency update and lockfile review workflow
- `vcb.chapter.codex_playbooks` → active
- `vcb.chapter.dependency_package_framework_decisions` → active
- `vcb.chapter.refactoring_without_breaking_everything` → active
- `vcb.failure.dependency_bloat` → active: migration introduces unnecessary package or framework drag
- `vcb.failure.hallucinated_apis` → active: verify migration API names against real docs

## Remove dead code
- `vcb.workflow.refactoring` → active: behavior-preserving refactor workflow
- `vcb.chapter.codex_playbooks` → active
- `vcb.chapter.refactoring_without_breaking_everything` → active
- `vcb.chapter.reviewing_codex_output` → active
- `vcb.failure.broad_refactor_drift` → active: dead-code cleanup changes behavior or hides migration
- `vcb.failure.ci_false_confidence` → active: narrow green checks may miss removed edge cases

## Improve documentation
- `vcb.workflow.documentation_updates` → active: documentation update workflow tied to code, docs, and release context
- `vcb.chapter.codex_playbooks` → active
- `vcb.chapter.prompt_library_to_team_workflow` → active
- `vcb.failure.done_claim_without_evidence` → active: docs must not publish unsupported summary claims

## Build an MVP prototype

- `tool.figma` → active companion for UI flow, component, prototype, and handoff evidence before implementation
- `tool.linear` → active companion when MVP scope, issue ownership, or team planning is needed
- `tool.docker` → active companion when the MVP needs local services or reproducible environment setup
- `tool.replit` → active: browser-based prototyping, hosted development, learning apps, and quick demo publishing with review/exit-path guardrails
- `tool.lovable` → active: AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails
- `tool.bolt` → active: browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points
- `tool.github` → active companion: repo source of truth when a prototype becomes shared code
- `tool.github_actions` → active companion: CI/check evidence when the prototype becomes production-bound
- `tool.npm` → active companion: package manifests, scripts, lockfiles, installs, and audit evidence
- `tool.playwright` → active companion: browser/end-to-end evidence for UI claims
- `vcb.chapter.codex_playbooks` → active fallback
- `vcb.chapter.first_serious_app` → active fallback
- `vcb.chapter.feature_slicing` → active fallback
- `vcb.constraints.build_vs_maintenance` → active: prototype versus production/maintenance constraint choice
- `vcb.constraints.scope_budget` → active: low-cost MVP workflow without losing review evidence

## Harden auth-sensitive code

- `tool.codex_security` → active: Codex Security plugin/cloud scans, security diff review, finding validation, threat-model-informed triage, and reviewed fix preparation
- `tool.clerk` → active: authentication/session/user-management review when Clerk owns identity
- `tool.auth0` → active: IAM/OIDC/OAuth/API authorization review when Auth0 owns identity or API access
- `tool.supabase` → active: RLS, database policy, function secret, and auth-backed data-access review
- `tool.stripe` → active companion when auth controls payments, subscriptions, customer portals, or entitlement state
- `vcb.safety.security_review` → active companion
- `vcb.chapter.codex_playbooks` → active fallback
- `vcb.chapter.security_for_vibe_coders` → active fallback

## Build a first serious app

- `tool.vercel` → active: production-bound hosting, preview deployments, environment separation, and promotion evidence
- `tool.cloudflare` → active when edge/DNS/CDN/domain/routing/security posture is in scope
- `tool.netlify` → active when deploy previews, site deploys, functions, or deploy contexts are in scope
- `tool.supabase` → active: app database/backend/auth/storage with schema, RLS, migrations, and backup posture
- `tool.neon` → active when serverless Postgres, database branches, preview databases, or migration evidence are in scope
- `tool.clerk` → active: app authentication/user management when prebuilt identity is the chosen path
- `tool.auth0` → active: IAM/enterprise/B2B auth when OAuth/OIDC, APIs, or SSO posture matters
- `tool.stripe` → active: payments/subscriptions and real-money workflow evidence
- `tool.resend` → active when transactional email, notifications, sending domains, or templates are in scope
- `tool.sentry` → active: production error/performance evidence before and after launch
- `tool.posthog` → active: product analytics, feature flags, replay, and post-launch behavior evidence
- `tool.github` → active companion: repo/PR source of truth
- `tool.github_actions` → active companion: CI/check evidence
- `tool.playwright` → active companion: browser evidence
- `vcb.chapter.first_serious_app` → active fallback
- `vcb.chapter.senior_engineer_checklist` → active fallback
- `vcb.chapter.dependency_package_framework_decisions` → active fallback
- `vcb.workflow.first_serious_app` → planned

## Run the senior checklist

- `tool.docker` → active companion when local reproducibility, containerized services, environment parity, or Dockerized checks matter
- `tool.figma` → active companion when design handoff, UI states, prototype behavior, or visual acceptance evidence matters
- `tool.linear` → active companion when issue ownership, project scope, workflow status, or team execution hygiene matters
- `tool.vercel` → active: deployment, preview/production separation, environment, rollback, and release evidence
- `tool.cloudflare` → active: DNS/CDN/edge routing, Workers/Pages, cache/security posture, and public-domain evidence
- `tool.netlify` → active: site deploys, deploy previews, functions, deploy contexts, and rollback/deployment evidence
- `tool.supabase` → active: database/backend/auth/storage, schema/RLS, migration, backup, and data-access evidence
- `tool.neon` → active: serverless Postgres, database branching, connection, preview database, and migration evidence
- `tool.clerk` → active when Clerk owns authentication, users, sessions, organizations, or auth UI
- `tool.auth0` → active when Auth0 owns IAM, OAuth/OIDC, API authorization, or enterprise identity
- `tool.stripe` → active when payments, subscriptions, billing, webhooks, customer state, or entitlements are in scope
- `tool.resend` → active when transactional email, notifications, sending domains, templates, or email delivery evidence is in scope
- `tool.sentry` → active when production error/performance/release evidence is required
- `tool.posthog` → active when analytics, events, replay, feature flags, experiments, or product evidence are required
- `tool.github_actions` → active companion when check/release evidence matters
- `tool.playwright` → active companion when browser evidence matters
- `vcb.chapter.senior_engineer_checklist` → active fallback
- `vcb.chapter.reviewing_codex_output` → active fallback
- `vcb.chapter.git_discipline` → active fallback
- `vcb.constraints.production_quality` → active companion
- `vcb.constraints.recovery_budget` → active companion
## Evaluate or adopt an unofficial Codex practice

- `vcb.field.chatgpt_pm_codex_implementer` → active needs_more_evidence: ChatGPT PM / Codex implementer split remains too broad for bounded local reproduction
- `vcb.field.fresh_agent_review` → active reproduced: bounded local reproduction through PR review gate; not promoted as universal proof
- `vcb.field.context_reset_between_tasks` → active candidate: reset or summarize context between unrelated tasks
- `vcb.field.agents_md_first` → active candidate: minimal AGENTS.md early in durable repos
- `vcb.field.skeleton_todo_first` → active candidate: human skeleton/TODOs before agent implementation
- `vcb.field.strict_typecheck_lint_gates` → active reproduced: bounded local reproduction through VCB validator gate; not promoted as universal proof
- `vcb.field.greenfield_vs_production_rule` → active candidate: explicit project phase and compatibility posture
- `vcb.field.lessons_file_loop` → active candidate: temporary lessons loop before durable guidance promotion
- `vcb.field.multi_agent_review_consensus` → active needs_more_evidence: multi-agent review must not treat agreement as proof
- `vcb.field.contract_first_segmented_handoffs` → active candidate: contract-first segmented Codex handoffs based on one sanitized usage insight
- `vcb.chapter.field_notes_unofficial_practices` → active fallback: field-practice policy, evidence labels, and non-promotion rules
- `FIELD_PRACTICES.md` → register: Issue #7 status, promotion path, and review trigger for each practice
- `vcb.chapter.maintaining_updating_bible` → active companion: updating source/register/index posture
- `vcb.chapter.risk_managed_shortcuts` → active companion: shortcut harm-reduction layer

## Maintain or update the Bible
- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes
- `vcb.chapter.maintaining_updating_bible` → active fallback
- `vcb.chapter.field_notes_unofficial_practices` → active
- `vcb.chapter.risk_managed_shortcuts` → active
- `vcb.chapter.how_to_use_this_bible` → active
## Take a shortcut safely
- `vcb.shortcut.production_console_computer_use` → active: production console computer use guardrail card
- `vcb.shortcut.overbroad_ci_permissions` → active: overbroad ci permissions guardrail card
- `vcb.shortcut.long_lived_ci_secrets` → active: long-lived ci secrets guardrail card
- `vcb.shortcut.real_secrets_in_prototype` → active: real secrets in prototype guardrail card
- `vcb.shortcut.cloud_work_with_real_secrets` → active: cloud work with real secrets guardrail card
- `vcb.shortcut.full_access_automation` → active: full-access automation guardrail card
- `vcb.shortcut.unattended_mutation` → active: unattended mutation guardrail card
- `vcb.shortcut.always_allow_sensitive_apps` → active: always allow sensitive apps guardrail card
- `vcb.shortcut.skipping_tests` → active: skip-test shortcut; route to smallest relevant verification guardrail
- `vcb.shortcut.accepting_looks_done` → active: looks-done shortcut; route to completion-evidence gate
- `vcb.shortcut.broad_agent_permissions` → active: broad-permission shortcut; route to sandbox/approval and blast-radius controls
- `vcb.shortcut.unattended_long_runs` → active: unattended-run shortcut; route to milestones, isolation, and evidence reports
- `vcb.shortcut.broad_refactor` → active: broad-refactor shortcut; route to behavior-preserving refactor boundaries
- `vcb.shortcut.context_dumping` → active: context-dumping shortcut; route to curated context packet control
- `vcb.shortcut.adding_dependencies_fast` → active: fast dependency shortcut; route to package decision and lockfile review guardrails
- `vcb.shortcut.reviewing_cloud_summary_only` → active: cloud-summary-only shortcut; route to diff/check/artifact review guardrail
- `vcb.chapter.risk_managed_shortcuts` → active
- `vcb.concepts.blast_radius` → active
- `vcb.concepts.recoverability` → active
- `vcb.concepts.rollback` → active

## Choose Codex operating mode

- `vcb.chapter.choosing_codex_operating_mode` → active
- `vcb.chapter.budget_aware_codex_workflows` → active
- `vcb.chapter.build_phase_vs_maintenance_phase` → active
- `vcb.concepts.blast_radius` → active
- `vcb.concepts.recoverability` → active
- `vcb.constraints.operating_mode` → active: choose Codex surface, permission level, task size, and supervision rhythm
- `vcb.constraints.attention_budget` → active: adapt delegation to available human review attention

## Choose budget-aware Codex workflow

- `vcb.chapter.budget_aware_codex_workflows` → active
- `vcb.pricing_snapshot.openai_codex` → snapshot
- `vcb.chapter.cost_benefit_analysis` → active
- `vcb.chapter.choosing_codex_operating_mode` → active
- `vcb.constraints.scope_budget` → active: cheapest reliable workflow under tight usage or money constraints
- `vcb.constraints.review_budget` → active: high-throughput workflow with isolation and review capacity
- `vcb.constraints.usage_burn` → active: usage burn and API budget control
- `vcb.constraints.recovery_budget` → active: recovery-cost-aware scope control

## Choose a primary Codex tool surface

- `tool.codex` → active: start here when deciding between App, CLI, IDE, Cloud, GitHub Review, and codex exec
- `tool.codex_app` → active: supervised desktop/local project work
- `tool.codex_cli` → active: terminal and command-backed local work
- `tool.codex_ide_extension` → active: editor-context work
- `tool.codex_cloud` → active: isolated cloud/background delegation
- `tool.codex_github_review` → active: PR review signal
- `tool.codex_exec` → active: non-interactive scripts and CI-style reports

## Choose a Codex adjunct surface

- `tool.codex_worktrees` → active: worktree isolation for parallel local/app tasks and automation change separation
- `tool.codex_subagents` → active: parallel specialist agents for bounded analysis, exploration, and disjoint implementation work
- `tool.codex_automations` → active: recurring/report-first Codex background work with review owner and stop conditions
- `tool.codex_computer_use` → active: desktop GUI operation with app permissions, visible-state risk, and human supervision
- `tool.codex_browser` → active: in-app rendered-page preview, comments, screenshots, and browser verification
- `tool.codex_chrome_extension` → active: signed-in Chrome browser workflows with website approvals and account-risk controls

## Audit a missing ecosystem tool

- `TOOL_REGISTER.md` → active register route: check Chunk 40 coverage-gap audit before assuming the catalog is complete.
- `tool.cloudflare`, `tool.netlify`, `tool.neon`, `tool.resend`, `tool.vitest`, and `tool.storybook` → active newly authored coverage-gap cards.
- Deferred IDs such as `tool.render`, `tool.railway`, `tool.fly_io`, `tool.firebase`, `tool.aws`, `tool.gcp`, `tool.azure`, `tool.digitalocean`, `tool.postmark`, `tool.sendgrid`, `tool.mailgun`, `tool.notion`, `tool.google_docs`, `tool.jira`, `tool.onepassword`, `tool.doppler`, `tool.infisical`, `tool.better_stack`, `tool.datadog`, `tool.paddle`, `tool.lemon_squeezy`, `tool.jest`, and `tool.cypress` route through `TOOL_REGISTER.md` with active companions until authored.

## Choose a tool stack

- `tool.docker` → active: local containers, reproducible dev services, Dockerfiles, Compose stacks, and rebuild/isolation evidence
- `tool.figma` → active: design/prototype/component handoff and frontend design-intent evidence
- `tool.linear` → active: issue/project/workflow planning and team execution hygiene
- `tool.cloudflare` → active: DNS/CDN/edge/Workers/Pages route when the stack includes public traffic, edge logic, domains, or cache/security behavior
- `tool.netlify` → active: deploy-preview, site deployment, functions, and deploy-context route
- `tool.neon` → active: serverless Postgres, branching, preview database, and migration-evidence route
- `tool.resend` → active: transactional email, sending-domain, templates, and notification-delivery route
- `tool.vitest` → active: Vite-native unit/component testing and JavaScript/TypeScript test-evidence route
- `tool.storybook` → active: component workshop, isolated UI states, component docs, and UI handoff route
- `tool.vercel` → active: hosting, preview deployments, environment separation, deployment evidence, and production promotion guardrails
- `tool.supabase` → active: Postgres database/backend/auth/storage, schema/RLS, migrations, backups, functions, and data-access guardrails
- `tool.clerk` → active: authentication, user management, sessions, organizations, and application identity guardrails
- `tool.auth0` → active: IAM, OAuth/OIDC, applications/APIs, enterprise/B2B identity, and authorization architecture guardrails
- `tool.stripe` → active: payments, subscriptions, checkout, webhooks, billing state, and real-money fulfillment guardrails
- `tool.sentry` → active: error monitoring, tracing, performance, release evidence, and production debugging guardrails
- `tool.posthog` → active: product analytics, event taxonomy, session replay, feature flags, experiments, and product-evidence guardrails
- `tool.replit` → active: browser-based prototyping, hosted development, learning apps, and quick demo publishing with review/exit-path guardrails
- `tool.lovable` → active: AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails
- `tool.bolt` → active: browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points
- `tool.chatgpt` → active: planning, explanation, product thinking, source-backed research synthesis, and data/document analysis before implementation
- `tool.claude` → active: alternate AI review, architecture critique, long-form explanation, and source-checked second-opinion analysis
- `tool.cursor` → active: AI IDE-native planning, local multi-file edits, diff review, and supervised agentic coding workflows
- `tool.github_copilot` → active: GitHub/IDE-native suggestions, chat, repository-connected coding help, and PR/branch-adjacent assistance
- `tool.windsurf` → active: agentic AI IDE workflows with Cascade-style planning, editing, tool calls, checkpoints, and plugin support
- `tool.codex` → active companion: first-party Codex tool-family chooser
- `tool.github` → active companion: repository collaboration, pull requests, branch protection, issues, and code-review source of truth
- `tool.github_actions` → active companion: CI workflows, check evidence, secrets, token permissions, and repository automation
- `tool.npm` → active companion: JavaScript package manifests, scripts, lockfiles, installs, and audit evidence
- `tool.playwright` → active companion: browser/end-to-end tests, screenshots, traces, and UI verification evidence
- `vcb.chapter.tool_stack_catalog` → active fallback
- `vcb.chapter.cost_benefit_analysis` → active fallback
- `vcb.shortcut.tool_sprawl` → active: keep the tool stack small enough to audit, revoke, and explain

## Use other AIs with Codex

- `tool.chatgpt` → active: planning, explanation, product thinking, source-backed research synthesis, and data/document analysis before implementation
- `tool.claude` → active: alternate AI review, architecture critique, long-form explanation, and source-checked second-opinion analysis
- `tool.cursor` → active: AI IDE-native planning, local multi-file edits, diff review, and supervised agentic coding workflows
- `tool.github_copilot` → active: GitHub/IDE-native suggestions, chat, repository-connected coding help, and PR/branch-adjacent assistance
- `tool.windsurf` → active: agentic AI IDE workflows with Cascade-style planning, editing, tool calls, checkpoints, and plugin support
- `vcb.shortcut.many_ais_same_files` → active companion: multi-AI same-file risk
- `vcb.shortcut.best_of_n_without_review` → active companion: answer-shopping risk
- `vcb.shortcut.consensus_as_correctness` → active companion: agreement is not proof
- `vcb.shortcut.model_routing_guesswork` → active companion: model/tool routing by guesswork
- `vcb.chapter.when_to_use_other_ais` → active fallback

## Diagnose bad estimates and confident wrong output
- `vcb.shortcut.trusting_estimates_before_inspection` → active: route when an estimate is accepted before repo, code, dependency, and test inspection
- `vcb.shortcut.ignoring_model_biases` → active: route when confident output may reflect plausible-pattern bias or user-pleasing bias
- `vcb.shortcut.consensus_as_correctness` → active: route when multiple AI answers agree but have not been verified
- `vcb.shortcut.best_of_n_without_review` → active: route when answer-shopping replaces source/diff/test review
- `vcb.chapter.what_codex_is_bad_at` → active
- `vcb.chapter.model_biases_failure_biases_bad_estimates` → active
- `vcb.chapter.failure_modes_codex_work` → active
- `vcb.concepts.diff` → active
- `vcb.failure.hallucinated_apis` → active: plausible API claim lacks contract evidence
- `vcb.failure.done_claim_without_evidence` → active: confident summaries need evidence
- `vcb.failure.context_pollution` → active: stale context can produce confident wrong output

## Learn foundational software concepts before asking Codex to edit
- `vcb.concepts.api_basics` → active
- `vcb.concepts.frontend_backend` → active
- `vcb.concepts.database_schema` → active
- `vcb.concepts.authentication` → active
- `vcb.concepts.authorization` → active
- `vcb.concepts.state` → active
- `vcb.concepts.async` → active
- `vcb.concepts.dependency` → active
- `vcb.concepts.test` → active
- `vcb.concepts.typecheck` → active
- `vcb.concepts.lint` → active
- `vcb.concepts.migration` → active
- `vcb.concepts.environment_variable` → active
- `vcb.concepts.build_step` → active
- `vcb.concepts.ci` → active
- `vcb.concepts.feature_flag` → active
- `vcb.concepts.observability` → active
- `vcb.chapter.how_to_use_this_bible` → active
- `vcb.chapter.senior_engineer_checklist` → active

## Bootstrap or harden a serious app conceptually

- `tool.vercel` → active companion: hosting/deployment environment concepts made concrete
- `tool.supabase` → active companion: database/backend/auth/storage concepts made concrete
- `tool.clerk` → active companion: authentication/session/user concepts made concrete
- `tool.auth0` → active companion: authorization/IAM/API access concepts made concrete
- `tool.stripe` → active companion: payment/subscription concepts made concrete
- `tool.sentry` → active companion: observability/error evidence concepts made concrete
- `tool.posthog` → active companion: analytics/feature-flag/session-replay concepts made concrete
- `vcb.concepts.api_basics` → active
- `vcb.concepts.frontend_backend` → active
- `vcb.concepts.database_schema` → active
- `vcb.concepts.authentication` → active
- `vcb.concepts.authorization` → active
- `vcb.concepts.environment_variable` → active
- `vcb.concepts.ci` → active
- `vcb.concepts.feature_flag` → active
- `vcb.concepts.observability` → active
- `vcb.chapter.first_serious_app` → active fallback

## Choose or use a Codex feature
- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes
- `tool.codex_security` → active: Codex Security plugin/cloud scans, security diff review, finding validation, threat-model-informed triage, and reviewed fix preparation
- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

- `tool.codex_worktrees` → active: worktree isolation for parallel local/app tasks and automation change separation
- `tool.codex_subagents` → active: parallel specialist agents for bounded analysis, exploration, and disjoint implementation work
- `tool.codex_automations` → active: recurring/report-first Codex background work with review owner and stop conditions
- `tool.codex_computer_use` → active: desktop GUI operation with app permissions, visible-state risk, and human supervision
- `tool.codex_browser` → active: in-app rendered-page preview, comments, screenshots, and browser verification
- `tool.codex_chrome_extension` → active: signed-in Chrome browser workflows with website approvals and account-risk controls

- `vcb.codex.app` → active: Codex App
- `vcb.codex.cli` → active: Codex CLI
- `vcb.codex.ide_extension` → active: Codex IDE Extension
- `vcb.codex.cloud` → active: Codex Cloud / Web
- `vcb.codex.github_review` → active: Codex GitHub PR Review
- `vcb.codex.config` → active: Codex Config
- `vcb.codex.agents_md` → active: AGENTS.md
- `vcb.codex.skills` → active: Codex Skills
- `vcb.codex.mcp` → active: MCP for Codex
- `vcb.codex.hooks` → active: Codex Hooks
- `vcb.codex.automations` → active: Codex Automations
- `vcb.codex.subagents` → active: Codex Subagents
- `vcb.codex.computer_use` → active: Codex Computer Use
- `vcb.codex.feature_maturity` → active companion
- `vcb.codex.changelog_monitoring` → active companion
## Monitor Codex maturity, changelog, or deprecations
- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes
- `SOURCE_REGISTER.md` → active companion register
- `DEPRECATION_REGISTER.md` → active companion register
- `vcb.chapter.maintaining_updating_bible` → active fallback

## Review, Safety, and Verification Workflow Cards

- `vcb.workflow.codex_output_review` → active: Codex output review by diff, checks, and risk
- `vcb.workflow.reviewing_diffs` → active: local diff review and hunk-level risk scan
- `vcb.workflow.github_pr_review` → active: Codex-assisted PR review without treating AI as approval
- `vcb.safety.security_review` → active: trust-boundary, auth, data, and exploitability review
- `vcb.safety.secrets` → active: credentials, tokens, CI secrets, browser/session exposure
- `vcb.workflow.ci_triage` → active: failed-check and log triage before mutation
- `vcb.workflow.ci_noninteractive` → active: Codex in CI with least privilege and auditable outputs
- `vcb.safety.production_red_lines` → active: hard-stop gates for production-risk work

## Frontend, Refactor, Dependency, Release, and Documentation Workflows
- `vcb.workflow.frontend_work` → active: frontend state, responsive behavior, and browser evidence
- `vcb.workflow.visual_qa` → active: screenshot and visual-regression review
- `vcb.workflow.accessibility_review` → active: accessibility checks, keyboard paths, labels, and WCAG-guided review
- `vcb.workflow.refactoring` → active: behavior-preserving refactor workflow with tests and diff review
- `vcb.workflow.dependency_decisions` → active: new dependency/package/framework decision workflow
- `vcb.workflow.dependency_update_review` → active: dependency update and lockfile review workflow
- `vcb.workflow.release_notes` → active: release-note drafting from verified change sources
- `vcb.workflow.documentation_updates` → active: documentation update workflow tied to code, docs, and release context

## Constraint and Budget Topic Cards

- `vcb.constraints.operating_mode` → active: choose Codex surface, task size, permission, and supervision mode by task constraint
- `vcb.constraints.attention_budget` → active: shape delegation around available human review attention
- `vcb.constraints.usage_burn` → active: manage usage burn, credits, API spend, context size, and retries without freezing prices
- `vcb.constraints.recovery_budget` → active: choose scope and permissions based on rollback and repair cost
- `vcb.constraints.build_vs_maintenance` → active: change Codex workflow by prototype, MVP, production, maintenance, refactor, or hotfix phase
- `vcb.constraints.production_quality` → active: production-quality evidence and release-readiness gate
- `vcb.constraints.scope_budget` → active: cheapest reliable Codex path under tight usage or money constraints
- `vcb.constraints.review_budget` → active: high-throughput Codex work with isolation, review bandwidth, and recovery gates

## Security and Permission Shortcut Cards

- `vcb.shortcut.production_console_computer_use` → active: production console computer use security/permission shortcut guardrails
- `vcb.shortcut.overbroad_ci_permissions` → active: overbroad ci permissions security/permission shortcut guardrails
- `vcb.shortcut.long_lived_ci_secrets` → active: long-lived ci secrets security/permission shortcut guardrails
- `vcb.shortcut.real_secrets_in_prototype` → active: real secrets in prototype security/permission shortcut guardrails
- `vcb.shortcut.cloud_work_with_real_secrets` → active: cloud work with real secrets security/permission shortcut guardrails
- `vcb.shortcut.full_access_automation` → active: full-access automation security/permission shortcut guardrails
- `vcb.shortcut.unattended_mutation` → active: unattended mutation security/permission shortcut guardrails
- `vcb.shortcut.always_allow_sensitive_apps` → active: always allow sensitive apps security/permission shortcut guardrails

## Use hooks, MCP, skills, or external tools
- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

- `vcb.shortcut.unofficial_tools` → active: evaluate unofficial tools in disposable, least-privilege environments
- `vcb.shortcut.hook_overreach` → active: keep hooks objective and enforceable
- `vcb.shortcut.trusting_external_tool_output` → active: verify provenance, freshness, and scope before acting on tool output

## Set up or configure Codex for a repo
- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

- `vcb.shortcut.skipping_setup` → active: do setup inspection before edits
- `vcb.shortcut.default_config_forever` → active: review config defaults as repo risk changes
- `vcb.shortcut.skipping_agents_md` → active: add minimal durable repo guidance when repeated friction appears
- `vcb.shortcut.overstuffing_agents_md` → active: prune durable repo guidance
- `vcb.shortcut.stale_agents_md` → active: refresh stale AGENTS.md before relying on it

## Add hooks, tools, or external context
- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

- `vcb.shortcut.unofficial_tools` → active: evaluate unofficial tool provenance and permissions before use
- `vcb.shortcut.hook_overreach` → active: keep hooks objective, fast, and narrow
- `vcb.shortcut.trusting_external_tool_output` → active: verify tool output before edits or decisions

## Setup/config/process shortcut cards

- `vcb.shortcut.skipping_setup` → active: before editing a repo whose setup, run, test, or build path is unknown
- `vcb.shortcut.default_config_forever` → active: when Codex config defaults have outlived the project phase
- `vcb.shortcut.skipping_agents_md` → active: when repeated project guidance should become durable repo guidance
- `vcb.shortcut.overstuffing_agents_md` → active: when AGENTS.md is being used as a context dump
- `vcb.shortcut.stale_agents_md` → active: when persistent guidance may be outdated or contradicted
- `vcb.shortcut.unofficial_tools` → active: before adopting unofficial plugins, MCP servers, wrappers, or scripts
- `vcb.shortcut.hook_overreach` → active: when hooks are being used as broad policy or proof of safety
- `vcb.shortcut.trusting_external_tool_output` → active: when Codex relies on MCP/plugin/web/tool output for changes

## Configure Codex or AGENTS.md safely

- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

- `vcb.shortcut.default_config_forever` → active: conservative default plus named risky profiles
- `vcb.shortcut.skipping_agents_md` → active: add minimal durable guidance after repeated mistakes
- `vcb.shortcut.overstuffing_agents_md` → active: prune AGENTS.md to durable repo facts
- `vcb.shortcut.stale_agents_md` → active: verify and update persistent guidance after repo changes

## Adopt tools, hooks, plugins, or MCP safely

- `tool.codex_skills` → active: reusable workflow package guidance before creating or installing skills
- `tool.codex_mcp` → active: MCP server scope, auth, provenance, and external-tool boundary guidance
- `tool.codex_hooks` → active: deterministic hook guardrails, event mechanics, side-effect review, and rollback guidance
- `tool.codex_config` → active: config and tool-default posture for MCP, hooks, approvals, and profiles
- `tool.codex_agents_md` → active: durable guidance for tool-use rules and repo conventions
- `vcb.shortcut.unofficial_tools` → active: vet source, permissions, credentials, and uninstall path before install
- `vcb.shortcut.hook_overreach` → active: keep hooks objective, fast, and not the only safety boundary
- `vcb.shortcut.trusting_external_tool_output` → active: require provenance and verification for tool output

## Adopt skills, MCP, plugins, hooks, or reusable process safely

- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

- `vcb.shortcut.skill_overkill` → active: avoid creating a skill before a repeated workflow earns it
- `vcb.shortcut.skill_sprawl` → active: audit overlapping skills and disabled stale reusable workflows
- `vcb.shortcut.tool_sprawl` → active: add one tool at a time with owner, purpose, and exit path
- `vcb.shortcut.tool_sprawl_mcp` → active: keep MCP servers scoped, allow-listed, and purpose-bound
- `vcb.shortcut.brittle_hooks` → active: keep hooks fast, deterministic, report-first, and reviewed
- `vcb.shortcut.process_overhead_for_tiny_project` → active: avoid heavyweight process before a tiny project earns it
- `vcb.shortcut.team_workflow_without_team` → active: use solo evidence workflow before team handoff process exists
- `vcb.shortcut.copy_pasting_playbook_blindly` → active: tailor reusable playbooks to actual risk, scope, and done evidence

## Task routes for multi-AI/model-bias shortcuts

- `vcb.shortcut.many_ais_same_files` → active: using multiple AI systems on the same files without one owner, one branch strategy, and one integration path
- `vcb.shortcut.parallel_agents_edit_same_files` → active: letting multiple agents mutate overlapping files at the same time and hoping the merge will be obvious later
- `vcb.shortcut.best_of_n_without_review` → active: asking several AIs for answers, then accepting the one that looks best without checking diffs, tests, source evidence, or risks
- `vcb.shortcut.cherry_picking_ai_answers` → active: choosing the answer that confirms your preferred plan instead of the answer with the best evidence
- `vcb.shortcut.consensus_as_correctness` → active: treating agreement between multiple AIs as proof that a claim, estimate, fix, or design is correct
- `vcb.shortcut.trusting_estimates_before_inspection` → active: believing an AI estimate before the model has inspected the actual code, dependencies, tests, constraints, and unknowns
- `vcb.shortcut.ignoring_model_biases` → active: forgetting that models can be biased toward plausible answers, overconfident summaries, common patterns, pleasing the user, and underestimating hidden project constraints
- `vcb.shortcut.model_routing_guesswork` → active: choosing a model, reasoning level, surface, or AI tool by brand feeling, stale advice, or price anxiety instead of current docs, task shape, risk, and evidence needs
- `vcb.shortcut.subagent_swarm` → active: spawning many subagents or custom agents before each has a bounded question, role, context, output format, and integration plan

## Parallel Cloud and Automation Shortcut Routes

- `vcb.shortcut.unattended_cloud_delegation` → active: bounded cloud/background delegation with branch/worktree isolation, stop conditions, and review packets
- `vcb.shortcut.ambiguous_cloud_task` → active: plan-first guardrails for vague cloud tasks before mutation
- `vcb.shortcut.cloud_task_without_context` → active: delegation packet and context-gap checks for cloud work
- `vcb.shortcut.parallel_cloud_sprawl` → active: task matrix, isolated branches/worktrees, and integration owner for parallel cloud work
- `vcb.shortcut.conflicting_parallel_agents` → active: one mutating owner per file/behavior and one integrator
- `vcb.shortcut.automation_spam` → active: recurring automations must be actionable, deduplicated, and quiet when nothing changed
- `vcb.shortcut.automation_mutation_without_review` → active: report/propose first; branch-only mutation with human review if unavoidable
- `vcb.shortcut.browser_clicking_without_repro` → active: exact GUI/browser repro and evidence before mutation
- `vcb.shortcut.logged_in_browser_secrets` → active: fake/staging accounts and scoped approvals for signed-in browser/GUI work

## Repository, CI, dependency, and QA tool routes

- `tool.github` → active: repository collaboration, pull requests, branch protection, issues, and code-review source of truth
- `tool.github_actions` → active: CI workflows, check evidence, secrets, token permissions, and repository automation
- `tool.github_dependabot` → active: dependency alerts, security update PRs, version update PRs, and dependency-maintenance queue
- `tool.npm` → active: JavaScript package manifests, scripts, lockfiles, installs, and audit evidence
- `tool.playwright` → active: browser/end-to-end tests, screenshots, traces, and UI verification evidence
- `tool.openssf_scorecard` → active: supply-chain health signals, repository hardening checks, and dependency-adoption risk review

## Choose an AI coding, AI IDE, or planning tool

- `tool.chatgpt` → active: planning, explanation, product thinking, source-backed research synthesis, and data/document analysis before implementation
- `tool.claude` → active: alternate AI review, architecture critique, long-form explanation, and source-checked second-opinion analysis
- `tool.cursor` → active: AI IDE-native planning, local multi-file edits, diff review, and supervised agentic coding workflows
- `tool.github_copilot` → active: GitHub/IDE-native suggestions, chat, repository-connected coding help, and PR/branch-adjacent assistance
- `tool.windsurf` → active: agentic AI IDE workflows with Cascade-style planning, editing, tool calls, checkpoints, and plugin support
- `tool.codex` → active companion: primary first-party Codex implementation surface chooser
- `vcb.chapter.tool_stack_catalog` → active fallback
- `vcb.chapter.when_to_use_other_ais` → active fallback


## Choose a browser-dev, app-builder, or UI-generation tool

- `tool.replit` → active: browser-based prototyping, hosted development, learning apps, and quick demo publishing with review/exit-path guardrails
- `tool.lovable` → active: AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails
- `tool.bolt` → active: browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points
- `vcb.chapter.tool_stack_catalog` → active fallback
- `vcb.constraints.build_vs_maintenance` → active companion: choose prototype/MVP/production posture before picking a builder

## Choose a Docker, Figma, or Linear tool path

- `tool.docker` → active: use when the user needs containers, Compose, local services, rebuildable dev/test environments, or Dockerized isolation evidence
- `tool.figma` → active: use when the user needs design handoff, components, prototypes, screenshots, Dev Mode inspection, or UI intent/spec evidence
- `tool.linear` → active: use when the user needs issue tracking, project planning, team workflows, cycles, ownership, or execution hygiene
- `tool.github` → active companion when repo/PR source of truth matters
- `tool.github_actions` → active companion when CI/check evidence matters
- `vcb.chapter.tool_stack_catalog` → active fallback
- `vcb.shortcut.tool_sprawl` → active companion: keep the tool stack small enough to audit, revoke, and explain

## Choose a hosting, backend/auth, payment, observability, or analytics tool

- `tool.vercel` → active: hosting, preview deployments, environment separation, deployment evidence, and production promotion guardrails
- `tool.cloudflare` → active: DNS/CDN/edge/domain routing, Workers/Pages, cache/security controls, and public traffic posture
- `tool.netlify` → active: deploy previews, static/full-stack site deploys, functions, deploy contexts, and rollback/deployment evidence
- `tool.supabase` → active: Postgres database/backend/auth/storage, schema/RLS, migrations, backups, functions, and data-access guardrails
- `tool.neon` → active: serverless Postgres, branches, preview databases, connection evidence, migration review, and database recovery posture
- `tool.clerk` → active: authentication, user management, sessions, organizations, and application identity guardrails
- `tool.auth0` → active: IAM, OAuth/OIDC, applications/APIs, enterprise/B2B identity, and authorization architecture guardrails
- `tool.stripe` → active: payments, subscriptions, checkout, webhooks, billing state, and real-money fulfillment guardrails
- `tool.resend` → active: transactional email, notifications, sending domains, templates, and delivery blast-radius review
- `tool.sentry` → active: error monitoring, tracing, performance, release evidence, and production debugging guardrails
- `tool.posthog` → active: product analytics, event taxonomy, session replay, feature flags, experiments, and product-evidence guardrails

<!-- VCB:STOP_RETRIEVAL reason="by_task_complete" -->
<!-- VCB:END_INDEX id=vcb.index.by_task -->
