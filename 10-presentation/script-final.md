# BOPADIGITAL Final Presentation Script — 13 Minutes

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

Good morning. We are Team 2, and today we will present BOPADIGITAL. We developed this digital sales platform for BOPACORP S.A., an Ecuadorian telecommunications company and a commercial partner of Movistar Ecuador.

The project started because the company had three main problems. First, employees sent commercial documents through different channels. This caused delays and extra visits to the office. Second, supervisors and managers could not easily see advisor visits or negotiation progress. Third, the company used many spreadsheets and manual messages to manage clients and prepare sales reports.

Our goal was to put this business sales process in one digital system. The final solution has a public website and job portal, a content management system, an internal CRM, a mobile application for advisors, a REST API, and a shared TypeScript package.

The final scope includes login, role permissions, clients, negotiations, visits, documents, reports, the service catalog, public content, vacancies, job applications, company settings, and mobile tasks. The client removed Offer Matrices, subsidy calculations, and their approval process from the final scope. For this reason, we will not show those features today.

The first requirements document had 68 user stories. We removed 13 stories related to Offer Matrices, so the final product has 55 active stories. Today, we will show important cases for visitors, candidates, administrators, managers, supervisors, coordinators, and advisors.

Now, my teammate will explain how we organized the project and why we chose this architecture.

## Person 2 — Scrum, Architecture, and Technical Decisions (2 minutes 30 seconds)

We developed BOPADIGITAL in seven Scrum sprints and used ClickUp to plan the work. Sprint 1 created the foundations, login, and role permissions. Sprints 2 and 3 added the business features and API integration. Sprints 4 to 6 focused on testing, risk, security, and CI. Sprint 7 completed deployment, manuals, validation, and project closure. Each sprint included planning, review, and retrospective activities. The client reviewed the stages and gave final acceptance after Sprint 7.

Web, CRM, and Mobile communicate with one REST API. The API uses Express and TypeScript, with routes, controllers, and services. Drizzle connects the services with PostgreSQL. The Shared package keeps data types and validation consistent across the applications. This modular structure separates the business areas while keeping one backend.

The source code and packages come from GitHub. We also used feature branches, Pull Requests, reviews, and CI checks before integration. A deployment script starts Web, CRM, and API with Docker Compose on the server. Caddy provides secure HTTPS access and domain routing. The API connects to PostgreSQL and file storage.

We compared alternatives before selecting the stack. We selected React and Vite over Angular or Vue because the team already knew React and development time was limited. Express kept the API in TypeScript instead of adding Django or Laravel. PostgreSQL fit our business rules and data-integrity needs better than MySQL. Expo reused our React and TypeScript knowledge instead of adding Flutter or separate native applications. Docker Compose was more repeatable than starting every service manually.

These decisions gave us one consistent TypeScript ecosystem. Next, my teammate will present testing and standards.

## Person 3 — Test Management and Standards Comparison (2 minutes 30 seconds)

**On screen:** test pyramid/evidence table, ISO comparison slide.

### Testing results — approximately 1 minute

We organized our tests in different levels. Static analysis and strict TypeScript find some problems before the program runs. Unit and component tests check business rules and screen behavior. Integration tests check HTTP responses, login, role permissions, record ownership, and input validation. Playwright checks full tasks in a real browser. We keep deployment checks separate because they do not prove that a user task works.

The recorded API run has 61 files and 415 passing tests, with 94.84 percent line coverage. CRM has 12 API and permission integration cases, plus 16 passing Playwright tests. Web has 15 integration checks and 3 passing Chromium tests. Mobile has 15 test suites and 98 passing tests above the required coverage for critical code. The Shared package checks its data rules, public files, package, and use by the four applications.

### ISO/IEC/IEEE 29119-1 comparison — approximately 1 minute 30 seconds

We compared our work with ISO/IEC/IEEE 29119-1:2022, mainly Sections 4.4 to 4.7. These sections cover test design, project planning, communication, and test problems.

