---
id: vcb.register.pricing_snapshots
title: PRICING_SNAPSHOT_REGISTER
artifact_type: register
version: 1.0.1-postrelease.issue4
status: issue_4_ai_coding_tools_snapshot
created_on: 2026-06-08
last_verified: '2026-06-12'
next_review_due: '2026-07-12'
review_cadence: monthly
---

<!-- VCB:BEGIN_REGISTER id=vcb.register.pricing_snapshots version=1.0.1-postrelease.issue4 -->

# PRICING_SNAPSHOT_REGISTER

**Purpose:** Track dated pricing snapshots. Exact prices, credits, limits, quotas, and plan packaging are not stable guidance.

## Current Snapshot Status

Chunk 12 captured the first exact OpenAI/Codex pricing snapshot. Issue #4 adds a bounded non-OpenAI pricing slice for active AI coding, AI IDE, browser-dev, app-builder, and UI-generation tools. Hosting, database, and observability pricing categories remain deferred.

## Snapshot Files

| Snapshot ID | Snapshot file | Scope | Last checked | Next review | Status |
|---|---|---|---|---|---|
| `vcb.pricing_snapshot.openai_codex` | `pricing-snapshots/2026-06-09-openai-codex.md` | OpenAI / Codex plan, credit, and usage details | 2026-06-09 | 2026-07-09 | active_snapshot |
| `vcb.pricing_snapshot.ai_coding_tools` | `pricing-snapshots/2026-06-12-ai-coding-tools.md` | non-OpenAI active AI coding, AI IDE, browser-dev, app-builder, and UI-generation tools | 2026-06-12 | 2026-07-12 | active_snapshot |
| `vcb.pricing_snapshot.hosting` | `pricing-snapshots/2026-06-08-hosting.md` | hosting/deployment tools | not captured | TBD | deferred |
| `vcb.pricing_snapshot.databases` | `pricing-snapshots/2026-06-08-databases.md` | database/backend tools | not captured | TBD | deferred |
| `vcb.pricing_snapshot.observability` | `pricing-snapshots/2026-06-08-observability.md` | observability/analytics tools | not captured | TBD | deferred |

## Snapshot Rules

- Store exact values only with retrieval date.
- Link official vendor page first.
- State what was not verified.
- Include next review date.
- Keep stable topic cards free of volatile exact pricing.
- Treat exact values in snapshots as stale after their review date.

## Issue #4 Post-Release Pricing Slice Note

This live repository now has 2 active pricing snapshots: `vcb.pricing_snapshot.openai_codex` and `vcb.pricing_snapshot.ai_coding_tools`. This does not mutate the historical Final Release 1 package record, where non-OpenAI exact pricing was deferred. `vcb.pricing_snapshot.openai_codex` is Codex-specific and does not freeze exact ChatGPT plan pricing; ChatGPT plan prices remain uncaptured until a scoped snapshot owns them.

## Chunk 42 Release-Candidate Disposition Note

Chunk 42 does not add pricing snapshots. It confirms the release-candidate disposition: `vcb.pricing_snapshot.openai_codex` remains the only active exact pricing snapshot, and non-OpenAI pricing categories remain deferred documented limitations. Stable prose must continue avoiding exact cross-vendor prices, quotas, credits, plan limits, and package claims unless a future editor-approved pricing-snapshot slice captures them.

## Chunk 41 Finalization Readiness Audit Note

Chunk 41 does not add pricing snapshots. Finalization audit state: 1 active pricing snapshot (`vcb.pricing_snapshot.openai_codex`) and 4 deferred pricing categories (`vcb.pricing_snapshot.ai_coding_tools`, `vcb.pricing_snapshot.hosting`, `vcb.pricing_snapshot.databases`, and `vcb.pricing_snapshot.observability`). Exact cross-vendor cost guidance is not release-ready until scoped pricing snapshots are captured or the release explicitly excludes exact pricing coverage.

<!-- VCB:STOP_RETRIEVAL reason="pricing_snapshot_register_complete" -->
<!-- VCB:END_REGISTER id=vcb.register.pricing_snapshots -->
