# BOPADIGITAL Final Delivery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `subagent-driven-development` (recommended) or execute this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver every artifact required for the Software Engineering II final partial, backed by reproducible tests, current evidence, and a 13-minute English demonstration.

**Architecture:** The deliverable is a coordinated evidence package around the existing multi-repository platform: API, CRM, public web, mobile, shared contracts, deployment, and communications. Each evidence item must be traceable to a rubric criterion, a repository artifact, and—when applicable—a requirement, user story, test case, and captured result.

**Tech Stack:** Node.js 22, TypeScript, Express, Drizzle, React, Vite, Expo 54, Vitest, React Testing Library, Playwright, GitHub Actions, Docker Compose, Caddy, LaTeX.

---

## Scope and authoritative references

- Final specification and marking scheme: `06-project2p/02FinalProjectSpec_en.md` and `06-project2p/Rubric_2.txt`.
- Previous-report baseline: `05-reports/T2BOPADIGITAL.pdf` and `../../ING/BOPADIGITAL/mainETS_english_se2.tex`.
- Requirements and user stories: `02-requirements/BOPADIGITAL_REQUIREMENTS_SPECIFICATION_DOCUMENT.md`.
- Architecture: `00-architecture/repos-architecture.md`.
- Scrum evidence: `03-scrum/BOPADIGITAL_Scrum_Final_Corregido.md`.
- Client evidence: `../communications/README.md` and the associated evidence files.

## Rubric-to-evidence matrix

| Rubric criterion | Pts | Required final evidence | Primary location | Current status |
|---|---:|---|---|---|
| Project information | 3 | Client, objectives, scope, scenarios, user-story/sprint counts | Final report + slides | Baseline exists; refresh with current scope |
| Architectural decisions | 3 | Component/deployment diagrams and justified technology choices | Final report | Baseline exists; update mobile and production facts |
| Feature demonstration | 10 | English recording, 13 minutes, equal participation, one role per scenario | Video + slides + report link | New recording required |
| Testing management | 4 | Test strategy, levels, execution evidence, ownership | Final report | Expand and update |
| User manual appendix | 10 | Role-based instructions and current screenshots | Final report appendix + source PDF | Create |
| Installation guide appendix | 10 | Reproducible local/production setup and troubleshooting | Final report appendix + source PDF | Create formal guide |
| Project, communication, architecture evidence | 10 | Indexed client evidence, acceptance forms, repo/tool links, diagrams | Report + `communications` | Strong base; re-verify links/current facts |
| Risk-based testing and documentation | 10 | Risk matrix, traceability, test cases, results, screenshots | `06-project2p/` + report | Create |
| Scrum evidence | 5 | Backlog, sprint plans/reviews, charts, acceptance forms | Context repo + report | Base exists; package concisely |
| Coding standards and diagnostics | 10 | Biome/TypeScript configuration and passing execution evidence | Repos + CI artifacts + report | Tooling exists; capture current evidence |
| CI with quality data | 10 | GitHub Actions runs, coverage/test reports, build output | `.github/workflows/` + report | CI exists; quality reports missing |
| Acceptance-test tool | 10 | Automated end-to-end scenarios and execution report | Web/CRM test setup + CI artifacts | Create |
| SOLID, patterns, refactoring | 5 | Concrete code examples and before/after refactoring evidence | Final report | Document current architecture and one refactor |
| Optional extras | 3 | Profiling, GUI test automation, load test | Report + artifacts | Playwright can cover GUI automation |

## Delivery rules

- Do not describe a feature as implemented unless it is demonstrable in the current application and covered by captured evidence.
- Keep mobile in the scope: the repository is `../bopacorp-mobile`; use real Expo screenshots and tests, not claims copied from the previous report.
- Treat the previous LaTeX document as a baseline only. Replace the title, dates, links, video duration, implementation claims, and screenshots that are not current.
- Never include real production secrets or reusable credentials in the public report, manuals, screenshots, or repositories.
- Every test case must link a requirement/user story to an actual execution result.

## Recommended execution order

### Track 1: Delivery foundation and traceability

**Files:**
- Create: `06-project2p/final-delivery-tracker.md`
- Create: `06-project2p/requirements-test-traceability.md`
- Modify: `06-project2p/final-delivery-plan.md`

