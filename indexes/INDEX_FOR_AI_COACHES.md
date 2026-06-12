---
id: vcb.index.for_ai_coaches
title: INDEX_FOR_AI_COACHES
artifact_type: index
version: 0.41.0-draft.chunk40
status: chunk_40_updated
created_on: '2026-06-08'
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: quarterly
---

<!-- VCB:BEGIN_INDEX id=vcb.index.for_ai_coaches version=0.41.0-draft.chunk40 -->

# INDEX_FOR_AI_COACHES

> Status: Current routing index. Entries marked active have authored source files; entries marked planned are future routes.

## Human is rushing
- `vcb.concepts.blast_radius` → active
- `vcb.concepts.recoverability` → active
- `vcb.chapter.plan_first_code_second` → active
- `vcb.prompting.plan_first` → active: coach a plan-before-editing gate
- `vcb.chapter.acceptance_criteria` → active
- `vcb.prompting.acceptance_criteria` → active: turn done into evidence
- `vcb.chapter.senior_engineer_checklist` → active
- `vcb.failure.done_claim_without_evidence` → active: interrupt vague done claims before acceptance
- `vcb.failure.context_pollution` → active: rushing often feeds stale or excessive context
- `vcb.shortcut.skipping_setup` → active: slow down enough to inspect setup before edits
- `vcb.shortcut.default_config_forever` → active: check whether defaults fit the current risk

## Human is over-trusting Codex
- `vcb.concepts.diff` → active
- `vcb.chapter.reviewing_codex_output` → active
- `vcb.chapter.failure_modes_codex_work` → active
- `vcb.shortcut.accepting_diff_without_review` → planned
- `vcb.failure.hallucinated_apis` → active: require contract evidence for plausible claims
- `vcb.failure.done_claim_without_evidence` → active: require artifact-backed completion evidence
- `vcb.failure.ci_false_confidence` → active: treat green checks as limited evidence

## Human is budget-constrained
- `vcb.chapter.context_management` → active
- `vcb.prompting.context_management` → active: reduce token waste and stale-context retries
- `vcb.chapter.feature_slicing` → active
- `vcb.workflow.feature_slicing` → active: smallest reliable build step
- `vcb.chapter.codex_playbooks` → active
- `vcb.constraints.scope_budget` → active: cheapest reliable workflow without skipping evidence
- `vcb.constraints.usage_burn` → active: usage burn and pricing-snapshot posture

## Human wants fastest possible path
- `vcb.shortcut.parallel_cloud_sprawl` → active: speed from parallel cloud tasks only works with independent scopes and review capacity
- `vcb.shortcut.conflicting_parallel_agents` → active: parallel mutation must be disjoint or serialized through one integrator
- `vcb.chapter.cloud_delegation_parallel_work` → active
- `vcb.chapter.subagents_parallel_thinking` → active
- `vcb.chapter.automations_recurring_work` → active
- `vcb.shortcut.unattended_long_runs` → active: shortcut risk: long autonomous work without checkpoints
- `vcb.constraints.review_budget` → active: high-throughput workflow with review capacity
- `vcb.constraints.recovery_budget` → active: speed bounded by recovery cost

## Human wants to skip planning, tests, review, or security
- `tool.codex_security` → active: Codex Security plugin/cloud scans, security diff review, finding validation, threat-model-informed triage, and reviewed fix preparation

- `vcb.shortcut.real_secrets_in_prototype` → active: stop real secrets in prototypes
- `vcb.shortcut.cloud_work_with_real_secrets` → active: stop real secrets in delegated cloud work
- `vcb.chapter.plan_first_code_second` → active
- `vcb.prompting.plan_first` → active: enforce plan-first when risk is nontrivial
- `vcb.chapter.writing_updating_tests` → active
- `vcb.workflow.testing` → active: nearest check and no weakened tests
- `vcb.chapter.reviewing_codex_output` → active
- `vcb.chapter.security_for_vibe_coders` → active
- `vcb.shortcut.skipping_plan` → planned
- `vcb.shortcut.skipping_tests` → active: shortcut risk: skipped verification and hidden regressions
- `vcb.shortcut.skipping_pr_review` → planned
- `vcb.shortcut.skipping_security_review` → planned
- `vcb.failure.weakened_tests` → active: reject making tests easier to pass
- `vcb.failure.ci_false_confidence` → active: reject check summaries that do not map to real coverage

