# Registro de evidencia de testing — CRM

Este archivo se debe completar durante la ejecución. No registrar `Pass` por inspección estática.

## 1. Identificación de ejecución

| Campo | Valor |
|---|---|
| ID de ejecución | `CRM-F1-2026-08-15-01` |
| Fecha/hora | `2026-08-15T15:31:47-05:00` |
| Tester | Codex agent |
| Repositorio CRM | `/home/gabrieltumbaco/code/BOPACORP/bopacorp-crm` |
| SHA CRM | `57cb6a6b8fa16743984b8b2598466bb16a135ffd` |
| SHA API | Pendiente o N/A |
| SHA shared | Pendiente o N/A |
| Node/npm | `v22.22.2 / 10.9.7` |
| Sistema operativo | `Linux 7.1.3-101.fc43.x86_64 x86_64` |
| Navegador/dispositivo | N/A; pruebas Vitest en `jsdom` |
| Ambiente/base URL | `VITE_API_URL=http://test.local/api/v1` (solo test; sin secretos) |

## 2. Comandos base

| Comando | Resultado | Duración | Artifact |
|---|---|---:|---|
| `npm ci` | Pass; 678 paquetes instalados y auditados | ~32 s | Salida de npm |
| `npm run test:run` | Pass; 4 archivos y 9 tests | 14.36 s | Log de consola |
| `npm run test:coverage` | Pass; 4 archivos y 9 tests | 16.10 s | `coverage/index.html`, `coverage/lcov.info` |
| `npm run lint` | Pass; 223 archivos revisados, sin fixes | 0.43 s | Log de consola |
| `npx tsc -b --noEmit` | Pass; sin errores | ~29 s | Log de consola |
| `npm run build` | Pass; Vite transformó 3820 módulos | ~29 s | Log de consola; `dist/` ignorado |
| `npm run test:e2e` | No ejecutado; fuera del alcance de Fase 1 | — | — |

Nota de entorno: la primera ejecución aislada de `npm ci` no pudo escribir los logs de npm dentro del sandbox y terminó con `Exit handler never called`. Se repitió la misma instalación con acceso de ejecución aprobado y finalizó correctamente; no se identificó un defecto del proyecto. La auditoría de npm informó 11 vulnerabilidades (3 moderadas y 8 altas); `npm audit fix` no se ejecutó porque queda fuera del alcance de esta fase.

## 3. Resultado por caso

| Caso | Requisito/riesgo | Precondiciones | Resultado esperado | Observado | Estado | Evidencia | Defecto/retest |
|---|---|---|---|---|---|---|---|
| `CRM-AUTH-001` | Auth/RBAC | Sin sesión | Redirige a login | Pendiente | Not run | Pendiente | — |
| `CRM-CLI-001` | Cliente válido | Cuenta y datos semilla | Cliente creado | Pendiente | Not run | Pendiente | — |
| `CRM-NEG-006` | Estado comercial | Negociación editable | Estado cambia y crea historial | Pendiente | Not run | Pendiente | — |
| `CRM-VIS-005` | Verificación | Visita pendiente, rol supervisor | Visita verificada | Pendiente | Not run | Pendiente | — |
| `CRM-DOC-007` | Documento/rechazo | Documento pendiente | Motivo obligatorio | Pendiente | Not run | Pendiente | — |
| `CRM-REP-007` | Cálculo/exportación | Dataset conocido | CSV con columnas y valores correctos | Pendiente | Not run | Pendiente | — |
| `CRM-E2E-001` | Journey comercial | Cuenta asesor | Flujo completo exitoso | Pendiente | Not run | Pendiente | — |

## 4. Resumen de cobertura

