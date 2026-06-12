---
id: vcb.chunk_report.chunk_2
title: Chunk 2 Report — Codex Mental Model and Surfaces
artifact_type: chunk_report
version: 0.3.1-draft.chunk2-revision
status: waiting_for_editor_review_chunk_2_revision
created_on: 2026-06-08
last_verified: 2026-06-08
next_review_due: 2026-07-08
review_cadence: event_driven
---

<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_2 version=0.3.1-draft.chunk2-revision -->

# Chunk 2 Report — Codex Mental Model and Surfaces

## Chunk ID and Scope

**Chunk ID:** `chunk_2_codex_mental_model_and_surfaces`

**Scope completed:**

- `vcb.chapter.codex_mental_model`
- `vcb.chapter.vibe_coder_advantage_and_risk`
- `vcb.chapter.codex_surfaces`

**Explicit non-scope:** setup/config, sandbox/approvals, Git discipline, deep prompting chapters, workflow playbooks, full Codex feature topic cards, pricing snapshots, tool catalog recommendations, and shortcut cards beyond register references.

**Revision scope:** repository hygiene only. This revision fixes namespace routing, evidence taxonomy wording, synthesis namespace declaration, Chapter 2 evidence metadata, and validation language. No Chunk 3 material was authored. One existing active Chunk 1 concept card (`vcb.concepts.blast_radius`) received evidence-metadata/source-hygiene cleanup only, because the restored E3 taxonomy would otherwise leave a stale evidence label.

## Canonical Review Package

Canonical review package: one timestamped authoritative zip.

Package filename:

```text
vibe-coding-bible-chunk-2-revision-20260608T141440Z-authoritative.zip
```

Do not submit older Chunk 0 or Chunk 1 zips or duplicate loose files for editor review.

## Files Created

- `chapters/01-codex-mental-model.md`
- `chapters/02-vibe-coder-advantage-and-risk.md`
- `chapters/03-codex-surfaces.md`
- `CHUNK_2_REPORT.md`

## Files Updated

- `README.md`
- `manifest.json`
- `llms.txt`
- `llms-full.txt`
- `SOURCE_REGISTER.md`
- `PRICING_SNAPSHOT_REGISTER.md`
- `topics/concepts/blast-radius.md`
- `CHANGELOG.md`
- `TREE.txt`
- `indexes/INDEX_BY_TASK.md`
- `indexes/INDEX_BY_CONCEPT.md`
- `indexes/INDEX_BY_CODEX_SURFACE.md`
- `indexes/INDEX_BY_FAILURE_MODE.md`
- `indexes/INDEX_BY_STABILITY.md`
- `indexes/INDEX_BY_BUDGET_PROFILE.md`
- `indexes/INDEX_FOR_AI_COACHES.md`
- `indexes/INDEX_BY_PROJECT_TYPE.md`
- `indexes/INDEX_BY_RECOVERABILITY.md`
- `indexes/INDEX_BY_RISK_LEVEL.md`
- `indexes/GLOSSARY.md`
- `indexes/PROMPT_LIBRARY.md`

## Design Decisions

1. **Chunk 2 stayed scoped.** Only Chapters 1–3 were authored. Setup/config, sandbox/approvals, and Git discipline remain explicitly deferred to Chunk 3.
2. **Chapter 1 frames Codex as an agent loop.** It avoids treating Codex as magic autocomplete and teaches intent, context, plan, patch, verification, review, recovery, and learning.
3. **Chapter 2 preserves vibe-coder speed while adding control.** It treats product instinct and iteration speed as real advantages, while naming the weak points: over-trust, weak tests, vague intent, dependencies, and production-mode confusion.
4. **Chapter 3 uses surface routing, not surface hype.** It chooses App, IDE, CLI, Cloud/Web, GitHub review, and SDK by context location, task length, risk, and attention.
5. **Surface facts are volatile.** Exact UI labels, platform support, plan access, commands, and feature availability are marked volatile and tied to official OpenAI source anchors.
6. **No exact pricing, credits, model limits, or plan quotas were added.** Pricing remains snapshot-only.
7. **Separated maintainer synthesis from evidence levels.** `VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE` is now an `evidence_basis` / `source_kind` marker, not a substitute for `E3_EXPERT_REPORT`.
8. **Corrected pricing namespace routing.** Planned pricing snapshots use `vcb.pricing_snapshot.*`, matching the manifest namespace policy and pricing snapshot register.

