# Manual Slide Guide for the BOPADIGITAL Presentation

## Purpose

Use this guide to create the slides manually with the official ESPOL template. Slides support the live pitch; they must not replace the live software demonstration. Keep text brief, use evidence from `BOPADIGITAL/mainETS_english_se2.tex`, and do not include Offer Matrices.

## Speaker Order

1. Person 1 — introduction and final scope
2. Person 2 — Scrum and architecture
3. Person 3 — testing and ISO 29119 comparison
4. Person 4 — public Web, CMS, and Manager demonstration
5. Person 5 — operational roles, Mobile, and conclusion

## Slide and Pitch Sequence

| Time | Slide | Speaker | Manual slide content | Change cue |
|---|---:|---|---|---|
| 0:00 | 1 | Person 1 | **BOPADIGITAL**; client; Team 2; five names; ESPOL identity | Start after greeting. |
| 0:20 | 2 | Person 1 | Three problems: document delays, limited field visibility, manual sales tracking | Change after introducing BOPACORP. |
| 1:05 | 3 | Person 1 | Final ecosystem: Web, CMS, CRM, Mobile, API, Shared | Change at “Our objective was…” |
| 1:45 | 4 | Person 1 | **55 active stories**, 7 sprints, excluded Offer Matrices, demonstrated roles | Change at “The original requirements…” |
| 2:30 | 5 | Person 2 | Seven-sprint horizontal timeline and final acceptance | Change when Person 2 begins. |
| 3:20 | 6 | Person 2 | Component diagram: clients → REST API → PostgreSQL; Shared contracts | Change at “Architecturally…” |
| 4:10 | 7 | Person 2 | Deployment diagram and technical decisions: React/Vite, Expo, Express, Drizzle, Docker, Caddy | Change at “The package…” |
| 5:00 | 8 | Person 3 | Testing levels: static, unit/component, integration, browser acceptance, deployment checks | Change when Person 3 begins. |
| 5:35 | 9 | Person 3 | Exact result cards: API 415; CRM 12 integration and 16 browser; Web 15 integration and 3 browser; Mobile 98 | Change at “The recorded API run…” |
| 6:00 | 10 | Person 3 | ISO 29119 comparison with three columns: **Followed**, **Partial**, **Not demonstrated** | Keep visible for the complete 1:30 comparison. |
| 7:30 | 11 | Person 4 | **LIVE DEMONSTRATION** title and scenario checklist only | Change when Person 4 begins; then leave presentation mode. |
| 10:05 | 12 | Person 5 | **LIVE DEMONSTRATION — Operational roles and Mobile** | Show briefly during speaker handoff, then return to live applications. |
| 12:15 | 13 | Person 5 | Conclusion: centralized platform, role-aware workflows, testing evidence, seven accepted sprints | Return to slides after the final live action. |
| 12:40 | 14 | Team | “Thank you — Questions”; repository/demo QR or public link if approved | Change after the conclusion. |

## Live Demonstration Block — 7:30 to 12:15

Do not fill this time with screenshots or prerecorded slide video. Exit presentation mode and show the running applications. Keep Slide 11 or 12 available only as a recovery screen.

### Person 4 — 7:30 to 10:05

1. **Visitor:** filter the catalog and open a service.
2. **Candidate:** show validation and submit a synthetic PDF application.
3. **Administrator:** edit a CMS text block, verify it publicly, then restore it.
4. **Manager:** open the dashboard and apply one report filter.

### Person 5 — 10:05 to 12:15

1. **Advisor:** open an assigned client, negotiation, visit, and document.
2. **Coordinator:** review the pending document and show approve/reject controls.
3. **Supervisor:** show scoped advisor monitoring and activity.
4. **Mobile Advisor:** show authentication and client, negotiation, and document navigation.

Use prepared synthetic records. Avoid typing long forms, waiting for uploads, exposing credentials, or improvising unsupported features. If a live component fails, explain the expected result briefly and use one clearly labeled backup screenshot; do not claim that the failed action passed.

## Slide Design Rules

- Use the official ESPOL template and consistent colors, fonts, and margins.
- Prefer one diagram, timeline, screenshot, or result table per slide.
- Use no more than five short bullets and avoid paragraphs from the report.
- Display testing values with their layer; never combine unrelated test counts.
- Keep the ISO slide visual: check mark for followed, warning for partial, dash for not demonstrated.
- Add source notes such as “Final report, Chapters 2 and 6” in small text.
- Rehearse slide changes and live-session logins before recording the classroom presentation.

## Final Manual Check

- Total duration is approximately 13 minutes.
- ISO comparison lasts approximately 1 minute 30 seconds.
- All five members participate for similar durations.
- Every relevant role appears in the pitch or live demonstration.
- Slides and spoken claims match the final report.
- The live presentation is recorded and uploaded within 24 hours.
