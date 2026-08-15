# Matriz de casos de prueba del CRM

**Última ejecución:** `CRM-F3-2026-08-15-01` sobre el working tree basado en `36ab4bf`.
**Leyenda:** `Existente` significa que el caso aparece en el código actual; `Pendiente` significa que aún debe implementarse o ejecutarse.

## 1. Casos existentes

| ID | Capa | Caso | Archivo | Estado |
|---|---|---|---|---|
| CRM-AUTH-001 | Componente | Redirigir al login sin sesión | `RequireAuth.test.tsx` | Pass — CRM-F2-2026-08-15-01 |
| CRM-AUTH-002 | Componente | Permitir contenido con permiso y rol | `RequirePermission.test.tsx` | Pass — CRM-F2-2026-08-15-01 |
| CRM-AUTH-003 | Componente | Redirigir cuando falta permiso | `RequirePermission.test.tsx` | Pass — CRM-F2-2026-08-15-01 |
| CRM-AUTH-004 | Integración de contexto | Guardar sesión, tokens y usuario al iniciar | `AuthContext.test.tsx` | Pass — CRM-F2-2026-08-15-01 |
| CRM-AUTH-005 | Integración de contexto | Limpiar estado local al cerrar | `AuthContext.test.tsx` | Pass — CRM-F2-2026-08-15-01 |
| CRM-API-001 | Unitario | Desenvolver respuesta `{ success: true }` | `api.test.ts` | Pass — CRM-F2-2026-08-15-01 |
| CRM-API-002 | Unitario | Normalizar sobre de error | `api.test.ts` | Pass — CRM-F2-2026-08-15-01 |
| CRM-API-003 | Unitario | No refrescar 401 en rutas públicas | `api.test.ts` | Pass — CRM-F2-2026-08-15-01 |

> El repositorio actualmente contiene seis declaraciones directas `it(...)` y un `it.each` con tres rutas públicas. La tabla separa comportamientos verificables para el plan; el registro de ejecución debe distinguir entre declaraciones, casos parametrizados y ejecuciones reales.

## 2. Autenticación y API boundary

| ID | Capa | Caso | Prioridad | Estado |
|---|---|---|---|---|
| CRM-AUTH-006 | Unitario | Login inválido muestra error de autenticación | P0 | Pass — CRM-F2-2026-08-15-01 |
| CRM-AUTH-007 | Unitario | `/auth/me` inválido limpia sesión | P0 | Pass — CRM-F2-2026-08-15-01 |
| CRM-AUTH-008 | Unitario | Refresh exitoso actualiza tokens | P0 | Pass — CRM-F2-2026-08-15-01 |
| CRM-AUTH-009 | Unitario | Refresh fallido cierra sesión | P0 | Pass — CRM-F2-2026-08-15-01 |
| CRM-AUTH-010 | Unitario | Requests concurrentes esperan un refresh | P1 | Pass — CRM-F2-2026-08-15-01 |
| CRM-AUTH-011 | Componente | `Can` oculta acción sin permiso | P0 | Pass — CRM-F2-2026-08-15-01 |
| CRM-AUTH-012 | Componente | `Can` filtra por rol | P0 | Pass — CRM-F2-2026-08-15-01 |
| CRM-API-004 | Unitario | Bearer token agregado a request | P0 | Pass — CRM-F2-2026-08-15-01 |
| CRM-API-005 | Unitario | Error de red se normaliza | P1 | Pass — CRM-F2-2026-08-15-01 |
| CRM-API-006 | Unitario | Respuesta paginada conserva metadata | P1 | Pass — CRM-F2-2026-08-15-01 |
| CRM-AUTH-013 | Unitario | Sesión almacenada se restaura desde `/auth/me` | P0 | Pass — CRM-F2-2026-08-15-01 |
| CRM-AUTH-014 | Componente | Cuenta bloqueada muestra el mensaje traducido | P0 | Pass — CRM-F2-2026-08-15-01 |
| CRM-AUTH-015 | Unitario | Storage persiste y elimina tokens actuales y legacy | P0 | Pass — CRM-F2-2026-08-15-01 |
| CRM-AUTH-016 | Unitario | JWT decodifica permisos y usa fallback seguro | P0 | Pass — CRM-F2-2026-08-15-01 |
| CRM-API-007 | Unitario | Servicios de auth envían login, logout y `/auth/me` | P0 | Pass — CRM-F2-2026-08-15-01 |

## 3. Clientes

