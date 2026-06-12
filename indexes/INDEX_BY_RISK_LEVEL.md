---
id: vcb.index.by_risk_level
title: INDEX_BY_RISK_LEVEL
artifact_type: index
version: 0.41.0-draft.chunk40
status: chunk_40_updated
created_on: '2026-06-08'
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: quarterly
---

<!-- VCB:BEGIN_INDEX id=vcb.index.by_risk_level version=0.41.0-draft.chunk40 -->

# INDEX_BY_RISK_LEVEL

> Status: Current routing index. Entries marked active have authored source files; entries marked planned are future routes.

## Prompting/workflow risk controls
- `vcb.prompting.four_part_prompt` → active: low-to-high risk scope control
- `vcb.prompting.acceptance_criteria` → active: moderate/high risk done-when control
- `vcb.prompting.plan_first` → active: high-risk or unknown-work planning gate
- `vcb.prompting.context_management` → active: sensitive/stale context control
- `vcb.workflow.unknown_codebase` → active: high-risk when repo is unfamiliar
- `vcb.workflow.feature_slicing` → active: reduces broad-feature blast radius
- `vcb.workflow.bug_repro` → active: required for nontrivial bugs
- `vcb.workflow.testing` → active: required for production-facing changes

## Low-risk local or disposable work
- `tool.docker` → active when disposable work needs reproducible local services, resettable containers, or dev-environment isolation
- `tool.figma` → active when disposable work is a UI/design sketch, prototype, or handoff artifact
- `tool.linear` → active when lightweight issue ownership, scope, or handoff is needed without process overhead
- `tool.v0` → active when output is a disposable UI sketch or reviewed frontend starting point
- `tool.replit` → active when the browser prototype is fake-data-only and has a discard/export/harden path
- `tool.lovable` → active only when generated full-stack behavior stays prototype-scoped and review-owned
- `tool.bolt` → active only when generated code, dependencies, tokens, and publish target are inspected before handoff
- `vcb.chapter.codex_playbooks` → active fallback
- `vcb.chapter.first_serious_app` → active fallback
- `vcb.shortcut.one_big_prompt` → planned
- `vcb.shortcut.eyeballing_ui` → planned

## Moderate-risk work requiring guardrails
- `vcb.chapter.feature_slicing` → active
- `vcb.chapter.debugging_with_reproduction` → active
- `vcb.chapter.writing_updating_tests` → active
- `vcb.chapter.reviewing_codex_output` → active
- `vcb.shortcut.skipping_plan` → planned
- `vcb.shortcut.skipping_setup` → active: local setup shortcuts need setup inspection and one verification command
- `vcb.shortcut.skipping_agents_md` → active: durable guidance shortcuts need minimal AGENTS.md rules after repeated mistakes
- `vcb.shortcut.overstuffing_agents_md` → active: over-broad AGENTS.md creates context and instruction risk
- `vcb.shortcut.stale_agents_md` → active: stale guidance needs maintenance review

## High-risk production work

- `tool.vercel` → active: production deployment, preview promotion, environment-variable, and rollback risk
- `tool.supabase` → active: production database/RLS/auth/storage/function and data-loss risk
- `tool.clerk` → active: authentication/session/user/org access risk
- `tool.auth0` → active: IAM/OIDC/OAuth/API authorization and tenant-governance risk
- `tool.stripe` → active: payment/subscription/webhook/entitlement and real-money risk
- `tool.sentry` → active: production error/performance evidence and privacy-filtering risk
- `tool.posthog` → active: product analytics/replay/feature-flag and privacy/decision risk
- `tool.codex_security` → active companion: security scans/findings/fix preparation
- `vcb.chapter.security_for_vibe_coders` → active fallback
- `vcb.chapter.ci_noninteractive_github_actions` → active fallback
- `vcb.chapter.github_pr_review_with_codex` → active fallback
- `vcb.chapter.senior_engineer_checklist` → active fallback
- `vcb.shortcut.unattended_mutation` → active: unattended mutation is not production-safe without isolation and human review
- `vcb.shortcut.default_config_forever` → active: production work needs risk-scaled config profiles
- `vcb.shortcut.hook_overreach` → active: hooks cannot replace production review, CI, or security checks
- `vcb.shortcut.trusting_external_tool_output` → active: external tool output requires provenance before production use