## Human asks whether Codex Security can replace security review

- `tool.codex_security` → active: Codex Security plugin/cloud scans, security diff review, finding validation, threat-model-informed triage, and reviewed fix preparation
- `vcb.safety.security_review` → active: companion route for human security ownership, evidence, and severity review
- `vcb.safety.production_red_lines` → active: production hard-stop companion route

## Human wants broad permissions, automation, or GUI control
- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

- `vcb.shortcut.unattended_cloud_delegation` → active: coach cloud delegation into branch/worktree isolation and stop conditions
- `vcb.shortcut.automation_mutation_without_review` → active: coach recurring/noninteractive mutation back to report/propose or branch-only review
- `vcb.shortcut.logged_in_browser_secrets` → active: stop signed-in production/browser secret exposure
- `vcb.shortcut.browser_clicking_without_repro` → active: require exact GUI/browser repro before mutation
- `vcb.shortcut.full_access_automation` → active: coach away from full-access automation
- `vcb.shortcut.unattended_mutation` → active: require isolation and review packets for unattended mutation
- `vcb.shortcut.always_allow_sensitive_apps` → active: avoid persistent sensitive app/site approval
- `vcb.shortcut.production_console_computer_use` → active: keep production GUI actions human-owned
- `vcb.chapter.sandboxing_and_approvals` → active
- `vcb.chapter.ci_noninteractive_github_actions` → active
- `vcb.chapter.computer_use_browser_gui_tasks` → active
- `vcb.shortcut.broad_agent_permissions` → active: shortcut risk: excessive filesystem, command, network, or tool permissions
- `vcb.shortcut.logged_in_gui_production_actions` → planned
- `vcb.shortcut.unofficial_tools` → active: external tool trust review before enabling broad access
- `vcb.shortcut.hook_overreach` → active: hooks need narrow deterministic scope

## Human asks for a giant app or first serious app

- `tool.vercel` → active: coach deployment/preview/production ownership and environment separation
- `tool.cloudflare` → active when domains, DNS/CDN, edge routing, Workers/Pages, cache, or public traffic controls matter
- `tool.netlify` → active when deploy previews, functions, deploy contexts, or static/full-stack site deploys matter
- `tool.supabase` → active: coach database/backend/auth/storage ownership and RLS/data boundaries
- `tool.neon` → active when Postgres branching, preview databases, connections, or migration review matter
- `tool.clerk` → active: coach auth/session/user-management fit and authorization limits
- `tool.auth0` → active: coach IAM/OIDC/OAuth/API authorization fit and enterprise/B2B complexity
- `tool.stripe` → active: coach payment/subscription/webhook/entitlement risk before launch
- `tool.resend` → active when transactional email, notifications, sending domains, or template delivery matter
- `tool.sentry` → active: coach production error/performance evidence and incident triage
- `tool.posthog` → active: coach analytics/replay/feature-flag evidence and privacy boundaries
- `vcb.chapter.first_serious_app` → active fallback
- `vcb.chapter.codex_playbooks` → active fallback
- `vcb.chapter.feature_slicing` → active fallback
- `vcb.workflow.feature_slicing` → active: prevent one-giant-app prompts
- `vcb.prompting.four_part_prompt` → active: force scope and done-when
- `vcb.shortcut.overbuilding_first_app` → planned

## Human keeps repeating the same prompt or mistake
- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

- `vcb.chapter.prompt_library_to_team_workflow` → active
- `vcb.chapter.agents_md_operating_manual` → active
- `vcb.chapter.skills_reusable_workflows` → active
- `vcb.chapter.hooks_deterministic_guardrails` → active
- `vcb.shortcut.skipping_agents_md` → active: convert repeated repo rules into minimal durable guidance
- `vcb.shortcut.stale_agents_md` → active: prune stale repeated guidance

## Human cites an unofficial Codex tactic

