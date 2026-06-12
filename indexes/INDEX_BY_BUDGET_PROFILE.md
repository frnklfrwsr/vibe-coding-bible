---
id: vcb.index.by_budget_profile
title: INDEX_BY_BUDGET_PROFILE
artifact_type: index
version: 0.41.0-draft.chunk40
status: chunk_40_updated
created_on: '2026-06-08'
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: quarterly
---

<!-- VCB:BEGIN_INDEX id=vcb.index.by_budget_profile version=0.41.0-draft.chunk40 -->

# INDEX_BY_BUDGET_PROFILE

> Status: Current routing index. Entries marked active have authored source files; entries marked planned are future routes.

## Plus or usage-constrained
- `vcb.chapter.four_part_prompt` → active
- `vcb.chapter.context_management` → active
- `vcb.chapter.feature_slicing` → active
- `vcb.chapter.codex_playbooks` → active
- `vcb.chapter.prompt_library_to_team_workflow` → active
- `vcb.constraints.scope_budget` → active: cheapest reliable workflow under tight constraints

## Pro or high-throughput
- `vcb.chapter.cloud_delegation_parallel_work` → active
- `vcb.chapter.subagents_parallel_thinking` → active
- `vcb.chapter.reviewing_codex_output` → active
- `vcb.chapter.ci_noninteractive_github_actions` → active
- `vcb.constraints.review_budget` → active: high-throughput workflow with isolation and review capacity

## API or pay-as-you-go automation
- `vcb.chapter.ci_noninteractive_github_actions` → active
- `vcb.chapter.automations_recurring_work` → active
- `vcb.chapter.codex_playbooks` → active
- `vcb.constraints.usage_burn` → active: usage burn and API budget controls

## Team or shared budget
- `vcb.chapter.prompt_library_to_team_workflow` → active
- `vcb.chapter.agents_md_operating_manual` → active
- `vcb.chapter.github_pr_review_with_codex` → active
- `vcb.chapter.senior_engineer_checklist` → active
- `vcb.constraints.team_shared_budget` → planned

## Low-attention review-later path
- `vcb.chapter.sandboxing_and_approvals` → active
- `vcb.chapter.cloud_delegation_parallel_work` → active
- `vcb.chapter.ci_noninteractive_github_actions` → active
- `vcb.chapter.automations_recurring_work` → active
- `vcb.chapter.senior_engineer_checklist` → active

## Production-quality path

- `tool.vercel` → active: production hosting, preview/production separation, deployment promotion, rollback, and deployment evidence
- `tool.cloudflare` → active: production DNS/CDN/edge routing, Workers/Pages, cache/security posture, and domain rollback evidence
- `tool.netlify` → active: production or preview deploys, deploy contexts, functions, environment variables, and rollback/deployment evidence
- `tool.supabase` → active: production database/backend/auth/storage, schema/RLS, migrations, backups, functions, and data-access review
- `tool.neon` → active: production or preview Postgres branches, migration review, connection evidence, and database recovery posture
- `tool.clerk` → active: authentication, sessions, user management, organizations, and app identity review when Clerk owns auth
- `tool.auth0` → active: IAM/OIDC/OAuth/API authorization and enterprise/B2B identity review when Auth0 owns auth
- `tool.stripe` → active: payments, subscriptions, checkout, webhooks, billing state, entitlement, and real-money review
- `tool.resend` → active: transactional email, sending domains, templates, notification delivery, and real-user email blast-radius review
- `tool.sentry` → active: production error, trace, performance, release, and incident evidence
- `tool.posthog` → active: product analytics, events, feature flags, experiments, replay, and product-behavior evidence
- `tool.vitest` → active companion: unit/component test evidence for production acceptance
- `tool.storybook` → active companion: component-state documentation, interaction tests, and design-handoff evidence
- `tool.codex_security` → active companion: security scans/findings/fix preparation
- `vcb.constraints.production_quality` → active companion: production-readiness evidence gate
- `vcb.chapter.git_discipline` → active fallback
- `vcb.chapter.writing_updating_tests` → active fallback
- `vcb.chapter.reviewing_codex_output` → active fallback
- `vcb.chapter.security_for_vibe_coders` → active fallback
- `vcb.chapter.senior_engineer_checklist` → active fallback

