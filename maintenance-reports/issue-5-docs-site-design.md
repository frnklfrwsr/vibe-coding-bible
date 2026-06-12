# Issue #5 Docs Site Design

## Objective

Resolve Issue #5 by adding a minimal human-readable docs site while preserving the GitHub Markdown repository as the canonical VCB source.

## Chosen Site Generator

The docs site uses MkDocs with the built-in `mkdocs` theme.

## Why MkDocs Was Chosen

MkDocs is small, static, Markdown-native, and easy to run in GitHub Actions with Python. The built-in theme avoids heavier styling dependencies and keeps the setup maintainable for a repository whose canonical content already lives as Markdown.

MkDocs Material was not used in Phase 1 because the first site version only needs simple static navigation and GitHub Pages deployment.

## First Version Includes

The first docs-site version includes:

- `mkdocs.yml`;
- `requirements-docs.txt`;
- reader-facing docs pages under `docs/`;
- navigation pages for task, concept, shortcut, tool, field-practice, and release/download entry points;
- an LLM usage guide that points to canonical LLM routing files;
- a GitHub Pages workflow at `.github/workflows/docs-site.yml`;
- this maintenance report.

The docs pages link to canonical repository files instead of duplicating the whole VCB corpus.

## Intentionally Not Included

Phase 1 does not:

- rewrite chapter, topic-card, shortcut-card, tool-card, field-practice, pricing-snapshot, source-register, or index content;
- duplicate the full VCB corpus into a second docs tree;
- generate one monolithic book file;
- alter `VCB:STOP_RETRIEVAL` markers;
- alter topic IDs;
- weaken `llms.txt` or `llms-full.txt`;
- add analytics or tracking;
- create a release.

## Canonical Source Preservation

GitHub remains the canonical source of truth. The docs site is a navigation and publishing layer only.

If a rendered docs page and a canonical repository Markdown file ever disagree, the repository file wins.

## LLM Routing Files

The docs site links to:

- `llms.txt`;
- `llms-full.txt`;
- `manifest.json`;
- `indexes/INDEX_BY_TASK.md`;
- `indexes/INDEX_BY_CONCEPT.md`;
- `indexes/INDEX_FOR_AI_COACHES.md`.

The docs-site change does not alter those files.

## Local Build

Install documentation dependencies outside the repository working tree or in an environment that does not generate committed files:

```powershell
python -m pip install -r requirements-docs.txt
```

Build without committing output:

```powershell
mkdocs build --strict --site-dir C:\path\outside\repo\vcb-docs-site
```

## GitHub Pages Deployment

The workflow `.github/workflows/docs-site.yml` runs on pushes to `main` and through `workflow_dispatch`.

It uses official GitHub Actions:

- `actions/checkout`;
- `actions/setup-python`;
- `actions/configure-pages`;
- `actions/upload-pages-artifact`;
- `actions/deploy-pages`.

The workflow permissions are limited to:

- `contents: read`;
- `pages: write`;
- `id-token: write`.

The workflow installs `requirements-docs.txt`, builds the MkDocs site with `mkdocs build --strict`, uploads the built site as a Pages artifact, and deploys it through GitHub Pages.

## Manual GitHub Pages Settings

After merge, repository maintainers may need to enable GitHub Pages with source set to **GitHub Actions**:

`Settings -> Pages -> Build and deployment -> Source -> GitHub Actions`

If Pages is already configured for GitHub Actions, no additional manual setting should be required.