- `vcb.field.chatgpt_pm_codex_implementer` → active candidate: ChatGPT PM / Codex implementer split
- `vcb.field.fresh_agent_review` → active candidate: fresh independent agent/session diff review
- `vcb.field.context_reset_between_tasks` → active candidate: reset or summarize context between unrelated tasks
- `vcb.field.agents_md_first` → active candidate: minimal AGENTS.md early in durable repos
- `vcb.field.skeleton_todo_first` → active candidate: human skeleton/TODOs before agent implementation
- `vcb.field.strict_typecheck_lint_gates` → active candidate: typecheck/lint/test gates after agent changes
- `vcb.field.greenfield_vs_production_rule` → active candidate: explicit project phase and compatibility posture
- `vcb.field.lessons_file_loop` → active candidate: temporary lessons loop before durable guidance promotion
- `vcb.field.multi_agent_review_consensus` → active candidate: multi-agent review with evidence, not consensus-as-proof
- `vcb.chapter.field_notes_unofficial_practices` → active fallback: evidence labels, promotion rules, and non-promotion policy
- `vcb.chapter.maintaining_updating_bible` → active companion
- `vcb.chapter.risk_managed_shortcuts` → active companion

## Human wants to skip a best practice
- `vcb.chapter.risk_managed_shortcuts` → active
- `vcb.concepts.blast_radius` → active
- `vcb.concepts.recoverability` → active
- `vcb.concepts.rollback` → active
- `vcb.shortcut.overstuffing_agents_md` → active: do not solve prompt discipline by dumping everything into AGENTS.md
- `vcb.shortcut.trusting_external_tool_output` → active: verify source/provenance before acceptance

## Human is updating Bible/source guidance
- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes
- `vcb.chapter.maintaining_updating_bible` → active fallback
- `vcb.chapter.field_notes_unofficial_practices` → active
## Human asks what plan or operating mode to use

- `vcb.shortcut.overbroad_ci_permissions` → active: align CI permissions with operating mode and risk
- `vcb.shortcut.long_lived_ci_secrets` → active: route CI credentials to scoped/short-lived alternatives
- `vcb.chapter.choosing_codex_operating_mode` → active
- `vcb.chapter.budget_aware_codex_workflows` → active
- `vcb.chapter.build_phase_vs_maintenance_phase` → active
- `vcb.pricing_snapshot.openai_codex` → snapshot
- `vcb.constraints.operating_mode` → active: operating-mode selector
- `vcb.constraints.attention_budget` → active: attention-aware delegation posture

## Human is buying tools instead of solving milestone risk

- `tool.docker` → active: local dev/container tool risk, environment parity, image/provenance, and secret/isolation guardrails
- `tool.figma` → active: design/prototype handoff risk, screenshot overtrust, stale specs, and design-code drift
- `tool.linear` → active: issue/project/workflow risk, status theater, missing owners, and planning without evidence
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
- `tool.chatgpt` → active companion: planning/explanation tool-choice risk
- `tool.claude` → active companion: alternate-review comparison risk
- `tool.cursor` → active companion: AI IDE implementation risk
- `tool.github_copilot` → active companion: IDE-native suggestion risk
- `tool.windsurf` → active companion: agentic IDE risk
- `vcb.shortcut.tool_sprawl` → active companion
- `vcb.chapter.tool_stack_catalog` → active fallback

## Human is overtrusting estimates or confident model output

- `vcb.shortcut.trusting_estimates_before_inspection` → active: intervene when the human accepts a time/scope/risk estimate before evidence inspection
- `vcb.shortcut.ignoring_model_biases` → active: intervene when confident phrasing masks model bias or missing evidence
- `vcb.shortcut.consensus_as_correctness` → active: intervene when multiple AI answers are treated as verification
- `vcb.shortcut.cherry_picking_ai_answers` → active: intervene when the human chooses the answer that supports a preferred outcome
- `vcb.shortcut.best_of_n_without_review` → active: intervene when answer-shopping replaces review and tests
- `vcb.chapter.what_codex_is_bad_at` → active
- `vcb.chapter.model_biases_failure_biases_bad_estimates` → active
- `vcb.chapter.reviewing_codex_output` → active

