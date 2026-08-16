# BOPADIGITAL Final Presentation Script — 13 Minutes

## Audit Summary (not spoken)

### Positive points in the previous script

- It used English, divided participation among five members, and followed a logical introduction–architecture–demo–testing sequence.
- It identified the client problem, principal applications, REST API, shared contracts, RBAC, CI, and representative user roles.
- It reserved most of the presentation for a live functional demonstration, which matches the highest-weight presentation criterion.

### Corrections applied

- The final project has **seven accepted sprints**, not four, and **55 active user stories** from 68 historical records, not 17 backlog items.
- Offer Matrices and their dependent approval/calculation stories are excluded from the final scope; they must not appear in the demo.
- Testing evidence is now stated with the exact results recorded in the final report instead of the unsupported claim that 20 acceptance cases all passed.
- The architecture distinguishes development Supabase from production PostgreSQL and avoids claiming that every component runs in the same container arrangement.
- The script now includes the required comparison with ISO/IEC/IEEE 29119-1:2022, including practices followed, partially followed, and not demonstrated.
- Timing gives every member approximately equal participation and preserves more than five minutes for role-based demonstration.

## Timing and Demo Preparation

| Time | Speaker | Focus |
|---|---|---|
| 0:00–2:30 | Person 1 | Client, problem, scope, stories, exclusions |
| 2:30–5:00 | Person 2 | Scrum, architecture, technical decisions |
| 5:00–7:30 | Person 3 | Testing evidence and standards comparison |
| 7:30–10:05 | Person 4 | Visitor, candidate, administrator, manager |
| 10:05–12:40 | Person 5 | Advisor, coordinator, supervisor, mobile, conclusion |
| 12:40–13:00 | Team | Buffer for transitions |

Before presenting, open the public Web, CRM, mobile recording/device, architecture diagrams, and test-result slide. Prepare authenticated sessions for Administrator, Manager, Supervisor, Advisor, and Coordinator. Use seeded or synthetic data and never expose credentials.

## Person 1 — Client, Problem, and Final Scope (2 minutes 30 seconds)

**On screen:** title, client, three operational problems, final scope.

Good morning. We are Team 2, and today we present BOPADIGITAL, the commercial digital platform developed for BOPACORP S.A., an Ecuadorian telecommunications company and strategic commercial partner of Movistar Ecuador.

The project began from three operational problems. First, commercial documents were exchanged through separate channels, producing delays and extra office visits. Second, supervisors and managers had limited visibility of advisor visits and negotiation progress. Third, client portfolios and sales reports depended heavily on spreadsheets and manual communication.

Our objective was to digitize and centralize this business-to-business commercial lifecycle. The final ecosystem includes a public website and employability portal, a content management interface, an internal CRM, a mobile advisor application, a REST API, and a shared TypeScript contract package.

The active scope covers authentication and role-based access, clients, negotiations, visits, documents, reports, catalog and public content, vacancies and applications, organization management, and advisor mobile workflows. The client removed Offer Matrices, subsidy calculations, and their approval stories from the final scope, so they are preserved only as historical traceability and are not part of this demonstration.

The original requirements baseline contained 68 user stories. Thirteen matrix-related records were excluded, leaving 55 active stories. Today, we will demonstrate representative acceptance scenarios for visitors, candidates, administrators, managers, supervisors, coordinators, and advisors.

I will now pass to my teammate, who will explain how we organized the project and why we selected this architecture.

## Person 2 — Scrum, Architecture, and Technical Decisions (2 minutes 30 seconds)

**On screen:** seven-sprint timeline, component diagram, deployment diagram.

We developed BOPADIGITAL through seven Scrum sprints, using ClickUp for planning and the communications repository for reviews and acceptance evidence.

Sprint 1 established repositories, database foundations, quality tools, authentication, and RBAC. Sprint 2 added catalog, CMS, employability, organization, users, the public Web, and initial CRM work. Sprint 3 consolidated the API and client integrations. Sprint 4 strengthened frontend tests and Scrum evidence. Sprint 5 focused on acceptance, integration, risk-based testing, metrics, and defect tracking. Sprint 6 added refactoring, static analysis, CI evidence, security, browser, and accessibility checks. Sprint 7 completed deployment, manuals, the final report, validation, and project closure. Each increment was reviewed, and final client acceptance was recorded after the seven sprints.

Architecturally, Web, CRM, and Mobile are independent clients of one versioned REST API. The API is an Express and TypeScript modular monolith: routes call controllers, controllers call services, and services use Drizzle to access PostgreSQL. This gives clear domain separation without the operational cost of microservices.

The package `@bopacorp/shared` provides Zod schemas, enums, types, and response contracts to the API and clients. React with Vite supports the Web and CRM, while Expo with React Native supports the advisor application. Development used a shared PostgreSQL database hosted by Supabase; production uses PostgreSQL through protected environment configuration. Docker Compose and Caddy provide reproducible deployment and HTTPS routing.

These decisions reuse TypeScript across the ecosystem, centralize authorization and business rules, and prevent clients from accessing the database directly. My teammate will now present how we tested those boundaries and how our process compares with an international testing standard.

## Person 3 — Test Management and Standards Comparison (2 minutes 30 seconds)

**On screen:** test pyramid/evidence table, ISO comparison slide.

### Testing results — approximately 1 minute