We **followed** several important ideas. We selected tests from the requirements and the main risks, such as access without permission, incorrect business states, unsafe uploads, lost public requests, and different data formats. We also combined several methods: static analysis, planned unit tests, API integration tests, browser acceptance tests, and automatic regression tests in CI. Our browser tests used safe artificial data and cleanup steps, so we could repeat them without leaving unwanted records. We reported results through test plans, coverage reports, evidence tables, and test files.

We also investigated failures before calling them software defects. For example, one Web test failed because its PDF test file had only four bytes. We changed it to a valid artificial 10-kilobyte PDF and ran the test again successfully.

We **partially followed** the standard because environment and incident reports were stored in different repositories, not in one formal test system. We **did not use** model-based test generation, fuzz testing, A/B testing, or tests that compare two versions. These methods were not selected for our main risks. A complete test on a real mobile device or emulator is also missing. Therefore, we follow selected ISO 29119 ideas, but we do not claim full certification.

We will now show the user-visible acceptance scenarios behind these results.

## Person 4 — Live Demonstration: Public Web, CMS, and Manager (2 minutes 35 seconds)

**On screen:** execute each action; do not narrate screens without showing them.

We begin as a visitor on the public website. The visitor can read information about BOPACORP, filter the service catalog, open a service, and send a contact request. This shows public access and form validation without a login.

Next, we open the job portal as a candidate. We select a vacancy and first send an incomplete form to show the validation messages. Then, we attach a valid artificial PDF résumé and complete the application. This case shows clear user feedback and safe file validation by the API.

Now, we use an Administrator account. In the CMS, the administrator opens a content block, changes its text, and saves it through the API. We check the new text on the public website. After this check, we restore the original text. This one case shows permission control, saved data, communication between Web and API, and safe cleanup.

We continue in the CRM as a Manager. The dashboard shows sales activity, the sales process, advisor results, and recent work. In the Reports section, the manager applies a filter and checks the results. The manager can see more business information, but the API still checks permissions and which records the user can access.

These cases cover the public catalog, contact requests, job applications, content management, and manager reports. They also show why browser tests are useful. A browser test checks navigation, messages, permissions, and what the user finally sees.

My teammate will finish the demonstration with the other business roles and the mobile application.

## Person 5 — Live Demonstration: Advisor, Coordinator, Supervisor, and Mobile (2 minutes 35 seconds)

**On screen:** use prepared records to avoid waiting for data entry or uploads.

We now enter the CRM as a Sales Advisor. The advisor opens an assigned client, creates or checks a negotiation, records a visit, and uploads a commercial document. The ownership rules limit which records the advisor can see or change.

Next, we change to the Documentation Coordinator. The coordinator opens the pending document, checks its information, and approves or rejects it with a required reason. This shows a controlled status change and clear feedback. It also shows that uploading a document and deciding its final status are different responsibilities.

We then use the Supervisor role. The supervisor checks assigned advisors, their sales work, their visits, and their progress. The supervisor does not receive full administrator access. The Advisor, Coordinator, Supervisor, and Manager sessions show the differences between the roles instead of only showing a permissions table.

Finally, we show the Mobile Advisor application. The advisor logs in and opens client, negotiation, and document tasks. Mobile uses the same REST API and shared data rules as the Web applications. Our automatic mobile tests cover these important modules. However, those tests are not the same as a complete test on a real phone. That full device test is not part of our recorded final results.

In conclusion, BOPADIGITAL changes separate manual sales tasks into one connected system with clear user roles. The final product is supported by seven accepted Scrum sprints, one shared architecture, repeatable quality checks, risk-based testing, user manuals, deployment documents, and final client acceptance.

Thank you for your attention. We are ready for your questions.

## Final Delivery Checklist

- Use the official ESPOL presentation template.
- Keep the complete live presentation at approximately 13 minutes.
- Ensure all five members speak for approximately the same duration.
- Show one user or persona for every relevant role; do not show Offer Matrices.
- Record the presentation and upload it to the lecturer-designated repository within 24 hours.
- Export and retain the presentation PDF; uploading the slide file is recommended by the project specification.
