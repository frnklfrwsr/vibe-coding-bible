---
id: vcb.index.by_concept
title: INDEX_BY_CONCEPT
artifact_type: index
version: 0.41.0-draft.chunk40
status: chunk_40_updated
created_on: '2026-06-08'
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: quarterly
---

<!-- VCB:BEGIN_INDEX id=vcb.index.by_concept version=0.41.0-draft.chunk40 -->

# INDEX_BY_CONCEPT

> Status: Current routing index. Entries marked active have authored source files; entries marked planned are future routes.

## Core software control concepts
- `vcb.concepts.diff` → active
- `vcb.concepts.blast_radius` → active
- `vcb.concepts.recoverability` → active
- `vcb.concepts.rollback` → active
- `vcb.concepts.git_branch` → active
- `vcb.concepts.pull_request` → active

## Codex mental model concepts
- `tool.codex_feature_maturity` → active: maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `vcb.codex.feature_maturity` → active companion: feature-maturity mechanics
- `vcb.chapter.codex_mental_model` → active fallback
- `vcb.chapter.vibe_coder_advantage_and_risk` → active fallback
- `vcb.chapter.codex_surfaces` → active fallback
- `vcb.codex.mental_model` → planned

## Prompting and work-order concepts
- `vcb.chapter.four_part_prompt` → active
- `vcb.chapter.plan_first_code_second` → active
- `vcb.chapter.context_management` → active
- `vcb.chapter.acceptance_criteria` → active
- `vcb.prompting.four_part_prompt` → active: goal/context/constraints/done-when work order
- `vcb.prompting.plan_first` → active: planning gate before risky edits
- `vcb.prompting.context_management` → active: context packet and stale-context control
- `vcb.prompting.acceptance_criteria` → active: evidence-backed done-when criteria

## Workflow concepts
- `vcb.chapter.understanding_unknown_codebase` → active
- `vcb.chapter.feature_slicing` → active
- `vcb.chapter.debugging_with_reproduction` → active
- `vcb.chapter.writing_updating_tests` → active
- `vcb.chapter.frontend_work` → active
- `vcb.chapter.refactoring_without_breaking_everything` → active
- `vcb.chapter.dependency_package_framework_decisions` → active
- `vcb.workflow.unknown_codebase` → active: read-only map before mutation
- `vcb.workflow.feature_slicing` → active: smallest reviewable vertical slice
- `vcb.workflow.bug_repro` → active: reproduce before fixing
- `vcb.workflow.testing` → active: executable verification evidence

## Persistent guidance and customization concepts
- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

- `vcb.chapter.agents_md_operating_manual` → active
- `vcb.chapter.codex_config_defaults` → active
- `vcb.chapter.skills_reusable_workflows` → active
- `vcb.chapter.mcp_external_tools` → active
- `vcb.chapter.hooks_deterministic_guardrails` → active

## Review, security, and automation concepts
- `tool.codex_security` → active: Codex Security plugin/cloud scans, security diff review, finding validation, threat-model-informed triage, and reviewed fix preparation

- `vcb.shortcut.automation_spam` → active: automation should filter attention, not create noise
- `vcb.shortcut.automation_mutation_without_review` → active: recurring mutation requires review gates and audit evidence
- `vcb.shortcut.unattended_cloud_delegation` → active: background delegation does not remove human ownership of merge/review
- `vcb.chapter.reviewing_codex_output` → active
- `vcb.chapter.github_pr_review_with_codex` → active
- `vcb.chapter.security_for_vibe_coders` → active
- `vcb.chapter.ci_noninteractive_github_actions` → active
- `vcb.safety.secrets` → active
- `vcb.safety.prompt_injection` → planned

## Advanced agentic workflow concepts
- `vcb.shortcut.parallel_cloud_sprawl` → active: parallel cloud work needs a task matrix and integration owner
- `vcb.shortcut.conflicting_parallel_agents` → active: parallel agents need file ownership and semantic conflict controls
- `vcb.shortcut.cloud_task_without_context` → active: cloud delegation needs explicit context and verification packet
- `vcb.chapter.cloud_delegation_parallel_work` → active
- `vcb.chapter.subagents_parallel_thinking` → active
- `vcb.chapter.automations_recurring_work` → active
- `vcb.chapter.computer_use_browser_gui_tasks` → active