## Do-not-do-in-production shortcuts
- `vcb.shortcut.broad_agent_permissions` → active: excessive filesystem, command, network, or tool permissions are never acceptable without a bounded sandbox and review gate
- `vcb.shortcut.production_console_computer_use` → active: production/admin GUI actions require manual execution or a supervised, reversible dry-run path
- `vcb.shortcut.full_access_automation` → active: full filesystem/network/tool access is not production-safe without least-privilege defaults and human approval
- `vcb.shortcut.overbroad_ci_permissions` → active: CI tokens should use explicit least privilege before any write-capable workflow runs
- `vcb.shortcut.long_lived_ci_secrets` → active: long-lived CI credentials are high-blast-radius production risk and need rotation or federation
- `vcb.shortcut.cloud_work_with_real_secrets` → active: delegated/cloud work should not receive real production secrets or sensitive user data
- `vcb.shortcut.unattended_mutation` → active: unattended write-capable mutation requires branch isolation, stop conditions, and human review
- `vcb.shortcut.always_allow_sensitive_apps` → active: persistent approvals for sensitive apps/sites are not production-safe
- `vcb.shortcut.skipping_security_review` → planned future companion; current active routes above cover least-privilege and security-sensitive shortcut handling
- `vcb.shortcut.generated_prototype_as_production_foundation` → planned
- `vcb.shortcut.unofficial_tools` → active: do not introduce unvetted tools with production credentials or write access
- `vcb.shortcut.trusting_external_tool_output` → active: do not treat external tool summaries as production evidence without verification

## Setup and process shortcuts with production risk

- `vcb.shortcut.skipping_setup` → active: high risk when setup ignorance produces unverified production changes
- `vcb.shortcut.default_config_forever` → active: high risk when stale defaults preserve broad permissions or unsafe approval policy
- `vcb.shortcut.stale_agents_md` → active: high risk when outdated durable guidance directs production or security-sensitive work
- `vcb.shortcut.unofficial_tools` → active: do-not-do-in-production unless provenance, permissions, isolation, and owner are reviewed
- `vcb.shortcut.hook_overreach` → active: high risk when brittle hooks replace review, CI, or human approval
- `vcb.shortcut.trusting_external_tool_output` → active: do-not-do-in-production when source, freshness, and artifact evidence are missing

## Never with real secrets or sensitive user data

- `tool.supabase` → active: service-role keys, RLS, database secrets, and sensitive data must stay out of unsafe prompts/prototypes
- `tool.clerk` → active: auth/session/user-management data requires explicit privacy and access review
- `tool.auth0` → active: IAM tenant/app/API credentials and token posture require explicit ownership
- `tool.stripe` → active: payment/customer/subscription state must not be tested with unsafe live credentials or unreviewed webhooks
- `tool.sentry` → active: errors/traces/replays must not collect secrets or sensitive payloads
- `tool.posthog` → active: analytics/replay events must avoid sensitive content and respect consent/privacy boundaries
- `tool.codex_security` → active companion: security scans/fixes must avoid unnecessary production secrets and sensitive user data
- `vcb.chapter.security_for_vibe_coders` → active fallback
- `vcb.chapter.computer_use_browser_gui_tasks` → active fallback
- `vcb.shortcut.real_secrets_in_prototype` → active: never use real credentials or user data in disposable prototypes
- `vcb.shortcut.cloud_work_with_real_secrets` → active: avoid cloud-agent secret exposure without scoped review

## Anecdotal or speculative workflow risk

- `vcb.field.chatgpt_pm_codex_implementer` → active candidate: ChatGPT PM / Codex implementer split
- `vcb.field.fresh_agent_review` → active candidate: fresh independent agent/session diff review
- `vcb.field.context_reset_between_tasks` → active candidate: reset or summarize context between unrelated tasks
- `vcb.field.agents_md_first` → active candidate: minimal AGENTS.md early in durable repos
- `vcb.field.skeleton_todo_first` → active candidate: human skeleton/TODOs before agent implementation
- `vcb.field.strict_typecheck_lint_gates` → active candidate: typecheck/lint/test gates after agent changes
- `vcb.field.greenfield_vs_production_rule` → active candidate: explicit project phase and compatibility posture
- `vcb.field.lessons_file_loop` → active candidate: temporary lessons loop before durable guidance promotion
- `vcb.field.multi_agent_review_consensus` → active candidate: multi-agent review with evidence, not consensus-as-proof
- `vcb.chapter.field_notes_unofficial_practices` → active fallback
- `vcb.chapter.maintaining_updating_bible` → active companion

