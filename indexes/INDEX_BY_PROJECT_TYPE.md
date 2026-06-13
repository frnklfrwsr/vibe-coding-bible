---
id: vcb.index.by_project_type
title: INDEX_BY_PROJECT_TYPE
artifact_type: index
version: 0.41.0-draft.chunk40
status: chunk_40_updated
created_on: '2026-06-08'
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: quarterly
---

<!-- VCB:BEGIN_INDEX id=vcb.index.by_project_type version=0.41.0-draft.chunk40 -->

# INDEX_BY_PROJECT_TYPE

> Status: Current routing index. Entries marked active have authored source files; entries marked planned are future routes.

## Prompting/workflow routes by project type
- `vcb.prompting.four_part_prompt` → active: all project types
- `vcb.prompting.acceptance_criteria` → active: required for production-facing and shared work
- `vcb.prompting.plan_first` → active: required for unknown, broad, or risky work
- `vcb.prompting.context_management` → active: required when repo/context is nontrivial
- `vcb.workflow.unknown_codebase` → active: inherited, open-source, generated, or legacy repos
- `vcb.workflow.feature_slicing` → active: MVP, public app, and team repos
- `vcb.workflow.bug_repro` → active: any nontrivial bug fix
- `vcb.workflow.testing` → active: production, shared, maintenance, and regression-prone work

## Throwaway prototype

- `tool.replit` → active: browser-based prototyping, hosted development, learning apps, and quick demo publishing with review/exit-path guardrails
- `tool.lovable` → active: AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails
- `tool.bolt` → active: browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points
- `vcb.concepts.diff` → active companion
- `vcb.concepts.blast_radius` → active companion
- `vcb.concepts.recoverability` → active companion
- `vcb.chapter.first_serious_app` → active fallback
- `vcb.chapter.codex_playbooks` → active fallback
- `vcb.shortcut.one_big_prompt` → active: keep prototype prompts sliced and disposable before treating generated output as foundation

## Learning project

- `tool.replit` → active: browser-based learning apps and fast publish/share feedback loops
- `tool.bolt` → active: beginner-friendly app/web prototype loops with token/review guardrails
- `tool.v0` → active: UI sketching and frontend component learning with code review
- `vcb.chapter.how_to_use_this_bible` → active fallback
- `vcb.chapter.vibe_coder_advantage_and_risk` → active fallback
- `vcb.chapter.codex_playbooks` → active fallback
- `vcb.chapter.failure_modes_codex_work` → active fallback

## Personal local tool
- `tool.docker` → active when the personal local tool needs containers, local services, reproducible setup, Dockerized checks, or resettable isolation evidence
- `vcb.concepts.git_branch` → active fallback
- `vcb.concepts.diff` → active
- `vcb.concepts.rollback` → active
- `vcb.chapter.git_discipline` → active
- `vcb.chapter.feature_slicing` → active

## Internal tool with non-sensitive data
- `vcb.chapter.understanding_unknown_codebase` → active
- `vcb.chapter.feature_slicing` → active
- `vcb.chapter.writing_updating_tests` → active
- `vcb.chapter.github_pr_review_with_codex` → active
- `vcb.chapter.prompt_library_to_team_workflow` → active

## Public app with users

- `tool.vercel` → active: preview/production deployment, environment separation, and release evidence
- `tool.supabase` → active: production-bound database/backend/auth/storage data posture
- `tool.clerk` → active: user auth/session/org management when selected
- `tool.auth0` → active: enterprise/API auth and authorization posture when selected
- `tool.stripe` → active: real-money payments/subscriptions and fulfillment evidence
- `tool.sentry` → active: error/performance/release monitoring
- `tool.posthog` → active: analytics, feature flags, session replay, and user-behavior evidence
- `tool.github` → active: repo/PR source of truth for production-bound work
- `tool.github_actions` → active: CI/check evidence before release
- `vcb.concepts.blast_radius` → active
- `vcb.concepts.recoverability` → active
- `vcb.chapter.security_for_vibe_coders` → active fallback
- `vcb.chapter.ci_noninteractive_github_actions` → active fallback
- `vcb.chapter.senior_engineer_checklist` → active fallback
- `vcb.safety.production_red_lines` → active