## Human is debugging without evidence
- `vcb.workflow.bug_repro` → active: reproduce before repair
- `vcb.workflow.testing` → active: regression and nearest-check evidence
- `vcb.prompting.acceptance_criteria` → active: expected/actual and done-when framing
- `vcb.chapter.debugging_with_reproduction` → active
- `vcb.failure.hallucinated_apis` → active: verify API/route claims during diagnosis
- `vcb.failure.done_claim_without_evidence` → active: require repro/check output before calling a bug fixed

## Human lacks foundational software vocabulary

- `tool.vercel` → active companion: hosting/deployment/environment vocabulary in practice
- `tool.supabase` → active companion: database/backend/auth/storage vocabulary in practice
- `tool.clerk` → active companion: authentication/session/user-management vocabulary in practice
- `tool.auth0` → active companion: authorization/IAM/OIDC/OAuth/API vocabulary in practice
- `tool.stripe` → active companion: payment/subscription/webhook vocabulary in practice
- `tool.sentry` → active companion: observability/error/tracing vocabulary in practice
- `tool.posthog` → active companion: analytics/event/feature-flag/replay vocabulary in practice
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

## Human asks for prompting or workflow help
- `vcb.prompting.four_part_prompt` → active: rewrite vague asks into work orders
- `vcb.prompting.plan_first` → active: decide whether to plan or implement
- `vcb.prompting.context_management` → active: curate context packets
- `vcb.prompting.acceptance_criteria` → active: define acceptance evidence
- `vcb.workflow.unknown_codebase` → active: map before mutation
- `vcb.workflow.feature_slicing` → active: choose the first vertical slice
- `vcb.workflow.bug_repro` → active: reproduce and patch narrowly
- `vcb.workflow.testing` → active: add/update focused tests and checks

## Human asks which primary Codex tool surface to use

- `tool.codex` → active: coach surface selection across first-party Codex tools
- `tool.codex_app` → active: recommend for supervised local desktop work when review/Git/worktrees matter
- `tool.codex_cli` → active: recommend for terminal-native command-backed work
- `tool.codex_ide_extension` → active: recommend for selected/open-file editor context
- `tool.codex_cloud` → active: recommend only for isolated review-later cloud tasks
- `tool.codex_github_review` → active: recommend as PR review signal, not merge authority
- `tool.codex_exec` → active: recommend for bounded non-interactive reports/scripts/CI runs

## Human asks which adjunct Codex surface to use

- `tool.codex_worktrees` → active: worktree isolation for parallel local/app tasks and automation change separation
- `tool.codex_subagents` → active: parallel specialist agents for bounded analysis, exploration, and disjoint implementation work
- `tool.codex_automations` → active: recurring/report-first Codex background work with review owner and stop conditions
- `tool.codex_computer_use` → active: desktop GUI operation with app permissions, visible-state risk, and human supervision
- `tool.codex_browser` → active: in-app rendered-page preview, comments, screenshots, and browser verification
- `tool.codex_chrome_extension` → active: signed-in Chrome browser workflows with website approvals and account-risk controls

## Human asks how to choose or use a Codex feature
- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes
- `tool.codex_security` → active: coach Codex Security feature/tool fit, evidence limits, threat-model context, and human security ownership
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

- `vcb.codex.app` → active: coach feature fit, guardrails, and volatile-source checks
- `vcb.codex.cli` → active: coach feature fit, guardrails, and volatile-source checks
- `vcb.codex.ide_extension` → active: coach feature fit, guardrails, and volatile-source checks
- `vcb.codex.cloud` → active: coach feature fit, guardrails, and volatile-source checks
- `vcb.codex.github_review` → active: coach feature fit, guardrails, and volatile-source checks
- `vcb.codex.config` → active: companion mechanics
- `vcb.codex.agents_md` → active: companion mechanics
- `vcb.codex.skills` → active: companion mechanics
- `vcb.codex.mcp` → active: companion mechanics
- `vcb.codex.hooks` → active: companion mechanics
- `vcb.codex.feature_maturity` → active companion
- `vcb.codex.changelog_monitoring` → active companion
## Review, Safety, and Verification Workflow Cards

