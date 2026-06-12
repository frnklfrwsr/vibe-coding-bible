---
id: vcb.index.by_recoverability
title: INDEX_BY_RECOVERABILITY
artifact_type: index
version: 0.41.0-draft.chunk40
status: chunk_40_updated
created_on: '2026-06-08'
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: quarterly
---

<!-- VCB:BEGIN_INDEX id=vcb.index.by_recoverability version=0.41.0-draft.chunk40 -->

# INDEX_BY_RECOVERABILITY

> Status: Current routing index. Entries marked active have authored source files; entries marked planned are future routes.

## Prompting/workflow recoverability controls
- `vcb.prompting.four_part_prompt` → active: improves recoverability by bounding scope
- `vcb.prompting.acceptance_criteria` → active: improves recoverability by naming evidence and gaps
- `vcb.prompting.plan_first` → active: avoids expensive wrong edits before they exist
- `vcb.prompting.context_management` → active: prevents stale-context recovery loops
- `vcb.workflow.unknown_codebase` → active: raises recoverability before first mutation
- `vcb.workflow.feature_slicing` → active: keeps changes revertible and reviewable
- `vcb.workflow.bug_repro` → active: preserves failure evidence for rollback/repair
- `vcb.workflow.testing` → active: catches regressions before they leave the branch

## Easy to recover

- `tool.v0` → active when output is a disposable UI sketch or copied component before repo merge
- `vcb.concepts.diff` → active
- `vcb.concepts.git_branch` → active
- `vcb.concepts.rollback` → active
- `vcb.chapter.git_discipline` → active
- `vcb.shortcut.one_big_prompt` → active: recoverable only when sliced, checkpointed, and reviewed before expansion

## Medium recoverability

- `tool.replit` → active when browser prototype is isolated and has a clear discard/export/harden path
- `tool.bolt` → active when generated code, dependencies, and publish target are inspected before handoff
- `tool.lovable` → active when full-stack app generation stays fake-data/staging-only until reviewed
- `vcb.chapter.feature_slicing` → active fallback
- `vcb.chapter.refactoring_without_breaking_everything` → active fallback
- `vcb.chapter.dependency_package_framework_decisions` → active fallback
- `vcb.chapter.cloud_delegation_parallel_work` → active fallback
- `vcb.shortcut.broad_refactor` → active: shortcut risk: cleanup drifting into behavior change

## Hard to recover

- `tool.stripe` → active: real-money payment/subscription/webhook mistakes can be hard to unwind
- `tool.supabase` → active: production schema/data/RLS/backup mistakes can be hard to recover
- `tool.clerk` → active: auth/session/user/org mistakes can lock users out or overgrant access
- `tool.auth0` → active: tenant/app/API/OIDC/OAuth configuration mistakes can break identity across systems
- `tool.vercel` → active companion: production deployment/environment mistakes need rollback/promotion discipline
- `tool.sentry` → active companion: improves recovery only if errors/traces/releases are configured and privacy-safe
- `tool.posthog` → active companion: feature flags and event evidence can improve recovery if owned and reversible
- `vcb.safety.production_red_lines` → active
- `vcb.safety.security_review` → active
- `vcb.shortcut.overbroad_ci_permissions` → active: overbroad tokens lower recoverability after compromise

## Improve recoverability before moving fast
- `vcb.concepts.recoverability` → active
- `vcb.chapter.sandboxing_and_approvals` → active
- `vcb.chapter.git_discipline` → active
- `vcb.chapter.senior_engineer_checklist` → active

## Make a shortcut recoverable before moving fast
- `vcb.chapter.risk_managed_shortcuts` → active
- `vcb.concepts.recoverability` → active
- `vcb.concepts.rollback` → active
- `vcb.chapter.git_discipline` → active

## Recover from stale or bad guidance

