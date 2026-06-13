<!-- VCB:BEGIN_TOPIC id=vcb.field.contract_first_segmented_handoffs version=1.0.1-post-release.issue23 -->
---
version: 1.0.1-post-release.issue23
last_verified: '2026-06-12'
last_reviewed: '2026-06-12'
audiences:
- human
- ai_coach
source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: true
  speculative: false
evidence_level: E4_COMMUNITY_FIELD_REPORT
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: community_field_report
evidence_scope: candidate field-practice card based on one sanitized public usage insight; official sources support related product behavior or engineering principles only
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
- mvp
- production_build
- maintenance
- major_refactor
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
id: vcb.field.contract_first_segmented_handoffs
title: Contract-First Segmented Handoffs
type: field_practice
status: active
field_practice_status: candidate
status_reason: 'Issue #23 is a single sanitized usage insight; useful enough to route, not enough to reproduce or promote.'
officially_endorsed: 'false'
review_cadence: monthly
next_review_due: '2026-07-12'
applies_to:
- Codex field practice
- AI-assisted software development
- planning-to-implementation handoff
- long-running bounded work
stability:
  principle: COMMUNITY_HACK
  surface: MODERATE
  pricing: STABLE
shortcut_profiles:
- vcb.shortcut.vague_prompt
- vcb.shortcut.one_big_prompt
- vcb.shortcut.skipping_plan
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.consensus_as_correctness
- vcb.shortcut.subagent_swarm
durable_principles:
- Codex should receive an already-reconciled implementation contract, not a pile of exploratory material it must infer from.
- Segmenting long work into one active contract package at a time keeps review, tests, and ownership bounded.
- Evidence labels must travel with unofficial practices until they are reproduced, promoted, or retired.
likely_to_change:
- Codex planning behavior, subagent behavior, review surfaces, context handling, and local project tooling
obsolete_when:
- Codex reliably reconciles planning inputs, contracts, tests, and review threads without explicit segmented handoff packages.
related_topics:
- vcb.field.chatgpt_pm_codex_implementer
- vcb.field.fresh_agent_review
- vcb.field.strict_typecheck_lint_gates
- vcb.field.multi_agent_review_consensus
- vcb.workflow.feature_slicing
- vcb.prompting.acceptance_criteria
- vcb.workflow.reviewing_diffs
- vcb.failure.done_claim_without_evidence
---

# Contract-First Segmented Handoffs

> Summary:
> Candidate field practice: Before Codex implements, have a planning or PM layer turn research into one explicit segment contract at a time, including inputs, outputs, tests, risks, and forbidden behavior. This card is based on one sanitized public usage insight. It is not official guidance, not reproduced, and not promoted.

## Quick Navigation

- 1. For the Human: Plain-Language Concept
- 2. For the AI Coach: How to Teach This to Your Human
- Shortcut Reality
- Budget and Constraint Notes
- Stable Core
- Volatile Surface
- Obsolescence Watch
- Evidence and Sources
- Related Topics

<!-- VCB:BEGIN_SECTION id=vcb.field.contract_first_segmented_handoffs.human -->
## 1. For the Human: Plain-Language Concept

### What this practice is

For long or ambiguous Codex work, do not hand Codex a broad goal plus research notes and ask it to figure out the contract. First, have a planning layer reconcile the options and write one segment package. Codex then implements only that active segment.

### Evidence status

This is a candidate field-practice card based on one sanitized public usage insight, Issue #23. It is `E4_COMMUNITY_FIELD_REPORT` evidence only. It is not official guidance, not reproduced locally, and not promoted.

### Why people try it

People try it when a long run keeps producing review churn because Codex has to infer field contracts, input/output rules, or test expectations from prose, exploratory patches, or contradictory drafts.

### What good looks like

Good: Codex receives a segment brief with explicit field contracts, accepted and rejected design choices, a negative-test matrix, risk notes, preflight checks, and a self-audit checklist. Raw exploratory drafts stay outside the active segment unless the PM layer explicitly promotes them into the controlling contract.

### What bad looks like

Bad: Codex receives research output and reference patches, then is expected to choose the contract, reconcile alternatives, format data, infer tests, and implement safely in one pass.