| ID | Capa | Caso | Prioridad | Estado |
|---|---|---|---|---|
| CRM-CLI-001 | Componente | Crear cliente con datos válidos | P0 | Pass — CRM-F3-2026-08-15-01; `BusinessClientForm.test.tsx` |
| CRM-CLI-002 | Componente | Rechazar RUC inválido | P0 | Pass — CRM-F3-2026-08-15-01; `BusinessClientForm.test.tsx` |
| CRM-CLI-003 | Componente | Rechazar campos obligatorios vacíos | P0 | Pass — CRM-F3-2026-08-15-01; `BusinessClientForm.test.tsx` |
| CRM-CLI-004 | Componente | Rechazar servicios/facturación negativos | P0 | Pass — CRM-F3-2026-08-15-01; `BusinessClientForm.test.tsx` |
| CRM-CLI-005 | Componente | Editar y desactivar cliente | P1 | Pendiente |
| CRM-CLI-006 | Integración frontend | Asesor queda limitado a sus clientes | P0 | Pendiente |
| CRM-CLI-007 | Integración frontend | Supervisor ve alcance supervisado | P0 | Pendiente |
| CRM-CLI-008 | Componente | Búsqueda, filtro y paginación | P1 | Pass — CRM-F3-2026-08-15-01; `useBusinessClients.test.tsx` |
| CRM-CLI-009 | Componente | Estado vacío y error de carga | P1 | Pendiente |

## 4. Negociaciones

| ID | Capa | Caso | Prioridad | Estado |
|---|---|---|---|---|
| CRM-NEG-001 | Componente | Crear negociación válida | P0 | Pass — CRM-F3-2026-08-15-01; `CreateNegotiationDialog.test.tsx`, `NegotiationForm.test.tsx` |
| CRM-NEG-002 | Componente | Editar fechas y observaciones | P1 | Pendiente |
| CRM-NEG-003 | Componente | Asesor no puede seleccionar otro asesor | P0 | Pass — CRM-F3-2026-08-15-01; `CreateNegotiationDialog.test.tsx` |
| CRM-NEG-004 | Componente | Tabla filtra por estado/asesor/tier | P1 | Pass — CRM-F3-2026-08-15-01; `crm-hooks.test.tsx` |
| CRM-NEG-005 | Componente | Kanban agrupa por estado | P1 | Pendiente |
| CRM-NEG-006 | Componente | Cambio de estado válido | P0 | Pass — CRM-F3-2026-08-15-01; `ChangeStateDialog.test.tsx` |
| CRM-NEG-007 | Componente | Estado que requiere nota rechaza nota vacía | P0 | Pass — CRM-F3-2026-08-15-01; `ChangeStateDialog.test.tsx` |
| CRM-NEG-008 | Componente | Drag-and-drop abre cambio bloqueado al destino | P1 | Pendiente |
| CRM-NEG-009 | Integración frontend | Historial refleja transición | P0 | Pendiente |
| CRM-NEG-010 | Componente | Falla de cambio no deja estado falso | P0 | Pass — CRM-F3-2026-08-15-01; `ChangeStateDialog.test.tsx` |
| CRM-NEG-011 | Componente | Cierre exige documentos obligatorios | P0 | Pass — CRM-F3-2026-08-15-01; `ChangeStateDialog.test.tsx`, `negotiations.service.test.ts` |

## 5. Visitas

| ID | Capa | Caso | Prioridad | Estado |
|---|---|---|---|---|
| CRM-VIS-001 | Componente | Crear visita con campos válidos | P0 | Pass — CRM-F3-2026-08-15-01; `CreateVisitSheet.test.tsx` |
| CRM-VIS-002 | Unitario | Geolocalización concedida se transforma correctamente | P1 | Pass — CRM-F3-2026-08-15-01; `CreateVisitSheet.test.tsx` |
| CRM-VIS-003 | Unitario | Permiso GPS denegado no rompe el flujo | P1 | Pass — CRM-F3-2026-08-15-01; `CreateVisitSheet.test.tsx` |
| CRM-VIS-004 | Componente | Observación obligatoria | P0 | Pass — CRM-F3-2026-08-15-01; `CreateVisitSheet.test.tsx` |
| CRM-VIS-005 | Componente | Supervisor verifica visita | P0 | Pass — CRM-F3-2026-08-15-01; `VisitActions.test.tsx` |
| CRM-VIS-006 | Componente | Asesor no ve botón de verificación | P0 | Pass — CRM-F3-2026-08-15-01; `VisitActions.test.tsx` permission gate |
| CRM-VIS-007 | Componente | Error y paginación de visitas | P1 | Pendiente |

