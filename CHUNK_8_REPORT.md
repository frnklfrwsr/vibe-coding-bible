---
id: vcb.chunk_report.8
chunk_id: chunk_8_review_security_shipping
title: "Chunk 8 Report — Review, Security, and CI/Non-Interactive Automation"
artifact_type: chunk_report
version: 0.1.0
status: waiting_for_editor_review
created_on: 2026-06-08
last_verified: 2026-06-08
next_review_due: 2026-09-08
review_cadence: monthly
---

<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.8 version=0.1.0 -->

# Chunk 8 Report — Review, Security, and CI/Non-Interactive Automation

## Chunk ID and Scope

**Chunk ID:** `chunk_8_review_security_shipping`

**Scope completed:**

- Chapter 23 — Reviewing Codex Output Like a Senior Engineer
- Chapter 24 — GitHub PR Review with Codex
- Chapter 25 — Security for Vibe Coders
- Chapter 26 — CI, Non-Interactive Codex, and GitHub Actions

**Explicit non-scope respected:** cloud delegation, subagents, automations, computer-use deep dive, operating-system/team workflow chapters, failure-mode catalog, playbooks, first serious app, senior checklist, field-practice expansion, pricing snapshots, tool catalog expansion, and full shortcut cards.

## Files Created

```text
vibe-coding-bible/
  CHUNK_8_REPORT.md
  chapters/
    23-reviewing-codex-output-like-senior-engineer.md
    24-github-pr-review-with-codex.md
    25-security-for-vibe-coders.md
    26-ci-non-interactive-codex-github-actions.md
```

## Files Updated

```text
README.md
manifest.json
llms.txt
llms-full.txt
SOURCE_REGISTER.md
SHORTCUT_REGISTER.md
TOOL_REGISTER.md
CHANGELOG.md
TREE.txt

indexes/INDEX_BY_TASK.md
indexes/INDEX_BY_CONCEPT.md
indexes/INDEX_BY_CODEX_SURFACE.md
indexes/INDEX_BY_FAILURE_MODE.md
indexes/INDEX_BY_STABILITY.md
indexes/INDEX_BY_BUDGET_PROFILE.md
indexes/INDEX_FOR_AI_COACHES.md
indexes/INDEX_BY_PROJECT_TYPE.md
indexes/INDEX_BY_RECOVERABILITY.md
indexes/INDEX_BY_RISK_LEVEL.md
indexes/INDEX_BY_SHORTCUT.md
indexes/INDEX_BY_TOOL_CATEGORY.md
indexes/GLOSSARY.md
indexes/PROMPT_LIBRARY.md
```

## What Changed

- Added `vcb.chapter.reviewing_codex_output`.
- Added `vcb.chapter.github_pr_review_with_codex`.
- Added `vcb.chapter.security_for_vibe_coders`.
- Added `vcb.chapter.ci_noninteractive_github_actions`.
- Updated routing indexes for senior diff review, Codex GitHub PR review, security review, secrets/prompt-injection risk, non-interactive Codex, report-only automation, CI permissions, and GitHub Actions.
- Registered planned shortcut IDs:
  - `vcb.shortcut.skipping_pr_review`
  - `vcb.shortcut.accepting_codex_review_as_approval`
  - `vcb.shortcut.skipping_security_review`
  - `vcb.shortcut.real_secrets_in_prototype`
  - `vcb.shortcut.unattended_mutation`
  - `vcb.shortcut.overbroad_ci_permissions`
  - `vcb.shortcut.long_lived_ci_secrets`
- Added tool-register anchors for Codex GitHub review, Codex Security, Codex exec, and GitHub Actions.
- Added official OpenAI, GitHub, and OWASP source records for Chunk 8 evidence.
- Kept exact pricing, plan limits, model-routing rules, context-window numbers, and unstable executable CI recipes out of stable prose.

## Sources Checked