### When it may help

- Long bounded runs split into multiple PRs.
- Multi-agent research where one owner must reconcile source-agent outputs.
- Data-shape, API, migration, or workflow changes where field contracts matter.
- Review churn where repeated findings point to unclear contracts rather than isolated bugs.

### When it is overkill

- Tiny copy edits or one-file fixes.
- Throwaway prototypes with no persistent data or user-facing risk.
- Tasks where the contract is already obvious from tests, types, or existing code.
- Work where creating the package costs more than reviewing the diff.

### Minimum viable version

For a small task, write only:

- segment goal;
- files or folder in scope;
- input and output contract;
- done-when evidence;
- forbidden behavior;
- one negative test or failure case;
- review command or check.

### Segment package checklist

Before Codex receives a segment package:

- all source-agent outputs have been reconciled by one PM or owner layer;
- the active segment contains the contract, risk notes, preflight checks, and self-audit;
- raw exploratory patches are excluded unless explicitly promoted;
- each meaningful field has type, allowed values, derivation, validation, fail-closed behavior, and negative tests;
- forbidden behaviors have structural tests or guards where feasible;
- the changelog explains which package version supersedes earlier versions;
- Codex is told to open only one segment until the current PR is clean and merged.

### Anti-pattern

Do not ask Codex to infer the contract. The planning layer should solve ambiguity before Codex mutates the repository.

<!-- VCB:END_SECTION id=vcb.field.contract_first_segmented_handoffs.human -->

<!-- VCB:BEGIN_SECTION id=vcb.field.contract_first_segmented_handoffs.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach this as an evaluation candidate for reducing ambiguity before mutation. Keep the evidence label visible and avoid turning one successful report into a default rule.

### Diagnostic questions

- Is the task long enough or ambiguous enough to justify a segment package?
- What exact contract would Codex otherwise have to infer?
- Which decisions belong to a planning/PM layer before implementation starts?
- What source-agent outputs are exploratory only?
- What tests or guards make forbidden behavior structurally hard?
- What would count as evidence that review churn decreased?

### Coaching tactics

- Ask the planning layer to choose one design and document rejected alternatives.
- Convert prose into field, input, output, validation, and failure contracts.
- Keep only one active segment in Codex context.
- Tie each segment to a PR-sized diff, checks, and review evidence.
- Treat repeated review comments as a possible contract mismatch.

### Prompt pattern

```text
You are a planning/contract agent, not Codex.
Resolve ambiguity before implementation.
Choose one design and list rejected alternatives.
Produce one segment package with:
- goal
- files in scope
- input/output contracts
- field rules
- negative tests
- forbidden behavior
- preflight checks
- self-audit
Codex should receive an already-solved contract, not a puzzle.
```

### Red flags

- "Codex can decide the contract from the examples."
- Raw research notes and reference patches are mixed into the active implementation folder.
- Multiple agents produce unreconciled alternatives and Codex is asked to merge them mentally.
- The package lacks negative tests for forbidden behavior.
- Review churn repeats around the same field, format, or boundary.

<!-- VCB:END_SECTION id=vcb.field.contract_first_segmented_handoffs.ai_coach -->

## Shortcut Reality

### Ideal practice

Separate planning, contract reconciliation, implementation, and verification. Codex should implement a bounded contract, then prove it with checks and review artifacts.

### What people often do instead

They use planning agents to produce more material, not clearer decisions. Codex then burns context and review cycles reconciling ambiguity that should have been resolved before implementation.

### When the shortcut may be acceptable

It may be acceptable to use a lightweight version for a medium-risk segment when the contract has real ambiguity and review cost is meaningful.

### When it becomes a bad trade

It becomes a bad trade when packaging turns into process theater, when it hides unresolved disagreement, or when a single successful report is promoted into mandatory ceremony for all tasks.

### Risk profile

- Probability: medium until a project has local evidence.
- Impact: low for small reversible segments; high when used to justify long autonomous mutation or production changes.
- Recoverability: medium if each segment maps to one branch/PR; low if multiple segments merge without fresh review.

### Blast radius

