---
id: vcb.register.tools
title: TOOL_REGISTER
artifact_type: register
version: 1.0.0-rc.1.chunk43
status: chunk_43_updated
created_on: '2026-06-08'
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: monthly
---

<!-- VCB:BEGIN_REGISTER id=vcb.register.tools version=1.0.0-rc.1.chunk43 -->

# TOOL_REGISTER

**Purpose:** Track active, deferred, planned, alias/companion, and excluded tool-catalog coverage while enforcing source/pricing hygiene.

## Tool Card Requirements

Each future tool card must include:

- official vendor source;
- dated pricing snapshot if exact pricing or limits are mentioned;
- setup effort;
- maintenance effort;
- debugging effort;
- lock-in risk;
- hidden cost risk;
- Codex integration value;
- best-fit cases;
- not-fit cases;
- obsolescence watch.

## Planned Tool Categories

| Category | Planned topic ID | Planned file |
|---|---|---|
| AI coding tools | `tool.ai_coding_tools` | `topics/tool-catalog/ai-coding-tools.md` |
| Repo and CI | `tool.repo_and_ci` | `topics/tool-catalog/repo-and-ci.md` |
| Hosting and deployment | `tool.hosting_and_deployment` | `topics/tool-catalog/hosting-and-deployment.md` |
| Databases and backend | `tool.databases_and_backend` | `topics/tool-catalog/databases-and-backend.md` |
| Auth | `tool.auth` | `topics/tool-catalog/auth.md` |
| Payments | `tool.payments` | `topics/tool-catalog/payments.md` |
| Email | `tool.email` | `topics/tool-catalog/email.md` |
| Observability | `tool.observability` | `topics/tool-catalog/observability.md` |
| Analytics | `tool.analytics` | `topics/tool-catalog/analytics.md` |
| Design and prototyping | `tool.design_and_prototyping` | `topics/tool-catalog/design-and-prototyping.md` |
| Project management | `tool.project_management` | `topics/tool-catalog/project-management.md` |
| Documentation | `tool.documentation` | `topics/tool-catalog/documentation.md` |
| Local dev and containers | `tool.local_dev_and_containers` | `topics/tool-catalog/local-dev-and-containers.md` |
| Security and secrets | `tool.security_and_secrets` | `topics/tool-catalog/security-and-secrets.md` |


## Chunk 42 Release-Candidate Disposition Note

Chunk 42 does not add, activate, defer, or exclude tool IDs. It confirms the release-candidate disposition: 52 active authored tool cards and 23 deferred/planned concrete ecosystem IDs are explicit, curated tool coverage is a documented limitation rather than a hidden blocker, and one-card-per-service expansion remains excluded until a future editor-approved slice. The Chunk 42 author package was not a release-candidate package; Release Candidate 1 was later produced by Chunk 43 as a packaging-only artifact.

## Chunk 36 Local Dev, Design, and Project-Management Tool Card Activation Note

Chunk 36 activates the local development/container, design/prototyping, and project-management rows for `tool.docker`, `tool.figma`, and `tool.linear` and binds them to authored tool cards under `topics/tool-catalog/`. Treat exact pricing, plan limits, seat limits, quota limits, Docker Desktop licensing details, current UI labels, command flags, container/security defaults, Figma feature availability, export/dev-mode mechanics, Linear workflow/status mechanics, integrations, automation behavior, and current capability claims as volatile vendor-source details or dated snapshot material, not stable prose.

## Chunk 35 Hosting, Backend/Auth, Payment, Observability, and Product-Analytics Tool Card Activation Note

The following planned third-party platform anchors are active as of Chunk 35: `tool.vercel`, `tool.supabase`, `tool.clerk`, `tool.auth0`, `tool.stripe`, `tool.sentry`, and `tool.posthog`. Treat exact pricing, plan limits, quota limits, current UI labels, deployment/database/auth/payment/analytics/observability limits, SDK setup mechanics, and feature availability as volatile vendor-source details or dated snapshot material, not stable prose.