- `openai.codex.github_review` — official Codex GitHub review setup, `@codex review`, automatic reviews, AGENTS.md review guidance, and serious-issue focus.
- `openai.codex.use_cases.github_code_reviews` — official Codex use case for PR reviews focused on regressions, missing tests, and risky behavior changes.
- `openai.codex.app_review` — official Codex app review-pane source for Git-backed change inspection.
- `openai.codex.noninteractive` — official Codex non-interactive mode source for `codex exec`, scripts/CI use, read-only default, structured output, and automation authentication cautions.
- `openai.codex.github_action` — official Codex GitHub Action source for CI/CD workflows using Codex.
- `openai.codex.security` — official Codex Security source for plugin/cloud positioning and research-preview caveat.
- `openai.codex.agent_approvals_security` and `openai.codex.cloud_internet_access` — official Codex sources for sandbox/approval combinations, full-access risk, network/internet access, prompt injection, exfiltration, and dependency risk.
- `github.docs.actions_secure_use`, `github.docs.github_token`, `github.docs.actions_oidc`, and `github.docs.actions_secrets` — official GitHub sources for Actions security, token permissions, OIDC, and secrets.
- `owasp.top10_web` and `owasp.llm_prompt_injection` — official OWASP sources for web application security risk awareness and LLM prompt-injection framing.

## Validation Summary

```text
VCB validation passed
Actual source files tracked in manifest: 91
Manifest source-file inventory matches actual package files: yes
source_files rich objects preserved: yes
Markdown files: 67
Markdown files with frontmatter/metadata fences: 67 / 67
Markdown files with VCB markers: 67 / 67
JSON files: 8
JSON parse check: passed
JSON Schema draft compile check: passed
Active chapter/topic files validated: 33
Active chapter/topic frontmatter schema validation: passed
Required Markdown headings present in active chapter/topic files: passed
VCB section marker pairing in active chapter/topic files: passed
New chapter files created in Chunk 8: 4
New chapter frontmatter schema validation: passed, 4 / 4
Required Chunk 8 files present: passed
Required chapter sections present: passed
Required VCB markers present in new chapter files: passed
README next-chunk route checked against manifest: passed
README root frontmatter status matches current chunk: passed
README body current chunk matches manifest current chunk: passed
Manifest editor_gate approval_applied matches current chunk transition: passed
Current chunk report chunk_id matches manifest active chunk: passed
Root governance metadata drift scan: passed
Index namespace drift scan covers active and planned index routes: passed
Active index routes point to authored active IDs: passed
Active shortcut_profiles resolve to SHORTCUT_REGISTER: passed
Planned shortcut index routes resolve to SHORTCUT_REGISTER or approved future shortcut IDs: passed
Evidence source IDs resolve to SOURCE_REGISTER or declared synthesis IDs: passed
SHORTCUT_REGISTER table row shape: passed
evidence_basis/source_kind values validated against schemas: passed
Official-source anchors checked for review/security/CI claims: passed
No exact pricing, plan limits, model-routing, or context-window numbers added to stable prose: passed
Canonical review package policy: one timestamped authoritative zip
Report final line: AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
```

Known exception: `.gitkeep` files are structural placeholders and intentionally contain no frontmatter or VCB markers.

## Design Decisions

1. **Review is evidence-first.** Chapter 23 treats Codex summaries as claims and diffs/checks as evidence.
2. **Codex PR review is a signal, not approval.** Chapter 24 explicitly separates automated review from human merge ownership.
3. **Security is concrete, not theatrical.** Chapter 25 centers assets, attacker-controlled input, trust boundaries, secrets, auth, user data, payments, and recovery.
4. **CI automation starts report-only.** Chapter 26 defaults to read-only/report-only workflows before mutation.
5. **Security and CI sources are official-first.** Codex-specific claims use official OpenAI docs; GitHub Actions claims use official GitHub docs; general web/LLM security risk framing uses OWASP.
6. **Volatile details stayed volatile.** Exact commands, action versions, payload details, plan access, model choices, pricing, and current limits are not treated as stable principles.

## Unresolved Questions

1. Whether Chapter 25 should later split into separate topic cards for secrets, auth, authorization, uploads, injection, prompt injection, dependency security, and production red lines.
2. Whether Chapter 26 should later split into `codex exec`, GitHub Action, CI secrets, OIDC, and read-only report automation topic cards.
3. Whether duplicate OpenAI source URL detection should become a hard validator check after source-register cleanup.
4. Whether security-related shortcut cards should be expanded earlier than the planned risk-managed-shortcut chunk.

## Next Recommended Chunk

**Chunk 9**, only after editor approval:

- Chapter 27 — Cloud Delegation and Parallel Work
- Chapter 28 — Subagents: Parallel Thinking Without Parallel Chaos
- Chapter 29 — Automations: Recurring Work Without Recurring Prompts
- Chapter 30 — Computer Use, Browser Work, and GUI Tasks

Do not start Chunk 10 operating-system/playbook material yet.

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.8 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
