# BOPADIGITAL Final Delivery Tracker

**Purpose:** Single checklist for the final partial. Update the status, owner, link, and verification date as each artifact becomes real.

**Status key:** `Not started` · `In progress` · `Ready for review` · `Verified`

## Submission-critical artifacts

| ID | Artifact | Rubric value | Source / target location | Owner | Status | Verification needed |
|---|---|---:|---|---|---|---|
| D-01 | English self-contained final PDF named `T2BOPADIGITAL.pdf` | Submission requirement | `../../ING/BOPADIGITAL/mainETS_english_final.tex` → final PDF | Team | Not started | Compile twice; inspect links, figures, tables, grammar, filename |
| D-02 | Final report source and current assets | Evidence integrity | `../../ING/BOPADIGITAL/assets/final/` | Report owner | Not started | Every screenshot/diagram must match final code/deployment |
| D-03 | English live-demo recording, 13 minutes, equal participation | 10 | Video URL + report link | Team | Not started | Time the full run; include one scenario per role |
| D-04 | Slide deck using ESPOL template | Presentation support | Shared presentation link/export | Team | Not started | Match final report facts and demo sequence |
| D-05 | Production deployment proof | Mandatory; absence is -100 | Screenshots, URLs, `/health` response, deployment date | DevOps owner | Not started | Verify live public web, CRM, API, and mobile build availability |
| D-06 | Client communications index and evidence | 10; absence is -30 | `../communications/README.md` | Communications owner | Ready for review | Confirm final acceptance forms, dates, and repository access |
| D-07 | Signed client acceptance form | Mandatory; absence is -100 | `../communications/signatures/` + final report appendix | Client liaison | Ready for review | Confirm signed final form is legible and linked |
| D-08 | Individual contributions section | Mandatory report content | Final report chapter | All members | Not started | Each contribution must map to commits/evidence |
| D-09 | Individual co-evaluations | Mandatory; absence is -50 | Aula Virtual confirmation | Each member | Not started | Each member submits independently |

## Rubric evidence tracker

| ID | Criterion | Pts | Evidence to create/capture | Primary repo or document | Status |
|---|---|---:|---|---|---|
| R-01 | Project information | 3 | Client, problem, objectives, scope, stakeholders, scenarios, story/sprint totals | Final report + slides | In progress: baseline exists |
| R-02 | Architectural decisions | 3 | Current component/deployment diagrams; comparisons and decision rationale | Final report + `00-architecture/` | In progress: refresh mobile/deployment facts |
| R-03 | Feature demonstration | 10 | 13-minute English role-based video and runbook | `06-project2p/presentation-runbook.md` | Not started |
| R-04 | Testing management/documentation | 4 | Testing strategy, test levels, calendar/owners, execution summary | `06-project2p/test-execution-log.md` | Not started |
| R-05 | User manual appendix | 10 | English role-based manual with current screenshots | `06-project2p/user-manual.md` | Not started |
| R-06 | Installation guide appendix | 10 | Prerequisites, setup, environment, deployment, validation, rollback/troubleshooting | `06-project2p/installation-guide.md` | Not started |
| R-07 | Project/communication/architecture evidence | 10 | Repository/tool access, diagrams, communication index, acceptance evidence | Final report + `communications` | In progress |
| R-08 | Risk-based testing | 10 | Risk matrix, requirement-to-test traceability, results, defects/retests | `06-project2p/risk-based-test-report.md` | Not started |
| R-09 | Scrum adherence | 5 | Backlog, sprint plans/reviews, acceptance forms, management-tool screenshots | `03-scrum/` + final report | Ready for review |
| R-10 | Coding standards and diagnostics | 10 | Biome/TypeScript/Husky evidence plus current successful commands | Repo configs + `06-project2p/quality-evidence.md` | In progress |
| R-11 | CI with quality data | 10 | CI runs, test/coverage summaries, build output, downloadable artifacts | `.github/workflows/` + report | In progress: coverage/artifacts absent |
| R-12 | Acceptance-test tool | 10 | Playwright scenarios, HTML report, screenshots/video, CI artifacts | `bopacorp-web/e2e/`, `bopacorp-crm/e2e/` | Not started |
| R-13 | SOLID, patterns, refactoring | 5 | Concrete code examples and one documented before/after refactor | Final report + source PR/commit | Not started |
| X-01 | GUI automation extra | 1 | Playwright test report | Same as R-12 | Not started |
| X-02 | Profiling extra | 1 | React/API profiling measurement and interpretation | `06-project2p/quality-evidence.md` | Not started |
| X-03 | Load-testing extra | 1 | k6/JMeter scenario, result, and interpretation | `06-project2p/quality-evidence.md` | Not started |

## Repository work tracker

| Repository | Final responsibility | Required evidence | Status |
|---|---|---|---|
| `../bopacorp-api` | REST API, authentication/RBAC, business workflows, API tests | Vitest/coverage output, CI run, API test cases | In progress: tests exist but coverage evidence must be added |
| `../bopacorp-crm` | Internal roles: admin, advisor, supervisor, coordinator, manager | RTL tests, Playwright role scenarios, screenshots | Not started for automated tests |
| `../bopacorp-web` | Public catalog, contact, jobs/application, CMS | RTL tests, Playwright public scenarios, screenshots | Not started for automated tests |
| `../bopacorp-mobile` | Advisor mobile workflows | Device/emulator smoke-test log, screenshots, mobile test evidence | Not started |
| `../bopacorp-shared` | Shared contracts and schemas | Build/CI evidence; test only for shared complex validation behavior | In progress: CI exists |
| `../deploy` | Local/deployment orchestration and Caddy guidance | Reproducible install/deploy validation evidence | In progress: formal guide required |
| `../communications` | Client history and acceptance evidence | Indexed current evidence and final form | Ready for review |
| `Bopadigital` | Requirements, SCRUM, report plan, manuals, traceability | Final documentation package | In progress |

## Weekly evidence cadence

1. After every accepted feature: update the traceability document with the exact test name and result.
2. After every CI run: save the run URL, commit SHA, date, and relevant artifacts in `quality-evidence.md`.
3. After every environment change: rerun the selected acceptance scenarios and capture deployment proof.
4. Before recording: freeze the demo scope, then regenerate screenshots/manual sections from that revision.
5. Before submission: mark every row above `Verified` only when a team member has opened the artifact and confirmed it.

## First sprint of final-delivery work

- [ ] Assign an owner and due date to every row R-01 through R-13.
- [ ] Create the four planned evidence documents: test execution log, risk-based test report, user manual, and installation guide.
- [ ] Add Playwright to Web and CRM, then complete the six scenarios in `requirements-test-traceability.md`.
- [ ] Add coverage reporting to the API and CI artifact upload to all relevant repositories.
- [ ] Capture one verified mobile-advisor smoke-test session on a real device or emulator.