- `vcb.workflow.codex_output_review` → active: Codex output review by diff, checks, and risk
- `vcb.workflow.reviewing_diffs` → active: local diff review and hunk-level risk scan
- `vcb.workflow.github_pr_review` → active: Codex-assisted PR review without treating AI as approval
- `vcb.safety.security_review` → active: trust-boundary, auth, data, and exploitability review
- `vcb.safety.secrets` → active: credentials, tokens, CI secrets, browser/session exposure
- `vcb.workflow.ci_triage` → active: failed-check and log triage before mutation
- `vcb.workflow.ci_noninteractive` → active: Codex in CI with least privilege and auditable outputs
- `vcb.safety.production_red_lines` → active: hard-stop gates for production-risk work

## Human asks for frontend, refactor, dependency, release-note, or documentation workflow help
- `tool.playwright` → active: browser/end-to-end tests, screenshots, traces, and UI verification evidence
- `tool.npm` → active: JavaScript package manifests, scripts, lockfiles, installs, and audit evidence
- `tool.github_dependabot` → active: dependency alerts, security update PRs, version update PRs, and dependency-maintenance queue
- `tool.openssf_scorecard` → active: supply-chain health signals, repository hardening checks, and dependency-adoption risk review
- `vcb.workflow.frontend_work` → active: frontend state, responsive behavior, and browser evidence
- `vcb.workflow.visual_qa` → active: screenshot and visual-regression review
- `vcb.workflow.accessibility_review` → active: accessibility checks, keyboard paths, labels, and WCAG-guided review
- `vcb.workflow.refactoring` → active: behavior-preserving refactor workflow with tests and diff review
- `vcb.workflow.dependency_decisions` → active: new dependency/package/framework decision workflow
- `vcb.workflow.dependency_update_review` → active: dependency update and lockfile review workflow
- `vcb.workflow.release_notes` → active: release-note drafting from verified change sources
- `vcb.workflow.documentation_updates` → active: documentation update workflow tied to code, docs, and release context

## Human asks for failure-mode diagnosis or accepts vague done claims
- `vcb.failure.hallucinated_apis` → active: coach contract lookup before trusting plausible APIs
- `vcb.failure.context_pollution` → active: coach context pruning and fresh source packets
- `vcb.failure.weakened_tests` → active: coach assertion, snapshot, mock, skip, and coverage review
- `vcb.failure.broad_refactor_drift` → active: coach behavior-preserving slices and diff boundaries
- `vcb.failure.dependency_bloat` → active: coach no-new-dependency first and maintenance-cost review
- `vcb.failure.ui_taste_gap` → active: coach state, responsive, browser, screenshot, and accessibility evidence
- `vcb.failure.ci_false_confidence` → active: coach CI log/artifact review and configured-check humility
- `vcb.failure.done_claim_without_evidence` → active: coach changed-file/check/screenshot/log evidence before acceptance

## Human needs constraint or budget coaching

- `vcb.constraints.operating_mode` → coach surface, permission, supervision, and evidence choices before coding
- `vcb.constraints.attention_budget` → coach low-attention users toward read-only, small-slice, or evidence-heavy delegation
- `vcb.constraints.usage_burn` → coach usage burn, context size, retries, MCP loading, and current pricing-source checks
- `vcb.constraints.recovery_budget` → coach rollback-first task sizing and permission control
- `vcb.constraints.build_vs_maintenance` → coach phase-appropriate speed versus stability tradeoffs
- `vcb.constraints.production_quality` → coach production-readiness gates and missing-evidence blocks
- `vcb.constraints.scope_budget` → coach constrained users toward low-cost but evidence-preserving workflows
- `vcb.constraints.review_budget` → coach high-throughput users away from review debt and parallel-write conflicts

## Coaching Routes — Active Shortcut Harm Reduction