## 6. Documentos y archivos

| ID | Capa | Caso | Prioridad | Estado |
|---|---|---|---|---|
| CRM-DOC-001 | Componente | Selección de negociación y tipo | P0 | Pass — CRM-F4-2026-08-15-01; `DocumentUploadDialog.test.tsx` |
| CRM-DOC-002 | Componente | PDF/JPG/PNG válidos | P0 | Pass — CRM-F4-2026-08-15-01; `DocumentUploadDialog.test.tsx` |
| CRM-DOC-003 | Componente | Extensión no permitida | P0 | Pass — CRM-F4-2026-08-15-01; `DocumentUploadDialog.test.tsx` |
| CRM-DOC-004 | Componente | Archivo mayor a 50 MB | P0 | Pass — CRM-F4-2026-08-15-01; `DocumentUploadDialog.test.tsx` |
| CRM-DOC-005 | Componente | Documento inicia pendiente | P0 | Pass — CRM-F4-2026-08-15-01; `documentation.service.test.ts`, `ChangeStateDialog.test.tsx` |
| CRM-DOC-006 | Componente | Aprobar documento autorizado | P0 | Pass — CRM-F4-2026-08-15-01; `DocumentActions.test.tsx` |
| CRM-DOC-007 | Componente | Rechazar sin motivo | P0 | Pass — CRM-F4-2026-08-15-01; `RejectDocumentDialog.test.tsx` |
| CRM-DOC-008 | Componente | Rechazar con motivo | P0 | Pass — CRM-F4-2026-08-15-01; `RejectDocumentDialog.test.tsx` |
| CRM-DOC-009 | Componente | Descargar individual y ZIP | P1 | Pass — CRM-F4-2026-08-15-01; `documentation.service.test.ts` |
| CRM-DOC-010 | Componente | Administrar tipos documentales | P1 | Pass — CRM-F4-2026-08-15-01; `DocumentTypeSheet.test.tsx`, `documentation.service.test.ts` |
| CRM-DOC-011 | Integración API | Proteger endpoints con RBAC | P0 | Pendiente en API |
| CRM-DOC-012 | Integración | Cierre con faltantes retorna error controlado | P0 | Pass frontend — CRM-F4-2026-08-15-01; `ChangeStateDialog.test.tsx`; API real pendiente |

## 7. Matriz limitada

| ID | Capa | Caso | Prioridad | Estado |
|---|---|---|---|---|
| CRM-MAT-001 | Componente | Crear matriz básica | P1 | Pass — CRM-F4-2026-08-15-01; `MatricesTab.test.tsx`, `matrices.service.test.ts` |
| CRM-MAT-002 | Componente | Guardar observaciones | P1 | Pass — CRM-F4-2026-08-15-01; `MatricesTab.test.tsx` |
| CRM-MAT-003 | Componente | Validar extensión de oferta | P1 | Pass — CRM-F4-2026-08-15-01; `MatricesTab.test.tsx` |
| CRM-MAT-004 | Componente | Validar extensión de plantilla | P1 | Pass — CRM-F4-2026-08-15-01; `MatricesTab.test.tsx` |
| CRM-MAT-005 | Componente | Descargar/eliminar adjunto con permiso | P1 | Pass — CRM-F4-2026-08-15-01; `MatricesTab.test.tsx`, `matrices.service.test.ts` |
| CRM-MAT-006 | Alcance | No probar subsidios/aprobación completa descoped | P0 | Declaración de alcance |

## 8. Reportes

| ID | Capa | Caso | Prioridad | Estado |
|---|---|---|---|---|
| CRM-REP-001 | Unitario | Totales con dataset conocido | P0 | Pendiente |
| CRM-REP-002 | Unitario | Estados contados correctamente | P0 | Pendiente |
| CRM-REP-003 | Unitario | Visitas y días promedio | P1 | Pendiente |
| CRM-REP-004 | Integración frontend | Supervisor limitado a equipo | P0 | Pendiente |
| CRM-REP-005 | Componente | Filtro de fechas | P1 | Pendiente |
| CRM-REP-006 | Componente | Tabla vacía y carga | P1 | Pendiente |
| CRM-REP-007 | Unitario | CSV conserva headers/valores | P0 | Pendiente |
| CRM-REP-008 | Componente | Generar exportación autorizado | P1 | Pendiente |

## 9. Catálogo, organización y empleabilidad

