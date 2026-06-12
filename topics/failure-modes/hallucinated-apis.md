<!-- VCB:BEGIN_TOPIC id=vcb.failure.hallucinated_apis version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
audiences:
- human
- ai_coach
source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: official OpenAI/Codex anchors, relevant vendor or named expert anchors
  where cited, and VCB maintainer synthesis for failure-mode control loops
budget_profiles:
- plus_constrained
- pro_high_throughput
- api_pay_as_you_go
- team_shared_budget
cost_postures:
- cheapest_reliable
- balanced
- fastest_possible
- production_quality
project_phases:
- prototype
- mvp
- production_build
- maintenance
- major_refactor
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.failure.hallucinated_apis
title: Hallucinated APIs and Fake Interfaces
type: failure_mode
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- API integrations
- Generated clients
- Typed codebases
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.vague_prompt
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.skipping_tests
- vcb.shortcut.ignoring_lint_typecheck
durable_principles:
- an API is a contract, not a naming guess
- real contracts must be found or created before callers depend on them
- mocks must mirror the real contract
likely_to_change:
- Codex contract-discovery features
- vendor APIs and SDK versions
- generated-client tooling
- package flags and options
- typechecker behavior
obsolete_when:
- agents can prove a called API exists and matches runtime behavior across local and
  external contracts without human review
related_topics:
- vcb.concepts.api_basics
- vcb.workflow.feature_slicing
- vcb.workflow.testing
- vcb.workflow.reviewing_diffs
- vcb.failure.done_claim_without_evidence
---

> Summary:
> Hallucinated APIs happen when Codex invents routes, methods, fields, packages, flags, callbacks, or response shapes that sound plausible but are not real in the target project or vendor contract.

## Quick Navigation
- For the Human
- For the AI Coach
- Shortcut Reality
- Budget and Constraint Notes
- Stable Core
- Volatile Surface
- Obsolescence Watch
- Evidence and Sources
- Related Topics

<!-- VCB:BEGIN_SECTION id=vcb.failure.hallucinated_apis.human -->
## 1. For the Human: Plain-Language Concept

### What this means

An API is a contract: this input means this behavior and this output. A hallucinated API is a fake contract. The code may look professional, but it calls something that does not exist, passes a field the server ignores, or assumes a response shape the real service never returns.

### Why it matters

This failure is common because software has many repeated naming patterns. Codex can infer a plausible name from nearby code, package conventions, or public examples. Plausible is not the same as real. The cure is to make the actual contract visible and then verify against it.

### The mental model

Treat every new API call like a key in a lock. The key shape must match the actual lock, not the lock Codex imagined.

### What good looks like

Good: “Before editing, find the real client method, route definition, generated type, or vendor doc. If it does not exist, stop and report options.”

### What bad looks like

Bad: “Use the billing API to add subscriptions” when no billing client, route, schema, or test fixture has been inspected.

### Minimal example

Ask Codex to name the evidence it used, the assumption it is making, the files it changed, and the verification that would catch this failure mode if it were wrong.

### Checklist

- real route/client/function located
- request and response shapes verified
- generated types or schemas reused
- no invented package, option, or flag
- test covers the contract boundary
<!-- VCB:END_SECTION id=vcb.failure.hallucinated_apis.human -->

<!-- VCB:BEGIN_SECTION id=vcb.failure.hallucinated_apis.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to separate plausible code from contract-backed code.

### Diagnose the human’s current model

- Where is the real contract defined?
- Which file proves the method or route exists?
- What type, schema, fixture, or test proves the response shape?
- Did Codex add a package or flag because it exists, or because it sounds conventional?
- What would fail first if this API is fake?

### Explanation strategy

Force a contract-finding pass before implementation. Ask Codex to cite local definitions, generated clients, OpenAPI/schema files, examples, or official vendor docs before it writes code. If the contract is absent, the correct output is a plan, not invented glue.

### Useful metaphor

Treat every new API call like a key in a lock. The key shape must match the actual lock, not the lock Codex imagined.

### Coaching tactics

- slow the human down at the first unsupported assumption
- ask for artifact-backed evidence instead of a verbal assurance
- separate read-only diagnosis from mutation
- require a smaller diff when review quality drops
- turn repeated misses into durable guidance only after the pattern is verified