## Auth/payment/data-sensitive system

- `tool.clerk` → active: app identity, sessions, user management, and organization access review
- `tool.auth0` → active: IAM/OIDC/OAuth/API authorization and enterprise/B2B identity review
- `tool.supabase` → active: database, RLS, function secret, and data-access review
- `tool.stripe` → active: payment/subscription/billing/webhook state review
- `tool.sentry` → active: sensitive production error/trace evidence with privacy filtering
- `tool.posthog` → active: analytics/replay/flag evidence with privacy and consent boundaries
- `tool.codex_security` → active companion: security scans/findings/fix preparation
- `vcb.concepts.rollback` → active
- `vcb.safety.secrets` → active
- `vcb.safety.security_review` → active
- `vcb.chapter.security_for_vibe_coders` → active fallback
- `vcb.chapter.sandboxing_and_approvals` → active fallback
- `vcb.chapter.codex_playbooks` → active fallback

## Team or shared repo

- `tool.linear` → active: issues, projects, workflows, cycles, ownership, and team execution hygiene
- `tool.github` → active companion: repository source of truth
- `tool.github_actions` → active companion: CI/check evidence
- `tool.docker` → active companion: reproducible local services and onboarding environment
- `tool.figma` → active companion: design handoff and product/spec alignment
- `tool.github_copilot` → active: GitHub/IDE-native AI assistance in shared repository workflows
- `tool.cursor` → active: AI IDE workflow when local edits and review ownership are explicit
- `tool.windsurf` → active: agentic IDE workflow when checkpoints and team controls are explicit
- `vcb.concepts.pull_request` → active
- `vcb.field.contract_first_segmented_handoffs` → active candidate: long bounded team handoffs where one reviewed segment contract limits drift
- `vcb.chapter.github_pr_review_with_codex` → active
- `vcb.chapter.prompt_library_to_team_workflow` → active
- `vcb.chapter.agents_md_operating_manual` → active
- `vcb.chapter.senior_engineer_checklist` → active

## Learning or experiment project

- `vcb.field.context_reset_between_tasks` → active candidate: cheap context reset trial between small experiments
- `vcb.field.skeleton_todo_first` → active candidate: constrain generated experiment shape before implementation
- `vcb.field.greenfield_vs_production_rule` → active candidate: keep experiment/prototype posture explicit
- `vcb.chapter.field_notes_unofficial_practices` → active fallback
- `vcb.chapter.risk_managed_shortcuts` → active companion

## Public or production project considering shortcut
- `vcb.chapter.risk_managed_shortcuts` → active
- `vcb.chapter.security_for_vibe_coders` → active
- `vcb.field.contract_first_segmented_handoffs` → active candidate: production-adjacent long handoffs need explicit contract, owner, checks, and rollback
- `vcb.concepts.blast_radius` → active
- `vcb.concepts.recoverability` → active

## Project type constraint routing

