<!-- VCB:BEGIN_TOPIC id=vcb.concepts.blast_radius version=0.1.1 -->
---
version: 0.1.1
last_verified: '2026-06-08'
review_cadence: annual
audiences:
- human
- ai_coach
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- Human software work
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
- disposable_prototype
project_phases:
- prototype
- mvp
- production_build
- maintenance
- emergency_hotfix
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.concepts.blast_radius
title: Blast Radius
type: concept
next_review_due: '2027-06-08'
source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
stability:
  principle: CORE_ENGINEERING
  surface: STABLE
  pricing: STABLE
shortcut_profiles:
- vcb.shortcut.broad_agent_permissions
- vcb.shortcut.unattended_long_runs
- vcb.shortcut.accepting_diff_without_review
durable_principles:
- risk is partly about how far damage can spread
- small local work needs lighter guardrails than production systems
- blast radius should set the strictness of the workflow
likely_to_change:
- specific Codex permission modes and sandbox labels
- tool-specific production deployment controls
obsolete_when:
- software work no longer has separable environments, users, data, credentials, or
  deployment boundaries
related_topics:
- vcb.concepts.recoverability
- vcb.concepts.diff
- vcb.concepts.rollback
- vcb.concepts.git_branch
- vcb.concepts.pull_request
- vcb.safety.production_red_lines
---

> Summary:
> Blast radius means how far damage can spread if a change goes wrong. Use it to decide how strict Codex guardrails need to be.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.blast_radius.human -->
## 1. For the Human: Plain-Language Concept

### What this means

**Blast radius** means: how far can damage spread if this goes wrong?

A firecracker in an empty driveway has a small blast radius. A spark in a warehouse full of fuel has a large blast radius.

Code works the same way.

### Why it matters

The same shortcut can be reasonable or reckless depending on blast radius.

Skipping tests on a local color change is not the same as skipping tests on payment logic. Letting Codex work unattended on a throwaway branch is not the same as letting it edit production deployment settings.

### The mental model

Classify the work by what it can touch:

| Blast radius | Examples | Guardrail level |
|---|---|---|
| Small | local file, fake data, prototype branch, CSS tweak | lightweight guardrails |
| Medium | shared repo, internal tool, real but non-sensitive data | branch, checks, review |
| Large | production database, auth, billing, user accounts, secrets, deployment | strong guardrails, review, rollback |
| Severe | real secrets, payment charges, data deletion, regulated data | stop and isolate before proceeding |

### What good looks like

Good use of blast radius sounds like:

```text
This is a local prototype with fake data. We can move fast, but commit first.
```

or:

```text
This touches billing and user data. We need a branch, tests, review, and rollback plan.
```

### What bad looks like

Bad use sounds like:

```text
It is only a small change.
```

Line count is not blast radius. A one-line permission bug can expose private data.

### Minimal example

```diff
- if current_user.id == invoice.owner_id:
+ if current_user:
    show_invoice(invoice)
```

Tiny diff. Large blast radius. It changes who can see invoices.

### Checklist

Ask:

- Could this affect real users?
- Could this touch real data?
- Could this expose or use secrets?
- Could this charge money or block a payment?
- Could this deploy automatically?
- Could this delete, migrate, or corrupt data?
- Could this affect shared teammates or production systems?
<!-- VCB:END_SECTION id=vcb.concepts.blast_radius.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.blast_radius.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Use blast radius to calibrate strictness. Do not over-police low-risk prototypes. Do push hard on production, secrets, money, auth, data deletion, and deployment.

### Diagnose the human’s current model

Ask:

- What environments can this change reach?
- What data can it read or mutate?
- Are real credentials available?
- Is auto-deploy enabled?
- Who suffers if it fails?
- How quickly would the human notice failure?

### Explanation strategy

Start with concrete buckets: local-only, shared/internal, public production, security-sensitive. Then tie each bucket to a guardrail level.

### Useful metaphors

- Firecracker in driveway versus spark in fuel warehouse.
- Sandbox versus live store.
- Toy cash register versus real payment terminal.

### Coaching tactics

If blast radius is small, give the minimum useful guardrail: commit first, keep the diff small, run the app manually.