## Operating-system concepts
- `vcb.chapter.prompt_library_to_team_workflow` → active
- `vcb.chapter.failure_modes_codex_work` → active
- `vcb.chapter.codex_playbooks` → active
- `vcb.chapter.first_serious_app` → active
- `vcb.chapter.senior_engineer_checklist` → active

## Field practices and evidence labels

- `vcb.field.chatgpt_pm_codex_implementer` → active needs_more_evidence: ChatGPT PM / Codex implementer split remains too broad for bounded local reproduction
- `vcb.field.fresh_agent_review` → active reproduced: bounded local reproduction through PR review gate; not promoted as universal proof
- `vcb.field.context_reset_between_tasks` → active candidate: reset or summarize context between unrelated tasks
- `vcb.field.agents_md_first` → active candidate: minimal AGENTS.md early in durable repos
- `vcb.field.skeleton_todo_first` → active candidate: human skeleton/TODOs before agent implementation
- `vcb.field.strict_typecheck_lint_gates` → active reproduced: bounded local reproduction through VCB validator gate; not promoted as universal proof
- `vcb.field.greenfield_vs_production_rule` → active candidate: explicit project phase and compatibility posture
- `vcb.field.lessons_file_loop` → active candidate: temporary lessons loop before durable guidance promotion
- `vcb.field.multi_agent_review_consensus` → active needs_more_evidence: multi-agent review must not treat agreement as proof
- `vcb.chapter.field_notes_unofficial_practices` → active fallback: field-practice taxonomy, promotion rules, and non-promotion rule
- `FIELD_PRACTICES.md` → register: candidate status and review trigger map
- `vcb.chapter.maintaining_updating_bible` → active companion

## Deprecation and update hygiene
- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes
- `vcb.chapter.maintaining_updating_bible` → active
- `vcb.chapter.how_to_use_this_bible` → active

## Risk-managed shortcuts and guardrails
- `vcb.chapter.risk_managed_shortcuts` → active
- `vcb.concepts.blast_radius` → active
- `vcb.concepts.recoverability` → active
- `vcb.concepts.rollback` → active

## Operating mode and constraints

- `vcb.chapter.choosing_codex_operating_mode` → active
- `vcb.chapter.budget_aware_codex_workflows` → active
- `vcb.chapter.build_phase_vs_maintenance_phase` → active
- `vcb.chapter.cost_benefit_analysis` → active

## Tool stack and multi-AI workflow

- `tool.docker` → active: local dev/container concept route for reproducible services, Dockerfiles, Compose, image provenance, and rebuild/isolation evidence
- `tool.figma` → active: design/prototyping concept route for components, prototypes, Dev Mode handoff, screenshots, and design-code drift control
- `tool.linear` → active: project-management concept route for issues, projects, workflows, cycles, and team execution hygiene
- `tool.replit` → active: browser-based prototyping, hosted development, learning apps, and quick demo publishing with review/exit-path guardrails
- `tool.lovable` → active: AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails
- `tool.bolt` → active: browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points
- `tool.chatgpt` → active: planning, explanation, product thinking, source-backed research synthesis, and data/document analysis before implementation
- `tool.claude` → active: alternate AI review, architecture critique, long-form explanation, and source-checked second-opinion analysis
- `tool.cursor` → active: AI IDE-native planning, local multi-file edits, diff review, and supervised agentic coding workflows
- `tool.github_copilot` → active: GitHub/IDE-native suggestions, chat, repository-connected coding help, and PR/branch-adjacent assistance
- `tool.windsurf` → active: agentic AI IDE workflows with Cascade-style planning, editing, tool calls, checkpoints, and plugin support
- `vcb.shortcut.many_ais_same_files` → active: concept route for coordinating multiple AI systems against the same files
- `vcb.shortcut.parallel_agents_edit_same_files` → active: concept route for same-file ownership, branch, and merge discipline
- `vcb.shortcut.best_of_n_without_review` → active: concept route for answer-shopping versus evidence review
- `vcb.shortcut.cherry_picking_ai_answers` → active: concept route for confirmation-biased answer selection
- `vcb.shortcut.model_routing_guesswork` → active: concept route for model/tool choice based on task shape, risk, evidence, and current docs
- `vcb.shortcut.subagent_swarm` → active: concept route for bounded subagent roles and integration control
- `vcb.chapter.tool_stack_catalog` → active
- `vcb.chapter.when_to_use_other_ais` → active
- `vcb.chapter.dependency_package_framework_decisions` → active
- `vcb.shortcut.tool_sprawl` → active: keep the tool stack small enough to audit, revoke, and explain