## Pricing Rule

Exact prices and exact limits must be placed in `pricing-snapshots/`, not in stable tool cards.


## Chunk 14 Codex Feature Surface Anchors

| Tool ID | Category | Status | Use for | Pricing/source note |
|---|---|---|---|---|
| `tool.codex_app` | codex_surface | active | desktop command-center surface for local projects, threads, review, worktrees, and automations | verify official app docs; UI/platform behavior volatile |
| `tool.codex_cli` | codex_surface | active | terminal-native local Codex work, commands, scripting, and non-interactive entrypoint | verify official CLI docs; commands and flags volatile |
| `tool.codex_ide_extension` | codex_surface | active | side-by-side IDE workflow with open-file/selection context and cloud delegation | verify official IDE extension docs; editor support/settings volatile |
| `tool.codex_feature_maturity` | codex_governance | active | maturity-label governance for Codex feature reliability, fallback posture, and production-readiness review | official OpenAI Codex docs only; maturity labels/meanings/status are volatile |
| `tool.codex_changelog_monitoring` | codex_governance | active | official Codex changelog monitoring for Bible maintenance, deprecation watch, and route/source refreshes | official OpenAI Codex changelog only; release entries and update cadence are volatile |

## Chunk 6 Tool Anchors

| Tool ID | Category | Status | Use for | Pricing/source note |
|---|---|---|---|---|
| `tool.playwright` | browser/testing | active | screenshot capture, visual comparisons, browser checks | verify official Playwright docs; exact config is volatile |
| `tool.npm` | package_manager | active | dependency manifests, install behavior, audit reports | verify official npm docs for command behavior |
| `tool.github_dependabot` | supply_chain | active | vulnerable dependency alerts and update PRs | verify official GitHub docs for behavior/UI |
| `tool.openssf_scorecard` | supply_chain | active | dependency/project health and supply-chain risk signals | verify official OpenSSF docs/project pages |


## Chunk 7 Codex Customization Anchors

| Tool ID | Category | Status | Use for | Pricing/source note |
|---|---|---|---|---|
| `tool.codex_agents_md` | codex_customization | active | durable repo guidance and project operating manuals | official OpenAI Codex docs only; pricing/plan details remain snapshot-only |
| `tool.codex_config` | codex_customization | active | local/project/profile configuration defaults | exact keys, precedence, and profiles are volatile; verify config reference |
| `tool.codex_skills` | codex_customization | active | reusable workflow packages | verify official skill format, locations, invocation, and plugin packaging details |
| `tool.codex_mcp` | codex_customization | active | external tool and context connections | verify official MCP setup, auth, server, and trust-boundary docs |
| `tool.codex_hooks` | codex_customization | active | deterministic lifecycle guardrails | verify official hook events, config, review, and trust mechanics docs |

## Chunk 8 Review/Security/Automation Anchors

| Tool ID | Category | Status | Use for | Pricing/source note |
|---|---|---|---|---|
| `tool.codex_github_review` | code_review | active | GitHub PR review, automatic review, review guidelines | official OpenAI Codex docs only; review behavior volatile |
| `tool.codex_security` | security | active | Codex Security plugin/cloud security review workflows, finding review, and reviewed fix preparation | official OpenAI Codex Security docs only; feature maturity/access/pricing/scan behavior volatile |
| `tool.codex_exec` | automation | active | non-interactive scripts and CI tasks | exact flags/auth behavior volatile; no pricing in stable prose |
| `tool.github_actions` | repo_ci | active | CI workflows, secrets, token permissions, OIDC, Codex GitHub Action | use official GitHub/OpenAI docs; pricing snapshots if exact costs appear |

## Chunk 9 Advanced Agentic Workflow Anchors

