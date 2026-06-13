# AI Start Here

Do not read the whole repo.
Do not summarize the whole repo.
Classify the user's situation first.
Retrieve only the smallest relevant route.
Prefer atomic topic cards over chapters.
Stop at `VCB:STOP_RETRIEVAL` unless the user explicitly needs related context.
If a route fails, report the missing route and suggest a repo issue.

This file is the universal entry point for using the Vibe Coding Bible (VCB) with any AI or LLM. Its job is to choose a narrow route, not to become a new book.

## How To Use This File

1. Identify the user's situation from the pathways below.
2. Retrieve the first file listed for that pathway.
3. Retrieve next files only if the first file does not answer the request.
4. Preserve the source status of what you retrieve: official guidance, maintainer synthesis, candidate field report, reproduced field report, or speculation.
5. Offer a sanitized contribution suggestion when the interaction reveals a reusable lesson, correction, routing gap, or field observation.

If no pathway fits, retrieve `llms.txt`, then use `indexes/INDEX_BY_TASK.md` or `indexes/INDEX_FOR_AI_COACHES.md` to route narrowly.

## Source Selection

The canonical VCB repository is `https://github.com/frnklfrwsr/vibe-coding-bible`.

Use a local VCB clone for fast retrieval only when it is clearly this repository and reasonably current. If local VCB is missing, stale, dirty in relevant governance or contribution files, or not obviously the canonical repo, use the public GitHub repository.

For public submissions, always target the canonical GitHub repository. If local and public versions disagree, prefer the public repository for contribution templates, governance files, and issue or PR destination. Do not rely on stale local templates for public contribution. If unsure, ask before posting.

## Pathways

