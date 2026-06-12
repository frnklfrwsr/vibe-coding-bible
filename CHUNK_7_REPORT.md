---
id: vcb.chunk_report.7
artifact_type: chunk_report
version: 0.8.0-draft.chunk7
status: waiting_for_editor_review
created_on: 2026-06-08
chunk_id: chunk_7_persistent_guidance_customization
---

<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.7 version=0.8.0-draft.chunk7 -->

# CHUNK 7 REPORT — Persistent Guidance and Customization

## Scope Completed

Chunk 7 only:

- Chapter 18 — AGENTS.md: Your Repo’s Operating Manual for Codex
- Chapter 19 — Codex Config: Making Good Defaults Automatic
- Chapter 20 — Skills: Reusable Workflows for Repeated Tasks
- Chapter 21 — MCP: Giving Codex External Tools Without Creating Chaos
- Chapter 22 — Hooks and Deterministic Guardrails

No Chunk 8 review/security/shipping material was started.

**Canonical review package:** `vibe-coding-bible-chunk-7-revision-20260608T214051Z-authoritative.zip`

## Files Created

```text
chapters/18-agents-md.md
chapters/19-codex-config.md
chapters/20-skills-reusable-workflows.md
chapters/21-mcp-external-tools.md
chapters/22-hooks-deterministic-guardrails.md
CHUNK_7_REPORT.md
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

## Design Decisions

1. **Customization ladder preserved.** The chapters separate prompt, AGENTS.md, config, skill, MCP, hook, and CI/test responsibilities instead of treating all customization as one bucket.
2. **Volatile product mechanics isolated.** Exact discovery behavior, config keys, skill invocation, MCP transports/auth, and hook events are marked as volatile and source-required.
3. **No setup/config drift into command reference.** The chapters explain stable decision rules and include only illustrative examples; exact operational snippets remain review-required.
4. **Shortcut layer expanded structurally, not as full cards.** New shortcut IDs are registered as planned, but full shortcut cards remain out of scope.
5. **MCP framed as capability plus attack surface.** The chapter emphasizes least privilege, read-only-first access, attribution, and external-content skepticism.
6. **Hooks framed as deterministic guardrails.** The chapter distinguishes model instructions from enforceable checks and warns against brittle or hidden hooks.

## Revision Notes

This Chunk 7 revision fixes root-governance metadata only:

- `README.md` frontmatter status now matches Chunk 7.
- `manifest.json` `editor_gate.approval_applied` now records Chunk 6 approval before Chunk 7 authorship.
- `scripts/validate_repository.py` now checks README/manifest/report chunk metadata consistency.
- The validation summary now includes root-governance metadata drift checks.

No Chunk 8 content was started.

## Sources Checked

- `openai.codex.agents_md` — official Codex source for AGENTS guidance discovery, layering, override behavior, and current volatile mechanics.
- `openai.codex.config_basic` — official Codex source for config file locations, project config, trust behavior, CLI/IDE shared config layers, and precedence.
- `openai.codex.config_advanced` — official Codex source for profiles, one-off overrides, project config limitations, hook config locations, and project root detection.
- `openai.codex.skills` — official Codex source for skills, metadata, explicit/implicit invocation, progressive disclosure, and skill locations.
- `openai.codex.use_cases.reusable_codex_skills` — official Codex source for saving workflows as skills.
- `openai.codex.mcp` — official Codex source for MCP purpose, server types, authentication concepts, and server instructions.
- `openai.codex.hooks` — official Codex source for hooks, use cases, lifecycle behavior, feature flag, and trust/review mechanics.
- `openai.codex.customization` — official Codex source for how AGENTS guidance, skills, and MCP fit together.
- `openai.codex.best_practices` — official Codex source for adding tools only when they unlock real workflows and turning repeated work into focused skills.

## Validation Summary

```text
VCB validation passed
Actual source files tracked in manifest: 86
Manifest source-file inventory matches actual package files: yes
source_files rich objects preserved: yes
Markdown files: 62
Markdown files with frontmatter/metadata fences: 62 / 62
Markdown files with VCB markers: 62 / 62
JSON files: 8
JSON parse check: passed
JSON Schema draft compile check: passed
Active chapter/topic files validated: 29
Active chapter/topic frontmatter schema validation: passed
Required Markdown headings present in active chapter/topic files: passed
VCB section marker pairing in active chapter/topic files: passed
New chapter files created in Chunk 7: 5
New chapter frontmatter schema validation: passed, 5 / 5
Required Chunk 7 files present: passed
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
No exact pricing, limits, model-routing, context-window numbers, or unstable UI-command recipes added to stable prose: passed
Canonical review package policy: one timestamped authoritative zip
Report final line: AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
```

## Unresolved Questions

1. Whether future dedicated `vcb.codex.*` topic cards should compile out of the chapter prose or be authored independently.
2. Whether Chunk 8 should add source-register duplicate-URL detection before or after security/CI content.
3. Whether hook examples should stay conceptual until a dedicated Codex hooks topic card can carry executable examples.
4. Whether MCP tool cards should live under `vcb.codex.mcp` topics first or the tool catalog first.

## Next Recommended Chunk

Chunk 8, only after editor approval:

- Chapter 23 — Reviewing Codex Output Like a Senior Engineer
- Chapter 24 — GitHub PR Review with Codex
- Chapter 25 — Security for Vibe Coders
- Chapter 26 — CI, Non-Interactive Codex, and GitHub Actions

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.7 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