- `vcb.shortcut.skipping_tests` → active: when the human wants to merge or continue without verification
- `vcb.shortcut.accepting_looks_done` → active: when the human trusts a polished final answer
- `vcb.shortcut.broad_agent_permissions` → active: when the human wants full access because setup feels slow
- `vcb.shortcut.unattended_long_runs` → active: when the human wants low-attention delegation or async progress
- `vcb.shortcut.broad_refactor` → active: when the human asks for cleanup/modernization without boundaries
- `vcb.shortcut.context_dumping` → active: when the human pastes excessive, stale, or sensitive context
- `vcb.shortcut.adding_dependencies_fast` → active: when the human or agent wants to install packages before proving need
- `vcb.shortcut.reviewing_cloud_summary_only` → active: when the human wants to accept background work from summary alone

## Human asks about Codex maturity, changelog, or deprecation watch
- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes
- `SOURCE_REGISTER.md` → active companion register
- `DEPRECATION_REGISTER.md` → active companion register

## Coaching Routes — Security and Permission Shortcuts

- `vcb.shortcut.production_console_computer_use` → active: production console computer use security/permission shortcut guardrails
- `vcb.shortcut.overbroad_ci_permissions` → active: overbroad ci permissions security/permission shortcut guardrails
- `vcb.shortcut.long_lived_ci_secrets` → active: long-lived ci secrets security/permission shortcut guardrails
- `vcb.shortcut.real_secrets_in_prototype` → active: real secrets in prototype security/permission shortcut guardrails
- `vcb.shortcut.cloud_work_with_real_secrets` → active: cloud work with real secrets security/permission shortcut guardrails
- `vcb.shortcut.full_access_automation` → active: full-access automation security/permission shortcut guardrails
- `vcb.shortcut.unattended_mutation` → active: unattended mutation security/permission shortcut guardrails
- `vcb.shortcut.always_allow_sensitive_apps` → active: always allow sensitive apps security/permission shortcut guardrails

## Coaching Routes — Setup and Process Shortcuts

- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

- `vcb.shortcut.skipping_setup` → coach when the human wants to code before project setup is known
- `vcb.shortcut.default_config_forever` → coach when old config defaults silently control new risk profiles
- `vcb.shortcut.skipping_agents_md` → coach when repeated repo guidance should become durable AGENTS.md guidance
- `vcb.shortcut.overstuffing_agents_md` → coach when the human wants to paste everything into AGENTS.md
- `vcb.shortcut.stale_agents_md` → coach when persistent guidance may be outdated
- `vcb.shortcut.unofficial_tools` → coach when a third-party tool/plugin/MCP server is adopted for speed
- `vcb.shortcut.hook_overreach` → coach when hooks are being used as broad policy or proof of safety
- `vcb.shortcut.trusting_external_tool_output` → coach when external tool output is accepted without source/evidence review

## Coaching Routes — Tool-Sprawl, Skill, and Process Shortcuts

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

## Coaching routes for multi-AI/model-bias shortcuts

- `tool.chatgpt` → active: planning, explanation, product thinking, source-backed research synthesis, and data/document analysis before implementation
- `tool.claude` → active: alternate AI review, architecture critique, long-form explanation, and source-checked second-opinion analysis
- `tool.cursor` → active: AI IDE-native planning, local multi-file edits, diff review, and supervised agentic coding workflows
- `tool.github_copilot` → active: GitHub/IDE-native suggestions, chat, repository-connected coding help, and PR/branch-adjacent assistance
- `tool.windsurf` → active: agentic AI IDE workflows with Cascade-style planning, editing, tool calls, checkpoints, and plugin support
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

## Human asks for CI, GitHub, dependency, or supply-chain tool choice

- `tool.github` → active: coach branches, PRs, branch protection, review owner, and rollback path.
- `tool.github_actions` → active: coach CI evidence, workflow permissions, secrets, logs, and flake triage.
- `tool.github_dependabot` → active: coach dependency alert/update PR review instead of auto-merge trust.
- `tool.npm` → active: coach package manifest, script, lockfile, and audit evidence review.
- `tool.playwright` → active: coach browser-test scope, artifacts, flake isolation, and UI evidence.
- `tool.openssf_scorecard` → active: coach supply-chain signals as triage, not safety certification.

## Human asks which AI coding, AI IDE, or planning tool to use