- `vcb.field.context_reset_between_tasks` → active candidate: recover from stale thread state by resetting with a handoff packet
- `vcb.field.lessons_file_loop` → active candidate: recover repeated corrections before promoting durable guidance
- `vcb.field.agents_md_first` → active candidate: recover missing durable guidance with a minimal project rule only after it proves durable
- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring and route/source refreshes
- `vcb.chapter.maintaining_updating_bible` → active fallback
- `vcb.chapter.field_notes_unofficial_practices` → active fallback

## Constraint choices by recoverability

- Easy-to-recover local work → `vcb.chapter.choosing_codex_operating_mode` active; lighter budget/workflow can be acceptable.
- Hard-to-recover production work → `vcb.chapter.budget_aware_codex_workflows` active; spend attention and usage on review/checks.
- Irreversible or secret-bearing work → `vcb.chapter.what_codex_is_bad_at` active; require threat model and rollback/rotation plan.

## Recoverability impact of foundational concepts

- `tool.supabase` → active companion: database/schema/migration/RLS recoverability is concrete platform risk
- `tool.clerk` → active companion: auth/session/user/org recoverability after access mistakes
- `tool.auth0` → active companion: IAM/OIDC/OAuth/API recoverability after tenant or token-policy mistakes
- `tool.stripe` → active companion: payment/subscription/webhook recoverability after real-money mistakes
- `tool.vercel` → active companion: deployment rollback and preview/production recovery
- `tool.sentry` → active companion: observability improves recovery with usable error/trace/release evidence
- `tool.posthog` → active companion: feature flags and behavior evidence can improve recovery if privacy-safe
- `vcb.concepts.database_schema` → active: low recoverability after real data migration
- `vcb.concepts.migration` → active: low recoverability unless backed up/staged
- `vcb.concepts.environment_variable` → active: low recoverability after secret leak
- `vcb.concepts.feature_flag` → active: high recoverability when flag is safe and server-side rules remain correct
- `vcb.concepts.ci` → active: improves recoverability by catching failures before merge/deploy
- `vcb.concepts.observability` → active: improves recovery by providing production evidence

## Recoverability by Codex feature

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

- `vcb.codex.app` → active: recovery plan and minimum guardrails
- `vcb.codex.cli` → active: recovery plan and minimum guardrails
- `vcb.codex.ide_extension` → active: recovery plan and minimum guardrails
- `vcb.codex.cloud` → active: recovery plan and minimum guardrails
- `vcb.codex.github_review` → active: recovery plan and minimum guardrails
- `vcb.codex.config` → active: recovery plan and minimum guardrails
- `vcb.codex.agents_md` → active: recovery plan and minimum guardrails
- `vcb.codex.skills` → active: recovery plan and minimum guardrails
- `vcb.codex.mcp` → active: recovery plan and minimum guardrails
- `vcb.codex.hooks` → active: recovery plan and minimum guardrails
- `vcb.codex.automations` → active: recovery plan and minimum guardrails
- `vcb.codex.subagents` → active: recovery plan and minimum guardrails
- `vcb.codex.computer_use` → active: recovery plan and minimum guardrails
- `vcb.codex.feature_maturity` → active: recovery plan and minimum guardrails
- `vcb.codex.changelog_monitoring` → active: recovery plan and minimum guardrails

## Review, Safety, and Verification Workflow Cards

- `vcb.workflow.codex_output_review` → active: Codex output review by diff, checks, and risk
- `vcb.workflow.reviewing_diffs` → active: local diff review and hunk-level risk scan
- `vcb.workflow.github_pr_review` → active: Codex-assisted PR review without treating AI as approval
- `vcb.safety.security_review` → active: trust-boundary, auth, data, and exploitability review
- `vcb.safety.secrets` → active: credentials, tokens, CI secrets, browser/session exposure
- `vcb.workflow.ci_triage` → active: failed-check and log triage before mutation
- `vcb.workflow.ci_noninteractive` → active: Codex in CI with least privilege and auditable outputs
- `vcb.safety.production_red_lines` → active: hard-stop gates for production-risk work