## Disposable prototype path
- `tool.docker` → active: resettable local services and containerized prototype dependencies when environment drift would waste review time
- `tool.figma` → active: disposable UI/design prototype and handoff path before implementation or app-builder generation
- `tool.linear` → active: lightweight scope/owner tracking when prototype work crosses people, days, or handoff boundaries
- `tool.replit` → active: browser-based prototyping, hosted development, learning apps, and quick demo publishing with review/exit-path guardrails
- `tool.lovable` → active: AI full-stack app-builder for product sketches and MVP flow validation with generated-app review guardrails
- `tool.bolt` → active: browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens and reviewable frontend starting points
- `vcb.constraints.build_vs_maintenance` → active companion: define prototype/MVP/production posture before generation
- `vcb.shortcut.real_secrets_in_prototype` → active companion: keep real credentials and production data out of disposable prototypes
- `vcb.chapter.first_serious_app` → active fallback
- `vcb.chapter.codex_playbooks` → active fallback
- `vcb.shortcut.generated_prototype_as_production_foundation` → planned future shortcut

## Budget-aware local-dev, design, and project-management tool routes

- `tool.docker` → active: local reproducibility and container setup add setup/maintenance cost but can reduce onboarding and environment-drift waste
- `tool.figma` → active: design/prototype work adds review and handoff cost but reduces implementation churn when product shape is uncertain
- `tool.linear` → active: issue/project hygiene adds process cost but reduces coordination loss when work crosses people or releases
- `vcb.constraints.build_vs_maintenance` → active companion

## Constrained users evaluating shortcuts or field practices

- `vcb.field.context_reset_between_tasks` → active candidate: cheap context-hygiene trial before spending more turns on stale context
- `vcb.field.skeleton_todo_first` → active candidate: cheapest way to constrain generated implementation shape
- `vcb.field.strict_typecheck_lint_gates` → active reproduced: use existing checks before adding new process
- `vcb.field.greenfield_vs_production_rule` → active candidate: avoid overbuilding or under-reviewing by stating phase
- `vcb.chapter.field_notes_unofficial_practices` → active fallback
- `vcb.chapter.risk_managed_shortcuts` → active fallback
- `vcb.concepts.recoverability` → active companion

## High-throughput users evaluating field practices

- `vcb.field.chatgpt_pm_codex_implementer` → active needs_more_evidence: split planning and implementation only when review owner can reconcile outputs
- `vcb.field.fresh_agent_review` → active reproduced: independent review signal before commit or merge
- `vcb.field.multi_agent_review_consensus` → active needs_more_evidence: compare evidence and disagreement; do not treat agreement as proof
- `vcb.field.lessons_file_loop` → active candidate: convert repeated corrections into durable guidance only after review
- `vcb.chapter.field_notes_unofficial_practices` → active fallback
- `vcb.chapter.risk_managed_shortcuts` → active fallback

## Maintenance budget and update hygiene
- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes
- `vcb.chapter.maintaining_updating_bible` → active
- `vcb.chapter.prompt_library_to_team_workflow` → active

## Plus / usage-constrained operating mode

- `vcb.chapter.choosing_codex_operating_mode` → active
- `vcb.chapter.budget_aware_codex_workflows` → active
- `vcb.chapter.context_management` → active
- `vcb.chapter.cost_benefit_analysis` → active

## Pro / high-throughput operating mode

- `vcb.chapter.budget_aware_codex_workflows` → active
- `vcb.chapter.cloud_delegation_parallel_work` → active
- `vcb.chapter.subagents_parallel_thinking` → active
- `vcb.shortcut.defaulting_to_high_throughput` → planned

## API / pay-as-you-go and team/shared budget

- `vcb.chapter.budget_aware_codex_workflows` → active
- `vcb.chapter.ci_noninteractive_github_actions` → active
- `vcb.chapter.tool_stack_catalog` → active
- `vcb.chapter.cost_benefit_analysis` → active

## Build high, maintain low strategy

- `vcb.chapter.build_phase_vs_maintenance_phase` → active
- `vcb.chapter.first_serious_app` → active
- `vcb.chapter.maintaining_updating_bible` → active
- `vcb.shortcut.permanent_high_usage_plan` → planned