- `tool.chatgpt` → active: planning, explanation, product thinking, source-backed research synthesis, and data/document analysis before implementation
- `tool.claude` → active: alternate AI review, architecture critique, long-form explanation, and source-checked second-opinion analysis
- `tool.cursor` → active: AI IDE-native planning, local multi-file edits, diff review, and supervised agentic coding workflows
- `tool.github_copilot` → active: GitHub/IDE-native suggestions, chat, repository-connected coding help, and PR/branch-adjacent assistance
- `tool.windsurf` → active: agentic AI IDE workflows with Cascade-style planning, editing, tool calls, checkpoints, and plugin support
- `tool.codex` → active companion: first-party Codex tool-family chooser
- `vcb.chapter.tool_stack_catalog` → active fallback
- `vcb.chapter.when_to_use_other_ais` → active fallback


## Human wants to prototype a UI or app quickly

- `tool.figma` → active: design files, prototype flows, components, and UI-intent handoff before code
- `tool.linear` → active companion when prototype scope/ownership/team handoff must be explicit
- `tool.docker` → active companion when the prototype needs local services or reproducible setup
- `tool.replit` → active: browser-based prototyping, hosted development, learning apps, and quick demo publishing with review/exit-path guardrails
- `tool.lovable` → active: AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails
- `tool.bolt` → active: browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points
- `vcb.shortcut.real_secrets_in_prototype` → active companion: prevent real secrets/data in prototype
- `vcb.failure.ui_taste_gap` → active companion: require UI states/accessibility/browser evidence
- `vcb.constraints.build_vs_maintenance` → active companion: define prototype/MVP/production posture before generation

## Human asks which hosting, backend/auth, payment, observability, or analytics tool to use

- `tool.vercel` → active: hosting, preview deployments, environment separation, deployment evidence, and production promotion guardrails
- `tool.cloudflare` → active when domains, DNS/CDN, edge routing, Workers/Pages, cache, or public traffic controls matter
- `tool.netlify` → active when deploy previews, functions, deploy contexts, or static/full-stack site deploys matter
- `tool.supabase` → active: Postgres database/backend/auth/storage, schema/RLS, migrations, backups, functions, and data-access guardrails
- `tool.neon` → active when Postgres branching, preview databases, connections, or migration review matter
- `tool.clerk` → active: authentication, user management, sessions, organizations, and application identity guardrails
- `tool.auth0` → active: IAM, OAuth/OIDC, applications/APIs, enterprise/B2B identity, and authorization architecture guardrails
- `tool.stripe` → active: payments, subscriptions, checkout, webhooks, billing state, and real-money fulfillment guardrails
- `tool.resend` → active when transactional email, notifications, sending domains, or template delivery matter
- `tool.sentry` → active: error monitoring, tracing, performance, release evidence, and production debugging guardrails
- `tool.posthog` → active: product analytics, event taxonomy, session replay, feature flags, experiments, and product-evidence guardrails

## Human asks which local-dev, design, or project-management tool to use

- `tool.docker` → active: coach local reproducibility, containers, Compose, dev/test service isolation, and host/secrets risk
- `tool.figma` → active: coach design intent, prototypes, components, Dev Mode handoff, screenshot evidence, and implementation verification limits
- `tool.linear` → active: coach issue/project/workflow ownership, team execution hygiene, and ticket-status evidence limits
- `vcb.shortcut.tool_sprawl` → active companion
- `vcb.chapter.tool_stack_catalog` → active fallback

## Human asks about a missing or undercovered ecosystem tool

- `TOOL_REGISTER.md` → active: check Chunk 40 active/deferred/alias/exclusion coverage before assuming catalog completeness.
- `tool.cloudflare`, `tool.netlify`, `tool.neon`, `tool.resend`, `tool.vitest`, and `tool.storybook` → active newly authored coverage-gap cards.
- Deferred tools in the register → coach to use the listed active companion card, current official docs, and explicit evidence requirements until a full card is authored.

<!-- VCB:STOP_RETRIEVAL reason="for_ai_coaches_complete" -->
<!-- VCB:END_INDEX id=vcb.index.for_ai_coaches -->