### Prompt patterns

```text
Plan first. Find the real API contract for [task]. Cite exact files, route definitions, generated types, package docs, or tests. Do not invent methods, fields, config flags, or response shapes. If the contract is missing, stop and propose the smallest way to discover or create it safely.
```

### Red flags to call out directly

- method name appears only in the new diff
- new optional field has no schema owner
- Codex imports a package that was not already used
- test mocks the invented shape instead of the real contract
- the implementation compiles only because everything is typed as any

### Exercises

- Ask the human to mark every new external call in a diff and point to the source that proves it exists.
- Ask the human to write one “stop condition” that would make Codex pause instead of pushing through.
- Review a previous agent diff and classify which evidence was missing.
<!-- VCB:END_SECTION id=vcb.failure.hallucinated_apis.ai_coach -->

## Shortcut Reality

### The ideal practice

Inspect the real contract, reuse existing types or generated clients, and run the smallest contract-level test.

### What users often do instead

Users accept plausible code because it names things the way they would have named them.

### When the shortcut may be fine

For a throwaway prototype with fake data, a placeholder interface is acceptable if it is named as fake and isolated.

### When the shortcut is a bad idea

It is a bad trade for payments, auth, data writes, external integrations, generated clients, or production APIs.

### Risk profile

- Probability of failure: Medium-high when the API is undocumented, loosely typed, or unfamiliar.
- Impact if it fails: High when fake contracts reach production paths or hide behind mocks.
- Ease of recovery: Good if caught at compile/test time; poor if mocks and UI flows validate the same fake assumption.
- Blast radius: Every caller relying on the invented contract, plus downstream data, billing, auth, or state transitions.
- Skill needed to recover: Medium for local APIs; high for third-party integrations and generated clients.
- Hidden cost: Fake tests, wasted debugging, brittle adapters, and false confidence in integrations.

### Minimum guardrails

- contract-finding pass
- schema/type reuse
- no invented fields
- contract test or integration check
- human review of external calls

### Recovery plan

- Stop adding callers.
- Search for every use of the fake method/field.
- Replace mocks with real fixtures or schemas.
- Patch the contract boundary first.
- Add a regression test proving the real shape.

## Budget and Constraint Notes

### Cheapest reliable path

Use local search, existing generated types, and one boundary test before spending more model time on implementation.

### Fastest high-usage path

High-throughput users can run one read-only contract-discovery task and one implementation task, but only after the contract task returns evidence.

### Low-attention path

Low-attention API work should be read-only or branch-isolated until the agent returns exact contract references.

### Production-quality path

Production integrations need contract evidence, typed boundaries, negative-path checks, and rollback.

### Prototype versus production

Prototype placeholders are fine when labeled. Production code must not pretend placeholders are real contracts.

### Maintenance phase

In maintenance, contract drift is a recurring cost. Prefer generated clients, schemas, and contract tests over repeated manual rediscovery.

## Stable Core

- an API is a contract, not a naming guess
- real contracts must be found or created before callers depend on them
- mocks must mirror the real contract

## Volatile Surface

- Codex contract-discovery features
- vendor APIs and SDK versions
- generated-client tooling
- package flags and options
- typechecker behavior

Review volatile details against official sources before freezing commands, UI labels, plan packaging, feature availability, model advice, package metadata, or exact tool behavior.

## Obsolescence Watch

- agents can prove a called API exists and matches runtime behavior across local and external contracts without human review

## Evidence and Sources

- `openai.codex.prompting` — Official OpenAI Codex prompting documentation for context and task framing.
- `openai.codex.workflows` — Official OpenAI Codex workflows guidance for explicit context, done criteria, and verification.
- `mdn.glossary.api` — Official MDN glossary source for API as an interface/contract concept.
- `mdn.learn_web_apis` — Official MDN guide for web API and abstraction framing.
- `typescript.docs.home` — Official TypeScript source for type-checking and typed code evidence.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable failure-mode, risk, review, budget, and recovery discipline.

## Related Topics

- `vcb.concepts.api_basics`
- `vcb.workflow.feature_slicing`
- `vcb.workflow.testing`
- `vcb.workflow.reviewing_diffs`
- `vcb.failure.done_claim_without_evidence`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.failure.hallucinated_apis -->