## Shortcut risk calibration
- `vcb.chapter.risk_managed_shortcuts` → active
- `vcb.concepts.blast_radius` → active
- `vcb.concepts.recoverability` → active

## Cost and tool risk

- `tool.docker` → active: containers can hide setup, storage, CPU/RAM, image-security, licensing, and CI/runtime costs
- `tool.figma` → active: design collaboration can hide seat, design-system, handoff, and implementation-reconciliation costs
- `tool.linear` → active: project-management tools can hide grooming, migration, reporting, automation, and coordination costs
- `tool.vercel` → active: hosting, preview deployments, environment separation, deployment evidence, and production promotion guardrails
- `tool.supabase` → active: Postgres database/backend/auth/storage, schema/RLS, migrations, backups, functions, and data-access guardrails
- `tool.clerk` → active: authentication, user management, sessions, organizations, and application identity guardrails
- `tool.auth0` → active: IAM, OAuth/OIDC, applications/APIs, enterprise/B2B identity, and authorization architecture guardrails
- `tool.stripe` → active: payments, subscriptions, checkout, webhooks, billing state, and real-money fulfillment guardrails
- `tool.sentry` → active: error monitoring, tracing, performance, release evidence, and production debugging guardrails
- `tool.posthog` → active: product analytics, event taxonomy, session replay, feature flags, experiments, and product-evidence guardrails
- `tool.replit` → active: quick browser prototypes can hide hosting, migration, secrets, and production-hardening costs
- `tool.lovable` → active: full-stack app generation can hide auth/data/cloud/governance review costs
- `tool.bolt` → active: browser app generation can hide token burn, generated-code review, and dependency cleanup costs
- `tool.v0` → active: visual/UI generation can hide accessibility, state, and integration costs
- `tool.chatgpt` → active companion: planning/explanation tool-choice risk
- `tool.claude` → active companion: alternate-review/tool-comparison risk
- `tool.cursor` → active companion: AI IDE review-debt risk
- `tool.github_copilot` → active companion: autocomplete/IDE suggestion risk
- `tool.windsurf` → active companion: agentic IDE tool risk
- Tool sprawl risk → `vcb.shortcut.tool_sprawl` active; `vcb.chapter.tool_stack_catalog` active fallback; `vcb.chapter.cost_benefit_analysis` active fallback.
- Pricing/plan volatility risk → `vcb.chapter.budget_aware_codex_workflows` active fallback; exact values require dated pricing snapshots.
- Model limitation risk → `vcb.chapter.what_codex_is_bad_at` active fallback; `vcb.chapter.model_biases_failure_biases_bad_estimates` active fallback.

## High-risk foundational concepts
- `vcb.concepts.authentication` → active
- `vcb.concepts.authorization` → active
- `vcb.concepts.database_schema` → active
- `vcb.concepts.migration` → active
- `vcb.concepts.environment_variable` → active
- `vcb.concepts.ci` → active
- `vcb.concepts.observability` → active

## Codex feature risk routing

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

- `vcb.codex.app` → active: risk-scaled guidance
- `vcb.codex.cli` → active: risk-scaled guidance
- `vcb.codex.ide_extension` → active: risk-scaled guidance
- `vcb.codex.cloud` → active: risk-scaled guidance
- `vcb.codex.github_review` → active: risk-scaled guidance
- `vcb.codex.config` → active: risk-scaled guidance
- `vcb.codex.agents_md` → active: risk-scaled guidance
- `vcb.codex.skills` → active: risk-scaled guidance
- `vcb.codex.mcp` → active: risk-scaled guidance
- `vcb.codex.hooks` → active: risk-scaled guidance
- `vcb.codex.automations` → active: risk-scaled guidance
- `vcb.codex.subagents` → active: risk-scaled guidance
- `vcb.codex.computer_use` → active: risk-scaled guidance
- `vcb.codex.feature_maturity` → active: risk-scaled guidance
- `vcb.codex.changelog_monitoring` → active: risk-scaled guidance

## Review, Safety, and Verification Workflow Cards