- Throwaway prototype → `tool.figma` active first when UI/design intent matters; `tool.docker` active companion when local services or reproducible setup matter; `tool.linear` active companion only when scope ownership or team handoff is needed; `tool.replit`, `tool.lovable`, `tool.bolt`, and `tool.v0` active app-builder/UI-generation routes; `vcb.constraints.build_vs_maintenance` active companion; `vcb.chapter.choosing_codex_operating_mode` active fallback; `vcb.chapter.tool_stack_catalog` active fallback; `vcb.shortcut.generated_prototype_as_production_foundation` planned future shortcut.
- Public app with users → `tool.vercel`, `tool.supabase`, `tool.clerk` or `tool.auth0`, `tool.sentry`, and `tool.posthog` active first when the project needs hosting, backend/auth, monitoring, or product evidence; `tool.stripe` active first when money movement is in scope; `vcb.chapter.cost_benefit_analysis`, `vcb.chapter.security_for_vibe_coders`, and `vcb.chapter.senior_engineer_checklist` active fallbacks.
- Auth/payment/data-sensitive system → `tool.clerk`, `tool.auth0`, `tool.supabase`, and `tool.stripe` active first for identity/data/payment surfaces; `tool.sentry` and `tool.posthog` active companions for monitored production behavior with privacy guardrails; `vcb.chapter.what_codex_is_bad_at`, `vcb.chapter.model_biases_failure_biases_bad_estimates`, and `vcb.chapter.security_for_vibe_coders` active fallbacks.

## Foundational concepts by project type
- Throwaway prototype → `vcb.concepts.frontend_backend`, `vcb.concepts.state`, `vcb.concepts.dependency` → active
- Personal local tool → `vcb.concepts.environment_variable`, `vcb.concepts.test`, `vcb.concepts.build_step` → active
- Public app with users → `vcb.concepts.authentication`, `vcb.concepts.authorization`, `vcb.concepts.ci`, `vcb.concepts.observability` → active
- Auth/payment/data-sensitive system → `vcb.concepts.database_schema`, `vcb.concepts.migration`, `vcb.concepts.environment_variable`, `vcb.concepts.feature_flag` → active

## Codex feature selection by project type

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

- `vcb.codex.app` → active: use only when project risk and attention match
- `vcb.codex.cli` → active: use only when project risk and attention match
- `vcb.codex.ide_extension` → active: use only when project risk and attention match
- `vcb.codex.cloud` → active: use only when project risk and attention match
- `vcb.codex.github_review` → active: use only when project risk and attention match
- `vcb.codex.config` → active: use only when project risk and attention match
- `vcb.codex.agents_md` → active: use only when project risk and attention match
- `vcb.codex.skills` → active: use only when project risk and attention match
- `vcb.codex.mcp` → active: use only when project risk and attention match
- `vcb.codex.hooks` → active: use only when project risk and attention match
- `vcb.codex.automations` → active: use only when project risk and attention match
- `vcb.codex.subagents` → active: use only when project risk and attention match
- `vcb.codex.computer_use` → active: use only when project risk and attention match
- `vcb.codex.feature_maturity` → active: use only when project risk and attention match
- `vcb.codex.changelog_monitoring` → active: use only when project risk and attention match

## Review, Safety, and Verification Workflow Cards

- `vcb.workflow.codex_output_review` → active: Codex output review by diff, checks, and risk
- `vcb.workflow.reviewing_diffs` → active: local diff review and hunk-level risk scan
- `vcb.workflow.github_pr_review` → active: Codex-assisted PR review without treating AI as approval
- `vcb.safety.security_review` → active: trust-boundary, auth, data, and exploitability review
- `vcb.safety.secrets` → active: credentials, tokens, CI secrets, browser/session exposure
- `vcb.workflow.ci_triage` → active: failed-check and log triage before mutation
- `vcb.workflow.ci_noninteractive` → active: Codex in CI with least privilege and auditable outputs
- `vcb.safety.production_red_lines` → active: hard-stop gates for production-risk work

## Project-type routes for frontend, refactor, dependency, release, and documentation workflows
- `vcb.workflow.frontend_work` → active: frontend state, responsive behavior, and browser evidence
- `vcb.workflow.visual_qa` → active: screenshot and visual-regression review
- `vcb.workflow.accessibility_review` → active: accessibility checks, keyboard paths, labels, and WCAG-guided review
- `vcb.workflow.refactoring` → active: behavior-preserving refactor workflow with tests and diff review
- `vcb.workflow.dependency_decisions` → active: new dependency/package/framework decision workflow
- `vcb.workflow.dependency_update_review` → active: dependency update and lockfile review workflow
- `vcb.workflow.release_notes` → active: release-note drafting from verified change sources
- `vcb.workflow.documentation_updates` → active: documentation update workflow tied to code, docs, and release context

