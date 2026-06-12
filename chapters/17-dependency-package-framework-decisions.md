<!-- VCB:BEGIN_TOPIC id=vcb.chapter.dependency_package_framework_decisions version=0.1.0 -->
---
id: vcb.chapter.dependency_package_framework_decisions
title: "Chapter 17 — Dependency, Package, and Framework Decisions"
type: chapter
chapter_number: 17
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-09-08'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- package managers
- dependency review
- supply-chain security
- framework selection

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
  surface: MODERATE
  pricing: STABLE

budget_profiles:
- plus_constrained
- pro_high_throughput
- api_pay_as_you_go
- team_shared_budget

cost_postures:
- cheapest_reliable
- balanced
- fastest_possible
- unattended_high_throughput
- production_quality
- disposable_prototype

project_phases:
- prototype
- mvp
- production_build
- maintenance
- major_refactor
- emergency_hotfix

attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation

shortcut_profiles:
- vcb.shortcut.adding_dependencies_fast
- vcb.shortcut.framework_churn
- vcb.shortcut.ignoring_lint_typecheck
- vcb.shortcut.unofficial_tools

durable_principles:
- Dependencies add capability, but also security, maintenance, bundle, license, and debugging cost.
- Ask for a no-new-dependency solution before adding a package.
- Framework decisions are architecture decisions, not convenience edits.
- Dependency changes need review, lockfile awareness, and rollback paths.

likely_to_change:
- package ecosystem health
- known vulnerabilities and advisories
- package-manager behavior
- framework recommendations
- Codex dependency-management capabilities
- GitHub dependency review and Dependabot feature details

obsolete_when:
- Codex can reliably evaluate package health, license, security, bundle/runtime impact, and migration cost without explicit review.
- The package ecosystem or project toolchain makes manual dependency review unnecessary for the targeted project class.

related_topics:
- vcb.chapter.acceptance_criteria
- vcb.chapter.git_discipline
- vcb.chapter.refactoring_without_breaking_everything
- vcb.chapter.writing_updating_tests
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.workflow.dependency_decisions
- vcb.failure.dependency_bloat
- vcb.tool_catalog.stack_recipes
---

> Summary:
> A dependency is not free code. It is code you now rely on, update, secure, debug, and explain. Codex should justify dependencies before adding them.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.dependency_package_framework_decisions.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A dependency is a package, library, framework, or external service your app relies on.

Dependencies can save huge time. They can also create hidden cost:

- security vulnerabilities,
- broken installs,
- bigger bundles,
- license problems,
- abandoned packages,
- confusing APIs,
- hard migrations,
- version conflicts,
- production outages.

Codex often reaches for packages because packages make implementation easier. That can be rational for a prototype. It can be expensive in a real product.

### The core rule

```text
Ask for the no-new-dependency solution first.
```

If the no-dependency solution is ugly, fragile, or expensive, then consider a package. But make the tradeoff explicit.

### Dependency decision ladder

Use this ladder before adding a package:

1. Can existing code solve it?
2. Can the standard library or framework solve it?
3. Is an existing project dependency already available?
4. Is a small local helper safer than a package?
5. Is a new dev-only dependency enough?
6. Does a new production dependency justify its cost?
7. Is this actually a framework or architecture decision?

A framework decision is bigger than a package decision. Choosing auth, ORM, database, state management, build tool, or UI framework can shape the whole app.

### What to check before adding a package

Ask Codex to inspect:

| Check | Why it matters |
|---|---|
| Purpose | Does it solve the exact problem or just feel convenient? |
| Existing alternatives | Is the project already using something similar? |
| Maintenance health | Is it active enough for your risk level? |
| Security | Are there known vulnerabilities? |
| License | Can the project legally use it? |
| Bundle/runtime cost | Does it slow frontend or server startup? |
| Native dependencies | Will install/build become harder? |
| Transitive dependencies | What extra packages come with it? |
| Lockfile diff | Did the package manager add a large dependency tree? |
| Migration cost | How hard is it to remove later? |

### Good dependency prompt

```text
Before adding any dependency, propose a no-new-dependency solution.

If you still recommend a package, justify it with:
- why existing code/framework utilities are insufficient,
- package name and purpose,
- whether it is production or dev-only,
- install command using this repo's package manager,
- files changed including lockfile,
- security/license/bundle/runtime risks,
- rollback plan.

Do not install until I approve.
```

### Framework decision prompt

