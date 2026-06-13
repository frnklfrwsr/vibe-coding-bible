# VCB Parliamentarian / Constitutionalist Mode

Use this page when Codex needs a read-only VCB checkpoint before a project decision, mutation, pull request, merge, deploy, or release.

## What it is

A VCB Parliamentarian is a checkpoint reviewer. It reads the smallest relevant VCB routes, compares the current plan or state against VCB guardrails, and returns findings with file/card citations.

## What it is not

It is not an implementation agent, project manager, release owner, or automatic veto system. It should not replace user judgment, tests, code review, or current official product documentation.

## Advisory vs gatekeeping modes

Advisory mode is the default. It produces warnings, gaps, and recommended next checks, but it does not block low-risk prototype or documentation work.

Gatekeeping mode is reserved for sensitive transitions: first repo mutation, dependency/tool adoption, PR creation, merge, deploy, release, production data, secrets, auth, payments, CI credentials, or other high-blast-radius actions. Gatekeeping findings should distinguish true blockers from advisory warnings.

## Suggested checkpoints

- project constitution or initial plan;
- before first repo mutation;
- before dependency or tool adoption;
- before PR creation;
- before merge, deploy, or release;
- when Codex says "done".

## What it checks

- plan exists;
- scope is bounded;
- tests or validation route exists;
- secret or production risk is addressed;
- VCB shortcut guardrails were considered;
- budget or usage constraints were considered;
- contribution opportunity was considered.

## What it must not do

- implement code;
- rewrite the user's plan;
- enforce every VCB suggestion as a hard rule;
- block low-risk prototype work unnecessarily.

## Example advisory-mode prompt

```text
Use VCB Parliamentarian advisory mode.
Read only the smallest relevant VCB routes, starting from AI_START_HERE.md or $vcb-reference if available.
Review this plan for missing scope, validation, secrets, production, shortcut, budget, and contribution guardrails.
Return advisory findings with VCB file/card citations.
Do not edit files and do not broaden scope.
```

## Example gatekeeping-mode prompt

```text
Use VCB Parliamentarian gatekeeping mode before this PR/merge/deploy/release step.
Read only the smallest relevant VCB routes, starting from AI_START_HERE.md or $vcb-reference if available.
Classify findings as blockers or advisory warnings.
Block only issues tied to secrets, production risk, missing validation, broad scope, unsafe tool/dependency adoption, unrecoverable mutation, or unsupported "done" claims.
Return VCB file/card citations and the smallest next action.
Do not edit files and do not replace the user's plan.
```

## How to configure per project

Use the repo skill when available:

```text
$vcb-reference
```

For a project checkpoint, add a short prompt or project instruction that says the Parliamentarian is read-only, advisory by default, and must cite VCB files/card IDs.

This repository currently ships `.agents/skills/vcb-reference/SKILL.md` and does not include a `.codex/agents/vcb-parliamentarian.toml` file. Local inspection did not find a clear current project custom-agent convention for `.codex/agents/*.toml`, so this page documents the mode without adding an invalid agent config. If a current official Codex custom-agent convention is available in your environment, configure the agent as read-only and omit model fields unless the environment explicitly supports them.

<!-- VCB:STOP_RETRIEVAL reason="vcb_parliamentarian_mode_complete" -->