## Recoverability routes for frontend, refactor, dependency, release, and documentation workflows
- `vcb.workflow.frontend_work` → active: frontend state, responsive behavior, and browser evidence
- `vcb.workflow.visual_qa` → active: screenshot and visual-regression review
- `vcb.workflow.accessibility_review` → active: accessibility checks, keyboard paths, labels, and WCAG-guided review
- `vcb.workflow.refactoring` → active: behavior-preserving refactor workflow with tests and diff review
- `vcb.workflow.dependency_decisions` → active: new dependency/package/framework decision workflow
- `vcb.workflow.dependency_update_review` → active: dependency update and lockfile review workflow
- `vcb.workflow.release_notes` → active: release-note drafting from verified change sources
- `vcb.workflow.documentation_updates` → active: documentation update workflow tied to code, docs, and release context

## Failure modes by recoverability
- `vcb.failure.context_pollution` → active: recoverable before mutation; expensive after broad edits.
- `vcb.failure.hallucinated_apis` → active: recoverable with contract tests; poor if fake mocks spread.
- `vcb.failure.weakened_tests` → active: recoverable from git history; poor if old failure is lost.
- `vcb.failure.broad_refactor_drift` → active: recoverable with small commits; poor with a mixed rewrite.
- `vcb.failure.dependency_bloat` → active: recoverable when isolated; poor when architecture depends on it.
- `vcb.failure.ui_taste_gap` → active: recoverable with isolated components; poor with style drift.
- `vcb.failure.ci_false_confidence` → active: recoverable with logs/artifacts; poor if mutation and approval blend.
- `vcb.failure.done_claim_without_evidence` → active: recoverable when caught before merge; poor after users or maintainers rely on false completion status.

## Constraint and budget recoverability routes

- `vcb.constraints.recovery_budget` → primary route for recovery-cost-aware task sizing
- `vcb.constraints.operating_mode` → choose read-only/write/cloud/local mode from rollback capacity
- `vcb.constraints.attention_budget` → low attention requires higher recoverability or read-only work
- `vcb.constraints.scope_budget` → cheapest reliable path requires cheap recovery
- `vcb.constraints.usage_burn` → avoid repeated expensive runs by narrowing context and slice size
- `vcb.constraints.build_vs_maintenance` → maintenance needs higher recoverability than prototype exploration
- `vcb.constraints.production_quality` → production work requires rollback and evidence gates
- `vcb.constraints.review_budget` → parallel work needs branch/worktree isolation and merge/recovery plan

## Shortcut Recoverability Routes

- `vcb.shortcut.skipping_tests` → active: recoverable before merge when nearest checks are run
- `vcb.shortcut.skipping_plan` → active: recover by stopping mutation and writing a files/checks/rollback plan
- `vcb.shortcut.one_big_prompt` → active: recover by splitting the broad diff into staged slices
- `vcb.shortcut.vague_prompt` → active: recover by rewriting the request as goal/context/constraints/done-when
- `vcb.shortcut.accepting_diff_without_review` → active: recover by reviewing changed files before merge
- `vcb.shortcut.ignoring_lint_typecheck` → active: recover by separating old failures from new changed-file failures
- `vcb.shortcut.coding_on_main` → active: recover by moving work to a branch or worktree before more mutation
- `vcb.shortcut.manual_testing_only` → active: recover by recording manual evidence and adding one repeatable check when feasible
- `vcb.shortcut.debugging_without_repro` → active: recover by reconstructing the failure evidence before patching further
- `vcb.shortcut.accepting_looks_done` → active: recoverable before merge when evidence is reconstructed
- `vcb.shortcut.broad_agent_permissions` → active: low recoverability if secrets or external state are exposed
- `vcb.shortcut.unattended_long_runs` → active: recoverable when branch/worktree isolation and checkpoints exist
- `vcb.shortcut.broad_refactor` → active: recoverable when the refactor is one branch and one behavior-preserving axis
- `vcb.shortcut.context_dumping` → active: recoverable by resetting polluted context and rebuilding the task packet
- `vcb.shortcut.adding_dependencies_fast` → active: recoverable if manifest/lockfile changes are isolated before architectural coupling
- `vcb.shortcut.reviewing_cloud_summary_only` → active: recoverable before merge by reviewing returned diff/check artifacts