## Workflow/prompting routes by budget profile
- `vcb.prompting.four_part_prompt` → active: cheapest way to prevent bad retries
- `vcb.prompting.context_management` → active: reduce token waste and stale-context loops
- `vcb.prompting.plan_first` → active: pay for planning only where wrong edits are expensive
- `vcb.prompting.acceptance_criteria` → active: avoid paying for unreviewable “looks done” work
- `vcb.workflow.feature_slicing` → active: buy one proven slice before broad implementation
- `vcb.workflow.testing` → active: run nearest relevant check instead of blind full-suite or no-check extremes

## Concept-first routes for constrained users
- `vcb.concepts.api_basics` → active: avoid expensive API guesswork
- `vcb.concepts.state` → active: reduce UI rework from stale/duplicate state
- `vcb.concepts.dependency` → active: avoid unnecessary packages
- `vcb.concepts.test` → active: pick the smallest meaningful verification
- `vcb.concepts.typecheck` → active: cheap correctness signal
- `vcb.concepts.lint` → active: cheap hygiene signal
- `vcb.concepts.build_step` → active: catch deploy blockers before wasting iterations

## Concept-first routes for production-quality work
- `vcb.concepts.authentication` → active
- `vcb.concepts.authorization` → active
- `vcb.concepts.database_schema` → active
- `vcb.concepts.migration` → active
- `vcb.concepts.environment_variable` → active
- `vcb.concepts.ci` → active
- `vcb.concepts.feature_flag` → active
- `vcb.concepts.observability` → active

## Budget-aware Codex feature selection

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

- `vcb.codex.app` → active: cost/attention tradeoffs
- `vcb.codex.cli` → active: cost/attention tradeoffs
- `vcb.codex.ide_extension` → active: cost/attention tradeoffs
- `vcb.codex.cloud` → active: cost/attention tradeoffs
- `vcb.codex.github_review` → active: cost/attention tradeoffs
- `vcb.codex.config` → active: cost/attention tradeoffs
- `vcb.codex.agents_md` → active: cost/attention tradeoffs
- `vcb.codex.skills` → active: cost/attention tradeoffs
- `vcb.codex.mcp` → active: cost/attention tradeoffs
- `vcb.codex.hooks` → active: cost/attention tradeoffs
- `vcb.codex.automations` → active: cost/attention tradeoffs
- `vcb.codex.subagents` → active: cost/attention tradeoffs
- `vcb.codex.computer_use` → active: cost/attention tradeoffs
- `vcb.codex.feature_maturity` → active: cost/attention tradeoffs
- `vcb.codex.changelog_monitoring` → active: cost/attention tradeoffs

## Budget-aware workflow/prompting cards

- `vcb.prompting.four_part_prompt` → active: cheapest reliable default because it reduces wasted turns.
- `vcb.prompting.acceptance_criteria` → active: prevents paying for ambiguous “almost done” loops.
- `vcb.prompting.plan_first` → active: spend planning tokens before expensive blind edits.
- `vcb.prompting.context_management` → active: avoid context dumping and stale-thread waste.
- `vcb.workflow.unknown_codebase` → active: short read-only orientation before paid implementation.
- `vcb.workflow.feature_slicing` → active: keep usage aligned to reviewable increments.
- `vcb.workflow.bug_repro` → active: stop paying for speculative fixes.
- `vcb.workflow.testing` → active: budget verification around smallest meaningful checks.

## Review, Safety, and Verification Workflow Cards

- `vcb.workflow.codex_output_review` → active: Codex output review by diff, checks, and risk
- `vcb.workflow.reviewing_diffs` → active: local diff review and hunk-level risk scan
- `vcb.workflow.github_pr_review` → active: Codex-assisted PR review without treating AI as approval
- `vcb.safety.security_review` → active: trust-boundary, auth, data, and exploitability review
- `vcb.safety.secrets` → active: credentials, tokens, CI secrets, browser/session exposure
- `vcb.workflow.ci_triage` → active: failed-check and log triage before mutation
- `vcb.workflow.ci_noninteractive` → active: Codex in CI with least privilege and auditable outputs
- `vcb.safety.production_red_lines` → active: hard-stop gates for production-risk work

