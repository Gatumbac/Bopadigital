# BOPADIGITAL final report: chapter plan

**Date:** 2026-08-15  
**Status:** In progress  
**Purpose:** Define what each chapter and appendix must contain, which rubric criteria it supports, which evidence is required, and when the section can be considered ready for the final English report.

## 1. Source of truth

The final report must be written and maintained from the following order of priority:

1. Current behavior and artifacts in the sibling implementation repositories.
2. The current requirements and rubric documents in this repository.
3. Current client, Scrum, testing, deployment, and acceptance evidence.
4. The active LaTeX source: BOPADIGITAL/mainETS_english_se2.tex.
5. ING_1_FINAL_REPORT.md and 99-reference-nintventario/ only as historical or structural references.

The previous Software Engineering I report and the Nintventario report are not evidence of current BOPADIGITAL behavior. A feature, test result, deployment, screenshot, or coverage value must be reported only after it is tied to a current revision, date, environment, and artifact.

## 2. Global writing and evidence rules

- Write the report in clear, formal English using the ETS template and the ESPOL/FIEC identity.
- Start objectives with infinitive verbs: “To support”, “To centralize”, “To reduce”, and similar forms.
- Describe the final scope, not every historical requirement. The matrix-construction and matrix-approval module is excluded by the client decision and must be presented as excluded or future work.
- Document the database environment boundary explicitly: Supabase is a development-only PostgreSQL hosting convenience; the production target is PostgreSQL hosted on the deployment server.
- Write the final report as a complete delivery narrative. Missing letters, screenshots, logs, or links are tracked as internal completion tasks and must be added to the evidence package; they should not be described in the final narrative as if the project were incomplete.
- Distinguish implementation evidence from runtime acceptance evidence. A route, component, test file, or diagram alone does not prove that a workflow passed.
- For every important result, record repository revision or SHA, execution date, environment, command or scenario, expected result, observed result, and evidence location.
- Do not present old screenshots, historical “Passed” claims, or static inspection as current verification.
- Use figures only when they clarify architecture, flow, user interaction, or evidence. Captures in manuals must show numbered steps, arrows, rectangles, or other consistent click indicators.
- Insert user manuals and installation guides as PDF appendices after their final PDFs and editable sources are available.
- Keep the LaTeX source self-contained and preserve the agreed table and typography standards:
  - Use longtable for long tables and L{width} left-aligned text columns.
  - Include “Continued from previous page” and “Continued on next page” in every longtable.
  - Avoid an isolated final horizontal line before endlastfoot.
  - Permit breaks in repository and package names so no table column overflows.
  - Keep the ETS body font unchanged. Use normal body text, emph for technical identifiers in prose, and texttt only for exact technical values where it improves readability.

## 3. Chapter-by-chapter plan

### Chapter 1 — INTRODUCTION AND PROJECT CONTEXT

**Current status:** Base content drafted; review against final evidence still required.

**Purpose:** Explain who the client is, which business problem was addressed, what BOPADIGITAL does, and what is included in the final project.

**Content to include:**

- Client and business context.
- Problem statement and operational bottlenecks.
- Project description and evolution from Software Engineering I to Software Engineering II.
- General and specific objectives.
- Final scope, exclusions, and limitations.
- Stakeholders, roles, and target users.
- Development timeline, number of sprints, and client acceptance milestones.
- Project dimensions and the scenarios selected for the final demonstration.

**Required evidence and sources:**

- Current requirements specification.
- Current client acceptance and communication records.
- CARTAS.md and Scrum records for sprint counts and milestones.
- Final repository list and verified project scope.

**Ready when:** Objectives use infinitive verbs, the matrix decision is reflected consistently, user/story and sprint counts match the current evidence, and no historical feature is presented as part of the final scope without verification.

### Chapter 2 — RELEVANT ARCHITECTURAL DECISIONS

**Current status:** Base content drafted; visual PDF and final deployment facts still require review.

**Purpose:** Justify the architecture and technology decisions that make the current system maintainable, testable, and deployable.

**Content to include:**

