# BOPADIGITAL — Context Repo

Context and reference documents for the **BOPADIGITAL** project. Used by agents building extra features on top of the platform.

## Project

- **Client**: BOPACORP S.A. — telecom company, strategic commercial partner of Movistar Ecuador.
- **System**: BOPADIGITAL — digitizes and centralizes the complete B2B telecom sales lifecycle.
- **Course**: ESPOL, Software Engineering II midterm project (Team T2).

## Codebase (separate repos, sibling `../proy/`)

| Repo | Role | Stack |
|------|------|-------|
| `bopacorp-api` | Single backend (REST) | Node 22+, Express 5, TS 6 ESM, PostgreSQL (Supabase for development), Drizzle, Zod 4, JWT, Vitest, Biome |
| `bopacorp-crm` | CRM frontend (supervisors/coordinators) | React + Vite + TS |
| `bopacorp-web` | Landing + CMS frontend | React + Vite + TS |
| `bopacorp-shared` | Shared Zod schemas/types (`@bopacorp/shared`) | TS |
| `bopacorp-mobile` | Field app (referenced, not in tree) | — |
| `communications` | Client comms evidence | — |
| `deploy` | Production deploy | Docker, Caddy |

## Document index

### 00-architecture/
- `repos-architecture.md` — **system-wide architecture** of all repos: topology, api modular-monolith module rules, crm/web structure, shared contract, deployment (ports, Docker Compose, Caddy). Read this first when building features.

### 01-project-spec/
- `01ProjectSpec_FirstEval_en.md` — academic project specification (objectives, deliverables, marking scheme).

### 02-requirements/
- `BOPADIGITAL_REQUIREMENTS_SPECIFICATION_DOCUMENT.md` — full requirements specification (SRS).
- `AUDITORIA_REQUISITOS_BOPADIGITAL.md` / `.pdf` — requirements audit.

### 03-scrum/
- `BOPADIGITAL_Scrum_Final_Corregido.md` — SCRUM evidence (backlog, planning, roles).

### 04-business/
- `GUIA_COMERCIAL.pdf` — commercial guide (sales domain context).
- `info_web.md` / `info_web.docx` — web/landing info.

### 05-reports/
- `T2BOPADIGITAL.pdf` — final project deliverable report.
- `InformeFinalPracticasEmpresariales.docx` — final internship report.

### 08-testing-plan-shared/
- `PLAN_TESTING_SHARED.md` — shared package testing strategy and execution by phase.
- `PHASE6_CONSUMER_COMPATIBILITY.md` — package exports, artifact and consumer compatibility evidence.

### 99-reference-nintventario/
- `Development_Report___Nintventario.md` / `.pdf` — **different project (Nintventario)**, kept as reference/example only. Not part of BOPADIGITAL scope.

## Notes for agents

- Primary source of truth for requirements: `02-requirements/`.
- Domain vocabulary and sales flow: `04-business/` + requirements SRS.
- Nintventario docs are reference material, not BOPADIGITAL requirements — do not implement from them.