## Project-type routes for failure modes
- `vcb.failure.hallucinated_apis` → active: hallucinated APIs and fake interface contracts
- `vcb.failure.context_pollution` → active: stale, noisy, excessive, or contradictory context
- `vcb.failure.weakened_tests` → active: tests changed to pass without proving behavior
- `vcb.failure.broad_refactor_drift` → active: refactor work drifting into behavior change or rewrite
- `vcb.failure.dependency_bloat` → active: unnecessary dependencies and supply-chain drag
- `vcb.failure.ui_taste_gap` → active: frontend work that renders but lacks state, responsive, accessibility, or polish evidence
- `vcb.failure.ci_false_confidence` → active: green CI mistaken for complete verification
- `vcb.failure.done_claim_without_evidence` → active: done claim without artifact evidence

## Failure modes by project type
- Prototypes: `vcb.failure.dependency_bloat`, `vcb.failure.ui_taste_gap`, `vcb.failure.context_pollution`
- Production builds: `vcb.failure.ci_false_confidence`, `vcb.failure.broad_refactor_drift`, `vcb.failure.dependency_bloat`
- Maintenance: `vcb.failure.broad_refactor_drift`, `vcb.failure.weakened_tests`, `vcb.failure.context_pollution`

## Constraint and budget routes by project phase

- Prototype → `vcb.constraints.scope_budget`, `vcb.constraints.build_vs_maintenance`, `vcb.constraints.usage_burn`
- MVP → `vcb.constraints.operating_mode`, `vcb.constraints.attention_budget`, `vcb.constraints.recovery_budget`
- Production build → `vcb.constraints.production_quality`, `vcb.constraints.recovery_budget`, `vcb.constraints.operating_mode`
- Maintenance → `vcb.constraints.build_vs_maintenance`, `vcb.constraints.attention_budget`, `vcb.constraints.scope_budget`
- Major refactor → `vcb.constraints.recovery_budget`, `vcb.constraints.review_budget`, `vcb.constraints.production_quality`
- Emergency hotfix → `vcb.constraints.recovery_budget`, `vcb.constraints.production_quality`, `vcb.constraints.attention_budget`

## Shortcut Harm-Reduction by Project Type

- `vcb.shortcut.skipping_tests` → active: skip-test shortcut; route to smallest relevant verification guardrail
- `vcb.shortcut.skipping_plan` → active: acceptable only when work is tiny, local, and recoverable
- `vcb.shortcut.one_big_prompt` → active: keep broad prototype prompts disposable or sliced
- `vcb.shortcut.vague_prompt` → active: require explicit goal/context/constraints/done-when for durable work
- `vcb.shortcut.accepting_diff_without_review` → active: shared or production work needs changed-file review
- `vcb.shortcut.ignoring_lint_typecheck` → active: shared or production work needs static-check triage
- `vcb.shortcut.coding_on_main` → active: risky for shared, public, or auto-deploying repos
- `vcb.shortcut.manual_testing_only` → active: prototype-tolerable but production work needs repeatable checks
- `vcb.shortcut.debugging_without_repro` → active: acceptable only for obvious local errors; risky for user-facing bugs
- `vcb.shortcut.accepting_looks_done` → active: looks-done shortcut; route to completion-evidence gate
- `vcb.shortcut.broad_agent_permissions` → active: broad-permission shortcut; route to sandbox/approval and blast-radius controls
- `vcb.shortcut.unattended_long_runs` → active: unattended-run shortcut; route to milestones, isolation, and evidence reports
- `vcb.shortcut.broad_refactor` → active: broad-refactor shortcut; route to behavior-preserving refactor boundaries
- `vcb.shortcut.context_dumping` → active: context-dumping shortcut; route to curated context packet control
- `vcb.shortcut.adding_dependencies_fast` → active: fast dependency shortcut; route to package decision and lockfile review guardrails
- `vcb.shortcut.reviewing_cloud_summary_only` → active: cloud-summary-only shortcut; route to diff/check/artifact review guardrail

