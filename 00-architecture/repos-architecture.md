# BOPADIGITAL — Repos Architecture

System-wide architecture of the BOPADIGITAL platform. Source: each repo's `CLAUDE.md` and `docs/`. Repos live in sibling `../proy/`.

## System topology

```
                     ┌──────────────────┐
                     │  @bopacorp/shared │  Zod schemas + TS types
                     │  (GitHub Packages)│  single source of contract
                     └─────────┬────────┘
             ┌─────────────────┼──────────────────┐
             │                 │                  │
     ┌───────▼──────┐   ┌──────▼───────┐   ┌──────▼───────┐
     │ bopacorp-web │   │ bopacorp-crm │   │bopacorp-mobile│
     │ public + CMS │   │ admin CRM    │   │ field app    │
     └───────┬──────┘   └──────┬───────┘   └──────┬───────┘
             │                 │                  │
             └────────► bopacorp-api ◄────────────┘
                        REST /api/v1
                              │
          PostgreSQL (dev: Supabase; prod: deployment server)
```

- All clients talk only to `bopacorp-api` over REST.
- All three clients + api share the contract via `@bopacorp/shared` (no duplicated types).
- API response envelope everywhere: `{ success, data, error: { code, message } }`.

## bopacorp-api — Modular Monolith (backend)

Stack: Node 22+, Express 5, TypeScript 6 (ESM only), Drizzle ORM, PostgreSQL, Zod 4, JWT (bcrypt), Pino, Vitest, Biome.

**Database environments:** Supabase is used as the shared PostgreSQL hosting service for development. It is not the intended production dependency. The production target is a PostgreSQL database hosted on the server where the application is deployed; the API keeps the same Drizzle persistence boundary and receives the environment-specific connection settings through protected configuration.

**Boot**: `src/index.ts` (dotenv + Zod env validation `src/config/env.ts`) → `src/server.ts` (Express app, middleware, route mounting).

**Module pattern** — each domain in `src/modules/[name]/`, exactly 3 files:
- `[name].routes.ts` — endpoints + middleware wiring (auth, validate). No DB, no logic.
- `[name].controller.ts` — parse req, call service, format `res.json()`. No SQL.
- `[name].service.ts` — business logic + Drizzle queries + typed errors. No req/res.

**Dependency flow** (one-way): `routes → controller → service → db`. No `*.schema.ts` in modules — all validation lives in `@bopacorp/shared`.

**Modules**: `auth`, `users`, `roles` (RBAC admin), `catalog` (+ catalog-items, CMS content), `contact-requests`, `org` (departments, employees, advisor-supervisors), `employability` (vacancies, candidates, applications).

**Cross-cutting** `src/shared/`: middleware (auth/validation/errors), error classes (`HttpError` hierarchy), utils (pagination), global types.

Ref: `bopacorp-api/docs/project-structure.md`, `api-conventions.md`, `auth.md`, `cms.md`, `drizzle-guide.md`, `soft-delete.md`.

## bopacorp-crm — admin SPA

Stack: React 19 + TypeScript + Vite + Tailwind v4 + shadcn/ui. Biome. No test framework yet.

- `src/app/` — shell: `MainLayout` (shadcn SidebarProvider + breadcrumb + outlet), `AppSidebar`.
- `src/modules/<domain>/` — feature modules (auth, catalog, negotiations, employability…) with `pages/`, some `components/`, `context/`.
- `src/services/` — Axios client `api.ts` (JWT auth, proactive token refresh, 401 retry queue), `auth-storage.ts` (localStorage tokens).
- `src/shared/ui/` — reusable business components (EntityTable, FilterBar, KpiCard, StateBadge), barrel-exported.
- `src/components/ui/` — shadcn primitives (radix-nova), excluded from Biome.
- `src/App.tsx` — all routes, Spanish paths (`/negociaciones`, `/catalogo`, `/empleabilidad/...`), protected via `<RequireAuth>`.

Patterns: path alias `@/ → src/`; `AuthProvider` listens to `bopacorp:token-refreshed` + `storage` events; typed unwrapping via `request<T>()`; Tailwind v4 CSS-var theming (config in `src/index.css`, no tailwind.config).

Ref: `bopacorp-crm/docs/00-phases-index.md`, `roles-permissions-matrix.md`, `crud-standards`, `Overview.md`.

## bopacorp-web — public site + CMS

Stack: React 19 + TypeScript + Vite 8 + Tailwind v4 + shadcn/ui. UI in Spanish.

- Entry `src/main.tsx` → `<AuthProvider>` → `<App/>` in `<StrictMode>` + `<TooltipProvider>`. React Router v7 declarative routes in `src/App.tsx`.
- `src/components/ui/` shadcn primitives; `src/lib/utils.ts` `cn()`; `src/hooks/`; `src/index.css` global + OKLCH tokens (`:root` / `.dark`).
- Path alias `@/ → ./src/`.
- **Design system authoritative in `DESIGN.md`** — preset `b0` owns colors/fonts/radius. Semantic tokens only (no raw Tailwind colors), no `dark:` overrides (next-themes flips `.dark`), `gap-*` spacing, `size-*` dims, lucide-react icons only.

Ref: `bopacorp-web/docs/arquitectura-modular-frontend-backend.md`, `backend-connection-guide.md`, `cache-strategy.md`, `DESIGN.md`.

## bopacorp-shared — contract package

Stack: Zod 4 + TypeScript 6, ESM, published to GitHub Packages as `@bopacorp/shared`. Consumed by api, web, crm, mobile.

Subpath exports (tree-shakeable):
```
@bopacorp/shared          → src/index.ts (re-exports all)
@bopacorp/shared/common   → primitives (UUID, email, pagination, timestamps), api-response wrappers
@bopacorp/shared/auth     → enums (from SQL CHECK constraints), request + response schemas
```
Publish: `npm version patch && npm publish`.

## Deployment

The deployment plan separates database environments: development uses the shared PostgreSQL service managed through Supabase, while production uses PostgreSQL hosted on the selected deployment server. Provisioning, migrations, access control, backups, and recovery must be verified for the production server before they are reported as completed.

Repo `../proy/deploy` — Docker Compose orchestrates local/prod. `deploy.sh` clones repos (except shared → npm), builds images, runs containers.

| Service | Repo | Host port → container | Notes |
|---------|------|----------------------|-------|
| `api` | bopacorp-api | `3001 → 3000` | Dockerfile.dev, JWT 15m/refresh 7d |
| `crm` | bopacorp-crm | `3002 → 5173` | `VITE_API_URL` → api `/api/v1`, `depends_on: api` |
| `web` | bopacorp-web | `3003 → 5173` | `VITE_API_URL` → api `/api/v1`, `depends_on: api` |

- Needs GitHub Packages `NPM_TOKEN` (`read:packages`) for `@bopacorp/shared`.
- Optional Caddy reverse proxy (`Caddyfile.example`) maps domains → local ports (HTTPS). Default public API host: `api-bopacorp.jointrymyride.com`.

Ref: `../proy/deploy/README.md`, `docker-compose.yml`, `Caddyfile.example`.