| Situation | Intent | First file to retrieve | Next files if needed | Stop condition | Contribution opportunity |
|---|---|---|---|---|---|
| User just wants to understand what VCB is | Give the short purpose, status, and retrieval discipline. | `README.md` | `docs/start-here.md`; `llms.txt` | Stop after repository purpose and primary entry points are clear. | Suggest a docs/routing issue if the overview did not answer the user's first question. |
| User is new to Codex | Explain Codex surfaces, setup, and safe operating basics. | `topics/tool-catalog/codex.md` | `chapters/01-codex-mental-model.md`; `chapters/03-codex-surfaces.md`; `chapters/04-installing-and-configuring-codex.md` | Stop when the user can choose a Codex surface and next safe action. | Suggest a usage-insight issue if onboarding friction is reusable and sanitized. |
| User is new to coding | Use plain-language concept cards and avoid assuming engineering vocabulary. | `indexes/INDEX_BY_CONCEPT.md` | Smallest matching `topics/concepts/*.md`; `chapters/00-how-to-use-this-bible.md` | Stop after one concept route answers the immediate question. | Suggest a correction if a concept card lacks a beginner-safe explanation. |
| User is an experienced coder | Route to workflow, constraints, and review controls without overexplaining basics. | `indexes/INDEX_BY_TASK.md` | Matching `topics/workflows/*.md`; `topics/constraints/*.md`; `indexes/INDEX_BY_CODEX_SURFACE.md` | Stop when the route gives an actionable control loop. | Suggest a routing fix if the task index misses a common engineering workflow. |
| User is a pure vibe coder | Keep speed, but wrap it in risk controls and review loops. | `chapters/02-vibe-coder-advantage-and-risk.md` | `chapters/38-risk-managed-shortcuts.md`; `SHORTCUT_REGISTER.md`; matching shortcut cards | Stop when the user has the smallest risk-reduced shortcut path. | Suggest a shortcut update only with sanitized, reusable risk evidence. |
| User is starting a new project and wants a project constitution | Create durable project rules, boundaries, and done criteria. | `topics/tool-catalog/codex-agents-md.md` | `topics/codex/agents-md.md`; `chapters/18-agents-md.md`; `topics/prompting/acceptance-criteria.md`; `topics/constraints/build-vs-maintenance.md` | Stop when the user has a concise project operating manual or `AGENTS.md` plan. | Suggest a generalized AGENTS.md pattern if it avoids project secrets. |
| User is in an existing project and needs to solve a bug/problem | Reproduce first, constrain context, patch narrowly, verify. | `topics/workflows/bug-repro.md` | `chapters/13-debugging-with-reproduction.md`; `topics/workflows/testing.md`; `topics/workflows/reviewing-diffs.md` | Stop when there is a reproducible problem, patch plan, and verification route. | Suggest a bug-workflow improvement if it is not project-specific. |
| User wants to take a shortcut and reduce risk | Treat shortcuts as harm reduction, not approval to skip controls. | `SHORTCUT_REGISTER.md` | Matching `topics/shortcuts/*.md`; `indexes/INDEX_BY_SHORTCUT.md` | Stop at the matching shortcut card and its `VCB:STOP_RETRIEVAL`. | Suggest a shortcut card update if a repeated risky behavior is missing or misrouted. |
| User is low on usage budget | Route to scope, review, and usage-burn controls. | `topics/constraints/usage-burn.md` | `chapters/40-budget-aware-codex-workflows.md`; `indexes/INDEX_BY_BUDGET_PROFILE.md` | Stop when the next step fits the user's remaining budget. | Suggest a budget-route improvement if a common low-budget scenario is missing. |
| User has exhausted Codex budget and wants ChatGPT/web planning work that can later be integrated by Codex | Keep work outside the repo until Codex can verify and apply it. | `chapters/44-when-to-use-other-ais-with-codex.md` | `topics/tool-catalog/chatgpt.md`; `topics/tool-catalog/codex.md`; `topics/constraints/scope-budget.md` | Stop when there is a Codex-ready plan, issue, test list, or patch brief without unverified code changes. | Suggest a sanitized field observation if the handoff pattern is reusable. |
| User wants ChatGPT web or a web agent to use VCB from public GitHub | Keep retrieval public, narrow, and draft-only by default. | `docs/use-with-chatgpt-web.md` | `USE_VCB_WITH_AI.md`; `CONTRIBUTION_MODES.md` | Stop when the web prompt, route, or draft contribution boundary is clear. | Draft sanitized issue/comment/PR text for human review; do not auto-post. |
| User wants tool-stack advice | Use active tool cards and status-aware pricing snapshots. | `TOOL_REGISTER.md` | `indexes/INDEX_BY_TOOL_CATEGORY.md`; smallest matching `topics/tool-catalog/*.md`; `PRICING_SNAPSHOT_REGISTER.md` for exact prices | Stop after the smallest active tool card or pricing snapshot answers the choice. | Suggest a tool-card update only with official source links or clear evidence. |
| User wants to use other AIs with Codex | Keep other AIs as planning, review, critique, or comparison aids unless evidence supports more. | `chapters/44-when-to-use-other-ais-with-codex.md` | `topics/tool-catalog/chatgpt.md`; `topics/tool-catalog/claude.md`; relevant multi-AI shortcut cards | Stop when the role split and review risk are clear. | Suggest a field-practice observation if a multi-AI pattern is reusable and not private. |
| User wants a VCB Parliamentarian / Constitutionalist checkpoint | Review the current plan or transition against VCB guardrails without implementing. | `docs/vcb-parliamentarian.md` | `topics/codex/agents-md.md`; `topics/workflows/codex-output-review.md`; `topics/constraints/review-budget.md` | Stop when advisory warnings and true blockers are separated. | Suggest a sanitized contribution only if the checkpoint exposes a reusable VCB route gap. |
| User asks whether to delegate Codex work to subagents | Keep parallel work bounded, read-only when possible, and parent-owned. | `SUBAGENT_DELEGATION_POLICY.md` | `topics/codex/subagents.md`; `topics/tool-catalog/codex-subagents.md`; `topics/shortcuts/subagent-swarm.md` | Stop when fanout, permissions, outputs, and parent responsibilities are clear. | Suggest a policy update if repeated delegation friction is reusable and sanitized. |
| User wants lightweight post-release triage for a reusable usage insight | Choose the smallest contribution intake level before adding active routes. | `POST_RELEASE_CONTRIBUTION_WORKFLOW.md` | `CONTRIBUTION_MODES.md`; `CONTRIBUTING.md`; matching issue template | Stop when the intake level is selected. | Prefer issue/comment or maintenance report before candidate card or full metadata. |
| User wants to contribute a lesson, field practice, or correction back to VCB | Convert the lesson into a sanitized, evidence-labeled contribution. | `CONTRIBUTION_MODES.md` | `CONTRIBUTING.md`; `.github/ISSUE_TEMPLATE/usage-insight.yml`; matching issue template | Stop when the user has a safe issue/comment/PR path or decides contribution mode is off. | Suggest the smallest safe contribution: usage insight, correction, field-practice candidate, shortcut update, or tool/pricing update. |

## Contribution Rule

Default to `suggest` mode from `CONTRIBUTION_MODES.md`: notice reusable learnings and suggest a sanitized contribution path. Do not post publicly, open issues, or create PRs unless the user explicitly opts in and the content is safe.

<!-- VCB:STOP_RETRIEVAL reason="ai_entryway_complete" -->