## Codex limitations and model biases

- `vcb.shortcut.ignoring_model_biases` → active: concept route for hallucination, overconfidence, pleasing bias, and common-pattern bias
- `vcb.shortcut.trusting_estimates_before_inspection` → active: concept route for estimates made before evidence inspection
- `vcb.shortcut.consensus_as_correctness` → active: concept route for agreement between AIs versus verification
- `vcb.shortcut.model_routing_guesswork` → active: concept route for volatile model-selection mechanics and stale model advice
- `vcb.chapter.what_codex_is_bad_at` → active
- `vcb.chapter.model_biases_failure_biases_bad_estimates` → active
- `vcb.chapter.failure_modes_codex_work` → active
- `vcb.chapter.reviewing_codex_output` → active

## Foundational software concepts for vibe coders
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

## Codex product features and surfaces

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
- `vcb.codex.feature_maturity` → active: Codex Feature Maturity
- `vcb.codex.changelog_monitoring` → active: Codex Changelog Monitoring

## Review, Safety, and Verification Workflow Cards

- `vcb.workflow.codex_output_review` → active: Codex output review by diff, checks, and risk
- `vcb.workflow.reviewing_diffs` → active: local diff review and hunk-level risk scan
- `vcb.workflow.github_pr_review` → active: Codex-assisted PR review without treating AI as approval
- `vcb.safety.security_review` → active: trust-boundary, auth, data, and exploitability review
- `vcb.safety.secrets` → active: credentials, tokens, CI secrets, browser/session exposure
- `vcb.workflow.ci_triage` → active: failed-check and log triage before mutation
- `vcb.workflow.ci_noninteractive` → active: Codex in CI with least privilege and auditable outputs
- `vcb.safety.production_red_lines` → active: hard-stop gates for production-risk work

## Frontend, Refactor, Dependency, Release, and Documentation Workflow Concepts
- `vcb.workflow.frontend_work` → active: frontend state, responsive behavior, and browser evidence
- `vcb.workflow.visual_qa` → active: screenshot and visual-regression review
- `vcb.workflow.accessibility_review` → active: accessibility checks, keyboard paths, labels, and WCAG-guided review
- `vcb.workflow.refactoring` → active: behavior-preserving refactor workflow with tests and diff review
- `vcb.workflow.dependency_decisions` → active: new dependency/package/framework decision workflow
- `vcb.workflow.dependency_update_review` → active: dependency update and lockfile review workflow
- `vcb.workflow.release_notes` → active: release-note drafting from verified change sources
- `vcb.workflow.documentation_updates` → active: documentation update workflow tied to code, docs, and release context

## AI coding failure-mode concepts
- `vcb.failure.hallucinated_apis` → active: fake API and interface-contract diagnosis
- `vcb.failure.context_pollution` → active: stale, noisy, excessive, or contradictory context diagnosis
- `vcb.failure.weakened_tests` → active: false-green test and assertion weakening diagnosis
- `vcb.failure.broad_refactor_drift` → active: behavior-preservation and scope-drift diagnosis
- `vcb.failure.dependency_bloat` → active: package/framework maintenance and supply-chain drag diagnosis
- `vcb.failure.ui_taste_gap` → active: frontend state, polish, accessibility, and responsive evidence diagnosis
- `vcb.failure.ci_false_confidence` → active: configured-check limitation and CI overtrust diagnosis
- `vcb.failure.done_claim_without_evidence` → active: unsupported completion summary and evidence-gap diagnosis

## Constraint and budget concepts