- Repository ecosystem and system boundaries.
- Client/API/shared-contract/persistence responsibilities.
- Technology selection comparisons and decisions.
- Authentication, authorization, RBAC, token responsibilities, and layered protection.
- Shared contracts, validation schemas, response envelopes, and data architecture.
- Component diagram.
- Deployment diagram and reverse-proxy/deployment explanation.

**Required evidence and sources:**

- Current architecture documentation and repository structure.
- API routes, middleware, services, shared contracts, and deployment configuration.
- Current component and deployment diagrams.
- Verified deployment facts, ports, domains, health checks, and external services.
- Explicit development/production database boundary: Supabase for shared development PostgreSQL, and PostgreSQL hosted on the selected deployment server for production.

**Ready when:** Every decision is linked to a real project constraint, diagrams match the final repositories, the deployment diagram is not treated as proof of a live environment by itself, and the excluded matrix module is not used to justify current architecture.

### Chapter 3 — SCRUM EVIDENCE

**Current status:** Scaffold only.

**Purpose:** Demonstrate that the product was developed through an organized Scrum process with traceable planning, reviews, acceptance, and improvement.

**Content to include:**

- Scrum roles and responsibilities.
- Teamwork or project-management tool.
- Product backlog and prioritization.
- Sprint backlogs and delivered scope for every sprint.
- Sprint reviews and client feedback.
- Sprint retrospectives and improvement actions.
- Project schedule, progress charts, and critical path.
- Project-management risks, kept separate from risk-based testing risks.

**Required evidence and sources:**

- 03-scrum/BOPADIGITAL_Scrum_Final_Corregido.md.
- Sprint acceptance forms and client communications.
- Current planning-tool exports or screenshots.
- CARTAS.md and the communications index.

**Ready when:** Each sprint has planned work, delivered work, review/acceptance evidence, and a concise result; the final sprint and closing activities are included; and the charts agree with the report narrative.

### Chapter 4 — CODING STANDARDS DOCUMENTATION

**Current status:** Scaffold only.

**Purpose:** Show how the team applied coding conventions, automation, SOLID principles, design patterns, and refactoring in the implementation.

**Content to include:**

- Build and repository automation.
- TypeScript, naming, formatting, module organization, and Biome rules.
- Git hooks, lint-staged, Commitlint, and pre-commit validation.
- Concrete SOLID examples from the current code.
- Design patterns used and why they fit the system.
- One verified refactoring example with before/after structure and its benefit.

**Required evidence and sources:**

- Configuration files in the API, CRM, Web, Mobile, Shared, and deployment repositories.
- Current lint, typecheck, build, and hook outputs.
- File paths and revision identifiers for the SOLID and refactoring examples.

**Ready when:** The chapter contains concrete code evidence rather than generic definitions, and every quality result comes from the final revision.

### Chapter 5 — PREEMPTIVE ERROR DETECTION

**Current status:** Scaffold only.

**Purpose:** Explain how defects are detected before runtime, merge, or deployment.

**Content to include:**

- TypeScript compiler diagnostics and strict typing.
- Biome linting and formatting diagnostics.
- Git-hook and CI quality gates.
- Observed preventive-quality results.
- Failures found, fixes applied, and relevant retests when applicable.

**Required evidence and sources:**

- TypeScript and Biome configuration.
- CI workflow files and successful run URLs.
- Command outputs with SHA, date, and environment.
- Build artifacts or logs that can be accessed by evaluators.

**Ready when:** The chapter clearly separates static/preemptive checks from runtime tests and includes reproducible quality data instead of only describing the tools.

### Chapter 6 — TEST CASES AND TEST MANAGEMENT

**Current status:** Scaffold only; API test evidence exists separately and must be frozen against a final revision.

**Purpose:** Present the testing strategy, risk-based prioritization, test management, execution results, and quality evidence required by the rubric.

**Content to include:**