The blast radius is the active segment, its branch or PR, the tests/guards it changes, and any downstream packages that rely on the same contract assumptions.

### Minimum guardrails

- one active segment at a time
- visible `candidate` and `E4_COMMUNITY_FIELD_REPORT` label
- explicit owner for contract choices
- raw exploratory material excluded from active context
- checks and review evidence before merge

### Recovery plan

Pause implementation. Extract the repeated review finding, rewrite the segment contract, mark the superseded package, rerun preflight checks, and continue only after the active contract is unambiguous.

## Budget and Constraint Notes

### Cheapest reliable path

Use the minimum viable segment package. Do not create a full folder hierarchy if a short contract table and negative-test list will control the risk.

### Fastest high-usage path

Segment packaging may save review time in long runs, but only if each segment is independent enough to merge cleanly. Parallel agents should inspect bounded questions, not create unreconciled implementation plans.

### Low-attention path

Use this only when the segment package makes review easier later: short scope, clear forbidden behavior, and exact checks. Low attention is not permission for Codex to infer missing contracts.

### Production-quality path

Production use needs explicit contracts, negative tests or guards, fresh CI, fresh review, resolved/outdated/non-actionable review threads, and live base-state checks before merge.

### Prototype versus production

Prototype use can stay lightweight. Production, maintenance, data-shape, auth, payment, or migration work needs stronger contract and rollback evidence.

### Build versus maintenance

During build, the pattern can reduce design drift. During maintenance, it must preserve compatibility, existing behavior, and user data expectations.

## Stable Core

- Implementation quality improves when ambiguous contracts are resolved before mutation.
- One segment at a time keeps review, tests, and recovery bounded.
- Negative tests and guards are stronger than prose-only forbidden behavior.
- Field practices need explicit evidence labels and local fit checks.

## Volatile Surface

- Codex planning ability, context handling, subagent behavior, and GitHub Review behavior may change.
- The usefulness of segment packages depends on project size, review budget, team skill, test reliability, and data-contract risk.
- Exact folder names, package templates, CI requirements, and review-thread mechanics are project-specific.

## Obsolescence Watch

Review this card monthly. Retire, narrow, or rewrite it when:

- Codex reliably reconciles planning inputs, contracts, tests, and review threads without explicit segmented handoff packages;
- the practice creates more package overhead than review-churn reduction;
- a project has tests/types strong enough that separate segment contracts add little value;
- multiple independent reports or local trials contradict the current guidance.

## Evidence and Sources

Evidence level for the practice ritual: `E4_COMMUNITY_FIELD_REPORT`. Source: `vcb.usage_insight.issue_23_contract_first_segmented_handoffs`.

This card is based on one sanitized public usage insight. It must not be presented as official guidance, reproduced locally, or promoted. Stronger evidence would require controlled local trials or additional independent reports.

Source anchors and principle support:

- `vcb.usage_insight.issue_23_contract_first_segmented_handoffs`
- `openai.codex.best_practices`
- `openai.codex.prompting`
- `openai.codex.workflows`
- `openai.codex.use_cases.follow_goals`

Notes:

- Official sources support nearby product mechanics and engineering principles, not the exact field-practice ritual.
- Maintainer synthesis supplies the control-loop framing, not external proof.
- Promotion requires the local evidence rule stated in the field-practice register.

## Related Topics

- `vcb.field.chatgpt_pm_codex_implementer`
- `vcb.field.fresh_agent_review`
- `vcb.field.strict_typecheck_lint_gates`
- `vcb.field.multi_agent_review_consensus`
- `vcb.workflow.feature_slicing`
- `vcb.prompting.acceptance_criteria`
- `vcb.workflow.reviewing_diffs`
- `vcb.failure.done_claim_without_evidence`
- `vcb.shortcut.vague_prompt`
- `vcb.shortcut.one_big_prompt`
- `vcb.shortcut.skipping_plan`
- `vcb.shortcut.accepting_diff_without_review`

<!-- VCB:STOP_RETRIEVAL reason="field_practice_card_complete" -->
<!-- VCB:END_TOPIC id=vcb.field.contract_first_segmented_handoffs -->
