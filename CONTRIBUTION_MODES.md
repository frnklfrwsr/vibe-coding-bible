# Contribution Modes

VCB can learn from real usage, but public contribution must not leak private project details. The default mode is `suggest`.

## Modes

| Mode | Behavior | Public posting allowed? |
|---|---|---|
| `off` | Do not notice, suggest, draft, or submit VCB contributions. | No |
| `suggest` | Notice reusable lessons and suggest a sanitized contribution path. This is the default. | No |
| `draft` | Draft a sanitized issue, comment, or PR text for the user to review. | No, not without explicit user approval |
| `auto-public-safe` | Submit only if the user explicitly opted in and the content is generalized, non-sensitive, and safe for public release. | Yes, with explicit opt-in |
| `auto-maintainer` | Maintainer-owned mode for trusted repository maintenance tasks where public contribution is already the purpose. | Yes, within maintainer scope |

## Default

Unless the user forbids it, use `suggest` mode:

- Notice reusable lessons.
- Suggest the smallest safe contribution path.
- Do not open issues, comment publicly, or create PRs without explicit user approval.

## Safe Contributions

Safe examples:

- A routing gap: "The AI could not find a low-budget debugging route."
- A correction: "A link in a tool card now redirects to a canonical vendor page."
- A field observation: "Fresh review caught a stale-context mistake in a public open-source PR."
- A shortcut update: "Users often skip lint/typecheck when quota is low; route them to budget-aware gates."
- A docs issue: "AI users need a clearer starting prompt for VCB."

Unsafe examples:

- Private repository names, customer names, credentials, logs, stack traces, or proprietary architecture.
- Exact business metrics, incident details, security findings, or unreleased product plans.
- Screenshots or code snippets from a private project unless explicitly approved and sanitized.
- Anonymous self-reports promoted as official best practice.
- Pricing claims from blogs, Reddit, old screenshots, or unofficial summaries.

## Sanitization Rules

Before drafting or submitting:

1. Remove project names, customer names, people names, secrets, account IDs, and private URLs.
2. Replace implementation details with general patterns.
3. Keep only the reusable lesson, route gap, correction, or evidence label.
4. State evidence level honestly: official source, local reproduction, expert report, community field report, or speculation.
5. Prefer an issue template over a PR unless the fix is small and source-backed.

## Issue, Comment, Or PR Decision Rules

- Use `.github/ISSUE_TEMPLATE/usage-insight.yml` for sanitized observations from real usage.
- Use `.github/ISSUE_TEMPLATE/bug-or-correction.yml` for broken links, stale facts, or bad routing.
- Use `.github/ISSUE_TEMPLATE/field-practice-proposal.yml` for candidate practices that need evidence grading.
- Use `.github/ISSUE_TEMPLATE/shortcut-card-update.yml` for shortcut-risk updates.
- Use `.github/ISSUE_TEMPLATE/tool-card-update.yml` for tool-card or source updates.
- Use a PR only when the user asks for a concrete repository edit and the change does not expose private information.

## Post-Release Intake

Use `POST_RELEASE_CONTRIBUTION_WORKFLOW.md` before turning a usage insight into repository content. The default intake level is issue/comment only. Escalate to maintenance report, candidate card, or full chunk-style metadata only when the observation passes the documented threshold and the extra route surface is justified.

<!-- VCB:STOP_RETRIEVAL reason="contribution_modes_complete" -->
