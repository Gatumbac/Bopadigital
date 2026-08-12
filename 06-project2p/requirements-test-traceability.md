# BOPADIGITAL Requirements-to-Test Traceability

**Purpose:** Connect requirements and user stories to reproducible acceptance tests, manual evidence, and the final demonstration. A `Pass` result can be recorded only after executing the named scenario on the final test/staging environment.

**Evidence naming:** `AT-<scenario>-<YYYY-MM-DD>-<commit>.png` for screenshots and `AT-<scenario>-<YYYY-MM-DD>-<commit>.webm` for recordings.

## Acceptance scenario register

| ID | Role / system | User journey | Requirements and user stories covered | Automated test target | Manual evidence | Demo |
|---|---|---|---|---|---|---|
| AT-01 | Public visitor — Web | Browse catalog, apply category/price/coverage filters, inspect service information, submit contact request | RF-CAT-001–004; HU-CAT-001–004 | `bopacorp-web/e2e/public-catalog-and-contact.spec.ts` | Filtered catalog, item detail, successful contact confirmation | Yes |
| AT-02 | Candidate — Web | Browse vacancy, open details, submit validated application with PDF résumé | RF-EMP-001–004; HU-EMP-001–004 | `bopacorp-web/e2e/job-application.spec.ts` | Vacancy page, invalid-form error, successful application | Yes |
| AT-03 | CMS administrator — Web/CRM | Authenticate, edit a CMS block, create/update a catalog item, verify public result | RF-CMS-001–005; HU-CMS-001–005 | `bopacorp-crm/e2e/admin-cms-catalog.spec.ts` | Login, edit/create action, public verification | Yes |
| AT-04 | Sales advisor — CRM | Authenticate, register client, create/update negotiation, schedule/register visit, upload a document | RF-CRM-001–008 and 021; RF-DOC-001–003 and 005; HU-CRM-001–008; HU-DOC-001–003 and 005 | `bopacorp-crm/e2e/advisor-commercial-workflow.spec.ts` | Client, negotiation, visit, document state screenshots | Yes |
| AT-05 | Supervisor/coordinator — CRM | Filter team work, assign/review client data, review document, and inspect pending work | RF-CRM-009–014 and 020; RF-DOC-004–008; HU-CRM-009–014 and 020; HU-DOC-004–008 | `bopacorp-crm/e2e/supervision-and-documents.spec.ts` | Role access, filtered results, approval/rejection with reason | Yes |
| AT-06 | Manager — CRM | Open reports, filter time range/advisors, inspect performance data and export a report | RF-REP-001–010; HU-REP-001–009 | `bopacorp-crm/e2e/manager-reports.spec.ts` | KPIs/chart, filter result, export file and access control | Yes |
| AT-07 | Advisor — Mobile | Login, list/create/update client, list/create/update negotiation, upload a document | Mobile scope supporting CRM/DOC stories; RF-CRM-001, 002, 007, 008, 021; RF-DOC-001–003, 005 | Mobile unit tests plus device/emulator smoke-test script | Device screenshots and OS/version execution log | Yes, if stable |

## Scenario execution template

Copy this table once per run into `06-project2p/test-execution-log.md`.

| Field | Required record |
|---|---|
| Scenario ID | Example: `AT-04` |
| Requirement/user-story IDs | Exact IDs from the scenario register |
| Environment | Local, test, staging, or production; include base URL/build identifier |
| Revision | Git commit SHA for every involved repository |
| Tester and date | Full name and local date/time |
| Preconditions | Role/account, seeded data, browser/device, network state |
| Steps | Numbered actions actually performed |
| Expected result | Result derived from the requirement acceptance criteria |
| Actual result | Observed behavior; no vague summaries |
| Result | Pass, fail, blocked, or not run |
| Evidence | Screenshot/video/report filename and URL |
| Defect/retest | Issue link, fix SHA, and retest result when applicable |

## Module coverage ledger

| Module | Requirement range | Final strategy | Current caution |
|---|---|---|---|
| CAT | RF-CAT-001–005 | Automate AT-01; include institutional-content check in CMS/public verification | The June audit is stale; verify current public behavior before reporting results |
| CMS | RF-CMS-001–005 | Automate AT-03 with authenticated edit and public-content verification | Capture permissions and changed content safely |
| EMP | RF-EMP-001–006 | Automate AT-02 for listing/application/PDF/validation | Email confirmation/result requirements require a real provider or must be documented as future work |
| CRM | RF-CRM-001–022 | Automate AT-04/AT-05; unit-test ownership and state rules | GPS/map, assignment/removal, activity, KPIs, and audit-log features need explicit verification before claims |
| MAT | RF-MAT-001–007 | Add an advisor/supervisor scenario only after full CRM matrix UI is demonstrable | Current CRM has service/hooks but no routed matrix page; do not include in demo until fixed |
| SUP | RF-SUP-001–006 | Cover with the matrix approval scenario if MAT is completed | Depends on the matrix UI and notification trigger behavior |
| DOC | RF-DOC-001–009 | Cover upload/review in AT-04/AT-05 and test invalid files/permissions | Bulk download, pending-advisor view, and notification delivery require verification |
| REP | RF-REP-001–010 | Automate AT-06; validate calculation datasets and exported content | Reports and notifications have newer CRM components than the June audit; test actual output, not old status labels |
| SEG | RF-SEG-001–003 | Unit-test API auth/RBAC; acceptance-test each protected role journey | Never show reusable passwords in evidence |
| NOT | RF-NOT-001–002 | Test notification bell/read behavior and event triggers when implemented | Bell/UI exists; automatic triggers and email delivery must be verified separately |
| RNF | RNF-001–026 | Record only measurable/verified claims: performance, compatibility, security, coverage, availability, deployment | Add load, accessibility, security, device, and coverage evidence for claims used in the report |

## Risk-based priorities

| Priority | Risk | Test cases that control it | Required evidence |
|---|---|---|---|
| Critical | Unauthorized access or cross-advisor data exposure | API auth/RBAC unit tests; AT-03 through AT-06 | Forbidden-route result, ownership result, CI output |
| Critical | Incorrect commercial state/approval decision | Negotiation/matrix service tests; AT-04/AT-05 | State history, rejection reason, audit/retest evidence |
| High | Invalid or unsafe document/resume upload | API upload tests; AT-02 and AT-04 | Valid PDF pass; invalid type/size fail; stored-document result |
| High | Public application/contact data lost or misvalidated | Web component tests; AT-01/AT-02 | Required-field errors and successful submission response |
| High | Incorrect management metrics/export | Report service tests; AT-06 | Seeded-data expected totals, chart/filter screenshot, exported file |
| Medium | GPS permission/location failure in field workflow | Mobile location tests and AT-07 smoke test | Permission-denied and granted-state evidence |
| Medium | Production regression after deployment | Playwright smoke suite and `/health` check | Deployment date, commit SHA, passing smoke report |

## Definition of done for a requirement in the final report

A requirement can be marked **implemented and tested** only when all apply:

- [ ] A current code path exists in the relevant repository.
- [ ] The responsible role can perform the workflow in the deployed/test environment.
- [ ] A unit/integration or acceptance test covers the core behavior where practical.
- [ ] The execution log shows a passing result on a known revision.
- [ ] A screenshot, video, test report, or exported artifact is available for the report/manual/demo.
- [ ] Any known limitation is written as a limitation/future improvement, not hidden by a completion claim.