- `vcb.workflow.codex_output_review` → active: Codex output review by diff, checks, and risk
- `vcb.workflow.reviewing_diffs` → active: local diff review and hunk-level risk scan
- `vcb.workflow.github_pr_review` → active: Codex-assisted PR review without treating AI as approval
- `vcb.safety.security_review` → active: trust-boundary, auth, data, and exploitability review
- `vcb.safety.secrets` → active: credentials, tokens, CI secrets, browser/session exposure
- `vcb.workflow.ci_triage` → active: failed-check and log triage before mutation
- `vcb.workflow.ci_noninteractive` → active: Codex in CI with least privilege and auditable outputs
- `vcb.safety.production_red_lines` → active: hard-stop gates for production-risk work

## Risk routes for frontend, refactor, dependency, release, and documentation workflows
- `vcb.workflow.frontend_work` → active: frontend state, responsive behavior, and browser evidence
- `vcb.workflow.visual_qa` → active: screenshot and visual-regression review
- `vcb.workflow.accessibility_review` → active: accessibility checks, keyboard paths, labels, and WCAG-guided review
- `vcb.workflow.refactoring` → active: behavior-preserving refactor workflow with tests and diff review
- `vcb.workflow.dependency_decisions` → active: new dependency/package/framework decision workflow
- `vcb.workflow.dependency_update_review` → active: dependency update and lockfile review workflow
- `vcb.workflow.release_notes` → active: release-note drafting from verified change sources
- `vcb.workflow.documentation_updates` → active: documentation update workflow tied to code, docs, and release context

## High-risk AI-coding failure modes
- `vcb.failure.hallucinated_apis` → active: Hallucinated APIs happen when Codex invents routes, methods, fields, packages, flags, callbacks, or response shapes that sound plausible but are not real in the target project or vendor contract.
- `vcb.failure.context_pollution` → active: Context pollution happens when stale, irrelevant, contradictory, or oversized context steers Codex away from the task that actually matters.
- `vcb.failure.weakened_tests` → active: Weakened tests happen when Codex makes tests pass by deleting assertions, broadening expectations, skipping checks, over-mocking behavior, or testing the implementation instead of the requirement.
- `vcb.failure.broad_refactor_drift` → active: Broad-refactor drift happens when a cleanup request turns into behavior changes, hidden migrations, new abstractions, deleted edge cases, or a rewrite nobody explicitly approved.
- `vcb.failure.dependency_bloat` → active: Dependency bloat happens when Codex adds packages, frameworks, plugins, or SDKs faster than the project can justify, maintain, audit, and update them.
- `vcb.failure.ui_taste_gap` → active: UI taste gap happens when generated frontend code technically works but feels generic, inconsistent, inaccessible, off-brand, poorly spaced, or incomplete across states and breakpoints.
- `vcb.failure.ci_false_confidence` → active: A CI false-confidence loop happens when green or agent-generated checks create confidence that the change is safe even though the wrong checks ran, checks were bypassed, permissions were too broad, or output was not reviewed.
- `vcb.failure.done_claim_without_evidence` → active: Done claim without evidence happens when a polished agent summary is accepted without changed-file, command, screenshot, log, diff, or acceptance-criteria proof.

## Constraint and budget risk controls

- `vcb.constraints.scope_budget` → low to moderate risk when bounded; high risk if checks are skipped for price
- `vcb.constraints.attention_budget` → moderate risk when review is deferred; high risk if write access is broad
- `vcb.constraints.usage_burn` → moderate financial/usage risk; higher when automation loops or MCP context are unbounded
- `vcb.constraints.operating_mode` → risk selector for surface, permission, supervision, and task size
- `vcb.constraints.recovery_budget` → high-risk work should be blocked when rollback is unclear
- `vcb.constraints.build_vs_maintenance` → production/maintenance phase raises risk of broad AI edits
- `vcb.constraints.production_quality` → high-risk work requires production-quality evidence and release gates
- `vcb.constraints.review_budget` → high risk unless isolated by file ownership, branches, and review bandwidth

## High-Risk Shortcut Harm-Reduction Cards

