# Trazabilidad funcional del manual

Este documento permite demostrar que los procedimientos del manual fueron construidos a partir del sistema y no de pantallas inventadas.

## Fuentes principales

| Fuente | Qué se verificó |
|---|---|
| `bopacorp-crm/src/App.tsx` | Rutas protegidas y guardas de autenticación/permisos. |
| `bopacorp-crm/src/app/Sidebar.tsx` | Menú visible por permisos y perfiles. |
| `bopacorp-crm/src/modules/*/pages` | Pantallas, filtros, tablas y navegación. |
| `bopacorp-crm/src/modules/*/components` | Formularios, diálogos, validaciones y acciones. |
| `bopacorp-crm/src/services/api.ts` | Comunicación con la API y manejo de sesión. |
| `bopacorp-api/src/server.ts` | Módulos y prefijos de las rutas REST. |
| `bopacorp-api/src/scripts/seed-role-permissions.ts` | Permisos iniciales por rol. |
| `bopacorp-shared/src/*` | Schemas, tipos, estados y reglas de entrada. |
| `bopacorp-crm/docs/roles-permissions-matrix.md` | Diseño documentado de roles y alcance. |
| `bopacorp-crm/docs/gaps/requirements-audit.md` | Limitaciones conocidas del alcance actual. |

## Mapa de procedimientos

| Procedimiento del manual | Frontend | API | Shared |
|---|---|---|---|
| Inicio de sesión | `modules/auth/pages/LoginPage.tsx`, `AuthContext.tsx` | `/api/v1/auth` | `auth/request.ts`, `auth/response.ts` |
| Clientes | `modules/clients` | `/api/v1/crm/business-clients` | `crm/request.ts` |
| Negociaciones | `modules/negotiations` | `/api/v1/crm/negotiations` | `crm/request.ts` |
| Visitas | `negotiations/components/CreateVisitSheet.tsx` | `/api/v1/crm/visits` | `crm/request.ts` |
| Documentación | `modules/documentation` | `/api/v1/documents`, `/document-uploads` | `documents`, `document-uploads` |
| Matrices | `negotiations/components/MatricesTab.tsx` | `/api/v1/matrices` | `matrices` |
| Reportes | `modules/reports` | `/api/v1/reports` | `reports` |
| Catálogo | `modules/catalog` | `/api/v1/catalog`, `/catalog-items` | `catalog` |
| Organización | `modules/org` | `/api/v1/org`, `/users` | `auth`, `core` |
| Empleabilidad | `modules/employability` | `/api/v1/employability` | `employability` |

## Limitaciones que el manual sí debe declarar

| Área | Situación actual |
|---|---|
| Matrices | La implementación actual cubre matriz básica, observaciones y dos espacios de adjuntos. No cubre líneas, subsidios ni aprobación completa. |
| Reportes | La exportación visible genera CSV. La especificación original menciona PDF/Excel, pero no debe afirmarse como disponible. |
| Notificaciones | El componente muestra notificaciones recientes; no existe una página histórica completa en el CRM actual. |
| Documentación | El resumen de pendientes depende de un endpoint cuya disponibilidad debe confirmarse en el ambiente desplegado. |
| Catálogo/CMS | Los bloques de contenido CMS aparecen en planificación, pero no forman parte de las rutas actuales de este CRM. |
| Empleabilidad | El CRM tiene páginas de vacantes y postulantes; no existe una página de administración de candidatos independiente. |
| Seguridad de sesión | Existe refresco automático de token, pero no se debe presentar como un cierre automático por inactividad. |

## Diferencias documentales encontradas

- `README.md` enlaza a `docs/CRM_FRONTEND_SYSTEM_PLAN.md`, pero el documento actual se encuentra como `docs/Overview.md`.
- Algunos documentos de fases describen funcionalidades planificadas que fueron reducidas o cambiaron de ruta.
- `CLAUDE.md` todavía indica que no existe framework de pruebas, aunque el checkout actual contiene pruebas Vitest/React Testing Library y configuración de CI.

Estas diferencias se conservan aquí para que el manual de usuario no las mezcle con funcionalidades confirmadas.
