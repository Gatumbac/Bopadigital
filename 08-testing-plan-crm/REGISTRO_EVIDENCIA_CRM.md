# Registro de evidencia de testing — CRM

Este archivo se debe completar durante la ejecución. No registrar `Pass` por inspección estática.

## 1. Identificación de ejecución

| Campo | Valor |
|---|---|
| ID de ejecución | `CRM-RUN-YYYY-MM-DD-NN` |
| Fecha/hora | Pendiente |
| Tester | Pendiente |
| Repositorio CRM | Pendiente |
| SHA CRM | Pendiente |
| SHA API | Pendiente o N/A |
| SHA shared | Pendiente o N/A |
| Node/npm | Pendiente |
| Sistema operativo | Pendiente |
| Navegador/dispositivo | Pendiente |
| Ambiente/base URL | Pendiente; nunca incluir secretos |

## 2. Comandos base

| Comando | Resultado | Duración | Artifact |
|---|---|---:|---|
| `npm ci` | Pendiente | — | — |
| `npm run test:run` | Pendiente | — | Log de consola |
| `npm run test:coverage` | Pendiente | — | `coverage/index.html`, `lcov.info` |
| `npm run lint` | Pendiente | — | Log de consola |
| `npx tsc -b --noEmit` | Pendiente | — | Log de consola |
| `npm run build` | Pendiente | — | Log de consola |
| `npm run test:e2e` | Pendiente | — | Reporte Playwright |

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
| Archivos actuales de baseline | — | — | — | — | Pendiente | Pendiente |
| Código crítico fase 2 | — | — | — | — | Pendiente | Pendiente |
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