## Budget-aware frontend, refactor, dependency, release, and documentation workflows
- `vcb.workflow.frontend_work` → active: frontend state, responsive behavior, and browser evidence
- `vcb.workflow.visual_qa` → active: screenshot and visual-regression review
- `vcb.workflow.accessibility_review` → active: accessibility checks, keyboard paths, labels, and WCAG-guided review
- `vcb.workflow.refactoring` → active: behavior-preserving refactor workflow with tests and diff review
- `vcb.workflow.dependency_decisions` → active: new dependency/package/framework decision workflow
- `vcb.workflow.dependency_update_review` → active: dependency update and lockfile review workflow
- `vcb.workflow.release_notes` → active: release-note drafting from verified change sources
- `vcb.workflow.documentation_updates` → active: documentation update workflow tied to code, docs, and release context

## Budget-aware failure-mode controls
- `vcb.failure.hallucinated_apis` → active: cheapest path is contract lookup before implementation.
- `vcb.failure.context_pollution` → active: cheapest path is context pruning before long runs.
- `vcb.failure.weakened_tests` → active: cheapest path is assertion review before broad CI runs.
- `vcb.failure.broad_refactor_drift` → active: cheapest path is one small behavior-preserving pass.
- `vcb.failure.dependency_bloat` → active: cheapest path is no-new-dependency first.
- `vcb.failure.ui_taste_gap` → active: cheapest path is target screenshot/state inventory before polish loops.
- `vcb.failure.ci_false_confidence` → active: cheapest path is log/artifact triage before mutation.
- `vcb.failure.done_claim_without_evidence` → active: cheapest path is requiring changed-file/check/screenshot/log evidence before more AI passes.

## Active Constraint and Budget Cards by Profile

### Plus or usage-constrained

- `vcb.constraints.scope_budget` → active: cheapest reliable workflow under tight usage or money constraints
- `vcb.constraints.usage_burn` → active: usage burn, context, retry, and current-source pricing checks
- `vcb.constraints.attention_budget` → active: spend scarce attention on scope and evidence

### Pro or high-throughput

- `vcb.constraints.review_budget` → active: parallel/high-usage work with isolation and review capacity
- `vcb.constraints.operating_mode` → active: choose surface and permission mode per task
- `vcb.constraints.recovery_budget` → active: prevent high-throughput work from exceeding rollback capacity

### Team or production-quality budget

- `vcb.constraints.build_vs_maintenance` → active: change team budget posture by phase
- `vcb.constraints.production_quality` → active: shared release gate and review evidence

## Shortcut Harm-Reduction Budget Routes

- `vcb.shortcut.skipping_tests` → active: cheapest reliable path is one nearest check rather than no verification
- `vcb.shortcut.accepting_looks_done` → active: cheapest reliable path is a completion-evidence table
- `vcb.shortcut.broad_agent_permissions` → active: cheapest reliable path is read-only or workspace-scoped permissions first
- `vcb.shortcut.unattended_long_runs` → active: cheapest reliable path is one milestone with a stop condition
- `vcb.shortcut.broad_refactor` → active: cheapest reliable path is one refactor axis per branch
- `vcb.shortcut.context_dumping` → active: cheapest reliable path is a curated context packet
- `vcb.shortcut.adding_dependencies_fast` → active: cheapest reliable path is no-new-dependency first
- `vcb.shortcut.reviewing_cloud_summary_only` → active: cheapest reliable path is a review packet focused on risky hunks

## Security and permission shortcut budget routes

- `vcb.shortcut.production_console_computer_use` → active: production console computer use security/permission shortcut guardrails
- `vcb.shortcut.overbroad_ci_permissions` → active: overbroad ci permissions security/permission shortcut guardrails
- `vcb.shortcut.long_lived_ci_secrets` → active: long-lived ci secrets security/permission shortcut guardrails
- `vcb.shortcut.real_secrets_in_prototype` → active: real secrets in prototype security/permission shortcut guardrails
- `vcb.shortcut.cloud_work_with_real_secrets` → active: cloud work with real secrets security/permission shortcut guardrails
- `vcb.shortcut.full_access_automation` → active: full-access automation security/permission shortcut guardrails
- `vcb.shortcut.unattended_mutation` → active: unattended mutation security/permission shortcut guardrails
- `vcb.shortcut.always_allow_sensitive_apps` → active: always allow sensitive apps security/permission shortcut guardrails

## Budget-aware setup/process shortcut controls

