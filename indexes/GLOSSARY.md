---
id: vcb.index.glossary
title: GLOSSARY
artifact_type: index
version: 0.41.0-draft.chunk40
status: chunk_40_updated
created_on: '2026-06-08'
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: quarterly
---

<!-- VCB:BEGIN_INDEX id=vcb.index.glossary version=0.41.0-draft.chunk40 -->

# GLOSSARY

> Status: Current routing index. Entries marked active have authored source files; entries marked planned are future routes.

## Core terms
- `diff` → `vcb.concepts.diff`
- `blast radius` → `vcb.concepts.blast_radius`
- `recoverability` → `vcb.concepts.recoverability`
- `rollback` → `vcb.concepts.rollback`
- `branch` → `vcb.concepts.git_branch`
- `pull request` → `vcb.concepts.pull_request`

## Codex and agent terms
- `Codex` → `tool.codex`, `vcb.codex.app`, `vcb.codex.cli`, `vcb.codex.cloud`
- `Codex surface` → `tool.codex`, `vcb.chapter.codex_surfaces`
- `Worktree` → `tool.codex_worktrees`, `vcb.concepts.git_branch`
- `Subagent` → `tool.codex_subagents`, `vcb.codex.subagents`
- `Automation` → `tool.codex_automations`, `vcb.codex.automations`
- `Computer Use` → `tool.codex_computer_use`, `vcb.codex.computer_use`
- `In-app browser` → `tool.codex_browser`, `vcb.workflow.visual_qa`
- `Chrome extension` → `tool.codex_chrome_extension`, `vcb.shortcut.logged_in_browser_secrets`
- `AGENTS.md` → `tool.codex_agents_md`; companion mechanics: `vcb.codex.agents_md`
- `MCP` → `tool.codex_mcp`; companion mechanics: `vcb.codex.mcp`
- `Hook` → `tool.codex_hooks`; companion mechanics: `vcb.codex.hooks`
- `Skill` → `tool.codex_skills`; companion mechanics: `vcb.codex.skills`

## Prompting and workflow terms

- Four-part prompt → `vcb.prompting.four_part_prompt` → active: goal, context, constraints, and done-when.
- Acceptance criteria → `vcb.prompting.acceptance_criteria` → active: observable completion rules.
- Plan first → `vcb.prompting.plan_first` → active: plan before mutation for complex or risky work.
- Context management → `vcb.prompting.context_management` → active: choose relevant context and avoid stale/context-dumped threads.
- Unknown codebase → `vcb.workflow.unknown_codebase` → active: map the repo before editing.
- Feature slice → `vcb.workflow.feature_slicing` → active: smallest useful vertical change.
- Reproduction → `vcb.workflow.bug_repro` → active: repeatable evidence of a bug before and after a fix.
- Testing workflow → `vcb.workflow.testing` → active: smallest meaningful checks without weakening existing tests.


## Field practice candidate terms

- `ChatGPT PM / Codex implementer` → `vcb.field.chatgpt_pm_codex_implementer` active needs_more_evidence; companion: `tool.chatgpt`, `tool.codex`.
- `fresh agent review` → `vcb.field.fresh_agent_review` active reproduced.
- `context reset` → `vcb.field.context_reset_between_tasks` active candidate; companion: `vcb.prompting.context_management`.
- `AGENTS.md first` → `vcb.field.agents_md_first` active candidate; companion mechanics: `tool.codex_agents_md`.
- `skeleton/TODO first` → `vcb.field.skeleton_todo_first` active candidate.
- `strict typecheck/lint gates` → `vcb.field.strict_typecheck_lint_gates` active reproduced; companions: `vcb.concepts.typecheck`, `vcb.concepts.lint`.
- `greenfield vs production rule` → `vcb.field.greenfield_vs_production_rule` active candidate; companion: `vcb.constraints.build_vs_maintenance`.
- `lessons file loop` → `vcb.field.lessons_file_loop` active candidate.
- `multi-agent review consensus` → `vcb.field.multi_agent_review_consensus` active needs_more_evidence; risk companion: `vcb.shortcut.consensus_as_correctness`.

## Review, security, and shipping terms