## Sources Checked

- `vcb.blueprint.v1` — governing blueprint and Chunk 2 scope.
- `aws.well_architected.design_principles` — official vendor anchor for small reversible changes, blast-radius reduction, and faster reversal framing.
- `openai.codex.overview` — official Codex positioning and high-level capabilities.
- `openai.codex.best_practices` — official context, validation, review, durable guidance, and surface-practice anchor.
- `openai.codex.llms_txt` — official Codex source-map pattern.
- `openai.codex.app` — official app surface anchor.
- `openai.codex.app_features` — official app feature anchor.
- `openai.codex.ide` — official IDE extension surface anchor.
- `openai.codex.cli` — official CLI surface anchor.
- `openai.codex.cloud` — official web/cloud background task anchor.
- `openai.codex.github_review` — official GitHub review integration anchor.
- `openai.codex.sdk` — official SDK/programmatic control anchor.
- `openai.codex.github_action` — official GitHub Action anchor.
- `openai.codex.feature_maturity` — official maturity-label anchor.
- `openai.codex.changelog` — official volatile-surface monitoring anchor.
- `openai.help.truthfulness` — official hallucination/confident-wrong caveat.
- `openai.hallucinations` — official hallucination research framing.

## Validation

```text
Actual source files tracked in manifest: 61
Manifest source-file inventory matches actual package files: yes
Markdown files: 38
Markdown files with YAML frontmatter: 38 / 38
Markdown files with VCB markers: 38 / 38
JSON files: 8
JSON parse check: passed
JSON Schema draft compile check: passed
New chapter files created in Chunk 2: 3
New chapter frontmatter basic validation: passed, 3 / 3
Required Chunk 2 files present: passed
Required chapter sections present: passed
Required VCB markers present in new chapter files: passed
README next-chunk route checked against manifest: passed
Codex surface source anchors checked: passed
Index namespace drift scan covers active and planned index routes: passed
Pricing snapshot route uses canonical `vcb.pricing_snapshot.openai_codex`: passed
E3 evidence definition restored to blueprint meaning: passed
Maintainer synthesis separated from evidence level: passed
`vcb.synthesis.*` declared as non-topic source namespace: passed
Blast-radius concept evidence metadata aligned with restored E3 definition: passed
Canonical review package policy: one timestamped authoritative zip
Report final line: AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
```

Known exception: `.gitkeep` files are structural placeholders and intentionally contain no frontmatter or VCB markers.

## Unresolved Questions

1. Whether Chapter 3 should later be split into individual Codex surface topic cards (`vcb.codex.app`, `vcb.codex.cli`, `vcb.codex.cloud`, etc.) before or after setup/config chapters.
2. Whether `vcb.chapter.vibe_coder_advantage_and_risk` should later get companion failure-mode cards for summary confidence bias, weak tests, and hallucinated APIs.
3. Whether `evidence_basis` / `source_kind` should be added to future schema validation for chapters and topics.
4. Whether `llms-full.txt` should become a generated full concatenation after Chunk 3 or remain a compact source map until a release milestone.

## Next Recommended Chunk

**Chunk 3:**

- Chapter 4 — Installing and Configuring Codex Without Creating a Mess
- Chapter 5 — Sandboxes, Approvals, and Why Full Access Is Usually a Bad Default
- Chapter 6 — Git Discipline for Vibe Coders

Do not start Chunk 3 until the editor returns:

```text
EDITOR_STATUS: APPROVED_FOR_NEXT_CHUNK
```

<!-- VCB:STOP_RETRIEVAL reason="chunk_2_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_2 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