Our strategy separates evidence by level. Static analysis and strict TypeScript detect problems before execution. Unit and component suites validate business rules and interfaces. Integration tests verify HTTP contracts, authentication, RBAC, ownership, and validation. Playwright exercises complete browser journeys, while deployment checks remain separate from user acceptance.

The recorded API run contains 61 files and 415 passing tests, with 94.84 percent line coverage. CRM records 12 API and RBAC integration cases and 16 passing Playwright tests. Web records 15 integration checks and 3 passing Chromium journeys. Mobile records 15 suites and 98 tests above its critical-code threshold. The Shared package validates schemas, exports, packaging, and consumer compatibility.

### ISO/IEC/IEEE 29119-1 comparison — approximately 1 minute 30 seconds

We compared our process with ISO/IEC/IEEE 29119-1:2022, especially Sections 4.4 to 4.7: test design and execution, project integration, communication, and incident management.

We **followed** several of its main concepts. First, we selected tests from requirements and project risks, particularly unauthorized access, invalid commercial states, unsafe uploads, lost public requests, and contract drift. Second, we combined approaches instead of depending on one technique: static analysis, scripted unit tests, API integration, browser acceptance, and automated regression in continuous integration. Third, our browser tests used synthetic data and cleanup so that mutable cases could be repeated. We also communicated results through test plans, coverage reports, evidence registers, and artifacts for different repositories.

Our defect handling also reflects the standard. A failed test was treated as an incident requiring investigation, not immediate proof of a software defect. For example, a Web application test failed because its PDF fixture was only four bytes. We corrected the test data to a valid synthetic 10-kilobyte file and executed the mutation suite again successfully.

We **partially followed** the standard because environment-readiness and incident reports were distributed across repositories instead of one formal test-management system. We **did not use** model-based test generation, fuzz testing, A/B testing, or back-to-back testing because they were not selected for our highest project risks. Complete mobile device or emulator smoke testing also remains a limitation. Therefore, BOPADIGITAL demonstrates practical alignment with selected ISO 29119 concepts, but we do not claim certification or full conformance.

We will now show the user-visible acceptance scenarios behind these results.

## Person 4 — Live Demonstration: Public Web, CMS, and Manager (2 minutes 35 seconds)

**On screen:** execute each action; do not narrate screens without showing them.

We begin as a visitor on the public website. The visitor can inspect BOPACORP information, filter the service catalog, open a service, and submit a contact request. This demonstrates public access and form validation without authentication.

Next, we open the employability portal as a candidate. We select a vacancy and first submit incomplete information to show controlled validation. We then attach a valid synthetic PDF résumé and complete the application. This scenario verifies both user feedback and the API file boundary.

Now we use an Administrator account. In the CMS, the administrator opens a content block, edits its text, saves it through the authenticated API, and verifies the change on the public website. After verification, we restore the original value. This shows authorization, persistence, public integration, and safe cleanup in one scenario.

We continue in the CRM as a Manager. The role-aware dashboard summarizes commercial activity, sales funnels, advisor results, and recent operations. In Reports, the manager applies a filter and reviews the resulting indicators. The manager has broader operational visibility, while the API still enforces permissions and record scope.

These scenarios correspond to public catalog and contact, candidate application, administrator content management, and manager reporting acceptance flows. They also show why browser evidence complements unit tests: the browser confirms navigation, rendered feedback, permissions, and the final user-visible result.

My teammate will complete the demonstration with the operational roles and the advisor application.

## Person 5 — Live Demonstration: Advisor, Coordinator, Supervisor, and Mobile (2 minutes 35 seconds)

**On screen:** use prepared records to avoid waiting for data entry or uploads.

We now enter the CRM as a Sales Advisor. The advisor opens an assigned client, creates or reviews a negotiation, records a visit, and uploads a commercial document. Advisor ownership limits which records can be viewed or changed.

Next, we switch to the Documentation Coordinator. The coordinator opens the pending document, reviews its information, and approves or rejects it with the required reason. This demonstrates a controlled state transition, visible feedback, and the separation between uploading a document and deciding its status.

We then use the Supervisor role. The supervisor monitors assigned advisors, checks their commercial activity and visits, and reviews progress without receiving unrestricted administrator access. Together, the Advisor, Coordinator, Supervisor, and Manager sessions make the role differences visible instead of only describing the RBAC matrix.

Finally, we show the Mobile Advisor application. The advisor authenticates and accesses client, negotiation, and document workflows through the same REST API and shared contracts used by the Web clients. Our automated mobile evidence covers these critical modules. However, we explicitly separate that evidence from a complete physical-device qualification, which remains outside the recorded final run.

In conclusion, BOPADIGITAL replaces fragmented commercial work with one role-aware ecosystem. Its final scope is supported by seven accepted Scrum increments, shared architecture, repeatable quality controls, risk-based testing, user manuals, deployment documentation, and formal client acceptance.

Thank you for your attention. We are ready for your questions.

## Final Delivery Checklist

- Use the official ESPOL presentation template.
- Keep the complete live presentation at approximately 13 minutes.
- Ensure all five members speak for approximately the same duration.
- Show one user or persona for every relevant role; do not show Offer Matrices.
- Record the presentation and upload it to the lecturer-designated repository within 24 hours.
- Export and retain the presentation PDF; uploading the slide file is recommended by the project specification.