- Logged-in browser secrets — `vcb.shortcut.logged_in_browser_secrets` → active: signed-in browser/GUI work exposes account authority or sensitive data
- Browser clicking without repro — `vcb.shortcut.browser_clicking_without_repro` → active: GUI operation without exact steps, expected/actual result, and evidence target
- `diff review` → `vcb.chapter.reviewing_codex_output`
- `Codex PR review` → `tool.codex_github_review` active for Codex PR-review signal; `tool.github` active for repository/PR source of truth; `vcb.chapter.github_pr_review_with_codex` active fallback.
- `security review` → `vcb.safety.security_review` active for the smallest security-review workflow route; `tool.codex_security` active when Codex Security tooling is intended; `vcb.chapter.security_for_vibe_coders` active fallback.
- `non-interactive Codex` → `tool.codex_exec` active for scripted/CI-style Codex runs; `tool.github_actions` active when GitHub CI owns execution; `vcb.chapter.ci_noninteractive_github_actions` active fallback.
- `CI` → `tool.github_actions` active for workflow/check evidence; `tool.codex_exec` active when non-interactive Codex is the CI actor; `vcb.chapter.ci_noninteractive_github_actions` active fallback.
- `production deployment` → `tool.vercel` active for deployment/promotion evidence; `vcb.safety.production_red_lines` active companion.

## Operating-system terms
- `prompt library` → `vcb.chapter.prompt_library_to_team_workflow`
- `failure mode` → `vcb.chapter.failure_modes_codex_work`
- `playbook` → `vcb.chapter.codex_playbooks`
- `first serious app` → `vcb.chapter.first_serious_app`
- `senior engineer checklist` → `vcb.chapter.senior_engineer_checklist`

## Field Practice
- `vcb.chapter.field_notes_unofficial_practices` → active: unofficial or user-discovered tactic that must be labeled before adoption.

## Risk-Managed Shortcut
- `vcb.chapter.risk_managed_shortcuts` → active: shortcut guidance based on blast radius, recoverability, minimum guardrails, and recovery plan.

## Deprecation
- `vcb.chapter.maintaining_updating_bible` → active: marking obsolete guidance with replacement and reason rather than silently deleting it.

## Guardrail Ladder
- `vcb.chapter.risk_managed_shortcuts` → active: levels of protection from no guardrails through deployment guardrails.

## Constraint and tool-stack terms
- Operating mode → `vcb.chapter.choosing_codex_operating_mode` active.
- Build phase → `vcb.chapter.build_phase_vs_maintenance_phase` active.
- Maintenance phase → `vcb.chapter.build_phase_vs_maintenance_phase` active.
- Docker → `tool.docker` active for local containers, Dockerfiles, Compose stacks, reproducible services, and rebuild/isolation evidence.
- Figma → `tool.figma` active for design files, components, prototypes, Dev Mode handoff, screenshots, and design-intent evidence.
- Linear → `tool.linear` active for issues, projects, workflows, cycles, ownership, and team execution hygiene.
- Tool sprawl → `tool.docker`, `tool.figma`, and `tool.linear` active when local-dev, design, or planning tool choice is the concrete issue; `vcb.chapter.tool_stack_catalog` active fallback; `vcb.chapter.cost_benefit_analysis` active fallback.
- Total cost of ownership → `vcb.chapter.cost_benefit_analysis` active.
- Independent AI review → `tool.claude` active for alternate AI review and architecture critique; `tool.chatgpt` active for planning/explanation and source-backed synthesis; `vcb.chapter.when_to_use_other_ais` active fallback.

## Limitation and bias terms

- Optimism bias → `vcb.shortcut.trusting_estimates_before_inspection` active: estimates accepted before code, dependency, test, and constraint inspection; see also `vcb.shortcut.ignoring_model_biases`.
- Completion bias → `vcb.shortcut.ignoring_model_biases` active: confident done-sounding output can overstate certainty; see also `vcb.failure.done_claim_without_evidence`.
- Plausibility bias → `vcb.shortcut.ignoring_model_biases` active: plausible-pattern answers need evidence, source, diff, or check review before acceptance.
- Consensus bias / AI agreement → `vcb.shortcut.consensus_as_correctness` active: multiple matching AI answers are not independent verification.
- Answer-shopping bias → `vcb.shortcut.best_of_n_without_review` active and `vcb.shortcut.cherry_picking_ai_answers` active: choose by evidence, not by the most pleasing answer.
- Done claim without evidence → `vcb.failure.done_claim_without_evidence` active; pair with `vcb.shortcut.accepting_looks_done` and `vcb.shortcut.trusting_estimates_before_inspection` when the issue is shortcut behavior.
- Hallucinated API → `vcb.failure.hallucinated_apis` active; pair with `vcb.shortcut.ignoring_model_biases` when the hallucination is masked by fluent, plausible output.