- [ ] Create a tracker with one row per rubric criterion: owner, artifact path/URL, verification command, evidence date, and status.
- [ ] Build a traceability table for the demo-critical requirements: requirement ID, user story, role, acceptance-test scenario, automated test, manual test case, and screenshot/video timestamp.
- [ ] Select six demonstration scenarios: public applicant, CMS administrator, advisor, supervisor, coordinator, and manager.
- [ ] Mark feature gaps discovered during scenario rehearsal; only prioritize gaps that block a selected scenario or a rubric artifact.
- [ ] Commit documentation separately:

```bash
git add 06-project2p/
git commit -m "docs: add final delivery tracking"
```

### Track 2: Acceptance testing with Playwright

**Files:**
- Create: `../bopacorp-web/playwright.config.ts`
- Create: `../bopacorp-web/e2e/public-catalog-and-application.spec.ts`
- Create: `../bopacorp-crm/playwright.config.ts`
- Create: `../bopacorp-crm/e2e/role-workflows.spec.ts`
- Modify: `../bopacorp-web/package.json`
- Modify: `../bopacorp-crm/package.json`
- Modify: `../bopacorp-web/.github/workflows/ci.yml`
- Modify: `../bopacorp-crm/.github/workflows/ci.yml`

- [ ] Add Playwright with a dedicated `test:e2e` script in both web repositories.
- [ ] Implement public-web acceptance scenarios: filter catalog, submit contact request, inspect vacancy, and submit a valid PDF application.
- [ ] Implement CRM acceptance scenarios using test accounts: advisor client/negotiation flow; supervisor review; coordinator document decision; manager reports; administrator CMS/catalog flow.
- [ ] Save HTML reports, screenshots, and videos as CI artifacts on failure and as release evidence for the final run.
- [ ] Run the scenarios against a controlled test/staging environment with seeded non-sensitive data.
- [ ] Update the traceability table with test filenames and passing execution dates.

### Track 3: Unit, integration, and coverage evidence

**Files:**
- Modify: `../bopacorp-api/vitest.config.ts`
- Modify: `../bopacorp-api/package.json`
- Create: focused `*.test.ts` files beside critical API services/controllers
- Create: `../bopacorp-crm/vitest.config.ts`
- Create: `../bopacorp-crm/src/**/*.test.tsx` for critical UI flows
- Create: `../bopacorp-web/vitest.config.ts`
- Create: `../bopacorp-web/src/**/*.test.tsx` for critical public flows
- Modify: relevant `package.json` and `.github/workflows/ci.yml` files

- [ ] Enable V8 coverage for API tests and generate `coverage/lcov.info` plus a human-readable summary.
- [ ] Add React Testing Library to CRM and Web; test guards, form validation, permission gating, and API-state success/error behavior.
- [ ] Prioritize tests for authentication/RBAC, client ownership, document upload validation, matrix state transitions, report calculations, catalog filters, and job application validation.
- [ ] Make CI run tests with coverage and upload the reports as artifacts; do not use formatting commands that mutate source during CI validation.
- [ ] Record the final passing command output and coverage summary in the testing evidence document.

### Track 4: Mobile verification

**Files:**
- Create: `../bopacorp-mobile/__tests__/` or co-located mobile tests following project conventions
- Create: `06-project2p/mobile-test-evidence.md`
- Modify: `../bopacorp-mobile/package.json`
- Modify: final report source under `../../ING/BOPADIGITAL/`

- [ ] Inspect the Expo routes and select supported advisor workflows for the final scope.
- [ ] Add automated tests for login/session storage, client/negotiation data handling, and GPS permission/error states where testable.
- [ ] Execute device or emulator smoke tests for login, client/negotiation navigation, document selection, and location capture.
- [ ] Capture device screenshots and record OS/device/version, build identifier, account role, expected result, and actual result.
- [ ] Include only verified mobile functionality in the final report, user manual, and demo.

### Track 5: Resolve demo-blocking implementation gaps

**Files:**
- Modify: `../bopacorp-crm/src/App.tsx`
- Create: matrix pages/components under `../bopacorp-crm/src/modules/matrices/`
- Modify: corresponding API/shared-contract files only when a selected scenario requires an absent endpoint/contract
- Modify: `06-project2p/requirements-test-traceability.md`