- `vcb.constraints.operating_mode` → active: choose the Codex surface, task size, permission level, and check-in rhythm from the constraints of the work instead of copying a generic setup
- `vcb.constraints.attention_budget` → active: treat human focus as a finite budget and choose Codex delegation levels that fit how much review attention is actually available
- `vcb.constraints.usage_burn` → active: control plan limits, credits, API spend, context size, and repeated runs without freezing exact pricing into stable guidance
- `vcb.constraints.recovery_budget` → active: choose task size and permissions from how expensive it would be to undo the work if Codex is wrong
- `vcb.constraints.build_vs_maintenance` → active: change Codex task size, review strictness, and budget posture as a project moves from prototype to MVP to production maintenance
- `vcb.constraints.production_quality` → active: define the minimum evidence and guardrails needed before Codex-assisted work is treated as production-ready
- `vcb.constraints.scope_budget` → active: get useful Codex output under tight usage or money constraints without cutting the checks that make the result trustworthy
- `vcb.constraints.review_budget` → active: use higher usage, parallelism, cloud tasks, or automation only when isolation, review capacity, and recovery paths keep the work controllable

## Active Shortcut Harm-Reduction Concepts

- `vcb.shortcut.skipping_tests` → active: skip-test shortcut; route to smallest relevant verification guardrail
- `vcb.shortcut.accepting_looks_done` → active: looks-done shortcut; route to completion-evidence gate
- `vcb.shortcut.broad_agent_permissions` → active: broad-permission shortcut; route to sandbox/approval and blast-radius controls
- `vcb.shortcut.unattended_long_runs` → active: unattended-run shortcut; route to milestones, isolation, and evidence reports
- `vcb.shortcut.broad_refactor` → active: broad-refactor shortcut; route to behavior-preserving refactor boundaries
- `vcb.shortcut.context_dumping` → active: context-dumping shortcut; route to curated context packet control
- `vcb.shortcut.adding_dependencies_fast` → active: fast dependency shortcut; route to package decision and lockfile review guardrails
- `vcb.shortcut.reviewing_cloud_summary_only` → active: cloud-summary-only shortcut; route to diff/check/artifact review guardrail

## Security and permission shortcut concepts

- `vcb.shortcut.production_console_computer_use` → active: production console computer use security/permission shortcut guardrails
- `vcb.shortcut.overbroad_ci_permissions` → active: overbroad ci permissions security/permission shortcut guardrails
- `vcb.shortcut.long_lived_ci_secrets` → active: long-lived ci secrets security/permission shortcut guardrails
- `vcb.shortcut.real_secrets_in_prototype` → active: real secrets in prototype security/permission shortcut guardrails
- `vcb.shortcut.cloud_work_with_real_secrets` → active: cloud work with real secrets security/permission shortcut guardrails
- `vcb.shortcut.full_access_automation` → active: full-access automation security/permission shortcut guardrails
- `vcb.shortcut.unattended_mutation` → active: unattended mutation security/permission shortcut guardrails
- `vcb.shortcut.always_allow_sensitive_apps` → active: always allow sensitive apps security/permission shortcut guardrails

## Setup, configuration, and process shortcut concepts

- `vcb.shortcut.skipping_setup` → active: setup is part of the evidence path, not clerical overhead.
- `vcb.shortcut.default_config_forever` → active: configuration must change with risk and phase.
- `vcb.shortcut.skipping_agents_md` → active: durable guidance beats repeated prompt memory.
- `vcb.shortcut.overstuffing_agents_md` → active: durable guidance should stay concise and current.
- `vcb.shortcut.stale_agents_md` → active: stale repo guidance becomes context pollution.
- `vcb.shortcut.unofficial_tools` → active: tool adoption creates a new trust boundary.
- `vcb.shortcut.hook_overreach` → active: deterministic hooks are not senior-engineer judgment.
- `vcb.shortcut.trusting_external_tool_output` → active: tool output requires provenance, freshness, and scope checks.

## Tool-sprawl, skill, MCP, hook, and reusable-workflow shortcut concepts