## Foundational concept terms
- **API** → `vcb.concepts.api_basics` → active
- **Frontend / backend** → `vcb.concepts.frontend_backend` → active
- **Database schema** → `vcb.concepts.database_schema` → active
- **Authentication** → `vcb.concepts.authentication` → active concept-first route; companions: `tool.clerk`, `tool.auth0`, and `tool.supabase` when product auth tooling is in scope.
- **Authorization** → `vcb.concepts.authorization` → active concept-first route; companions: `tool.auth0`, `tool.clerk`, `tool.supabase`, and `vcb.safety.security_review` when access-control tooling or review is in scope.
- **State** → `vcb.concepts.state` → active
- **Async / promise / race condition** → `vcb.concepts.async` → active
- **Dependency** → `vcb.concepts.dependency` → active
- **Test** → `vcb.concepts.test` → active
- **Typecheck** → `vcb.concepts.typecheck` → active
- **Lint** → `vcb.concepts.lint` → active
- **Migration** → `vcb.concepts.migration` → active
- **Environment variable** → `vcb.concepts.environment_variable` → active
- **Build step** → `vcb.concepts.build_step` → active
- **CI** → `vcb.concepts.ci` → active concept-first route; companions: `tool.github_actions`, `tool.codex_exec`, and `tool.github` when workflow/check/PR evidence is in scope.
- **Feature flag** → `vcb.concepts.feature_flag` → active
- **Observability** → `vcb.concepts.observability` → active concept-first route; companions: `tool.sentry`, `tool.posthog`, and `tool.vercel` when error, analytics, replay, deployment, or runtime evidence is in scope.

## Codex feature-card terms
- `feature maturity` → `tool.codex_feature_maturity`; companion mechanics: `vcb.codex.feature_maturity`
- `Codex changelog` → `tool.codex_changelog_monitoring`; companion mechanics: `vcb.codex.changelog_monitoring`
- `Codex update watch` → `tool.codex_changelog_monitoring`
- `Codex deprecation watch` → `tool.codex_changelog_monitoring`; companion register: `vcb.register.deprecations`
- `Codex Security` → `tool.codex_security`; companion workflow: `vcb.safety.security_review`

- `Codex App` → `tool.codex_app`; companion mechanics: `vcb.codex.app`
- `Codex CLI` → `tool.codex_cli`; companion mechanics: `vcb.codex.cli`
- `Codex IDE Extension` → `tool.codex_ide_extension`; companion mechanics: `vcb.codex.ide_extension`
- `Codex Cloud` → `tool.codex_cloud`; companion mechanics: `vcb.codex.cloud`
- `Codex GitHub Review` → `tool.codex_github_review`; companion mechanics: `vcb.codex.github_review`
- `Codex automation` → `tool.codex_automations`; companion mechanics: `vcb.codex.automations`
- `Codex subagent` → `tool.codex_subagents`; companion mechanics: `vcb.codex.subagents`
- `Computer Use` → `tool.codex_computer_use`; companion mechanics: `vcb.codex.computer_use`
- `Codex worktree` → `tool.codex_worktrees`
- `in-app browser` → `tool.codex_browser`
- `Codex Chrome extension` → `tool.codex_chrome_extension`
- `Codex config` → `tool.codex_config`; companion mechanics: `vcb.codex.config`
- `AGENTS.md` → `tool.codex_agents_md`; companion mechanics: `vcb.codex.agents_md`
- `Codex skill` → `tool.codex_skills`; companion mechanics: `vcb.codex.skills`
- `MCP` → `tool.codex_mcp`; companion mechanics: `vcb.codex.mcp`
- `Codex hook` → `tool.codex_hooks`; companion mechanics: `vcb.codex.hooks`
## Review, Safety, and Verification Workflow Cards

- `vcb.workflow.codex_output_review` → active: Codex output review by diff, checks, and risk
- `vcb.workflow.reviewing_diffs` → active: local diff review and hunk-level risk scan
- `vcb.workflow.github_pr_review` → active: Codex-assisted PR review without treating AI as approval
- `vcb.safety.security_review` → active: trust-boundary, auth, data, and exploitability review
- `vcb.safety.secrets` → active: credentials, tokens, CI secrets, browser/session exposure
- `vcb.workflow.ci_triage` → active: failed-check and log triage before mutation
- `vcb.workflow.ci_noninteractive` → active: Codex in CI with least privilege and auditable outputs
- `vcb.safety.production_red_lines` → active: hard-stop gates for production-risk work