```text
Plan only. Do not install or migrate.

We are considering [framework/package].
Compare:
1. keep current stack,
2. add this dependency,
3. choose a different option,
4. write a small local implementation.

For each option, include:
- setup cost,
- maintenance cost,
- security risk,
- lock-in risk,
- migration cost,
- how Codex would verify it,
- when this choice becomes regrettable.
```

### Lockfiles matter

A lockfile records the exact dependency tree installed by the package manager. If Codex changes a dependency, review both the manifest and the lockfile.

For JavaScript projects, dependency changes often touch `package.json` and a lockfile such as `package-lock.json`, `pnpm-lock.yaml`, or `yarn.lock`.

Do not accept a dependency diff by only reading the top-level package name. The real blast radius may be in the transitive tree.

### Good dependency change looks like

Good:

- no-new-dependency option considered first,
- one package added for a clear reason,
- existing package manager used,
- package placed in production or dev dependency correctly,
- lockfile included,
- tests/build run,
- security review considered,
- rollback is simple.

Bad:

- package added without asking,
- duplicate library added when one exists,
- framework migration mixed into a feature,
- lockfile ignored,
- vulnerabilities dismissed,
- dependency added to production when dev-only would work,
- bundle/runtime impact not considered.

### Checklist

Before accepting a package or framework change, ask:

- Did Codex try no-new-dependency first?
- Is this a production dependency or dev dependency?
- Did it use the repo’s package manager?
- Did lockfiles change?
- Did tests/build/lint still pass?
- Does this touch auth, payments, secrets, file upload, or deployment?
- Is the package maintained and compatible?
- Can I remove it later if I regret this?

<!-- VCB:END_SECTION id=vcb.chapter.dependency_package_framework_decisions.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.dependency_package_framework_decisions.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that dependency choices are cost/risk choices, not just code shortcuts. The AI coach should make Codex justify new packages and separate prototype convenience from production liability.

### Diagnose the human’s current model

Ask:

- Is the user trying to save time in a disposable prototype or shipping durable production code?
- Is Codex adding a package because the problem is hard, or because it is a common pattern?
- Is the package already present in the repo?
- Does the change affect auth, payments, secrets, build tooling, deployment, or database access?
- Is this a small package, a framework decision, or a stack migration?

### Explanation strategy

Use this framing:

```text
A dependency is a tiny vendor relationship. Even if it is free, you now depend on its updates, security, install behavior, and future compatibility.
```

Then require the decision ladder: no-new-dependency first, existing project dependency second, new dependency only with justification.

### Useful metaphors

- **Dependencies are roommates.** They help with chores, but they bring habits, mess, and obligations.
- **A framework is a foundation.** Do not swap foundations while painting a room.
- **The lockfile is the guest list.** It shows everyone who came in with the package.

### Coaching tactics

When the user wants to add a package quickly:

```text
For a prototype, that can be acceptable. The safer minimum is to isolate it on a branch, inspect the lockfile, run build/test, and record why this package can be removed later.
```

When the work is production-sensitive:

```text
Do not let Codex install yet. Ask for a package decision memo and no-new-dependency alternative first.
```

When Codex proposes a framework migration:

```text
That is not a small implementation detail. Treat it as architecture work: plan, spike, compare options, and migrate only as a separate project.
```

### Prompt patterns

#### No-new-dependency first

```text
Solve this without adding dependencies if feasible.
If you think a dependency is justified, stop and explain the tradeoff before installing anything.
```

#### Dependency review prompt

```text
Review this dependency diff.
Flag:
- new production dependencies,
- duplicate libraries,
- large transitive changes,
- lockfile surprises,
- license or security concerns,
- build/runtime risk,
- auth/payment/secret impact,
- rollback complexity.
```

#### Framework decision memo

```text
Create a framework decision memo. Do not edit code.
Include the current stack, proposed stack, migration cost, lock-in risk, maintenance burden, verification plan, and exit strategy.
```

### Red flags to call out directly

- New package added without approval.
- Package added for a few lines of code.
- Multiple libraries doing the same job.
- Framework migration hidden inside a feature.
- Lockfile diff is large and unreviewed.
- Production dependency used for test-only tooling.
- Security or license check skipped on production code.
- Codex claims “small change” while changing package manager or build tool.

### Exercises

1. Ask the human to classify a package as dev-only, production, framework, or service dependency.
2. Review a lockfile diff and explain why the top-level package name is not the full story.
3. Turn “install a library for this” into a no-new-dependency-first prompt.

<!-- VCB:END_SECTION id=vcb.chapter.dependency_package_framework_decisions.ai_coach -->

## Shortcut Reality

### The ideal practice