- `vcb.shortcut.skill_overkill` → active: avoid creating a skill before a repeated workflow earns it
- `vcb.shortcut.skill_sprawl` → active: audit overlapping skills and disabled stale reusable workflows
- `vcb.shortcut.tool_sprawl` → active: add one tool at a time with owner, purpose, and exit path
- `vcb.shortcut.tool_sprawl_mcp` → active: keep MCP servers scoped, allow-listed, and purpose-bound
- `vcb.shortcut.brittle_hooks` → active: keep hooks fast, deterministic, report-first, and reviewed
- `vcb.shortcut.process_overhead_for_tiny_project` → active: avoid heavyweight process before a tiny project earns it
- `vcb.shortcut.team_workflow_without_team` → active: use solo evidence workflow before team handoff process exists
- `vcb.shortcut.copy_pasting_playbook_blindly` → active: tailor reusable playbooks to actual risk, scope, and done evidence

## Multi-AI and model-bias shortcut concepts

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

## Repository, CI, dependency, and QA concepts

- `tool.github` → active: repository, branch, pull-request, issue, and review-collaboration concept route.
- `tool.github_actions` → active: CI workflow, check, secret, token, runner, and automation evidence route.
- `tool.github_dependabot` → active: dependency-alert and update-PR concept route.
- `tool.npm` → active: package manifest, script, lockfile, install, and audit concept route.
- `tool.playwright` → active: browser test, end-to-end flow, screenshot, and trace concept route.
- `tool.openssf_scorecard` → active: supply-chain health and repository hardening signal route.

## AI coding and IDE tool concepts

- `tool.chatgpt` → active: planning, explanation, product thinking, source-backed research synthesis, and data/document analysis before implementation
- `tool.claude` → active: alternate AI review, architecture critique, long-form explanation, and source-checked second-opinion analysis
- `tool.cursor` → active: AI IDE-native planning, local multi-file edits, diff review, and supervised agentic coding workflows
- `tool.github_copilot` → active: GitHub/IDE-native suggestions, chat, repository-connected coding help, and PR/branch-adjacent assistance
- `tool.windsurf` → active: agentic AI IDE workflows with Cascade-style planning, editing, tool calls, checkpoints, and plugin support
- `vcb.chapter.tool_stack_catalog` → active fallback
- `vcb.chapter.when_to_use_other_ais` → active fallback


## AI app-builder and UI-generation concepts

- `tool.replit` → active: browser-based prototyping, hosted development, learning apps, and quick demo publishing with review/exit-path guardrails
- `tool.lovable` → active: AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails
- `tool.bolt` → active: browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points
- `vcb.concepts.frontend_backend` → active companion: know what generated app layers mean
- `vcb.concepts.state` → active companion: generated UI needs state behavior
- `vcb.concepts.dependency` → active companion: generated package choices require review

## Hosting, backend/auth, payment, observability, and analytics concepts

- `tool.vercel` → active companion: hosting/deployment environments, preview/production promotion, and release evidence
- `tool.supabase` → active companion: database schema, migration, backend functions, RLS, and storage/auth data concepts
- `tool.clerk` → active companion: authentication, sessions, users, organizations, and auth UI concepts
- `tool.auth0` → active companion: authorization, IAM, OAuth/OIDC, APIs, and enterprise identity concepts
- `tool.stripe` → active companion: payment, subscription, customer, webhook, and entitlement concepts
- `tool.sentry` → active companion: observability, errors, traces, releases, and production debugging concepts
- `tool.posthog` → active companion: events, feature flags, analytics, funnels, replay, and experiment concepts

## Ecosystem tool concepts

- Edge platform / CDN / DNS routing → `tool.cloudflare` active; `vcb.constraints.production_quality` companion.
- Deploy preview / deploy context / serverless function hosting → `tool.netlify` active; `tool.vercel` companion.
- Serverless Postgres / database branch / preview database → `tool.neon` active; `vcb.concepts.database_schema` and `tool.supabase` companions.
- Transactional email / sending domain / template email → `tool.resend` active; auth/payment/user-state tools as companions.
- Unit test runner / Vite-native tests / component test evidence → `tool.vitest` active; `vcb.workflow.testing` companion.
- Component workshop / isolated UI state / component documentation → `tool.storybook` active; `tool.figma` and `vcb.workflow.frontend_work` companions.

<!-- VCB:STOP_RETRIEVAL reason="by_concept_complete" -->
<!-- VCB:END_INDEX id=vcb.index.by_concept -->
