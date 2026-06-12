---
id: vcb.protocol.authoring
title: AUTHORING_PROTOCOL
artifact_type: protocol
version: 0.1.1-draft
status: chunk_0_revised
last_verified: 2026-06-08
next_review_due: 2026-07-08
review_cadence: monthly
---

<!-- VCB:BEGIN_PROTOCOL id=vcb.protocol.authoring version=0.1.1-draft -->

# AUTHORING_PROTOCOL

**Purpose:** Define how author agents create The Vibe Coding Bible in controlled, editor-gated chunks.

## Author Role

The author agent writes and updates source files. It does not approve its own work. It must stop at the editor gate after each chunk.

## Required Chunk Loop

1. State the chunk ID and scope.
2. Read the governing blueprint and current repository state.
3. Resolve scope boundaries before writing.
4. Research current facts when needed.
5. Write or update Markdown source.
6. Include required metadata and VCB signposts in every chapter/topic.
7. Update indexes if new topic IDs are added.
8. Update source register if sources are used.
9. Update deprecation/watchlist metadata if relevant.
10. Produce a chunk report.
11. Stop with `AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW`.

## Scope Discipline

Do not write future chunks early.

| Current scope | Allowed | Not allowed |
|---|---|---|
| Chunk 0 | scaffolding, protocols, registers, indexes, schemas | full chapters, full topic cards, pricing snapshots |
| Chunk 1 | Chapter 0 and core concept cards | Codex product surface chapters |
| Tool catalog chunk | tool cards and source/pricing snapshots | uncited vendor claims |
| Field-practice chunk | labeled field-practice cards | presenting anecdotes as official guidance |

## Canonical Topic Namespace Policy

Topic IDs are stable API-like identifiers. Directories may be plural; IDs use the canonical namespace below.

| Canonical namespace | Source path | Use |
|---|---|---|
| `vcb.concepts.*` | `topics/concepts/` | Plain-language software concept cards |
| `vcb.codex.*` | `topics/codex/` | Codex surfaces, features, configuration, and official behavior anchors |
| `vcb.prompting.*` | `topics/prompting/` | Prompt structure, context, constraints, done-when, and cost-aware prompting |
| `vcb.workflow.*` | `topics/workflows/` | Workflows and playbooks. Use singular `workflow` in IDs. |
| `vcb.safety.*` | `topics/safety/` | Sandboxing, permissions, secrets, security review, prompt injection, and production red lines |
| `vcb.shortcut.*` | `topics/shortcuts/` | Individual risk-managed shortcut cards. Use singular `shortcut` in IDs. |
| `vcb.constraints.*` | `topics/constraints/` | Budget, attention, operating mode, phase, and cost constraints |
| `vcb.field.*` | `topics/field-practices/` | Field-practice cards |
| `vcb.tool_catalog.*` | `topics/tool-catalog/` | Tool-category overview topics |
| `vcb.failure.*` | `topics/failure-modes/` | Failure-mode cards |
| `vcb.chapter.*` | `chapters/` | Narrative chapter wrappers |
| `tool.*` | `topics/tool-catalog/` | Individual tool cards |

Reserved non-topic namespaces: `vcb.register.*`, `vcb.protocol.*`, `vcb.index.*`, `vcb.chunk_report.*`, `vcb.pricing_snapshot.*`, `vcb.manifest`, `vcb.llms`, `vcb.llms_full`, and `vcb.repo.*`.

Do not introduce ad hoc roots such as `vcb.review.*`, `vcb.testing.*`, `vcb.git.*`, `vcb.frontend.*`, `vcb.security.*`, `vcb.dependencies.*`, `vcb.automation.*`, or `vcb.shortcuts.*` unless the manifest is changed first and the editor approves the new root. Existing redirects are recorded in `manifest.json`; indexes must use the canonical IDs.

Shortcut cards use:

```yaml
type: shortcut
shortcut_type: risk_managed_shortcut
```

## Topic Authoring Contract

Every chapter/topic must include:

```markdown
<!-- VCB:BEGIN_TOPIC id=... version=... -->
---
id:
title:
type: # concept | codex_feature | workflow | shortcut | field_practice | tool_card | failure_mode | chapter
shortcut_type: # required only when type: shortcut; value: risk_managed_shortcut
version:
last_verified:
next_review_due:
review_cadence:
audiences:
  - human
  - ai_coach
applies_to:
source_status:
evidence_level:
stability:
budget_profiles:
attention_modes:
project_phases:
shortcut_profiles:
durable_principles:
likely_to_change:
obsolete_when:
related_topics:
---
...
<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=... -->
```

## Required Sections for Every Chapter/Topic

- `## 1. For the Human: Plain-Language Concept`
- `## 2. For the AI Coach: How to Teach This to Your Human`
- `## Shortcut Reality`
- `## Budget and Constraint Notes`
- `## Stable Core`
- `## Volatile Surface`
- `## Obsolescence Watch`
- `## Evidence and Sources`
- `## Related Topics`

## Attention / Supervision Modes

Every future chapter/topic must declare at least one `attention_modes` value:

- `continuous_supervision` — the human is watching while Codex works.
- `periodic_check_in` — Codex can proceed in bounded steps, but the human will check at milestones.
- `low_attention_review_later` — Codex may work longer, but the output must be isolated and reviewable.
- `unattended_requires_isolation` — unattended work is acceptable only with branches/worktrees, no secrets, no production access, and a recovery path.

Low-attention work needs narrower scope, stronger isolation, and clearer final reports.

## Style Rules

- Write plainly in human sections.
- Use tactical, technical guidance in AI coach sections.
- Define jargon.
- Use metaphors only when they clarify.
- Do not moralize about shortcuts.
- Prefer harm reduction: tradeoff, blast radius, recoverability, minimum guardrails, and recovery plan.
- Avoid overstuffed cards. Split large topics.
- Favor navigability over linear elegance.

## Source Rules

- Codex/OpenAI facts: official OpenAI first.
- Vendor/tool facts: official vendor first.
- Pricing/limits: dated snapshot only.
- Community practice: label as field report with reproducibility caveat.
- Speculation: label as `E5_SPECULATIVE` and include an obsolescence trigger.

## Author Chunk Report Template

```markdown
# Chunk Report: [chunk_id]

## Scope

## Files Created/Updated

## Design Decisions

## Sources Checked

## Validation

## Unresolved Questions

## Deprecation/Watchlist Updates

## Next Recommended Chunk
```

## Stop Gate

End every chunk with exactly:

```text
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
```

<!-- VCB:STOP_RETRIEVAL reason="authoring_protocol_complete" -->
<!-- VCB:END_PROTOCOL id=vcb.protocol.authoring -->
