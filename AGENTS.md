# Repository Guidelines

## Project Structure & Module Organization

This repository is the documentation and evidence hub for BOPADIGITAL; executable applications live in sibling repositories such as `../bopacorp-api`, `../bopacorp-crm`, and `../bopacorp-web`. Start with `README.md` and `00-architecture/repos-architecture.md`. Requirements live in `02-requirements/`, Scrum records in `03-scrum/`, business references in `04-business/`, and delivery plans and evidence indexes in `06-project2p/`. The canonical report source is `BOPADIGITAL/mainETS_english_se2.tex`; its figures and appendices belong under `BOPADIGITAL/appendices/`. Treat `99-reference-nintventario/` as formatting reference only, not project scope.

## Build, Test, and Development Commands

There is no application build or root test suite in this repository. Use focused document checks:

- `chktex BOPADIGITAL/mainETS_english_se2.tex` checks common LaTeX issues.
- `git diff --check` detects whitespace errors and conflict markers.
- `git status --short` confirms that only intended evidence and documentation changed.

Compile the final report in Overleaf with `BOPADIGITAL/` as the working directory. After compilation, visually inspect tables, page breaks, listings, links, and missing images. Run application tests only in the relevant sibling repository and record its commit SHA, environment, result, and artifact.

## Writing Style & Naming Conventions

Keep Markdown concise, use descriptive headings, and preserve the language already used by each document. Use repository-relative paths and meaningful lowercase kebab-case names for new guides, for example `06-project2p/release-evidence-guide.md`. Follow the existing LaTeX template and macros; do not create another report entry point. Place exact commands and identifiers in code formatting, and distinguish verified results from planned or historical claims.

## Evidence and Validation Guidelines

Documentation changes are tested through source checks and rendered review. Never treat an old screenshot or a written “passed” claim as current proof. Evidence should identify the tested SHA, date, environment, observed result, and artifact. Do not fabricate screenshots, acceptance records, credentials, or runtime results.

## Commit & Pull Request Guidelines

History generally follows Conventional Commits, including `feat: final report` and `docs(bopadigital): centralize shared testing references`. Use `docs(scope): summary` for documentation-only work and a precise `feat:` only for substantial deliverables. Pull requests should describe scope, list changed documents, link the requirement or issue, report validation commands, and include rendered screenshots when layout changes. Never commit secrets, temporary Overleaf bundles, or unrelated sibling-repository changes.
