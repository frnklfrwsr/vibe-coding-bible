# Lightweight Post-Release Contribution Workflow

Use this workflow when a usage insight, correction, or community observation may help VCB but should not automatically trigger full chunk-style metadata, routing, changelog, validator, and report overhead.

## Contribution intake levels

1. Issue/comment only

   Default for most usage insights. The contribution stays in GitHub issue or comment form, with labels or status only. No repository content changes are required.

2. Maintenance report only

   Use when an observation is useful to preserve but is not ready to become an active retrieval target. The report may summarize triage, evidence posture, and follow-up work. It should not add an active route.

3. Candidate card

   Use only when the observation is distinct, sanitized, reusable, non-duplicative, and worth retrieval. Evidence remains `E4_COMMUNITY_FIELD_REPORT` unless the behavior is reproduced or supported by stronger sources. Candidate cards require minimal routes only.

4. Full chunk-style metadata

   Use only when the change affects active routing, registers, manifest, `TREE.txt`, source register, validator behavior, or public docs. Full chunk-style metadata should not be automatic for every community insight.

## Candidate-card threshold

A candidate card requires all of the following:

- public-safe sanitized issue or contribution text;
- clear reusable workflow or pattern;
- no existing card already covers the same route;
- explicit evidence level;
- no official or reproduced claim unless supported;
- clear affected route surfaces;
- maintainer decision that active retrieval is useful.

## Minimal route rule

A candidate card should start with minimum viable routing:

- `FIELD_PRACTICES.md` or the relevant register;
- one primary LLM route;
- one AI-coach or task-index route if relevant;
- docs or `README.md` only if normal users need discovery.

Broader route, index, changelog, manifest, `TREE.txt`, source-register, or validator updates are added only when required by the repository contract.

## PR #25 lesson

PR #25 was useful because it converted Issue #23 into a sanitized candidate field-practice/workflow-pattern route. It also showed that one usage insight can become too heavy if every observation triggers a full metadata, routing, changelog, report, and validator cascade.

Treat the PR #25 pattern as the exception. The default post-release path is the smallest useful contribution level that preserves privacy, evidence posture, and route quality.

## Maintainer checklist

- Does this observation need active retrieval, or is an issue/comment enough?
- Would a maintenance report preserve the lesson without adding route surface?
- If a candidate card is proposed, does it pass every threshold above?
- Are route updates limited to the smallest files that real users or AI coaches need?
- Is any full chunk-style metadata justified by a concrete repository contract?

<!-- VCB:STOP_RETRIEVAL reason="post_release_contribution_workflow_complete" -->