- [ ] Rehearse each selected end-to-end scenario before starting new feature work.
- [ ] Implement the complete matrix user interface only if it is selected for the advisor/supervisor demo: list, create/edit, item totals, attachment handling, submit, approve/reject, and history.
- [ ] Keep reports and notification evidence current; these modules already have CRM routes/components and should be verified instead of rebuilt.
- [ ] Decide whether email notifications, GPS map views, audit-log UI, and encryption are in final demo scope. If omitted, state them as future work rather than completed functionality.
- [ ] Add/update tests before and after every behavior change, then update the traceability table.

### Track 6: Manuals and operational evidence

**Files:**
- Create: `06-project2p/user-manual.md`
- Create: `06-project2p/installation-guide.md`
- Create: `06-project2p/risk-based-test-report.md`
- Create: `06-project2p/test-execution-log.md`
- Modify: `../deploy/README.md` only for verified corrections

- [ ] Write the user manual in English from the passed acceptance scenarios, with prerequisites, role/permission notes, numbered steps, expected outcome, and current screenshots.
- [ ] Cover public user, administrator, advisor, supervisor, coordinator, manager, and mobile advisor workflows only when verified.
- [ ] Write the installation guide with prerequisites, GitHub Packages access, environment files, database/migration steps, Docker Compose startup, Caddy/HTTPS setup, validation commands, rollback, and troubleshooting.
- [ ] Write the risk-based report: probability, impact, risk score, control, linked test cases, results, defects, and retest result.
- [ ] Capture current production evidence only after confirming it is accessible; include health endpoint, web/CRM pages, and deployed-version/date screenshots.

### Track 7: CI, standards, and quality package

**Files:**
- Modify: `../bopacorp-api/.github/workflows/ci.yml`
- Modify: `../bopacorp-crm/.github/workflows/ci.yml`
- Modify: `../bopacorp-web/.github/workflows/ci.yml`
- Modify: `../bopacorp-shared/.github/workflows/ci.yml`
- Create: `06-project2p/quality-evidence.md`

- [ ] Standardize CI jobs: install, lint, typecheck, unit test, coverage, end-to-end test where applicable, build, and artifact upload.
- [ ] Capture successful run URLs/screenshots and a compact per-repository quality table.
- [ ] Document Biome, strict TypeScript, Husky, commitlint, API layering, React feature modules, shared schemas, and a concrete refactoring example as SOLID/pattern evidence.
- [ ] Verify every reported quality result is from the final code revision, not the previous partial.

### Track 8: Final report, submission package, and presentation

**Files:**
- Create: `../../ING/BOPADIGITAL/mainETS_english_final.tex`
- Create: `../../ING/BOPADIGITAL/assets/final/` for current diagrams and screenshots
- Create: final PDF named `T2BOPADIGITAL.pdf`
- Create: `06-project2p/presentation-runbook.md`

- [ ] Copy the prior LaTeX report into a final source file; never overwrite the midterm source.
- [ ] Update title, dates, deliverable links, repository list, production verification, test results, architecture diagrams, risk-based results, manuals, individual contributions, and future-work statements.
- [ ] Include the user manual and installation guide as appendices; link all repository, tool, video, and communication evidence.
- [ ] Run LaTeX compilation twice and manually inspect the table of contents, figure/table references, URLs, screenshot legibility, and English grammar.
- [ ] Prepare a 13-minute English runbook with equal speaking time, role-specific scenarios, test evidence, architecture explanation, and a recovery plan for demo outages.
- [ ] Record the presentation, upload it within the lecturer's stated deadline, and update the report link.
- [ ] Final verification checklist: report filename, public access permissions, signed acceptance form, communications index, deployed system, video, and individual co-evaluations.

## Acceptance gates before submission

- [ ] All selected acceptance scenarios pass locally and in CI, with artifacts retained.
- [ ] Test traceability and risk-based report contain no unexecuted cases marked as passed.
- [ ] User manual and installation guide reflect the final deployed build.
- [ ] The final LaTeX PDF is English, self-contained, current, and named `T2BOPADIGITAL.pdf`.
- [ ] Every linked repository/tool/video is accessible to evaluators.
- [ ] Production deployment and client acceptance evidence are verified on the final revision.
- [ ] Each team member submits the required individual co-evaluation.

## Dependencies and sequencing

1. Complete Track 1 before feature selection.
2. Run Tracks 2, 3, and 4 in parallel once test environments/accounts are available.
3. Start Track 5 only for scenario blockers identified by Tracks 2–4.
4. Write Tracks 6 and 7 from real execution outputs, not planned claims.
5. Complete Track 8 after the tested scope and evidence are frozen.