- Testing strategy and test levels: unit, integration, API, frontend, acceptance, and manual testing.
- Test ownership, environments, data, calendar, entry criteria, exit criteria, and defect handling.
- Risk-based testing linked as Risk -> Requirement -> Test case -> Observed result -> Evidence -> Retest.
- API unit and integration testing, including authentication, RBAC, ownership, validation, state transitions, and persistence boundaries.
- Frontend testing for critical CRM and public-web flows.
- Acceptance testing using the selected tool and the AT-01 to AT-07 scenarios.
- Execution results, blocked cases, defects, fixes, and retests.
- Application profiling only if the optional criterion is actually pursued.

**Required evidence and sources:**

- 06-project2p/software1-risk-to-testing-plan.md.
- 06-project2p/requirements-test-traceability.md.
- Current test files, commands, coverage summaries, CI artifacts, and test reports.
- API and frontend repository revisions.
- Screenshots, HTML reports, videos, or logs for acceptance scenarios.

**Testing rules:** The rubric does not require 100% global unit-test coverage. RNF-021 requires at least 80% coverage of critical code; the report must show the measured result for the final revision and explain uncovered non-critical helpers or boundaries. Prioritize risk and business impact over an arbitrary global percentage. Use Arrange-Act-Assert, equivalence partitions, boundary values, decision tables, state-transition tests, parameterized cases, deterministic fixtures, mocks/fakes, and Supertest where appropriate.

**Ready when:** No test is marked as passed without an execution artifact; the API, CRM, Web, and Mobile claims are separated by evidence; coverage and CI data identify revision/date/environment; and every high-priority risk has a control and result.

### Chapter 7 — SYSTEM DESCRIPTION AND DEMONSTRATION

**Current status:** Scaffold only.

**Purpose:** Describe the final verified system from the user’s perspective and provide the sequence for the English live demonstration.

**Content to include:**

- General system description.
- Verified public website workflows.
- Verified CMS and catalog workflows.
- Verified CRM workflows by role: administrator, advisor, supervisor, coordinator, and manager.
- Mobile workflows only when device or emulator evidence exists.
- Feature demonstration runbook with timing, speaker, role, preconditions, expected result, and fallback.

**Required evidence and sources:**

- Current URLs and deployed revision.
- Acceptance scenarios AT-01 through AT-07.
- Current screenshots and demonstration recording.
- Requirements, user stories, and acceptance criteria.

**Ready when:** The chapter and presentation demonstrate only available workflows, include one user per role where required, state the number of stories and sprints, explain the architecture briefly, and fit the approximately 13-minute English presentation with balanced participation.

### Chapter 8 — INDIVIDUAL CONTRIBUTIONS AND AUTHORSHIP

**Current status:** Scaffold only.

**Purpose:** Make each team member’s contribution and authorship transparent and traceable.

**Content to include:**

- Individual contributions by feature, repository, evidence, and rubric criterion.
- Relevant commits, pull requests, documents, tests, diagrams, manuals, and presentation responsibilities.
- Authorship declaration consistent with the project and ESPOL/ACM guidance.

**Required evidence and sources:**

- Git history and repository artifacts.
- Sprint assignments and acceptance evidence.
- Individual contribution statements agreed by the team.

**Ready when:** Every member has specific evidence-backed contributions and the section does not rely on vague statements such as “helped with development”.

## 4. Appendix plan

| Appendix | Content | Main evidence |
|---|---|---|
| Repositories, tools and project links | Source repositories, deployment, project-management tool, video, communications, and evaluation links | Accessible URLs and permission checks |
| Software building and deployment evidence | Build outputs, deployed revision, health checks, ports, domains, and release evidence | Current command/log/screenshot evidence |
| Project presentation and demonstration | Presentation link, recording, runbook, timing, and scenario evidence | English video and slides |
| Client communications and acceptance | Indexed communications, sprint acceptance, and final signed acceptance | communications index and signed forms |
| System deployment guide | Operational deployment steps and verified production procedure | Deployment README, commands, troubleshooting |
| Installation guide | Local prerequisites, packages, environment, database, Docker, Caddy, validation, rollback, and troubleshooting | Editable guide and final PDF |
| User manuals | Role-based instructions with prerequisites, clicks, screenshots, expected results, and limitations | Editable manuals and final PDF files |
| Testing artifacts, traceability and schedule | Risk matrix, requirement/test mapping, test logs, coverage, CI artifacts, incidents, retests, and schedule | Current execution records |