| Conjunto | Statements | Branches | Functions | Lines | Fecha | Artifact |
|---|---:|---:|---:|---:|---|---|
| Archivos actuales de baseline (4 archivos configurados originalmente) | 47.02% | 34.72% | 50.00% | 45.80% | 2026-08-15 | Resumen de consola; reemplazado localmente por el reporte crítico |
| Código crítico fase 2 (10 archivos de auth/API) | 40.17% | 22.22% | 42.37% | 39.63% | 2026-08-15 | `coverage/index.html`, `coverage/lcov.info` |
| Código crítico fase 2 después de implementar pruebas | 92.76% | 80.34% | 98.30% | 93.11% | 2026-08-15 | `coverage/index.html`, `coverage/lcov.info` |
| Código crítico Fase 3 (21 archivos configurados) | 84.48% | 70.15% | 82.72% | 84.97% | 2026-08-15 | `coverage/index.html`, `coverage/lcov.info` |
| Código crítico Fase 4 (33 archivos configurados) | 80.97% | 64.85% | 76.88% | 82.12% | 2026-08-15 | `coverage/index.html`, `coverage/lcov.info` |
| Código crítico final | — | — | — | — | Pendiente | Pendiente |

## 5. Ejecución en CI

| Campo | Valor |
|---|---|
| URL del workflow | Pendiente |
| Run ID | Pendiente |
| SHA | Pendiente |
| Fecha | Pendiente |
| Resultado | Pendiente |
| Artifact de cobertura | Pendiente |
| Artifact E2E | Pendiente |
| Persona que revisó | Pendiente |

## 6. Defectos y retests

| Defecto | Caso | Síntoma | Fix SHA | Fecha fix | Retest | Evidencia |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

## 7. Regla de publicación

Un resultado puede aparecer como `Pass` en el informe final solamente si existe:

1. caso identificado;
2. revisión conocida;
3. resultado observado;
4. artifact o captura reproducible;
5. retest registrado cuando hubo defecto.

## 8. Ejecución de Fase 2

| Campo | Valor |
|---|---|
| ID de ejecución | `CRM-F2-2026-08-15-01` |
| Fecha/hora | `2026-08-15T15:43:41-05:00` |
| Revisión base | `3c4dd5175acda0be1a7119e136f2c22572a8b41b` |
| Estado de revisión | Working tree con cambios de Fase 2 sin commit |
| Tests | Pass; 10 archivos y 49 tests |
| Cobertura | Pass; 92.76% statements, 80.34% branches, 98.30% functions, 93.11% lines |
| Lint | Pass; 230 archivos revisados |
| TypeScript | Pass; `npx tsc -b --noEmit` |
| Build | Pass; Vite transformó 3820 módulos |
| Artefactos | `coverage/index.html`, `coverage/lcov.info` |
| CI remoto | Pendiente; no marcar Pass por inspección local |

### Casos Fase 2 ejecutados

| Caso | Resultado observado | Estado | Evidencia |
|---|---|---|---|
| `CRM-AUTH-006` a `CRM-AUTH-016` | Login, sesión, permisos, roles, storage y JWT exitosos | Pass | `CRM-F2-2026-08-15-01`; reporte de cobertura |
| `CRM-API-004` a `CRM-API-007` | Bearer, errores, paginación, refresh y servicios auth exitosos | Pass | `CRM-F2-2026-08-15-01`; reporte de cobertura |

## 9. Ejecución de Fase 3

| Campo | Valor |
|---|---|
| ID de ejecución | `CRM-F3-2026-08-15-01` |
| Fecha/hora | `2026-08-15T16:10:00-05:00` |
| Revisión base | `36ab4bf16a16b9d97d5d668e5ec7542c7b0a75ee` |
| Estado de revisión | Working tree con cambios de Fase 3 sin commit |
| Node/npm | `v22.22.2 / 10.9.7` |
| Ambiente/base URL | `VITE_API_URL=http://test.local/api/v1` (solo test; sin secretos) |
| Tests | Pass; 20 archivos y 84 tests |
| Cobertura | Pass informativo; 84.48% statements, 70.15% branches, 82.72% functions, 84.97% lines |
| Conjunto medido | 21 archivos críticos incluidos explícitamente en `vite.config.ts` |
| Lint | Pass; 241 archivos revisados |
| TypeScript | Pass; `npx tsc -b --noEmit` |
| Build | Pass; Vite transformó 3820 módulos |
| Artefactos | `coverage/index.html`, `coverage/lcov.info` |
| CI remoto/API real/E2E | Pendiente |