## Frontend, Refactor, Dependency, Release, and Documentation Workflow Terms
- `vcb.workflow.frontend_work` → active: frontend state, responsive behavior, and browser evidence
- `vcb.workflow.visual_qa` → active: screenshot and visual-regression review
- `vcb.workflow.accessibility_review` → active: accessibility checks, keyboard paths, labels, and WCAG-guided review
- `vcb.workflow.refactoring` → active: behavior-preserving refactor workflow with tests and diff review
- `vcb.workflow.dependency_decisions` → active: new dependency/package/framework decision workflow
- `vcb.workflow.dependency_update_review` → active: dependency update and lockfile review workflow
- `vcb.workflow.release_notes` → active: release-note drafting from verified change sources
- `vcb.workflow.documentation_updates` → active: documentation update workflow tied to code, docs, and release context

## Failure-mode glossary entries
- `vcb.failure.hallucinated_apis` → active: invented or unsupported APIs, routes, fields, packages, flags, callbacks, or response shapes.
- `vcb.failure.context_pollution` → active: stale, irrelevant, contradictory, or oversized context that steers Codex toward the wrong target.
- `vcb.failure.weakened_tests` → active: tests made easier to pass instead of preserving behavior evidence.
- `vcb.failure.broad_refactor_drift` → active: cleanup or modernization drifting into behavior change, migration, or rewrite.
- `vcb.failure.dependency_bloat` → active: packages or frameworks added faster than the project can justify, maintain, or audit them.
- `vcb.failure.ui_taste_gap` → active: generated UI that works mechanically but misses product feel, states, accessibility, or responsiveness.
- `vcb.failure.ci_false_confidence` → active: green checks or CI summaries treated as stronger evidence than they are.
- `vcb.failure.done_claim_without_evidence` → active: polished completion claims without changed-file, command, screenshot, log, or acceptance evidence.

## Constraint and budget terms

- `vcb.constraints.operating_mode` → operating mode: the selected Codex surface, task size, permission level, and supervision rhythm
- `vcb.constraints.attention_budget` → attention budget: the human focus available for planning, check-ins, diff review, and acceptance
- `vcb.constraints.usage_burn` → usage burn: how quickly Codex work consumes included limits, credits, API spend, or shared budget
- `vcb.constraints.recovery_budget` → recovery budget: the time, expertise, rollback path, and confidence available to undo bad work
- `vcb.constraints.build_vs_maintenance` → phase constraint: the difference between exploratory build work and low-surprise maintenance work
- `vcb.constraints.production_quality` → production-quality constraint: evidence and guardrails required before work is trusted for real users
- `vcb.constraints.scope_budget` → cheapest reliable workflow: the lowest-cost path that still preserves evidence and recovery
- `vcb.constraints.review_budget` → high-throughput workflow: parallel or high-usage Codex work with isolation, review capacity, and recovery gates

## Active Shortcut Harm-Reduction Terms

- `vcb.shortcut.skipping_tests` → active: accepting generated changes without nearest verification
- `vcb.shortcut.accepting_looks_done` → active: accepting polished output without evidence
- `vcb.shortcut.broad_agent_permissions` → active: granting more authority than the task needs
- `vcb.shortcut.unattended_long_runs` → active: allowing long agent work without checkpoints
- `vcb.shortcut.broad_refactor` → active: broad cleanup without behavior-preservation boundaries
- `vcb.shortcut.context_dumping` → active: pasting excessive, stale, or sensitive context
- `vcb.shortcut.adding_dependencies_fast` → active: adding packages before proving need and reviewability
- `vcb.shortcut.reviewing_cloud_summary_only` → active: accepting background work from prose summary without diff/artifact review

## Security and permission shortcut terms