| Tool ID | Category | Status | Use for | Pricing/source note |
|---|---|---|---|---|
| `tool.codex_cloud` | cloud_delegation | active | background cloud tasks, PR proposals, isolated high-throughput work | official OpenAI docs only; usage/pricing details volatile |
| `tool.codex_worktrees` | isolation | active | parallel local/app tasks without disturbing active checkout | verify Codex app and Git worktree docs |
| `tool.codex_subagents` | parallel_agents | active | parallel analysis, custom agents, specialist reports | verify official subagent docs; model routing volatile |
| `tool.codex_automations` | recurring_work | active | scheduled recurring tasks and findings inbox | verify official automation docs; exact schedule/UI volatile |
| `tool.codex_computer_use` | gui_automation | active | desktop app/browser/GUI operation and verification | verify official computer-use docs; OS permissions volatile |
| `tool.codex_browser` | browser_testing | active | in-app browser preview, comments, browser verification | verify official browser docs; signed-in limitations volatile |
| `tool.codex_chrome_extension` | browser_signed_in_workflows | active | signed-in Chrome browser tasks, website allowlists/blocklists, browser-history and account-context risk | verify official Chrome extension docs; permissions and setup are volatile |

## Chunk 12 Tool Stack Catalog Anchors

| Tool ID | Category | Status | Use for | Pricing/source note |
|---|---|---|---|---|
| `tool.codex` | ai_coding | active | repo-aware coding agent, implementation, review, cloud/local workflows | official OpenAI Codex docs; pricing highly volatile |
| `tool.chatgpt` | planning_explanation | active | product thinking, planning, explanation, PM-style prompt shaping, source-backed research, and data/document analysis | official OpenAI/ChatGPT docs; plan packaging, models, tools, and pricing volatile |
| `tool.claude` | alternate_ai_review | active | independent architecture/review perspective, long-form explanation, and source-verified critique | official Anthropic/Claude docs; model, plan, and Claude Code surface behavior volatile |
| `tool.cursor` | ai_ide | active | IDE-native coding assistance, local file editing, plan-first agent work, and diff review | official Cursor docs/security docs; pricing, models, agent behavior, and privacy controls volatile |
| `tool.github_copilot` | ai_ide | active | GitHub/IDE-native autocomplete, chat, repository-connected assistance, and agentic branch/PR workflows | official GitHub Copilot docs; pricing, org policy, feature availability, and model routing volatile |
| `tool.windsurf` | ai_ide | active | agentic AI IDE workflow, Cascade planning/editing, checkpoints, tool calls, and plugin support | official Windsurf/Devin docs; product naming, pricing, admin controls, and agent mechanics volatile |
| `tool.replit` | browser_dev | active | browser-based prototyping, hosted development, learning apps, and quick demo publishing | official Replit docs; pricing, hosting/runtime limits, publishing controls, and integrations volatile |
| `tool.lovable` | app_builder | active | AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails | official Lovable docs; pricing, cloud/backend, integrations, publishing, and governance controls volatile |
| `tool.bolt` | app_builder | active | browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails | official Bolt docs; token, hosting, integrations, generation, and publish behavior volatile |
| `tool.v0` | ui_generation | active | AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points | official v0/Vercel docs; pricing, models, deployment, API, design-system, and generation mechanics volatile |
| `tool.github` | repo_ci | active | version control, PRs, issues, code review, Actions integration | official GitHub docs; pricing/features volatile |
| `tool.vercel` | hosting | active | hosting, preview deployments, production deployment evidence, and environment separation | official Vercel docs/pricing; exact values snapshot-only |
| `tool.supabase` | database_backend_auth | active | Postgres database, backend/auth/storage, RLS-aware app data, and MVP backend review | official Supabase docs/pricing; exact values snapshot-only |
| `tool.stripe` | payments | active | payments, subscriptions, checkout, webhooks, billing objects, and real-money state review | official Stripe docs/pricing; exact fees snapshot-only |
| `tool.clerk` | auth | active | authentication, user management, sessions, organizations, and auth UI workflows | official Clerk docs/pricing; exact values snapshot-only |
| `tool.auth0` | auth | active | IAM, OAuth/OIDC, applications/APIs, enterprise/B2B auth, and authorization architecture | official Auth0 docs/pricing; exact values snapshot-only |
| `tool.sentry` | observability | active | error monitoring, tracing, performance, session replay, release evidence, and incident debugging | official Sentry docs/pricing; exact values snapshot-only |
| `tool.posthog` | analytics | active | product analytics, event taxonomy, session replay, feature flags, experiments, and product evidence | official PostHog docs/pricing; exact values snapshot-only |
| `tool.docker` | local_dev_containers | active | reproducible local services, Dockerfiles, Compose stacks, containerized dev/test environments, and isolation/rebuild evidence | official Docker docs/pricing; exact values, commands, defaults, and Docker Desktop licensing details snapshot/source-check only |
| `tool.figma` | design | active | collaborative design files, components, prototypes, Dev Mode handoff, screenshots, and design-intent evidence | official Figma docs/pricing; exact values, seat limits, Dev Mode mechanics, and feature availability source-check only |
| `tool.linear` | project_management | active | issues, projects, teams, workflows, cycles, planning status, and product/team execution hygiene | official Linear docs/pricing; exact values, workflow mechanics, automation behavior, and integrations source-check only |
| `tool.cloudflare` | edge_hosting_security | active | DNS, CDN/security controls, Workers, Pages, edge deployment, and domain/routing evidence | official Cloudflare docs; exact limits, pricing, runtime behavior, and security defaults source-check only |
| `tool.netlify` | hosting_deployment | active | site deploys, deploy previews, functions, deploy contexts, and rollback/deployment evidence | official Netlify docs; exact limits, pricing, build/runtime behavior, and UI labels source-check only |
| `tool.neon` | database_backend | active | serverless Postgres, database branches, preview database workflows, connection evidence, and migration review | official Neon docs; exact limits, pricing, auth/storage/functions availability, and connection mechanics source-check only |
| `tool.resend` | email_delivery | active | transactional email API, sending-domain review, templates, delivery evidence, and notification workflows | official Resend docs; exact limits, pricing, deliverability, and API mechanics source-check only |
| `tool.vitest` | testing | active | Vite-native unit/component tests, watch-mode feedback, test evidence, and CI-adjacent JavaScript verification | official Vitest docs; exact config, environment, browser mode, and API behavior source-check only |
| `tool.storybook` | ui_testing_documentation | active | component workshop, isolated UI states, component documentation, interaction tests, and design-handoff evidence | official Storybook docs; exact addons, test runner behavior, builders, and version mechanics source-check only |