## Security and permission shortcuts by project type

- `vcb.shortcut.production_console_computer_use` → active: production console computer use security/permission shortcut guardrails
- `vcb.shortcut.overbroad_ci_permissions` → active: overbroad ci permissions security/permission shortcut guardrails
- `vcb.shortcut.long_lived_ci_secrets` → active: long-lived ci secrets security/permission shortcut guardrails
- `vcb.shortcut.real_secrets_in_prototype` → active: real secrets in prototype security/permission shortcut guardrails
- `vcb.shortcut.cloud_work_with_real_secrets` → active: cloud work with real secrets security/permission shortcut guardrails
- `vcb.shortcut.full_access_automation` → active: full-access automation security/permission shortcut guardrails
- `vcb.shortcut.unattended_mutation` → active: unattended mutation security/permission shortcut guardrails
- `vcb.shortcut.always_allow_sensitive_apps` → active: always allow sensitive apps security/permission shortcut guardrails

## Setup/process shortcuts by project type

- `vcb.shortcut.skipping_setup` → active: acceptable only for disposable prototypes; risky for shared or production repos.
- `vcb.shortcut.default_config_forever` → active: risky when solo prototype settings become team defaults.
- `vcb.shortcut.skipping_agents_md` → active: risky for teams and recurring project work.
- `vcb.shortcut.overstuffing_agents_md` → active: risky for long-lived repos and teams using shared guidance.
- `vcb.shortcut.stale_agents_md` → active: risky in maintenance-heavy projects.
- `vcb.shortcut.unofficial_tools` → active: risky for security-sensitive, regulated, or production-adjacent repos.
- `vcb.shortcut.hook_overreach` → active: risky for teams when hooks become brittle workflow blockers.
- `vcb.shortcut.trusting_external_tool_output` → active: risky when external tools influence production, dependency, or security decisions.

## Project-size routes for tool-sprawl and reusable-process shortcuts

- `vcb.shortcut.skill_overkill` → active: avoid creating a skill before a repeated workflow earns it
- `vcb.shortcut.skill_sprawl` → active: audit overlapping skills and disabled stale reusable workflows
- `vcb.shortcut.tool_sprawl` → active: add one tool at a time with owner, purpose, and exit path
- `vcb.shortcut.tool_sprawl_mcp` → active: keep MCP servers scoped, allow-listed, and purpose-bound
- `vcb.shortcut.brittle_hooks` → active: keep hooks fast, deterministic, report-first, and reviewed
- `vcb.shortcut.process_overhead_for_tiny_project` → active: avoid heavyweight process before a tiny project earns it
- `vcb.shortcut.team_workflow_without_team` → active: use solo evidence workflow before team handoff process exists
- `vcb.shortcut.copy_pasting_playbook_blindly` → active: tailor reusable playbooks to actual risk, scope, and done evidence

## Project routes for multi-AI/model-bias shortcuts

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

## Repository, CI, dependency, and QA project routes

- Prototype web app → `tool.github`, `tool.npm`, `tool.playwright` → active; keep checks small and reviewable.
- Production web app → `tool.github`, `tool.github_actions`, `tool.github_dependabot`, `tool.npm`, `tool.playwright`, `tool.openssf_scorecard` → active; require PR, CI, dependency, and browser evidence.
- Maintenance dependency work → `tool.github_dependabot`, `tool.npm`, `tool.github_actions`, `tool.openssf_scorecard` → active; review update PRs, lockfiles, advisories, and CI artifacts.
- Supply-chain-sensitive library → `tool.github`, `tool.github_actions`, `tool.github_dependabot`, `tool.openssf_scorecard` → active; treat automated signals as triage, not certification.