- `vcb.shortcut.skipping_tests` → active: skip-test shortcut; route to smallest relevant verification guardrail
- `vcb.shortcut.accepting_looks_done` → active: looks-done shortcut; route to completion-evidence gate
- `vcb.shortcut.broad_agent_permissions` → active: broad-permission shortcut; route to sandbox/approval and blast-radius controls
- `vcb.shortcut.unattended_long_runs` → active: unattended-run shortcut; route to milestones, isolation, and evidence reports
- `vcb.shortcut.broad_refactor` → active: broad-refactor shortcut; route to behavior-preserving refactor boundaries
- `vcb.shortcut.context_dumping` → active: context-dumping shortcut; route to curated context packet control
- `vcb.shortcut.adding_dependencies_fast` → active: fast dependency shortcut; route to package decision and lockfile review guardrails
- `vcb.shortcut.reviewing_cloud_summary_only` → active: cloud-summary-only shortcut; route to diff/check/artifact review guardrail

## Security and permission shortcut risk routes

- `vcb.shortcut.production_console_computer_use` → active: production console computer use security/permission shortcut guardrails
- `vcb.shortcut.overbroad_ci_permissions` → active: overbroad ci permissions security/permission shortcut guardrails
- `vcb.shortcut.long_lived_ci_secrets` → active: long-lived ci secrets security/permission shortcut guardrails
- `vcb.shortcut.real_secrets_in_prototype` → active: real secrets in prototype security/permission shortcut guardrails
- `vcb.shortcut.cloud_work_with_real_secrets` → active: cloud work with real secrets security/permission shortcut guardrails
- `vcb.shortcut.full_access_automation` → active: full-access automation security/permission shortcut guardrails
- `vcb.shortcut.unattended_mutation` → active: unattended mutation security/permission shortcut guardrails
- `vcb.shortcut.always_allow_sensitive_apps` → active: always allow sensitive apps security/permission shortcut guardrails

## Setup/config/process shortcut risk routes

- `vcb.shortcut.skipping_setup` → active: setup unknowns can turn a cheap patch into repeated failed runs
- `vcb.shortcut.default_config_forever` → active: stale permissive defaults can silently widen every future task
- `vcb.shortcut.skipping_agents_md` → active: missing durable guidance creates repeated human-memory dependency
- `vcb.shortcut.overstuffing_agents_md` → active: overloaded guidance pollutes every future prompt
- `vcb.shortcut.stale_agents_md` → active: authoritative-looking stale guidance misroutes future agent work
- `vcb.shortcut.unofficial_tools` → active: unofficial tools can add supply-chain, credential, and data-sharing risk
- `vcb.shortcut.hook_overreach` → active: hooks can create false confidence when used beyond objective guardrails
- `vcb.shortcut.trusting_external_tool_output` → active: external tool output can be stale, partial, injected, or misinterpreted

## Do-not-do-in-production setup/process shortcuts

- `vcb.shortcut.unofficial_tools` → active: never install unvetted unofficial tools with production credentials or broad repo access
- `vcb.shortcut.trusting_external_tool_output` → active: do not mutate production/security-sensitive code from unverified tool output
- `vcb.shortcut.default_config_forever` → active: do not carry permissive prototype defaults into production work
- `vcb.shortcut.hook_overreach` → active: do not treat hooks as the only production safety boundary

## Tool-sprawl, skill, and reusable process shortcut risk routes

- `vcb.shortcut.skill_overkill` → active: avoid creating a skill before a repeated workflow earns it
- `vcb.shortcut.skill_sprawl` → active: audit overlapping skills and disabled stale reusable workflows
- `vcb.shortcut.tool_sprawl` → active: add one tool at a time with owner, purpose, and exit path
- `vcb.shortcut.tool_sprawl_mcp` → active: keep MCP servers scoped, allow-listed, and purpose-bound
- `vcb.shortcut.brittle_hooks` → active: keep hooks fast, deterministic, report-first, and reviewed
- `vcb.shortcut.process_overhead_for_tiny_project` → active: avoid heavyweight process before a tiny project earns it
- `vcb.shortcut.team_workflow_without_team` → active: use solo evidence workflow before team handoff process exists
- `vcb.shortcut.copy_pasting_playbook_blindly` → active: tailor reusable playbooks to actual risk, scope, and done evidence

## High-risk multi-AI and model-bias shortcuts

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

## Repository, CI, dependency, and QA risk routes