## Chunk 27 Primary Codex Tool Card Activation Note

Chunk 27 activates the primary OpenAI/Codex execution-surface rows already declared in the earlier tool-anchor tables and binds them to authored tool cards under `topics/tool-catalog/`. Keep each tool ID declared once in this register; route inventories live in README, manifest, indexes, and LLM maps.


## Chunk 28 Adjunct OpenAI/Codex Tool Card Activation Note

Chunk 28 activates the adjunct first-party OpenAI/Codex surface rows already declared in the Chunk 9 advanced-agentic workflow anchors. Keep each tool ID declared once in this register; route inventories live in README, manifest, indexes, and LLM maps.


## Chunk 30 Codex Security Tool Card Activation Note

Chunk 30 activates the first-party OpenAI/Codex Security row already declared in the Chunk 8 review/security/automation anchors and binds it to `topics/tool-catalog/codex-security.md`. Keep the tool ID declared once in this register; route inventories live in README, manifest, indexes, and LLM maps.


## Chunk 31 Codex Governance and Maintenance Tool Card Activation Note

Chunk 31 activates the first-party OpenAI/Codex governance rows for tool.codex_feature_maturity and tool.codex_changelog_monitoring and binds them to authored tool cards under `topics/tool-catalog/`. Keep each tool ID declared once in this register; route inventories live in README, manifest, indexes, and LLM maps.

## Chunk 33 AI Coding, AI IDE, and AI Planning Tool Card Activation Note

