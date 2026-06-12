<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_16 version=0.1.0 -->
---
id: vcb.chunk_report.chunk_16
artifact_type: chunk_report
version: 0.1.0
chunk_id: chunk_16_review_safety_workflow_topic_cards
status: waiting_for_editor_review
created_on: '2026-06-09'
last_verified: '2026-06-09'
canonical_review_package: vibe-coding-bible-chunk-16-revision-20260609T173434Z-authoritative.zip
---

# Chunk 16 Report — Review, Safety, and Verification Workflow Topic Cards

Chunk 16 authored a bounded review/safety workflow topic-card slice after Chunk 15 approval. This Chunk 16 revision repairs editor-identified index terminal signposts, source-register table placement, and validator coverage without starting Chunk 17 or expanding scope. The slice ties Codex output review, diff review, PR review, security review, secrets handling, CI triage, non-interactive CI, and production-risk gates to the approved narrative chapters and active Codex feature cards.

## Scope Authored

Created 8 active topic cards:

- `vcb.workflow.codex_output_review` — `topics/workflows/codex-output-review.md`
- `vcb.workflow.reviewing_diffs` — `topics/workflows/reviewing-diffs.md`
- `vcb.workflow.github_pr_review` — `topics/workflows/github-pr-review.md`
- `vcb.safety.security_review` — `topics/safety/security-review.md`
- `vcb.safety.secrets` — `topics/safety/secrets.md`
- `vcb.workflow.ci_triage` — `topics/workflows/ci-triage.md`
- `vcb.workflow.ci_noninteractive` — `topics/workflows/ci-noninteractive.md`
- `vcb.safety.production_red_lines` — `topics/safety/production-red-lines.md`

## Revision Applied After Editor Review

This Chunk 16-only revision fixes editor-blocking repository-contract issues without starting Chunk 17 or expanding the content slice.

- Added missing `VCB:STOP_RETRIEVAL` and matching `VCB:END_INDEX` markers to updated index files.
- Moved Chunk 16 source records into a declared `## Chunk 16 Source Records` table in `SOURCE_REGISTER.md`.
- Tightened `scripts/validate_repository.py` to catch index terminal marker gaps, cross-artifact VCB begin/end mismatches, and source-register rows outside declared source tables.
- Added explicit maintenance-phase budget language to the eight Chunk 16 topic cards.

## Explicit Non-Scope Preserved

Chunk 16 did not start:

- full tool-card expansion;
- full shortcut-card expansion;
- field-practice-card expansion;
- pricing snapshot expansion;
- broad workflow expansion outside the approved review/safety slice;
- new narrative chapters.

## Files Created

- `CHUNK_16_REPORT.md`
- `topics/workflows/codex-output-review.md`
- `topics/workflows/reviewing-diffs.md`
- `topics/workflows/github-pr-review.md`
- `topics/safety/security-review.md`
- `topics/safety/secrets.md`
- `topics/workflows/ci-triage.md`
- `topics/workflows/ci-noninteractive.md`
- `topics/safety/production-red-lines.md`

## Files Updated

- `README.md`
- `manifest.json`
- `llms.txt`
- `llms-full.txt`
- `SOURCE_REGISTER.md`
- `CHANGELOG.md`
- `TREE.txt`
- `scripts/validate_repository.py`
- `indexes/GLOSSARY.md`
- `indexes/INDEX_BY_BUDGET_PROFILE.md`
- `indexes/INDEX_BY_CODEX_SURFACE.md`
- `indexes/INDEX_BY_CONCEPT.md`
- `indexes/INDEX_BY_FAILURE_MODE.md`
- `indexes/INDEX_BY_PROJECT_TYPE.md`
- `indexes/INDEX_BY_RECOVERABILITY.md`
- `indexes/INDEX_BY_RISK_LEVEL.md`
- `indexes/INDEX_BY_SHORTCUT.md`
- `indexes/INDEX_BY_STABILITY.md`
- `indexes/INDEX_BY_TASK.md`
- `indexes/INDEX_BY_TOOL_CATEGORY.md`
- `indexes/INDEX_FOR_AI_COACHES.md`
- `indexes/PROMPT_LIBRARY.md`

## Source Review

Official OpenAI/Codex sources checked or reused as anchors:

- `openai.codex.app_review`
- `openai.codex.github_review`
- `openai.codex.use_cases.github_code_reviews`
- `openai.codex.workflows`
- `openai.codex.best_practices`
- `openai.codex.security`
- `openai.codex.security_plugin`
- `openai.codex.security_setup`
- `openai.codex.security_threat_model`
- `openai.codex.noninteractive`
- `openai.codex.github_action`
- `openai.codex.use_cases.automation_bug_triage`
- `openai.codex.agent_approvals_security`
- `openai.codex.cloud_internet_access`
- `openai.codex.app_computer_use`