## Security and permission shortcut recoverability routes

- `vcb.shortcut.production_console_computer_use` → active: production console computer use security/permission shortcut guardrails
- `vcb.shortcut.overbroad_ci_permissions` → active: overbroad ci permissions security/permission shortcut guardrails
- `vcb.shortcut.long_lived_ci_secrets` → active: long-lived ci secrets security/permission shortcut guardrails
- `vcb.shortcut.real_secrets_in_prototype` → active: real secrets in prototype security/permission shortcut guardrails
- `vcb.shortcut.cloud_work_with_real_secrets` → active: cloud work with real secrets security/permission shortcut guardrails
- `vcb.shortcut.full_access_automation` → active: full-access automation security/permission shortcut guardrails
- `vcb.shortcut.unattended_mutation` → active: unattended mutation security/permission shortcut guardrails
- `vcb.shortcut.always_allow_sensitive_apps` → active: always allow sensitive apps security/permission shortcut guardrails

## Setup/process shortcut recoverability

- `vcb.shortcut.skipping_setup` → active: recover by capturing setup and rerunning authoritative checks.
- `vcb.shortcut.default_config_forever` → active: recover by reverting config and creating risk-specific profiles.
- `vcb.shortcut.skipping_agents_md` → active: recover by adding minimal durable guidance after repeated mistakes.
- `vcb.shortcut.overstuffing_agents_md` → active: recover by pruning stale/task-specific guidance.
- `vcb.shortcut.stale_agents_md` → active: recover by updating commands, rules, and source references.
- `vcb.shortcut.unofficial_tools` → active: recover by disabling tool, revoking credentials, and reviewing touched files/logs.
- `vcb.shortcut.hook_overreach` → active: recover by moving subjective checks to review/CI and leaving hooks objective.
- `vcb.shortcut.trusting_external_tool_output` → active: recover by re-checking provenance, source freshness, and affected decisions.

## Recoverability routes for tool-sprawl and process shortcuts

- `tool.docker` → active: recover by resetting containers/volumes, rebuilding images, reviewing Dockerfiles/Compose, and isolating secrets from images
- `tool.figma` → active: recover by comparing design versions, comments, prototype flows, component state, and implementation evidence
- `tool.linear` → active: recover by restoring issue/project ownership, closing stale status loops, and tying tickets to evidence
- `vcb.shortcut.skill_overkill` → active: avoid creating a skill before a repeated workflow earns it
- `vcb.shortcut.skill_sprawl` → active: audit overlapping skills and disabled stale reusable workflows
- `vcb.shortcut.tool_sprawl` → active: add one tool at a time with owner, purpose, and exit path
- `vcb.shortcut.tool_sprawl_mcp` → active: keep MCP servers scoped, allow-listed, and purpose-bound
- `vcb.shortcut.brittle_hooks` → active: keep hooks fast, deterministic, report-first, and reviewed
- `vcb.shortcut.process_overhead_for_tiny_project` → active: avoid heavyweight process before a tiny project earns it
- `vcb.shortcut.team_workflow_without_team` → active: use solo evidence workflow before team handoff process exists
- `vcb.shortcut.copy_pasting_playbook_blindly` → active: tailor reusable playbooks to actual risk, scope, and done evidence

## Recoverability routes for multi-AI/model-bias shortcuts

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

## Repository, CI, dependency, and QA recoverability routes

