<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_14 version=0.1.2 -->
---
id: vcb.chunk_report.chunk_14
chunk_id: chunk_14_codex_feature_topic_cards
title: Chunk 14 Report — Codex Feature Topic Cards
artifact_type: chunk_report
version: 0.1.2
status: waiting_for_editor_review
created_on: 2026-06-09
last_verified: 2026-06-09
canonical_review_package: vibe-coding-bible-chunk-14-revision-20260609T151704Z-authoritative.zip
---

# Chunk 14 Report — Codex Feature Topic Cards

## Scope Completed

Chunk 14 expanded a bounded set of Codex feature/topic cards only:

- `vcb.codex.app` — `topics/codex/app.md`
- `vcb.codex.cli` — `topics/codex/cli.md`
- `vcb.codex.ide_extension` — `topics/codex/ide-extension.md`
- `vcb.codex.cloud` — `topics/codex/cloud.md`
- `vcb.codex.github_review` — `topics/codex/github-review.md`
- `vcb.codex.config` — `topics/codex/config.md`
- `vcb.codex.agents_md` — `topics/codex/agents-md.md`
- `vcb.codex.skills` — `topics/codex/skills.md`
- `vcb.codex.mcp` — `topics/codex/mcp.md`
- `vcb.codex.hooks` — `topics/codex/hooks.md`
- `vcb.codex.automations` — `topics/codex/automations.md`
- `vcb.codex.subagents` — `topics/codex/subagents.md`
- `vcb.codex.computer_use` — `topics/codex/computer-use.md`
- `vcb.codex.feature_maturity` — `topics/codex/feature-maturity.md`
- `vcb.codex.changelog_monitoring` — `topics/codex/changelog-monitoring.md`

No full tool-card expansion, shortcut-card expansion, field-practice-card expansion, or broad workflow-card expansion was started.

## Chunk 14 Revision

**Revision scope:** governance/signpost hygiene only. No new Chunk 15 content was authored.

Editor-requested fixes applied:

- Normalized `README.md` and `manifest.json` next-chunk routing to `chunk_15_workflow_prompting_topic_cards`.
- Updated index/register VCB begin-marker versions to match file frontmatter versions.
- Removed duplicate Codex feature full-list routing blocks from primary indexes.
- Expanded `scripts/validate_repository.py` so the reported governance checks are machine-enforced.
- Hardened frontmatter parsing so marker-prefixed topics/reports validate without accidentally parsing body horizontal rules as YAML.

## Files Created

```text
vibe-coding-bible/
  CHUNK_14_REPORT.md
  topics/codex/app.md
  topics/codex/cli.md
  topics/codex/ide-extension.md
  topics/codex/cloud.md
  topics/codex/github-review.md
  topics/codex/config.md
  topics/codex/agents-md.md
  topics/codex/skills.md
  topics/codex/mcp.md
  topics/codex/hooks.md
  topics/codex/automations.md
  topics/codex/subagents.md
  topics/codex/computer-use.md
  topics/codex/feature-maturity.md
  topics/codex/changelog-monitoring.md
```

## Files Updated

```text
README.md
manifest.json
llms.txt
llms-full.txt
SOURCE_REGISTER.md
TOOL_REGISTER.md
CHANGELOG.md
TREE.txt
scripts/validate_repository.py

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

## Sources Checked

Official OpenAI Codex docs were checked for the Codex app, CLI, IDE extension, web/cloud, GitHub review, config, AGENTS.md, skills, MCP, hooks, automations, subagents, computer use, feature maturity, and changelog monitoring. The feature cards cite source-register IDs such as `openai.codex.app`, `openai.codex.cli`, `openai.codex.ide`, `openai.codex.cloud`, `openai.codex.github_review`, `openai.codex.config_basic`, `openai.codex.agents_md`, `openai.codex.skills`, `openai.codex.mcp`, `openai.codex.hooks`, `openai.codex.app_automations`, `openai.codex.subagents`, `openai.codex.app_computer_use`, `openai.codex.feature_maturity`, and `openai.codex.changelog`.

Exact commands, UI labels, feature availability, platform support, model routing, and plan/usage details remain volatile and are not frozen into stable guidance.

## Validation Summary

### Validator output

```text
VCB validation passed
active chapter/topic files validated: 85
shortcut IDs registered: 98
tool IDs registered: 46
pricing snapshots active: 1
```

### Machine-enforced checks

- Manifest source-file inventory matches actual package files: passed
- Manifest source_artifacts inventory matches actual package files: passed
- Manifest all_tracked_files matches source_files and actual package files: passed
- Canonical review package references are consistent across manifest fields: passed
- New Codex feature topic files created in Chunk 14: passed
- Required Chunk 14 Codex feature-card slice present: passed
- Required topic sections present: passed
- Required VCB markers present in new Codex feature files: passed
- llms.txt / llms-full.txt source-map versions match current chunk: passed
- README root frontmatter status matches current chunk: passed
- README body current chunk matches manifest current chunk: passed
- README and manifest next-chunk IDs match exactly: passed
- Index/register VCB begin-marker versions match frontmatter versions: passed
- Duplicate Codex feature full-list sections removed from primary indexes: passed
- Active Chunk 14 machine-claim catalog matches validator checks: passed
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

- No exact pricing, plan limits, model-routing recipes, context-window numbers, or unstable UI-command recipes were added to stable prose.
- Codex feature cards stayed within Chunk 14 scope; no Chunk 15 content was authored.
- Canonical review package policy remains one timestamped authoritative zip.

## Design Decisions

1. **Codex feature cards are atomic.** They do not repeat the narrative chapters; they provide retrieval-friendly surface/feature guidance.
2. **Official facts are source-anchored.** Every card uses official OpenAI source IDs for product behavior and maintainer synthesis only for risk/workflow guidance.
3. **Volatile detail is isolated.** Exact commands, UI flows, model routing, plan packaging, platform support, and feature labels are kept in volatile sections.
4. **Shortcut handling stays harm-reduction oriented.** Each card explains acceptable shortcuts, bad-idea cases, minimum guardrails, and recovery.
5. **Tool cards remain future work.** `TOOL_REGISTER.md` gained planned surface anchors, but no full tool-card expansion was authored.

## Next Recommended Chunk

**Chunk 15:** `chunk_15_workflow_prompting_topic_cards`, only after editor approval:

- Continue bounded individual topic-card expansion.
- Recommended slice: prompting/workflow cards tied to core Codex operating behavior.
- Do not combine with full tool-card expansion, shortcut-card expansion, or field-practice-card expansion.

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_14 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
