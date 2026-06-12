<!-- VCB:BEGIN_REPORT id=vcb.report.chunk_39 version=0.40.0-draft.chunk39 -->
---
id: vcb.report.chunk_39
title: Chunk 39 Report — Field-Practice Evidence and LLM Source-Map Cleanup
artifact_type: chunk_report
version: 0.40.0-draft.chunk39
status: waiting_for_editor_review
chunk_id: chunk_39_field_practice_evidence_and_llm_map_cleanup
last_verified: '2026-06-11'
---

# Chunk 39 Report — Field-Practice Evidence and LLM Source-Map Cleanup

## Scope

Chunk 39 performed bounded repository-contract cleanup after Chunk 38.

In scope:

- field-practice evidence-label hygiene outside the Chunk 38 candidate table;
- Chapter 36 field-practice evidence-scope canonicalization;
- LLM source-map consolidation for generation-specific active tool-card list clutter;
- route clarification where field practice, prototype, production readiness, and tool choice could route either to concept guidance or active tool cards;
- validator checks for the exact cleanup contract.

Out of scope and not started:

- No new field-practice cards;
- No new tool cards;
- No category placeholder cards;
- No pricing snapshots;
- No shortcut-card expansion;
- No broad workflow expansion;
- No broad security/secrets expansion;
- No narrative chapters;
- No promotion, local reproduction, retirement, or expansion of Chunk 38 candidate field practices.

## Files created

- `CHUNK_39_REPORT.md`

## Files updated

- `README.md`
- `manifest.json`
- `llms.txt`
- `llms-full.txt`
- `FIELD_PRACTICES.md`
- `chapters/36-field-notes-unofficial-practices.md`
- `CHANGELOG.md`
- `TREE.txt`
- `scripts/validate_repository.py`

## Cleanup changes

- FIELD_PRACTICES.md evidence shorthand normalized in the status-label and promotion-policy prose.
- Chapter 36 evidence_scope normalized to canonical labels: `E4_COMMUNITY_FIELD_REPORT`, `E2_REPRODUCED_LOCALLY`, and `E3_EXPERT_REPORT`.
- Chapter 36 AI-coach evidence-label prompt now distinguishes `E0_OFFICIAL_DOCS` mechanics/principle support from evidence that would promote a field-practice ritual.
- LLM generation-specific active tool-card lists consolidated by removing `Active Chunk 27` through `Active Chunk 36` tool-card inventory sections from `llms.txt` and `llms-full.txt`.
- LLM maps now point canonical active tool-card inventory lookup to `README.md` / `## Active Tool Cards` and `TOOL_REGISTER.md`.
- LLM routes now clarify field-practice candidate status, prototype/app-builder routing, production-readiness platform evidence, and generic tool-choice routing.

## Evidence and status posture

No field practice was promoted, reproduced, retired, or expanded. All nine Chunk 38 field-practice cards remain active retrieval targets with candidate practice status.

Official docs remain product-mechanics or principle support only unless a later source review establishes that an official source supports the exact practice claim. Community or candidate rituals remain labeled conservatively.

## Validator coverage added

`scripts/validate_repository.py` validator coverage tightened for Chunk 39, including:

- canonical evidence-label checks in `FIELD_PRACTICES.md` status-label and promotion-policy prose;
- rejection of bare evidence shorthand and slash-combined evidence labels in the cleaned field-practice policy sections;
- Chapter 36 `evidence_scope` and AI-coach evidence-label canonicalization checks;
- LLM current-active Chunk 39 phrase checks;
- rejection of generation-specific active tool-card list headings in `llms.txt` and `llms-full.txt`;
- LLM route freshness checks for field-practice candidate status, prototype/app-builder choice, production-readiness tool evidence, and generic tool choice;
- report inventory, package inventory, and scope guardrails.

## Revision notes

- Revised after editor review: stale nested manifest package references repaired in manifest.source_artifacts package_file and review_package.
- Revised after editor review: manifest.validation_expectations current_chunk_scope_boundaries now names Chunk 39 and states the cleanup-only boundary, including no new field-practice cards and no field-practice promotion, reproduction, or retirement.
- Revised after editor review: validator coverage tightened for nested package-reference aliases and current-chunk scope-boundary metadata.

## Validation

Final validator result:

```text
VCB validation passed
active chapter/topic files validated: 230
shortcut IDs registered: 98
tool IDs registered: 46
pricing snapshots active: 1
```

## Package hygiene

Authoritative package:

```text
vibe-coding-bible-chunk-39-revision-20260611T223000Z-authoritative.zip
```

Package hygiene:

```text
zip entries: 320
unique entries: 320
duplicates: 0
directory-only entries: 0
__pycache__ / .pyc entries: 0
files extracted: 320
```

## Notes for editor

Chunk 39 is cleanup-only. It reduces LLM-map tool-card inventory clutter without removing semantic fast routes, and it tightens field-practice evidence taxonomy without changing candidate practice status.

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.report.chunk_39 -->

AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
