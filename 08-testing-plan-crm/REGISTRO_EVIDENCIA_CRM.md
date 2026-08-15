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