- `vcb.shortcut.skipping_setup` → active: setup inspection prevents expensive wrong edits.
- `vcb.shortcut.default_config_forever` → active: config review avoids paying with rework or incident response.
- `vcb.shortcut.skipping_agents_md` → active: minimal durable guidance saves repeated prompt/setup cost.
- `vcb.shortcut.overstuffing_agents_md` → active: concise AGENTS.md reduces usage burn and review noise.
- `vcb.shortcut.stale_agents_md` → active: pruning stale guidance reduces hidden maintenance cost.
- `vcb.shortcut.unofficial_tools` → active: disposable evaluation prevents credential/tooling recovery cost.
- `vcb.shortcut.hook_overreach` → active: objective hooks avoid slow brittle process tax.
- `vcb.shortcut.trusting_external_tool_output` → active: provenance checks avoid rework from wrong external context.

## Budget-aware tool-sprawl and reusable-process shortcut controls

- `vcb.shortcut.skill_overkill` → active: avoid creating a skill before a repeated workflow earns it
- `vcb.shortcut.skill_sprawl` → active: audit overlapping skills and disabled stale reusable workflows
- `vcb.shortcut.tool_sprawl` → active: add one tool at a time with owner, purpose, and exit path
- `vcb.shortcut.tool_sprawl_mcp` → active: keep MCP servers scoped, allow-listed, and purpose-bound
- `vcb.shortcut.brittle_hooks` → active: keep hooks fast, deterministic, report-first, and reviewed
- `vcb.shortcut.process_overhead_for_tiny_project` → active: avoid heavyweight process before a tiny project earns it
- `vcb.shortcut.team_workflow_without_team` → active: use solo evidence workflow before team handoff process exists
- `vcb.shortcut.copy_pasting_playbook_blindly` → active: tailor reusable playbooks to actual risk, scope, and done evidence

## Budget routes for multi-AI/model-bias shortcuts

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

## Budget-aware AI coding, AI IDE, and planning tool routes

- `tool.chatgpt` → active: planning, explanation, product thinking, source-backed research synthesis, and data/document analysis before implementation
- `tool.claude` → active: alternate AI review, architecture critique, long-form explanation, and source-checked second-opinion analysis
- `tool.cursor` → active: AI IDE-native planning, local multi-file edits, diff review, and supervised agentic coding workflows
- `tool.github_copilot` → active: GitHub/IDE-native suggestions, chat, repository-connected coding help, and PR/branch-adjacent assistance
- `tool.windsurf` → active: agentic AI IDE workflows with Cascade-style planning, editing, tool calls, checkpoints, and plugin support
- `vcb.constraints.usage_burn` → active companion
- `vcb.chapter.tool_stack_catalog` → active fallback

## Budget-aware hosting, backend/auth, payment, observability, and analytics routes

- `tool.vercel` → active: hosting/deployment cost, preview/production environments, and hidden platform usage should be source-checked before production.
- `tool.supabase` → active: database/backend/auth/storage and function usage can create hidden data, backup, migration, and operational cost.
- `tool.clerk` → active: auth/user/org/session usage and support needs should match the product phase.
- `tool.auth0` → active: enterprise/IAM complexity can outgrow prototype budgets quickly.
- `tool.stripe` → active: real-money integration cost includes support, refunds, disputes, tax, fulfillment, and reconciliation.
- `tool.sentry` → active: observability cost is justified by incident reduction only when signals have owners.
- `tool.posthog` → active: event/replay/flag cost and privacy overhead must be budgeted before broad instrumentation.

## Coverage-gap budget routes

- `tool.cloudflare` → active: cheapest path is DNS/edge/report-only review before public traffic changes; production path needs rollback and security/cache review.
- `tool.netlify` → active: cheapest path is preview-only deploy evidence; production path needs env-context, function, and rollback review.
- `tool.neon` → active: cheapest path is disposable branch/fake data; production path needs schema/migration/backup/data-owner review.
- `tool.resend` → active: cheapest path is sandbox/fake-recipient email; production path needs domain, template, consent, and delivery/error review.
- `tool.vitest` → active: cheapest path is nearest unit/component check; production path requires coverage against acceptance criteria and CI companion.
- `tool.storybook` → active: cheapest path is targeted stories for risky UI states; production path requires app/browser/accessibility evidence companions.

<!-- VCB:STOP_RETRIEVAL reason="by_budget_profile_complete" -->
<!-- VCB:END_INDEX id=vcb.index.by_budget_profile -->