- Lower risk / read-only evidence → `tool.github`, `tool.playwright`, `tool.openssf_scorecard` → active when used for review-only reports.
- Medium risk / repository mutation → `tool.github`, `tool.github_dependabot`, `tool.npm` → active; inspect PRs, lockfiles, and dependency changes before merge.
- High risk / CI credentials or release gates → `tool.github_actions` → active; pair with `vcb.shortcut.overbroad_ci_permissions` and `vcb.shortcut.long_lived_ci_secrets`.
- High risk / dependency and supply-chain posture → `tool.github_dependabot`, `tool.npm`, `tool.openssf_scorecard` → active; treat scores, audits, and alerts as evidence requiring human review.
- High risk / browser verification relied on for release → `tool.playwright` → active; require reproducible tests and artifacts, not screenshots alone.

## AI coding, AI IDE, and planning tool risk routes

- `tool.chatgpt` → active: planning, explanation, product thinking, source-backed research synthesis, and data/document analysis before implementation
- `tool.claude` → active: alternate AI review, architecture critique, long-form explanation, and source-checked second-opinion analysis
- `tool.cursor` → active: AI IDE-native planning, local multi-file edits, diff review, and supervised agentic coding workflows
- `tool.github_copilot` → active: GitHub/IDE-native suggestions, chat, repository-connected coding help, and PR/branch-adjacent assistance
- `tool.windsurf` → active: agentic AI IDE workflows with Cascade-style planning, editing, tool calls, checkpoints, and plugin support
- `vcb.shortcut.parallel_agents_edit_same_files` → active companion
- `vcb.shortcut.best_of_n_without_review` → active companion


## Browser-dev, app-builder, and UI-generation risk routes

- `tool.replit` → active: browser-based prototyping, hosted development, learning apps, and quick demo publishing with review/exit-path guardrails
- `tool.lovable` → active: AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails
- `tool.bolt` → active: browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points
- `vcb.shortcut.real_secrets_in_prototype` → active: real data/secrets in generated prototypes is high risk
- `vcb.failure.ui_taste_gap` → active: generated UI needs state, responsive, accessibility, and polish evidence

## Local dev, design, and project-management tool risk routes

- `tool.docker` → active: Docker/container risk around local reproducibility, host access, secrets, image provenance, ports, volumes, and dev/prod parity claims
- `tool.figma` → active: Figma/design-handoff risk around screenshot overtrust, stale design state, missing UI states, and design-code drift
- `tool.linear` → active: Linear/project-management risk around status theater, stale tickets, missing owners, and planning without evidence
- `vcb.shortcut.tool_sprawl` → active companion
- `vcb.chapter.tool_stack_catalog` → active fallback

## Hosting, backend/auth, payment, observability, and analytics risk routes

- `tool.vercel` → active: hosting, preview deployments, environment separation, deployment evidence, and production promotion guardrails
- `tool.supabase` → active: Postgres database/backend/auth/storage, schema/RLS, migrations, backups, functions, and data-access guardrails
- `tool.clerk` → active: authentication, user management, sessions, organizations, and application identity guardrails
- `tool.auth0` → active: IAM, OAuth/OIDC, applications/APIs, enterprise/B2B identity, and authorization architecture guardrails
- `tool.stripe` → active: payments, subscriptions, checkout, webhooks, billing state, and real-money fulfillment guardrails
- `tool.sentry` → active: error monitoring, tracing, performance, release evidence, and production debugging guardrails
- `tool.posthog` → active: product analytics, event taxonomy, session replay, feature flags, experiments, and product-evidence guardrails

## Ecosystem coverage and deferred-tool risk

- `tool.cloudflare` → active: high when DNS/CDN/edge routing, cache, public domains, or security posture can affect production traffic.
- `tool.netlify` → active: medium-high when deploy previews/functions/environment contexts affect production or public demos.
- `tool.neon` → active: high when schema, branches, migrations, or persistent data can affect production state.
- `tool.resend` → active: high when real users receive email or auth/payment notifications depend on delivery behavior.
- `tool.vitest` → active: medium when green tests may be overtrusted or weakened; higher when they gate release alone.
- `tool.storybook` → active: medium when component docs/isolated states are mistaken for product proof; higher when design-code drift reaches production.
- Deferred ecosystem IDs in `TOOL_REGISTER.md` → active audit route: do not treat deferred as safe or unimportant; use companion cards and current official docs.

<!-- VCB:STOP_RETRIEVAL reason="by_risk_level_complete" -->
<!-- VCB:END_INDEX id=vcb.index.by_risk_level -->