Official vendor/security sources checked or reused as anchors:

- `git.docs.diff`
- `git.docs.status`
- `github.docs.pull_requests`
- `github.docs.branch_protection`
- `github.docs.actions_ci`
- `github.docs.actions_secure_use`
- `github.docs.github_token`
- `github.docs.actions_secrets`
- `github.docs.actions_oidc`
- `owasp.top10_web`
- `owasp.llm_prompt_injection`
- `owasp.secrets_management`

Maintainer synthesis used only as synthesis:

- `vcb.synthesis.stable_engineering_practice`

## Validation Summary

Command run from repository root:

```text
python scripts/validate_repository.py
```

Expected result for the submitted package:

```text
VCB validation passed
active chapter/topic files validated: 101
shortcut IDs registered: 98
tool IDs registered: 46
pricing snapshots active: 1
```

### Machine-enforced checks

- Manifest source-file inventory matches actual package files: passed
- Manifest source_artifacts inventory matches actual package files: passed
- Manifest all_tracked_files matches source_files and actual package files: passed
- Canonical review package references are consistent across manifest fields: passed
- New review/safety workflow topic files created in Chunk 16: passed
- Required Chunk 16 review/safety workflow-card slice present: passed
- Manifest review_safety_workflow_cards map matches authored Chunk 16 files: passed
- Manifest chunk_16_required_topic_ids matches authored Chunk 16 IDs: passed
- Required topic sections present: passed
- Required VCB markers present in new review/safety workflow files: passed
- llms.txt / llms-full.txt source-map versions match current chunk: passed
- README root frontmatter status matches current chunk: passed
- README body current chunk matches manifest current chunk: passed
- README and manifest next-chunk IDs match exactly: passed
- Index/register VCB begin-marker versions match frontmatter versions: passed
- Index files include STOP_RETRIEVAL and matching END_INDEX markers: passed
- VCB begin/end marker pairs exist across Markdown artifacts: passed
- SOURCE_REGISTER source rows are inside declared Source ID tables: passed
- Duplicate review/safety full-list sections removed from primary indexes: passed
- Active Chunk 16 machine-claim catalog matches validator checks: passed
- Manifest editor_gate approval_applied matches current chunk transition: passed
- Current chunk report chunk_id matches manifest active chunk: passed
- Root governance metadata drift scan: passed
- Index namespace drift scan covers active and planned index routes: passed
- Active index routes point to authored active IDs: passed
- Active shortcut_profiles resolve to SHORTCUT_REGISTER: passed
- Index shortcut routes resolve to SHORTCUT_REGISTER: passed
- Index tool IDs resolve to TOOL_REGISTER: passed
- Evidence source IDs resolve to SOURCE_REGISTER: passed
- Active chunk report source IDs resolve to SOURCE_REGISTER: passed
- Active chunk report tool-anchor claims resolve to TOOL_REGISTER: passed
- source_status.official_openai matches Evidence and Sources sections: passed
- source_status.official_vendor matches Evidence and Sources sections: passed
- Duplicate source URL detection: passed
- Frontmatter parser accepts marker-prefixed files and ignores body horizontal rules: passed
- Report final line is AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW: passed

### Manual/editorial checks

- Scope stayed within the approved bounded review/safety workflow slice.
- Human sections use plain language, examples, good/bad contrasts, and checklists.
- AI coach sections include diagnostic questions, coaching tactics, red flags, and prompt patterns.
- Shortcut Reality sections include acceptable cases, bad-idea cases, probability/impact/recoverability, blast radius, minimum guardrails, and recovery plans.
- Budget and Constraint Notes distinguish cheapest reliable, fastest high-usage, low-attention, production-quality, prototype, and maintenance postures.
- Stable Core, Volatile Surface, and Obsolescence Watch separate durable control-loop practice from product, UI, CI, and security-tool drift.
- Revised validation now covers index terminal signposts, cross-artifact begin/end marker pairing, and source-register table placement defects.

## Design Decisions

- Review/safety workflow cards point back to existing chapters instead of replacing them.
- Codex review, GitHub review, Codex Security, non-interactive mode, and GitHub Actions details are treated as volatile product/vendor surfaces.
- Production red lines are framed as operating-mode gates rather than moral rules.
- Shortcut IDs remain registered shortcut routes, not authored shortcut topic cards.
- Exact pricing, plan limits, model routing, and feature availability were not frozen into stable prose.

## Recommended Next Chunk

Recommended next chunk after approval: `chunk_17_frontend_refactor_dependency_workflow_topic_cards`.

Scope: bounded workflow topic-card expansion for frontend verification, safe refactoring, dependency/change review, release-note, and documentation workflows.

Do not start full tool-card expansion, full shortcut-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, or new narrative chapters.

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_16 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