If blast radius is large, require isolation, branch/worktree, tests, diff review, backup or rollback plan, and no broad permissions with real secrets.

### Prompt patterns

```text
Classify this task by blast radius before editing.
List what files, data, users, credentials, and deployment paths it could affect.
Then propose the minimum guardrails.
```

```text
Move fast, but keep blast radius small.
Use fake data, avoid production config, and do not touch auth, payments, migrations, or secrets.
```

### Red flags to call out directly

- “It is only one line” when the line affects auth, permissions, data, or billing.
- Broad agent permissions on a machine with `.env` files or cloud credentials.
- Auto-deploy from the current branch.
- Codex editing files outside the requested scope.
- Long unattended work on ambiguous production tasks.

### Exercises

Give the human three tasks and ask them to rank blast radius:

1. Change a button color in a branch.
2. Add a database migration for user roles.
3. Update payment webhook validation.

Then ask what guardrail changes between the three.
<!-- VCB:END_SECTION id=vcb.concepts.blast_radius.ai_coach -->

## Shortcut Reality

### The ideal practice

Classify blast radius before giving Codex autonomy or accepting a shortcut.

### What users often do instead

Users classify risk by how easy the change looks, not by what it can damage.

### When the shortcut may be fine

For small local-only work, it may be fine to use lightweight review and manual checks.

### When the shortcut is a bad idea

For production, secrets, auth, payments, migrations, user data, or deployment, shortcuts need stronger guardrails or should stop entirely.

### Risk profile

- Probability of failure: depends on ambiguity and tool autonomy.
- Impact if it fails: determined by blast radius.
- Ease of recovery: improves with branch, Git checkpoint, fake data, staging, backups, and rollback.
- Blast radius: the subject of this topic.
- Skill needed to recover: rises with production state, security exposure, and data mutation.
- Hidden cost: large blast-radius mistakes create cleanup, trust, incident, and support costs.

### Minimum guardrails

- Name the environment: local, branch, staging, production.
- Remove real secrets when possible.
- Use fake data for prototypes.
- Commit before risky work.
- Disable auto-deploy or use a branch.
- Require review for auth, payments, migrations, secrets, and deployment.

### Recovery plan

If blast radius was underestimated, stop the task. Identify affected files, users, data, and credentials. Move to rollback or containment before adding new changes.

### AI coach guidance

Match strictness to blast radius. The right tone is not always “slow down.” It is “move at the speed the blast radius permits.”

## Budget and Constraint Notes

### Cheapest reliable path

Spend one short reasoning pass on blast radius before implementation. This prevents expensive rework.

### Fastest high-usage path

Use agents for implementation and fresh-agent review only after the blast radius is bounded by branch/worktree/isolation.

### Low-attention path

Low-attention work is acceptable only when blast radius is small or the work is isolated and reviewable later.

### Production-quality path

Large blast radius requires tests, review, rollback, monitoring, and a clear deployment path.

## Stable Core

- Risk severity depends on what can be damaged.
- Line count does not determine blast radius.
- Guardrail strictness should scale with blast radius.

## Volatile Surface

- Codex permission modes.
- Cloud/worktree isolation behavior.
- Hosting auto-deploy settings.
- Secret-management tool behavior.

## Obsolescence Watch

Review if Codex permission models or deployment systems materially change how isolated work can be guaranteed.

## Evidence and Sources

- Evidence level: `E0_OFFICIAL_DOCS` for official vendor/OpenAI anchors that support blast-radius reduction through smaller, reversible, constrained changes.
- Evidence basis: `VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE` for the maintainer-authored mapping from blast-radius thinking to vibe-coding guardrails. This synthesis basis is not an evidence level.
- `vcb.blueprint.v1`: governing shortcut and risk taxonomy.
- `aws.well_architected.design_principles`: official AWS Well-Architected anchor for small reversible changes reducing blast radius and improving reversibility.
- `openai.codex.best_practices`: official OpenAI source anchor for constraints, verification, and reusable project guidance.

## Related Topics

- `vcb.concepts.recoverability`
- `vcb.concepts.rollback`
- `vcb.concepts.diff`
- `vcb.concepts.git_branch`
- `vcb.safety.production_red_lines`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.blast_radius -->