### Casos Fase 3 ejecutados

| Caso | Resultado observado | Estado | Evidencia |
|---|---|---|---|
| `CRM-CLI-001` a `CRM-CLI-004` | Formulario de cliente válido, RUC inválido, obligatorios y valores negativos | Pass | `BusinessClientForm.test.tsx`; `CRM-F3-2026-08-15-01` |
| `CRM-CLI-008` | Hook envía búsqueda, advisor, estado, orden y paginación | Pass | `useBusinessClients.test.tsx`; `CRM-F3-2026-08-15-01` |
| `CRM-NEG-001`, `CRM-NEG-003`, `CRM-NEG-004` | Creación, ownership del asesor y filtros | Pass | `CreateNegotiationDialog.test.tsx`; `crm-hooks.test.tsx` |
| `CRM-NEG-006`, `CRM-NEG-007`, `CRM-NEG-010`, `CRM-NEG-011` | Cambio válido, nota obligatoria, fallo controlado y documentos obligatorios | Pass | `ChangeStateDialog.test.tsx`; `negotiations.service.test.ts` |
| `CRM-VIS-001` a `CRM-VIS-006` | Creación, GPS concedido/denegado, observación y permisos de acciones | Pass | `CreateVisitSheet.test.tsx`; `VisitActions.test.tsx` |

Los casos de edición visual, páginas de alcance por supervisor, Kanban/drag-and-drop, historial observable y estados vacíos/error que no aparecen aquí permanecen `Pendiente`. La suite usa mocks y jsdom; no demuestra todavía autorización ni persistencia de un API real.

## 10. Ejecución de Fase 4

| Campo | Valor |
|---|---|
| ID de ejecución | `CRM-F4-2026-08-15-01` |
| Fecha/hora | `2026-08-15T17:00:50-05:00` |
| Revisión base | `68790800a4aede85bcacf9a197445cc5a59dd12b` |
| Estado de revisión | Working tree con cambios de Fase 4 sin commit |
| Node/npm | `v22.22.2 / 10.9.7` |
| Ambiente/base URL | `VITE_API_URL=http://test.local/api/v1` (solo test; sin secretos) |
| Tests | Pass; 28 archivos y 116 tests |
| Cobertura | Pass informativo; 80.97% statements, 64.85% branches, 76.88% functions, 82.12% lines |
| Conjunto medido | 33 archivos críticos incluidos explícitamente en `vite.config.ts` |
| Lint | Pass; 250 archivos revisados |
| TypeScript | Pass; `npx tsc -b --noEmit` y `npm run build` |
| Build | Pass; Vite transformó 3820 módulos |
| Artefactos | `coverage/index.html`, `coverage/lcov.info` |
| CI remoto/API real/E2E | Pendiente |

### Casos Fase 4 ejecutados

| Caso | Resultado observado | Estado | Evidencia |
|---|---|---|---|
| `CRM-DOC-001` a `CRM-DOC-005` | Selección, formatos válidos, extensión inválida, límite de tamaño y estado pendiente | Pass | `DocumentUploadDialog.test.tsx`; `documentation.service.test.ts`; `CRM-F4-2026-08-15-01` |
| `CRM-DOC-006` a `CRM-DOC-010` | Aprobación, rechazo, permisos, descargas y administración de tipos | Pass | `DocumentActions.test.tsx`; `RejectDocumentDialog.test.tsx`; `DocumentTypeSheet.test.tsx`; `CRM-F4-2026-08-15-01` |
| `CRM-DOC-012` | Cierre con documentos obligatorios, faltantes y error de backend controlado | Pass frontend | `ChangeStateDialog.test.tsx`; API real pendiente |
| `CRM-MAT-001` a `CRM-MAT-005` | Creación, observaciones, extensiones, tamaño, descarga y eliminación por permiso | Pass | `MatricesTab.test.tsx`; `matrices.service.test.ts`; `CRM-F4-2026-08-15-01` |

La suite utiliza mocks y jsdom; la autorización, persistencia y límites del storage contra el API real permanecen pendientes. El cálculo de subsidios y la aprobación completa de matrices están fuera de alcance según la matriz.