- Good recoverability → `tool.github` with small branches/PRs and revertable diffs.
- Good-to-moderate recoverability → `tool.github_actions` when workflows are report-first and least-privilege.
- Moderate recoverability → `tool.github_dependabot` and `tool.npm`; lockfile/dependency changes are revertable but can hide transitive breakage.
- Moderate recoverability → `tool.playwright`; test flakes and browser environment drift require artifact-based triage.
- Moderate-to-poor recoverability → `tool.openssf_scorecard` when scores are converted into rigid policy without context or exception handling.

## Recoverability routes for AI coding and IDE tools

- `tool.chatgpt` → active: planning, explanation, product thinking, source-backed research synthesis, and data/document analysis before implementation
- `tool.claude` → active: alternate AI review, architecture critique, long-form explanation, and source-checked second-opinion analysis
- `tool.cursor` → active: AI IDE-native planning, local multi-file edits, diff review, and supervised agentic coding workflows
- `tool.github_copilot` → active: GitHub/IDE-native suggestions, chat, repository-connected coding help, and PR/branch-adjacent assistance
- `tool.windsurf` → active: agentic AI IDE workflows with Cascade-style planning, editing, tool calls, checkpoints, and plugin support
- `vcb.workflow.reviewing_diffs` → active companion
- `tool.github` → active companion


## Browser-dev, app-builder, and UI-generation recoverability routes

- `tool.replit` → active: browser-based prototyping, hosted development, learning apps, and quick demo publishing with review/exit-path guardrails
- `tool.lovable` → active: AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails
- `tool.bolt` → active: browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points
- `vcb.concepts.recoverability` → active companion: require exit path before prototype becomes source of truth
- `vcb.concepts.rollback` → active companion: branch/PR/revert path for generated code

## Local dev, design, and project-management recoverability routes

- `tool.docker` → active: local environment recoverability, rebuild/reset posture, volume cleanup, image provenance, and containerized test evidence
- `tool.figma` → active: design-handoff recoverability, version/comment review, prototype-state review, and design-code drift evidence
- `tool.linear` → active: issue/project recoverability, owner/status repair, scope cleanup, and team execution hygiene
- `vcb.constraints.recovery_budget` → active companion
- `vcb.chapter.tool_stack_catalog` → active fallback

## Hosting, backend/auth, payment, observability, and analytics recoverability routes

- `tool.vercel` → active: hosting, preview deployments, environment separation, deployment evidence, and production promotion guardrails
- `tool.supabase` → active: Postgres database/backend/auth/storage, schema/RLS, migrations, backups, functions, and data-access guardrails
- `tool.clerk` → active: authentication, user management, sessions, organizations, and application identity guardrails
- `tool.auth0` → active: IAM, OAuth/OIDC, applications/APIs, enterprise/B2B identity, and authorization architecture guardrails
- `tool.stripe` → active: payments, subscriptions, checkout, webhooks, billing state, and real-money fulfillment guardrails
- `tool.sentry` → active: error monitoring, tracing, performance, release evidence, and production debugging guardrails
- `tool.posthog` → active: product analytics, event taxonomy, session replay, feature flags, experiments, and product-evidence guardrails

## Ecosystem tool recoverability

- `tool.cloudflare` → medium-to-low recoverability after public DNS/cache/routing/security changes propagate; require rollback and audit trail.
- `tool.netlify` → medium recoverability when deploy rollback and environment context are clear; lower when functions/env vars affect users.
- `tool.neon` → medium-to-low recoverability for production data/migrations; higher for disposable branches with cleanup policy.
- `tool.resend` → low recoverability after real emails are sent; use fake recipients and reviewed recipient policy first.
- `tool.vitest` → high recoverability for local tests; lower if tests are weakened and false confidence reaches release.
- `tool.storybook` → medium recoverability for stale stories; lower when design-system drift spreads across product surfaces.

<!-- VCB:STOP_RETRIEVAL reason="by_recoverability_complete" -->
<!-- VCB:END_INDEX id=vcb.index.by_recoverability -->