- `vcb.shortcut.production_console_computer_use` — Production Console Computer Use: risk-managed shortcut card for using Codex Computer Use or browser control inside production/admin consoles where clicks can affect real users, money, data, or credentials.
- `vcb.shortcut.overbroad_ci_permissions` — Overbroad CI Permissions: risk-managed shortcut card for giving CI workflows broad repository, package, deployment, or cloud permissions because narrowing them takes setup time.
- `vcb.shortcut.long_lived_ci_secrets` — Long-Lived CI Secrets: risk-managed shortcut card for using persistent cloud/API tokens in CI because short-lived credentials, OIDC, or scoped environments take more setup.
- `vcb.shortcut.real_secrets_in_prototype` — Real Secrets in Prototype: risk-managed shortcut card for using live API keys, production databases, real customer accounts, or payment credentials in a prototype because fake data slows the first demo.
- `vcb.shortcut.cloud_work_with_real_secrets` — Cloud Work with Real Secrets: risk-managed shortcut card for delegating cloud/background Codex work while real credentials, tokens, or sensitive environment values are available to the task.
- `vcb.shortcut.full_access_automation` — Full-Access Automation: risk-managed shortcut card for running automated Codex or agent jobs with full filesystem, command, network, or credential access because approval prompts make automation inconvenient.
- `vcb.shortcut.unattended_mutation` — Unattended Mutation: risk-managed shortcut card for letting an agent change files, settings, data, CI, dependencies, or accounts while the human is not checking milestones or evidence.
- `vcb.shortcut.always_allow_sensitive_apps` — Always Allow Sensitive Apps: risk-managed shortcut card for permanently allowing Codex to use sensitive desktop apps, websites, or browser hosts so future prompts do not pause for approval.

## Setup and process shortcut cards

- `vcb.shortcut.skipping_setup` → active: editing before setup/run/test path is known.
- `vcb.shortcut.default_config_forever` → active: stale default Codex config after project risk changes.
- `vcb.shortcut.skipping_agents_md` → active: missing durable repo guidance for repeated Codex mistakes.
- `vcb.shortcut.overstuffing_agents_md` → active: oversized or noisy durable repo guidance.
- `vcb.shortcut.stale_agents_md` → active: outdated AGENTS.md commands or rules.
- `vcb.shortcut.unofficial_tools` → active: third-party/unofficial tool adoption without trust-boundary review.
- `vcb.shortcut.hook_overreach` → active: hooks used for subjective or overbroad enforcement.
- `vcb.shortcut.trusting_external_tool_output` → active: accepting tool output without provenance and verification.

## Tool-sprawl, skill, MCP, and process shortcut terms

- `vcb.shortcut.skill_overkill` → active: avoid creating a skill before a repeated workflow earns it
- `vcb.shortcut.skill_sprawl` → active: audit overlapping skills and disabled stale reusable workflows
- `vcb.shortcut.tool_sprawl` → active: add one tool at a time with owner, purpose, and exit path
- `vcb.shortcut.tool_sprawl_mcp` → active: keep MCP servers scoped, allow-listed, and purpose-bound
- `vcb.shortcut.brittle_hooks` → active: keep hooks fast, deterministic, report-first, and reviewed
- `vcb.shortcut.process_overhead_for_tiny_project` → active: avoid heavyweight process before a tiny project earns it
- `vcb.shortcut.team_workflow_without_team` → active: use solo evidence workflow before team handoff process exists
- `vcb.shortcut.copy_pasting_playbook_blindly` → active: tailor reusable playbooks to actual risk, scope, and done evidence


## Shortcut alias and redirected planned-route terms

- `vcb.shortcut.default_config_forever` — canonical active route for redirected planned alias `vcb.shortcut.using_global_config_for_everything`.
- `vcb.shortcut.many_ais_same_files` — canonical active route for redirected planned alias `vcb.shortcut.parallel_agents_same_files`.
- `vcb.shortcut.parallel_agents_edit_same_files` — canonical active route for redirected planned alias `vcb.shortcut.parallel_tasks_same_files`.
- `vcb.shortcut.browser_clicking_without_repro` — canonical active route for redirected planned aliases `vcb.shortcut.screenshot_only_verification` and `vcb.shortcut.unattended_gui_work`.
- `vcb.shortcut.unattended_cloud_delegation` — canonical active route for redirected planned alias `vcb.shortcut.unbounded_cloud_delegation`.
- `vcb.shortcut.conflicting_parallel_agents` — canonical active route for redirected planned aliases `vcb.shortcut.parallel_conflict` and `vcb.shortcut.parallel_write_conflicts`.
- `vcb.shortcut.logged_in_browser_secrets` — canonical active route for redirected planned alias `vcb.shortcut.browser_use_with_secrets`.