Manual and installation appendices must be inserted as PDFs only after the PDFs are compiled, reviewed, and copied to the final Overleaf package together with their editable source where required.

## 5. Rubric traceability

| Rubric criterion | Points | Primary chapter/appendix | Supporting evidence |
|---|---:|---|---|
| Project information | 3 | Chapter 1 and presentation appendix | Client, problem, scope, objectives, roles, scenarios, stories, and sprints |
| Architectural decisions | 3 | Chapter 2 | Comparisons, decisions, component diagram, deployment diagram |
| Feature demonstration | 10 | Chapter 7 and presentation appendix | Role-based scenarios, recording, slides, runbook |
| Testing management and documentation | 4 | Chapter 6 and testing appendix | Strategy, levels, owners, calendar, execution results |
| User manual | 10 | User-manual appendix | Role-based PDF and current screenshots |
| Installation guide | 10 | Installation appendix | Reproducible setup, deployment, validation, and troubleshooting |
| Project, communication, and architecture evidence | 10 | Chapters 1-3 and appendices | Indexed communications, acceptance, repositories, tools, and diagrams |
| Risk-based testing and test documentation | 10 | Chapter 6 and testing appendix | Risk matrix, traceability, results, defects, and retests |
| Scrum adherence | 5 | Chapter 3 and communications appendix | Backlogs, reviews, planning, charts, stories, and acceptance |
| Coding standards and diagnostics | 10 | Chapters 4-5 | Configurations and current successful command/CI evidence |
| Continuous integration with quality data | 10 | Chapters 5-6 and deployment/testing appendices | CI runs, coverage, test reports, builds, and artifacts |
| Acceptance-testing tool | 10 | Chapters 6-7 and testing/presentation appendices | Automated scenarios, reports, screenshots, and video |
| SOLID, patterns, and refactoring | 5 | Chapter 4 | Concrete code examples and before/after refactoring |

## 6. Submission gates

The final review must verify these items independently of chapter completion:

- Production deployment is accessible and documented.
- Final client acceptance form is signed, legible, current, and included.
- Communications evidence covers the project over time through final delivery.
- Repositories and online tools are accessible to evaluators.
- Co-evaluations are submitted by every team member.
- The report is an English, self-contained PDF with the required name, links, figures, tables, and appendices.
- The presentation is recorded within the required duration and includes balanced participation.
- No secret, token, password, or sensitive personal data appears in the report or evidence.

## 7. Recommended writing sequence

1. Freeze the final scope, user/story counts, sprint counts, roles, and excluded matrix decision.
2. Complete Chapter 3 from current Scrum and communication evidence.
3. Complete Chapters 4 and 5 from current repository configurations and CI results.
4. Execute and freeze API, CRM, Web, and Mobile evidence; then write Chapter 6.
5. Select only passing scenarios and write Chapter 7, manuals, installation guide, and demonstration runbook from them.
6. Complete Chapter 8 with team-approved contribution evidence.
7. Insert appendices and update all links, captions, labels, and cross-references.
8. Compile in Overleaf, inspect the PDF visually, correct overflow or orphaned content, and repeat until the final package is self-contained.

## 8. Definition of done for the report

The report is ready for submission only when every chapter has current evidence, every rubric criterion has a visible location in the report or appendices, every mandatory gate is verified, and the final PDF has been compiled and visually inspected in Overleaf.

## 9. Pending evidence tasks before final freeze

These tasks belong to the delivery checklist, not to the final narrative. They must be completed before the final PDF is frozen:

- [ ] Consolidate Sprint 1 through Sprint 7 acceptance letters and the final acceptance letter in the communications package.
- [ ] Update the communications README/index with file name, description, type, participants, date, and time for every evidence item.
- [ ] Insert the final sprint-review captures, supporting images, and signed documents in the corresponding appendix.
- [ ] Replace every remaining chapter TODO with current evidence or an explicit final-scope limitation.
- [ ] Freeze repository revisions, test results, deployment facts, links, manuals, and screenshots before the final Overleaf compile.