Chunk 33 activates the AI coding, AI IDE, and AI planning rows for `tool.chatgpt`, `tool.claude`, `tool.cursor`, `tool.github_copilot`, and `tool.windsurf` and binds them to authored tool cards under `topics/tool-catalog/`. Keep each tool ID declared once in this register; route inventories live in README, manifest, indexes, and LLM maps.

## Chunk 32 Repository, CI, Dependency, and QA Tool Card Activation Note

Chunk 32 activates the non-AI developer infrastructure tool rows for `tool.github`, `tool.github_actions`, `tool.github_dependabot`, `tool.npm`, `tool.playwright`, and `tool.openssf_scorecard` and binds them to authored tool cards under `topics/tool-catalog/`. Keep each tool ID declared once in this register; route inventories live in README, manifest, indexes, and LLM maps.

## Chunk 34 Browser-Dev, App-Builder, and UI-Generation Tool Card Activation Note

Chunk 34 activates the browser-dev, app-builder, and UI-generation rows for `tool.replit`, `tool.lovable`, `tool.bolt`, and `tool.v0` and binds them to authored tool cards under `topics/tool-catalog/`. Keep each tool ID declared once in this register; route inventories live in README, manifest, indexes, and LLM maps.


## Chunk 40 Tool-Catalog Coverage-Gap Audit Note

Chunk 40 confirms that the 46 active tool cards present before this chunk were not an exhaustive ecosystem catalog. This register now distinguishes active authored cards, deferred/planned ecosystem IDs, alias/companion routes, and explicit exclusions. Do not treat a missing full card as evidence that the tool is unimportant; route through this audit section and the smallest active companion card until a future chunk authors the exact tool card.

### Chunk 40 Active Ecosystem Expansion

The following coverage-gap tools are active as authored cards in Chunk 40: `tool.cloudflare`, `tool.netlify`, `tool.neon`, `tool.resend`, `tool.vitest`, and `tool.storybook`.

### Deferred / Planned Ecosystem Tool IDs