Use existing project capabilities first. Add packages only after a short decision review, security/license check where relevant, lockfile review, and verification.

### What users often do instead

They let Codex install a package because it makes the immediate code easier. They may not review the lockfile, transitive dependencies, license, bundle cost, or future migration cost.

### When the shortcut may be fine

Adding dependencies fast may be acceptable for:

- disposable demos,
- hackathon projects,
- local-only scripts,
- design prototypes,
- isolated spikes,
- fake-data experiments.

### When the shortcut is a bad idea

Do not rush dependency/framework choices for:

- auth,
- payments,
- secrets,
- cryptography,
- database migrations,
- deployment/build tooling,
- file uploads,
- production observability,
- user data handling,
- enterprise or regulated systems.

### Risk profile

- Probability of failure: low/medium for simple packages; high for framework or build-tool changes.
- Impact if it fails: low in prototypes; high when it affects production runtime, security, build, or deployment.
- Ease of recovery: medium if isolated; low if a framework migration spreads across the app.
- Blast radius: small for dev-only tooling; large for framework/runtime dependencies.
- Skill needed to recover: medium/high for package conflicts, native builds, or migrations.
- Hidden cost: ongoing updates, vulnerability triage, debugging, and lock-in.

### Minimum guardrails

- Ask for no-new-dependency solution first.
- Require approval before install.
- Use the project’s package manager.
- Review manifest and lockfile.
- Classify production vs dev dependency.
- Run build/test/lint.
- Avoid framework changes inside feature work.
- Record rollback plan.

### Recovery plan

If a dependency change goes wrong:

1. Inspect manifest and lockfile diff.
2. Revert dependency files first if the feature can survive without the package.
3. Clear installed artifacts if needed.
4. Run install/build/test from a clean state.
5. Retry with no-new-dependency solution or isolated spike.

### AI coach guidance

Do not reflexively reject packages. Reject unexplained packages. A good package can be the right trade. An unreviewed package is hidden architecture.

## Budget and Constraint Notes

### Cheapest reliable path

Prefer existing code, standard library/framework utilities, and small local helpers. Avoid exploratory package installs that burn time debugging toolchain issues.

### Fastest high-usage path

Use parallel comparison branches for competing approaches only when isolated. Pick one after reviewing dependency footprint and verification results.

### Low-attention path

Low-attention dependency changes are risky. Codex must return a dependency decision memo, manifest/lockfile changes, checks run, and rollback plan. Do not let it migrate frameworks unattended.

### Production-quality path

Require no-new-dependency attempt, package justification, security/license review where applicable, lockfile review, tests/build/lint, and separate architecture review for framework changes.

## Stable Core

- Dependencies add cost and risk even when price is zero.
- Existing stack and standard tools should be checked first.
- Lockfiles are part of the review surface.
- Framework changes are architecture decisions.
- Production dependency changes need stronger review than prototype shortcuts.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
- current package security advisories,
- package manager behavior,
- framework ecosystem health,
- GitHub dependency review and Dependabot feature details,
- OpenSSF/package-health scoring tools,
- Codex package-install and cloud-environment behavior.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when:

- major package-manager behavior changes,
- dependency review tools change materially,
- a package ecosystem changes its dominant framework recommendations,
- official Codex guidance adds native dependency review or package-health checks,
- supply-chain threat patterns change.

## Evidence and Sources

- Official OpenAI AGENTS.md guidance includes reusable project preferences such as asking for confirmation before adding new production dependencies: `openai.codex.agents_md`.
- Official npm docs define package dependencies/devDependencies, package-lock behavior, and security audits: `npm.docs.package_json`, `npm.docs.package_lock`, `npm.docs.security_audit`.
- Official GitHub docs support dependency alerts, dependency graph/review, and pull-request dependency-change review: `github.docs.dependabot_alerts`, `github.docs.dependency_graph`, `github.docs.dependency_review`.
- The no-new-dependency-first decision ladder and framework-as-architecture framing are maintainer synthesis from stable engineering practice: `vcb.synthesis.stable_engineering_practice`.

## Related Topics

- `vcb.chapter.acceptance_criteria`
- `vcb.chapter.git_discipline`
- `vcb.chapter.refactoring_without_breaking_everything`
- `vcb.chapter.writing_updating_tests`
- `vcb.concepts.blast_radius`
- `vcb.concepts.recoverability`
- `vcb.workflow.dependency_decisions`
- `vcb.failure.dependency_bloat`
- `vcb.tool_catalog.stack_recipes`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.dependency_package_framework_decisions -->