| ID | Capa | Caso | Prioridad | Estado |
|---|---|---|---|---|
| CRM-CAT-001 | Componente | Validar producto general | P1 | Pendiente |
| CRM-CAT-002 | Componente | Campos técnicos por tipo | P1 | Pendiente |
| CRM-CAT-003 | Componente | Beneficios y condiciones | P1 | Pendiente |
| CRM-CAT-004 | Componente | Publicar/activar producto | P1 | Pendiente |
| CRM-ORG-001 | Componente | Crear usuario y empleado | P1 | Pendiente |
| CRM-ORG-002 | Componente | Separar rol de acceso/organizacional | P0 | Pendiente |
| CRM-ORG-003 | Componente | Desbloquear con motivo válido | P0 | Pendiente |
| CRM-ORG-004 | Componente | Rechazar motivo corto | P1 | Pendiente |
| CRM-EMP-001 | Componente | Crear vacante válida | P1 | Pendiente |
| CRM-EMP-002 | Componente | Validar fechas de vacante | P1 | Pendiente |
| CRM-EMP-003 | Componente | Filtrar postulantes por estado | P1 | Pendiente |
| CRM-EMP-004 | Componente | Cambiar estado con notas | P1 | Pendiente |
| CRM-EMP-005 | Componente | Descargar CV autorizado | P1 | Pendiente |

## 10. End-to-end

| ID | Perfil | Journey | Prioridad | Estado |
|---|---|---|---|---|
| CRM-E2E-001 | Asesor | Login → cliente → negociación → visita | P0 | Pendiente |
| CRM-E2E-002 | Asesor | Documentar negociación | P0 | Pendiente |
| CRM-E2E-003 | Supervisor/coordinador | Revisar documento | P0 | Pendiente |
| CRM-E2E-004 | Manager/supervisor | Reporte y CSV | P1 | Pendiente |
| CRM-E2E-005 | Manager | Catálogo u organización | P1 | Pendiente |
| CRM-E2E-006 | Manager/web-admin | Vacante y postulante | P1 | Pendiente |
| CRM-E2E-007 | Perfil no autorizado | Ruta y acción protegida | P0 | Pendiente |

## 11. Regla de estados

- `Existente / ejecución pendiente`: el test está en el código, pero falta una ejecución registrada.
- `Pendiente`: falta crear el test o ejecutar el caso.
- `Pass`: solo después de guardar evidencia actual.
- `Fail`: el comportamiento observado no cumple el resultado esperado.
- `Blocked`: falta ambiente, cuenta, dato o dependencia externa; debe incluir motivo.
- `Descoped`: fuera del producto actual por una decisión de alcance documentada.

## 12. Ejecución de Fase 3

| Campo | Valor |
|---|---|
| ID de ejecución | `CRM-F3-2026-08-15-01` |
| Revisión base | `36ab4bf16a16b9d97d5d668e5ec7542c7b0a75ee` |
| Estado de revisión | Working tree con cambios de Fase 3 sin commit |
| Tests | Pass; 20 archivos y 84 tests |
| Cobertura | Pass informativo; 84.48% statements, 70.15% branches, 82.72% functions, 84.97% lines |
| Conjunto medido | 21 archivos críticos incluidos explícitamente en `vite.config.ts` |
| Lint | Pass; 241 archivos revisados |
| TypeScript | Pass; `npx tsc -b --noEmit` |
| Build | Pass; Vite transformó 3820 módulos |
| Artefactos | `coverage/index.html`, `coverage/lcov.info` |
| CI remoto/API real/E2E | Pendiente |

## 13. Ejecución de Fase 4

| Campo | Valor |
|---|---|
| ID de ejecución | `CRM-F4-2026-08-15-01` |
| Revisión base | `68790800a4aede85bcacf9a197445cc5a59dd12b` |
| Estado de revisión | Working tree con cambios de Fase 4 sin commit |
| Tests | Pass; 28 archivos y 116 tests |
| Cobertura | Pass informativo; 80.97% statements, 64.85% branches, 76.88% functions, 82.12% lines |
| Conjunto medido | 33 archivos críticos incluidos explícitamente en `vite.config.ts` |
| Lint | Pass; 250 archivos revisados |
| TypeScript | Pass; `npx tsc -b --noEmit` |
| Build | Pass; Vite transformó 3820 módulos |
| Artefactos | `coverage/index.html`, `coverage/lcov.info` |
| CI remoto/API real/E2E | Pendiente |