## Multi-AI/model-bias shortcut glossary routes

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

## Repository, CI, dependency, and QA tool terms

- `GitHub` → `tool.github`; companion concepts: `vcb.concepts.git_branch`, `vcb.concepts.pull_request`.
- `GitHub Actions` → `tool.github_actions`; companion workflow: `vcb.workflow.ci_triage`.
- `Dependabot` → `tool.github_dependabot`; companion workflow: `vcb.workflow.dependency_update_review`.
- `npm` → `tool.npm`; companion concept: `vcb.concepts.dependency`.
- `Playwright` → `tool.playwright`; companion workflows: `vcb.workflow.frontend_work`, `vcb.workflow.visual_qa`.
- `OpenSSF Scorecard` → `tool.openssf_scorecard`; companion tools: `tool.github_actions`, `tool.github_dependabot`.

## AI coding, AI IDE, and planning tool terms

- `ChatGPT` → `tool.chatgpt`; active planning/explanation/data-analysis route
- `Claude` → `tool.claude`; active alternate AI review and reasoning route
- `Cursor` → `tool.cursor`; active AI IDE route
- `GitHub Copilot` → `tool.github_copilot`; active GitHub/IDE-native AI coding route
- `Windsurf` → `tool.windsurf`; active agentic AI IDE route
- `Devin Desktop` → `tool.windsurf`; active Windsurf/Devin Desktop AI IDE route
- `AI IDE` → `tool.cursor`, `tool.github_copilot`, or `tool.windsurf`; choose by repo ownership, evidence, and review posture
- `alternate AI review` → `tool.claude` or `tool.chatgpt`; use `vcb.shortcut.consensus_as_correctness` as a risk companion


## Browser-dev, app-builder, and UI-generation tool terms

- `Replit` → `tool.replit`; browser-based prototyping, hosted development, learning apps, and quick demo publishing.
- `Lovable` → `tool.lovable`; AI full-stack app-builder for product sketches, MVP flow validation, and generated app handoff.
- `Bolt` → `tool.bolt`; browser-based website/app/mobile prototype builder with token and generated-code review guardrails.
- `v0` → `tool.v0`; AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points.
- `App builder` → `tool.lovable`, `tool.bolt`, `tool.replit`; companion risk: `vcb.shortcut.real_secrets_in_prototype`.
- `UI generation` → `tool.v0`; companion evidence: `tool.playwright`, `vcb.workflow.visual_qa`, `vcb.workflow.accessibility_review`.

## Hosting, Backend/Auth, Payment, Observability, and Analytics Tool Terms

- **Vercel** → `tool.vercel` → active: hosting, preview deployments, environment separation, and deployment evidence.
- **Supabase** → `tool.supabase` → active: Postgres database/backend/auth/storage and data-access guardrails.
- **Clerk** → `tool.clerk` → active: authentication, user management, sessions, organizations, and auth UI workflows.
- **Auth0** → `tool.auth0` → active: IAM, OAuth/OIDC, applications/APIs, and enterprise/B2B identity posture.
- **Stripe** → `tool.stripe` → active: payments, subscriptions, checkout, webhooks, and real-money state.
- **Sentry** → `tool.sentry` → active: error monitoring, tracing, performance, and production debugging evidence.
- **PostHog** → `tool.posthog` → active: product analytics, events, session replay, feature flags, and experiments.

## Tool-catalog coverage-gap terms

- Cloudflare → `tool.cloudflare` active for DNS/CDN/Workers/Pages/edge routing evidence.
- Netlify → `tool.netlify` active for deploy previews, deploy contexts, functions, and deployment evidence.
- Neon → `tool.neon` active for serverless Postgres, database branches, connection evidence, and migration review.
- Resend → `tool.resend` active for transactional email API, templates, sending-domain review, and notification evidence.
- Vitest → `tool.vitest` active for Vite-native JavaScript/TypeScript test evidence.
- Storybook → `tool.storybook` active for component workshop, isolated UI states, component docs, and UI handoff evidence.
- Missing ecosystem tool → `TOOL_REGISTER.md` active/deferred coverage audit first; use active companion routes instead of assuming the catalog is complete.

<!-- VCB:STOP_RETRIEVAL reason="glossary_complete" -->
<!-- VCB:END_INDEX id=vcb.index.glossary -->
