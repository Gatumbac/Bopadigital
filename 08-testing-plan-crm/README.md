# Plan de testing del CRM BOPACORP

Plan separado para elevar la cobertura y la evidencia de pruebas del frontend `bopacorp-crm`, en coordinación con `bopacorp-api` y `@bopacorp/shared`.

## Archivos

- [`PLAN_TESTING_CRM.md`](./PLAN_TESTING_CRM.md): estrategia y ejecución por fases.
- [`MATRIZ_CASOS_PRUEBA_CRM.md`](./MATRIZ_CASOS_PRUEBA_CRM.md): casos de prueba, capa, requisito y estado.
- [`REGISTRO_EVIDENCIA_CRM.md`](./REGISTRO_EVIDENCIA_CRM.md): plantilla para registrar ejecuciones, cobertura, CI, defectos y retests.

## Línea base

Al 15 de agosto de 2026, el CRM tiene Vitest, React Testing Library, jsdom y cobertura V8 configurados. Hay cuatro archivos de prueba, seis declaraciones directas `it(...)` y un `it.each` que genera tres ejecuciones adicionales, enfocados en autenticación, permisos, sesión y el cliente Axios. Todavía no existe cobertura automatizada de los módulos comerciales ni una suite end-to-end del CRM.

## Meta

Alcanzar al menos 80% de cobertura del conjunto de código frontend crítico, con pruebas de decisión para autenticación/RBAC, ownership, validaciones de formularios, cambios de estado, archivos y cálculos de reportes. La meta no se interpreta como 80% global de cada componente visual.

## Fuentes

- CRM: [`../../bopacorp-crm`](../../bopacorp-crm)
- API: [`../../bopacorp-api`](../../bopacorp-api)
- Shared: [`../../bopacorp-shared`](../../bopacorp-shared)
- Plan de riesgos existente: [`../06-project2p/software1-risk-to-testing-plan.md`](../06-project2p/software1-risk-to-testing-plan.md)
- Matriz de requisitos: [`../06-project2p/requirements-test-traceability.md`](../06-project2p/requirements-test-traceability.md)

## Estado

Este paquete define el trabajo; no afirma que las fases estén ejecutadas. Cada fase debe cerrarse con comando, SHA, fecha, resultado y artifact verificable.