| Tool ID | Category | Status | Intended future route | Interim companion route |
|---|---|---|---|---|
| `tool.render` | hosting_deployment | deferred_planned | hosting/deployment platform card if user demand or coverage slice prioritizes Render | `tool.vercel`, `tool.netlify`, `tool.github_actions` |
| `tool.railway` | hosting_backend | deferred_planned | app/backend deployment platform card if deployment/backend ergonomics slice is approved | `tool.vercel`, `tool.netlify`, `tool.supabase` |
| `tool.fly_io` | hosting_edge_runtime | deferred_planned | edge/app runtime deployment card if runtime/region/ops slice is approved | `tool.cloudflare`, `tool.vercel`, `tool.docker` |
| `tool.firebase` | backend_auth_hosting | deferred_planned | Firebase backend/auth/hosting card if Google-backed app platform slice is approved | `tool.supabase`, `tool.auth0`, `tool.vercel` |
| `tool.aws` | major_cloud_platform | deferred_planned | broad AWS platform card or scoped AWS category card only with narrow scope | `tool.cloudflare`, `tool.vercel`, `tool.docker` |
| `tool.gcp` | major_cloud_platform | deferred_planned | broad GCP platform card or scoped GCP category card only with narrow scope | `tool.firebase`, `tool.vercel`, `tool.docker` |
| `tool.azure` | major_cloud_platform | deferred_planned | broad Azure platform card or scoped Azure category card only with narrow scope | `tool.auth0`, `tool.vercel`, `tool.docker` |
| `tool.digitalocean` | cloud_hosting | deferred_planned | VPS/app/database hosting card if simple cloud hosting slice is approved | `tool.netlify`, `tool.vercel`, `tool.docker` |
| `tool.postmark` | email_delivery | deferred_planned | transactional email card if email-delivery comparison slice is approved | `tool.resend` |
| `tool.sendgrid` | email_delivery | deferred_planned | email API/marketing-delivery card if email-delivery comparison slice is approved | `tool.resend` |
| `tool.mailgun` | email_delivery | deferred_planned | email API/deliverability card if email-delivery comparison slice is approved | `tool.resend` |
| `tool.notion` | documentation_project_management | deferred_planned | docs/wiki/project knowledge card if documentation/tooling slice is approved | `tool.linear`, `tool.github` |
| `tool.google_docs` | documentation | deferred_planned | collaborative document/spec card if documentation/tooling slice is approved | `tool.github`, `tool.linear` |
| `tool.jira` | project_management | deferred_planned | issue/project-management card if enterprise planning slice is approved | `tool.linear`, `tool.github` |
| `tool.onepassword` | secrets_management | deferred_planned | secrets/password-management card if security/secrets tool slice is approved | `tool.github_actions`, `tool.docker` |
| `tool.doppler` | secrets_management | deferred_planned | secrets/config-management card if security/secrets tool slice is approved | `tool.github_actions`, `tool.vercel` |
| `tool.infisical` | secrets_management | deferred_planned | secrets/config-management card if security/secrets tool slice is approved | `tool.github_actions`, `tool.vercel` |
| `tool.better_stack` | observability_incident | deferred_planned | logs/uptime/incident observability card if observability expansion is approved | `tool.sentry`, `tool.posthog` |
| `tool.datadog` | observability | deferred_planned | broad observability/APM card if enterprise observability slice is approved | `tool.sentry`, `tool.posthog` |
| `tool.paddle` | payments_billing | deferred_planned | merchant-of-record/payment card if payments expansion is approved | `tool.stripe` |
| `tool.lemon_squeezy` | payments_billing | deferred_planned | merchant-of-record/payment card if payments expansion is approved | `tool.stripe` |
| `tool.jest` | testing | deferred_planned | JavaScript test runner card if legacy/test-runner comparison slice is approved | `tool.vitest`, `tool.npm` |
| `tool.cypress` | browser_testing | deferred_planned | browser/e2e testing card if browser-test comparison slice is approved | `tool.playwright`, `tool.vitest` |

### Alias / Companion Coverage Decisions

| Ecosystem surface | Status | Route decision |
|---|---|---|
| GitHub Issues | alias_companion | Use active `tool.github`; future separate `tool.github_issues` card is not needed unless issue/workflow depth outgrows `tool.github`. |
| GitHub Secrets | alias_companion | Use active `tool.github_actions` for CI secrets and workflow secret posture; use future secrets-management cards only when external secret-store comparison is scoped. |
| Every AWS/GCP/Azure service | explicit_exclusion_for_now | Do not create one card per cloud service by default. Use scoped major-cloud or service-family cards only after editor approval. |

## Chunk 37 Tool-Catalog Routing Cleanup Note

Chunk 37 did not add, remove, or activate tool IDs. It consolidated README tool-card inventory, removed generation-specific aggregate inventory blocks from indexes, preserved semantic active-tool routing, and tightened validation for duplicate semantic routes and source URL canonicalization.

## Chunk 41 Finalization Readiness Audit Note

Chunk 41 does not add or activate tool IDs. The finalization-readiness audit confirms the tool register currently distinguishes:

- 52 active authored tool cards under `topics/tool-catalog/`;
- 23 concrete deferred/planned ecosystem IDs in the Chunk 40 coverage-gap table;
- 14 older category placeholders under `## Planned Tool Categories`;
- alias/companion decisions for GitHub Issues and GitHub Secrets;
- an explicit exclusion against one-card-per-cloud-service expansion without scoped editor approval.

Release-candidate posture: tool coverage is explicit and navigable, but not exhaustive. Do not market the active 52-card set as complete ecosystem coverage unless a future editor-approved slice closes or explicitly accepts the deferred/planned rows.

<!-- VCB:STOP_RETRIEVAL reason="tool_register_complete" -->
<!-- VCB:END_REGISTER id=vcb.register.tools -->