## AI coding, AI IDE, and planning tool project routes

- `tool.chatgpt` → active: planning, explanation, product thinking, source-backed research synthesis, and data/document analysis before implementation
- `tool.claude` → active: alternate AI review, architecture critique, long-form explanation, and source-checked second-opinion analysis
- `tool.cursor` → active: AI IDE-native planning, local multi-file edits, diff review, and supervised agentic coding workflows
- `tool.github_copilot` → active: GitHub/IDE-native suggestions, chat, repository-connected coding help, and PR/branch-adjacent assistance
- `tool.windsurf` → active: agentic AI IDE workflows with Cascade-style planning, editing, tool calls, checkpoints, and plugin support
- `tool.codex` → active companion: first-party Codex tool-family chooser


## Browser-dev, app-builder, and UI-generation routes by project type

- `tool.replit` → active: browser-based prototyping, hosted development, learning apps, and quick demo publishing with review/exit-path guardrails
- `tool.lovable` → active: AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails
- `tool.bolt` → active: browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points
- `vcb.shortcut.real_secrets_in_prototype` → active companion: prototype data/secrets boundary
- `vcb.constraints.production_quality` → active companion: promote only after production evidence exists

## Local dev, design, and project-management routes by project type

- `tool.docker` → active: learning projects, local tools, shared repos, and production-bound apps that need reproducible services, environment parity, or containerized checks
- `tool.figma` → active: UI-heavy prototypes, frontend work, product flows, design handoff, and stakeholder review before implementation
- `tool.linear` → active: team/shared repos, scoped MVPs, multi-person execution, issue ownership, project planning, and maintenance queues
- `tool.github` → active companion for shared code and PR ownership
- `tool.github_actions` → active companion for CI/check evidence
- `vcb.chapter.tool_stack_catalog` → active fallback

## Hosting, backend/auth, payment, observability, and analytics routes by project type

- `tool.vercel` → active: hosting, preview deployments, environment separation, deployment evidence, and production promotion guardrails
- `tool.supabase` → active: Postgres database/backend/auth/storage, schema/RLS, migrations, backups, functions, and data-access guardrails
- `tool.clerk` → active: authentication, user management, sessions, organizations, and application identity guardrails
- `tool.auth0` → active: IAM, OAuth/OIDC, applications/APIs, enterprise/B2B identity, and authorization architecture guardrails
- `tool.stripe` → active: payments, subscriptions, checkout, webhooks, billing state, and real-money fulfillment guardrails
- `tool.sentry` → active: error monitoring, tracing, performance, release evidence, and production debugging guardrails
- `tool.posthog` → active: product analytics, event taxonomy, session replay, feature flags, experiments, and product-evidence guardrails

## Ecosystem coverage by project type

- Production web app with edge/DNS/deploy platform risk → `tool.cloudflare`, `tool.netlify`, `tool.vercel`, `tool.github_actions`, and `vcb.constraints.production_quality` active.
- Database-backed MVP or preview-database workflow → `tool.neon` active; `tool.supabase` companion.
- User-notification or email workflow → `tool.resend` active; `tool.clerk`, `tool.auth0`, and `tool.stripe` companions when auth/payment state triggers email.
- JavaScript app with local/unit evidence needs → `tool.vitest` active; `tool.npm` and `tool.github_actions` companions.
- Component-heavy UI or design-system project → `tool.storybook` active; `tool.figma`, `tool.playwright`, and `tool.vitest` companions.
- Missing named ecosystem tool → `TOOL_REGISTER.md` Chunk 40 coverage audit first; use deferred row companion route.

<!-- VCB:STOP_RETRIEVAL reason="by_project_type_complete" -->
<!-- VCB:END_INDEX id=vcb.index.by_project_type -->
