# Subagent Delegation Policy

Use this policy when Codex work may benefit from bounded parallel agents.

## When to use subagents

Use subagents when the work splits into independent questions and their findings can be integrated by one parent agent. Prefer read-only analysis before write-capable delegation.

## When not to use subagents

Do not use subagents when one focused pass is enough, when the task is vague, when agents would edit overlapping files, when review capacity is low, or when the work involves secrets, production access, or irreversible actions without a clear gate.

## Suitable tasks

- read-only route audit;
- source/register audit;
- docs/build smoke test;
- Codex Review comment classification;
- PR diff scope check;
- web-user flow dry run.

## Unsuitable tasks

- broad narrative writing;
- unbounded internet research;
- recursive planning;
- authority over final merge;
- secrets or production access.

## Lower-cost model guidance

Use the lowest capable model available for bounded mechanical checks. Do not assume any exact model exists unless it is available in the environment. The parent agent keeps final judgment and remains responsible for synthesis, edits, verification, and public actions.

## Max fanout

Default to 1-3 subagents. The hard cap is 4 unless the user explicitly asks for more.

## Parent responsibilities

The parent agent must:

- define one bounded question per subagent;
- state read-only or write permissions explicitly;
- prevent recursive subagent spawning;
- avoid waiting indefinitely;
- review cited evidence before acting;
- decide final content and edits;
- run validation or build checks;
- own the commit, PR body, and review response;
- stop if subagent findings would expand scope beyond the user's request.

<!-- VCB:STOP_RETRIEVAL reason="subagent_delegation_policy_complete" -->
