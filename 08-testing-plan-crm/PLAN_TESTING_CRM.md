# Plan de testing por fases — BOPACORP CRM

**Proyecto:** BOPADIGITAL — BOPACORP S.A.  
**Repositorio principal:** `bopacorp-crm`  
**Repositorios relacionados:** `bopacorp-api`, `bopacorp-shared`  
**Fecha base:** 15 de agosto de 2026  
**Responsable:** equipo de desarrollo/testing del proyecto  
**Estado:** Fase 4 automatizada parcialmente ejecutada; casos restantes, API real y CI remoto pendientes.

---

## 1. Objetivo

Llevar el testing del frontend CRM desde una cobertura inicial de autenticación y frontera HTTP hasta una estrategia reproducible que cubra los flujos comerciales críticos, las restricciones por rol y las integraciones principales.

El resultado esperado es poder afirmar, con evidencia actual:

1. Qué código se considera crítico.
2. Qué casos de prueba protegen cada regla importante.
3. Qué pruebas son unitarias, de componentes, de integración o end-to-end.
4. Qué porcentaje de cobertura se obtuvo y sobre qué conjunto se calculó.
5. Qué escenarios pasan, fallan o están bloqueados.
6. Qué limitaciones siguen fuera del alcance.

La meta académica es cubrir al menos el **80% del código crítico**, no prometer 80% global sin justificar el conjunto medido.

## 2. Línea base comprobada

### 2.1 Configuración existente

El CRM ya tiene:

- Vitest.
- React Testing Library.
- `@testing-library/user-event`.
- `@testing-library/jest-dom`.
- jsdom.
- `@vitest/coverage-v8`.
- Alias `@/` disponible en la configuración de Vitest.
- Setup global en `src/test/setup.ts`.
- Reportes de cobertura text, LCOV y HTML en `coverage/`.
- Scripts `npm run test:run` y `npm run test:coverage`.
- Job de CI que ejecuta lint, typecheck, cobertura, build y carga el artifact.

### 2.2 Pruebas existentes

| Archivo | Cobertura actual |
|---|---|
| `src/modules/auth/components/RequireAuth.test.tsx` | Redirección de usuario no autenticado. |
| `src/modules/auth/components/RequirePermission.test.tsx` | Permiso/rol permitido y redirección sin permiso. |
| `src/modules/auth/context/AuthContext.test.tsx` | Login, persistencia de tokens/usuario y logout. |
| `src/services/api.test.ts` | Sobre exitoso, sobre de error y 401 en rutas públicas. |

Hay seis declaraciones directas `it(...)` y un `it.each` que genera tres ejecuciones parametrizadas. Su estado debe confirmarse ejecutando la suite; la existencia del código no equivale a un resultado `Pass`.

### 2.3 Limitaciones de la línea base

- `vite.config.ts` mide explícitamente cuatro archivos, no todo el código crítico del CRM.
- No existe un umbral de cobertura que haga fallar el proceso automáticamente.
- No hay pruebas de clientes, negociaciones, visitas, documentos, matrices, reportes, catálogo, organización ni empleabilidad.
- No hay Playwright, Cypress u otra suite de navegador configurada en este repo.
- No hay evidencia de una sesión ejecutada contra un ambiente real o de prueba en este plan.

## 3. Definición de alcance

### 3.1 Código crítico incluido

El conjunto crítico se debe medir por módulos, no por número total de archivos. Inicialmente incluye:

#### Autenticación y seguridad

- `src/modules/auth/components/RequireAuth.tsx`
- `src/modules/auth/components/RequirePermission.tsx`
- `src/modules/auth/context/AuthContext.tsx`
- `src/modules/auth/hooks/usePermission.ts`
- `src/modules/auth/components/Can.tsx`
- `src/services/api.ts`
- `src/services/auth.service.ts`
- `src/services/auth-storage.ts`
- `src/services/jwt.ts`

#### CRM comercial

- `src/modules/clients`
- `src/modules/negotiations`
- `src/modules/overview`
- `src/modules/reports`

#### Control documental y archivos

- `src/modules/documentation`
- componentes de carga, aprobación, rechazo, descarga y validación de archivos.

#### Organización y acceso

- `src/modules/org`
- creación de empleado, asignaciones, roles organizacionales y desbloqueo.

#### Catálogo y empleabilidad

- `src/modules/catalog`
- `src/modules/employability`

Estos módulos se incorporan después de cerrar los flujos comerciales críticos. No se debe contar un archivo simplemente porque aparece en `src/`; debe tener lógica relevante para una decisión o flujo de usuario.

### 3.2 Código que puede excluirse con justificación

- Primitivas visuales de shadcn sin lógica de negocio propia.
- Íconos, imágenes, estilos y archivos generados.
- Configuración estática sin ramas de negocio.
- Tipos que no ejecutan lógica.
- Fixtures y archivos de prueba.
- Código muerto confirmado por análisis y revisión.

La exclusión debe quedar escrita en el informe de cobertura. Nunca se debe excluir un módulo solo porque es difícil de probar.

### 3.3 Matrices de oferta

El plan cubre la implementación actual y limitada de matrices como regresión de la negociación: creación básica, observaciones y adjuntos disponibles.

No se contará como funcionalidad implementada:

- cálculo de subsidios;
- líneas de productos y cantidades;
- aprobación completa de matrices;
- historial de matrices no expuesto por el CRM.

Esto mantiene el plan compatible con la decisión histórica de descartar el alcance completo de matrices y, al mismo tiempo, protege el código residual que todavía puede ser alcanzable desde la negociación.

## 4. Estrategia de niveles de prueba

| Nivel | Propósito | Herramienta | Dependencia |
|---|---|---|---|
| Unitario | Validar reglas puras, transformaciones y decisiones pequeñas. | Vitest | Ninguna o mocks locales. |
| Componente | Validar formularios, guards, tablas y diálogos con interacción de usuario. | Vitest + RTL + user-event | Providers y servicios mockeados. |
| Integración frontend | Validar hooks/servicios contra respuestas API simuladas y contratos. | Vitest; MSW opcional si se aprueba | Mock de API estable. |
| Integración API | Validar rutas, middleware, autorización, ownership y persistencia. | Suite del `bopacorp-api`, Supertest/Vitest | Base de prueba o dobles deterministas. |
| End-to-end | Validar journeys por rol en navegador. | Playwright recomendado | CRM, API, datos semilla y cuentas de prueba. |
| Aceptación manual | Validar GPS, descargas, permisos reales y evidencia visual. | Navegador/dispositivo | Ambiente controlado y datos anonimizados. |

Una prueba de un nivel no reemplaza a los demás. Por ejemplo, una prueba RTL del botón **Aprobar** no demuestra que la API rechace a un rol no autorizado.

## 5. Fases de ejecución

### Fase 0 — Congelar alcance, riesgos y datos

**Objetivo:** preparar una base reproducible antes de añadir casos.

**Duración estimada:** 0.5–1 día.

### Actividades

- Confirmar el commit base de `bopacorp-crm`, `bopacorp-api` y `bopacorp-shared`.
- Registrar versión de Node, npm, sistema operativo y navegador.
- Confirmar qué funcionalidades están dentro del reporte final.
- Separar funcionalidad actual, planificada y descoped.
- Crear cuentas de prueba para admin, manager, supervisor, asesor, coordinador y web-admin cuando el ambiente lo permita.
- Crear datos semilla anonimizados: clientes, negociaciones, documentos, vacantes y postulantes.
- Definir si se probará la API real, mocks o ambas capas.
- Confirmar que nunca se usarán contraseñas ni datos reales en el repositorio.

### Entregables

- Alcance firmado por el equipo.
- Inventario de roles y cuentas de prueba.
- Inventario de datos semilla.
- Riesgo → requisito → caso de prueba.
- SHA y ambiente de referencia.

### Criterio de salida

No se inicia la medición de cobertura final hasta que se conozca qué revisión y qué conjunto de código se está midiendo.

### Fase 1 — Medir la línea base y endurecer el runner

**Objetivo:** obtener la primera evidencia cuantitativa y hacer que el runner sea reproducible.

**Duración estimada:** 1 día.

### Actividades

1. Instalar dependencias con `npm ci`.
2. Ejecutar `npm run test:run`.
3. Ejecutar `npm run test:coverage`.
4. Guardar resumen de tests, cobertura y errores.
5. Ejecutar `npm run lint`.
6. Ejecutar `npx tsc -b --noEmit`.
7. Ejecutar `npm run build`.
8. Registrar SHA, fecha, Node, npm y resultado.
9. Revisar si el reporte de cobertura incluye únicamente los cuatro archivos actuales.
10. Definir el `include` de cobertura para el conjunto crítico, excluyendo configuración y UI sin lógica.

### Decisión sobre umbrales

No se debe colocar inmediatamente un umbral de 80% sobre todo `src/`, porque produciría un bloqueo artificial y mezclaría componentes visuales con lógica crítica.

El umbral se agrega en dos pasos:

- **Gates informativos:** generar reportes sin fallar por porcentaje mientras se amplía la suite.
- **Gate final:** exigir al menos 80% de líneas del conjunto crítico y revisar manualmente ramas de decisiones críticas.

### Entregables

- `coverage/index.html`.
- `coverage/lcov.info`.
- Resumen de consola.
- Registro de comandos en `REGISTRO_EVIDENCIA_CRM.md`.

### Criterio de salida

La suite base pasa y existe una medición reproducible, aunque el porcentaje inicial sea bajo.

### Resultado de ejecución de Fase 1 — 2026-08-15

- [x] Dependencias instaladas con `npm ci` sobre el SHA `57cb6a6b8fa16743984b8b2598466bb16a135ffd`.
- [x] Suite base ejecutada: 4 archivos y 9 tests, todos exitosos.
- [x] Reporte de cobertura generado en HTML y LCOV.
- [x] Lint, TypeScript y build de producción exitosos.
- [x] Alcance crítico configurado para 10 archivos de autenticación, autorización y servicios API.
- [x] Gate porcentual final todavía no activado; la cobertura del alcance crítico queda en 40.17% de statements y 39.63% de líneas.
- [ ] Artefacto y ejecución de CI verificados en GitHub Actions; pendiente de un run remoto.

La línea base original, limitada a cuatro archivos, obtuvo 47.02% de statements y 45.80% de líneas. Al ampliar el `include` al núcleo crítico aparecen caminos aún no probados en `Can`, `usePermission`, `LoginPage`, `auth.service` y `jwt`; estos quedan como entrada prioritaria de la Fase 2.

### Fase 2 — Completar autenticación, sesión y API boundary

**Objetivo:** cerrar el perímetro de seguridad y comunicación antes de probar pantallas de negocio.

**Duración estimada:** 1–2 días.

### Casos unitarios/componentes

- Login exitoso.
- Login inválido.
- Usuario bloqueado.
- Sesión restaurada desde localStorage.
- Sesión inválida al consultar `/auth/me`.
- Logout exitoso aunque falle la revocación remota.
- Permiso ausente.
- Rol requerido ausente.
- Permiso presente y rol ausente.
- Componente `Can` ocultando una acción.
- Permiso actualizado después de logout/login.

### Casos API boundary

- Sobre `{ success: true, data }`.
- Sobre paginado.
- Error con código y detalles.
- Error de red.
- 401 en ruta protegida.
- 401 en `/auth/login`, `/auth/refresh` y `/auth/register` sin refresh recursivo.
- Refresh exitoso.
- Refresh fallido y limpieza de sesión.
- Cola de requests que esperan un mismo refresh.
- Bearer token agregado a una solicitud autenticada.

### Entregables

- Pruebas adicionales de `AuthContext`, `Can`, `auth.service`, `auth-storage`, `jwt` y `api`.
- Tabla de decisión de 401/403.
- Evidencia de persistencia y limpieza de tokens.

### Criterio de salida

Las rutas protegidas, permisos y refresh no tienen caminos críticos sin prueba.

### Resultado de ejecución de Fase 2 — 2026-08-15

- [x] Se añadieron pruebas para `AuthContext`, guards, `Can`, `usePermission`, `LoginPage`, `auth-storage`, `auth.service`, `jwt` y `api`.
- [x] La suite ejecutó 10 archivos y 49 tests exitosos.
- [x] Se cubrieron login inválido y bloqueado, restauración desde `/auth/me`, logout con fallo remoto, permisos/roles, persistencia, JWT, Bearer token, paginación, errores de red, refresh, refresh fallido y cola concurrente.
- [x] Cobertura del conjunto crítico: 92.76% statements, 80.34% branches, 98.30% functions y 93.11% lines.
- [x] Lint, TypeScript y build de producción exitosos.
- [x] Se corrigió el retry de la primera request protegida para asignar el nuevo Bearer token después de un refresh exitoso.
- [ ] Ejecución remota y artifact de GitHub Actions pendientes.

La corrida `CRM-F2-2026-08-15-01` se realizó sobre el working tree basado en `3c4dd51`; el resultado debe asociarse al commit de Fase 2 cuando se cree.

### Fase 3 — Cubrir clientes, negociaciones y visitas

**Objetivo:** cubrir el flujo comercial principal del asesor y la supervisión.

**Duración estimada:** 3–5 días.

### Clientes

- Crear con campos obligatorios válidos.
- Rechazar RUC inválido o incompleto.
- Rechazar nombres vacíos.
- Rechazar servicios o facturación negativos.
- Editar información.
- Activar/desactivar.
- Asignar, reasignar y limpiar asesor según permiso.
- Filtrar por búsqueda, estado y asesor.
- Manejar lista vacía, error y paginación.

### Negociaciones

- Crear con cliente y asesor.
- Crear desde el flujo inline de cliente cuando aplique.
- Editar fechas y observaciones.
- Respetar el asesor propio para el rol asesor.
- Filtrar tabla.
- Renderizar estados en kanban.
- Cambiar estado desde detalle.
- Cambiar estado desde drag-and-drop.
- Exigir nota para estados que lo requieren.
- No permitir cambio no autorizado.
- Crear historial una sola vez.
- Solicitar documentos faltantes al cerrar.
- Manejar error del servidor sin dejar UI inconsistente.

### Visitas

- Crear con tipo, fecha y observaciones.
- Capturar GPS cuando el navegador concede permiso.
- Continuar sin GPS cuando el permiso es denegado.
- Rechazar coordenadas o fechas inválidas según contrato.
- Editar y eliminar según permiso.
- Verificar como supervisor.
- Ocultar verificación para asesor.
- Filtrar por estado, tipo y fechas.

### Entregables

- Tests RTL para formularios y diálogos críticos.
- Tests de servicios/hook con parámetros esperados.
- Fixtures por asesor, supervisor y manager.
- Evidencia de ownership y alcance de datos.

### Criterio de salida

El flujo cliente → negociación → visita tiene pruebas de camino feliz, validación, permisos y errores.

### Resultado de ejecución de Fase 3 — 2026-08-15

- [x] Se añadieron fixtures determinísticos en inglés para asesores, clientes, negociaciones, estados y visitas.
- [x] Se cubrieron contratos de servicios para clientes, negociaciones, cambios de estado, cierre multipart y visitas.
- [x] Se cubrieron formularios de clientes, negociaciones y visitas con validación, errores de servidor y permisos visibles.
- [x] Se cubrieron ownership del asesor al crear negociaciones, filtros paginados, notas obligatorias, documentos faltantes y fallos de transición.
- [x] Se cubrieron GPS concedido y denegado, verificación/eliminación por permiso y observación obligatoria.
- [x] Suite local: 20 archivos y 84 tests exitosos.
- [x] Cobertura del conjunto crítico medido: 84.48% statements, 70.15% branches, 82.72% functions y 84.97% lines sobre 21 archivos configurados.
- [x] Lint, TypeScript y build de producción exitosos.
- [ ] Quedan pendientes pruebas directas de páginas de alcance por supervisor, edición visual de cliente, Kanban/drag-and-drop, historial de transición y estados vacíos/error de algunas listas.
- [ ] CI remoto, API real y E2E de navegador siguen pendientes.

La ejecución se realizó sobre el working tree basado en `36ab4bf16a16b9d97d5d668e5ec7542c7b0a75ee`; los resultados no deben atribuirse a una revisión posterior hasta registrar el SHA del commit que incluya estos cambios.

### Fase 4 — Cubrir documentación, archivos y matriz limitada

**Objetivo:** proteger los datos que pueden bloquear un cierre comercial.

**Duración estimada:** 3–4 días.

### Documentación

- Selección obligatoria de negociación y tipo.
- Archivo obligatorio.
- PDF/JPG/PNG aceptados en la interfaz.
- Archivo mayor a 50 MB rechazado.
- Estado inicial pendiente.
- Aprobar un documento pendiente.
- Rechazar sin motivo: debe fallar.
- Rechazar con motivo: debe continuar.
- Descargar individual.
- Descargar conjunto ZIP cuando el permiso exista.
- Administrar tipos de documento.
- Filtrar por estado, asesor y búsqueda.
- Ocultar acciones para roles no autorizados.

### Cierre con documentos

- Cierre con todos los documentos obligatorios.
- Cierre con faltantes.
- Carga de documentos nuevos durante el cierre.
- Error del backend con tipos faltantes.
- No duplicar la transición si una petición falla.

### Matriz limitada

- Crear una matriz asociada a una negociación.
- Editar observaciones.
- Adjuntar oferta `.xlsx`, `.xls` o `.csv`.
- Adjuntar plantilla `.msg`, `.eml`, `.pdf` o `.html`.
- Descargar adjunto.
- Eliminar adjunto con permiso.
- No presentar ni probar cálculo de subsidios o aprobación completa.

### Entregables

- Fixtures de tipos obligatorios y estados.
- Archivos válidos, inválidos, vacíos y de tamaño límite.
- Tests de permisos de aprobación/rechazo.
- Evidencia de error de carga y recuperación.

### Criterio de salida

El sistema no puede aceptar silenciosamente un archivo inválido ni cerrar una negociación sin los documentos que el contrato marque como obligatorios.

### Resultado de ejecución de Fase 4 — 2026-08-15

- [x] Se añadieron fixtures determinísticos en inglés para tipos documentales, documentos, historial, matrices y adjuntos.
- [x] Se cubrieron servicios de documentos, tipos documentales, upload multipart, descargas, matrices y adjuntos.
- [x] Se cubrieron selección obligatoria, extensiones PDF/JPG/PNG, límite de 50 MB, estado pendiente, aprobación, rechazo y permisos.
- [x] Se cubrieron creación de matriz, observaciones, formatos de adjuntos, descargas, eliminación autorizada y cierre con documentos obligatorios.
- [x] Se agregaron validaciones explícitas de extensión documental y tamaño máximo de adjunto en el frontend.
- [x] Suite local: 28 archivos y 116 tests exitosos.
- [x] Cobertura del conjunto crítico medido: 80.97% statements, 64.85% branches, 76.88% functions y 82.12% lines sobre 33 archivos configurados.
- [x] Lint, TypeScript y build de producción exitosos.
- [ ] La protección RBAC/persistencia contra API real, el CI remoto y E2E de navegador siguen pendientes.
- [ ] La aprobación completa de matrices y el cálculo de subsidios permanecen fuera de alcance.

La ejecución se realizó sobre el working tree basado en `68790800a4aede85bcacf9a197445cc5a59dd12b`; los resultados no deben atribuirse a una revisión posterior hasta registrar el SHA del commit que incluya estos cambios.

### Fase 5 — Cubrir reportes y exportaciones

**Objetivo:** evitar resultados incorrectos en decisiones de gestión.

**Duración estimada:** 2–3 días.

### Casos

- Métricas con un asesor y datos conocidos.
- Métricas con varios asesores.
- Supervisor limitado a su equipo.
- Asesor limitado a su usuario en Inicio.
- Rango de fechas vacío.
- Rango que incluye los límites.
- Estados comerciales agregados correctamente.
- Conteo de visitas.
- Días promedio de cierre.
- Facturación y promedio por servicio.
- Tabla sin resultados.
- Edición de metas solo con permiso.
- CSV con headers y columnas esperadas.
- CSV con valores nulos o vacíos.
- Registro de exportación creado después de descargar.

### Entregables

- Dataset pequeño con resultado calculado manualmente.
- Caso de regresión para cada métrica.
- Archivo CSV de evidencia sin datos personales.
- Comparación esperado/observado.

### Criterio de salida

Los totales de prueba coinciden con el cálculo de referencia y la restricción de rol se conserva.

### Fase 6 — Cubrir catálogo, organización y empleabilidad

**Objetivo:** ampliar cobertura a módulos administrativos sin retrasar el núcleo comercial.

**Duración estimada:** 3–5 días.

### Catálogo

- Campos generales obligatorios.
- Precio y permanencia no negativos.
- Campos técnicos por tipo de producto.
- Beneficios dinámicos.
- Condiciones legales y temporales.
- Publicar/despublicar.
- Activar/desactivar.
- Crear, editar y desactivar tablas auxiliares.
- Solicitudes de contacto pendientes/atendidas.

### Organización

- Crear usuario y empleado.
- Rechazar contraseña que no cumpla política.
- Distinguir rol de acceso y rol organizacional.
- Asignar supervisores a asesores.
- Editar empleado.
- Activar/desactivar.
- Desbloquear con motivo válido.
- Rechazar motivo de desbloqueo menor al mínimo.

### Empleabilidad

- Crear vacante.
- Validar título, descripción y requisitos.
- Validar fecha de cierre posterior o igual a publicación.
- Publicar y despublicar.
- Filtrar vacantes.
- Consultar postulantes por vacante.
- Cambiar estado de postulación.
- Rechazar sin notas cuando sean obligatorias.
- Descargar CV PDF con permiso.

### Criterio de salida

Los módulos administrativos cubren sus validaciones de entrada y acciones de permiso principales, aunque su cobertura quede después del 80% del núcleo comercial.

### Fase 7 — Integración con la API y RBAC

**Objetivo:** demostrar que las pruebas de frontend no ocultan problemas de autorización o ownership en el backend.

**Responsable principal:** `bopacorp-api`, coordinado con este plan.

**Duración estimada:** 3–5 días.

### Tabla mínima de autorización

| Sesión | Permiso | Propietario | Resultado esperado |
|---|---|---|---|
| Sin token | Cualquiera | Cualquiera | 401. |
| Token válido | No tiene permiso | Cualquiera | 403. |
| Asesor | Sí | Propio | Permitido. |
| Asesor | Sí | Otro asesor | Denegado o no visible. |
| Supervisor | Sí | Asesor supervisado | Permitido según alcance. |
| Supervisor | Sí | Asesor no supervisado | Denegado o no visible. |
| Manager/admin | Sí | Cualquiera permitido | Permitido según permiso. |

### Casos backend coordinados

- Login, refresh, logout y bloqueo.
- RBAC de clientes, negociaciones, visitas y documentos.
- Ownership y alcance de asesor/supervisor.
- Transiciones válidas e inválidas.
- Documentos obligatorios y storage.
- Métricas y filtros de reporte.
- Validación Zod y errores de contrato.

### Entregables

- Reporte de tests API.
- Evidencia de respuestas 401/403/422/404/409 según corresponda.
- SHA coordinado de API, CRM y shared.
- Caso de contrato cuando frontend y API hayan tenido drift de versión.

### Criterio de salida

El frontend y la API presentan el mismo comportamiento de permisos para los escenarios aceptados y las diferencias conocidas están documentadas.

### Fase 8 — Pruebas end-to-end del CRM

**Objetivo:** demostrar journeys completos en navegador, no solo unidades aisladas.

**Herramienta recomendada:** Playwright.

**Duración estimada:** 3–5 días, sin contar preparación del ambiente.

### Preparación

- Añadir `@playwright/test` como dependencia de desarrollo.
- Crear `playwright.config.ts`.
- Definir `npm run test:e2e` y `npm run test:e2e:report`.
- Configurar `baseURL` del CRM.
- Preparar API y datos semilla.
- Usar variables de entorno para cuentas de prueba; nunca guardar contraseñas.
- Guardar estado autenticado por rol de forma segura o iniciar sesión por fixture.
- Generar reportes HTML, screenshots y videos solo en fallos.

### Journeys mínimos

| ID | Perfil | Journey |
|---|---|---|
| E2E-CRM-01 | Asesor | Login → crear cliente → crear negociación → registrar visita. |
| E2E-CRM-02 | Asesor | Abrir negociación → subir documento → consultar estado. |
| E2E-CRM-03 | Supervisor/coordinador | Abrir documentación → aprobar o rechazar con motivo. |
| E2E-CRM-04 | Supervisor/manager | Abrir reportes → filtrar período → generar CSV. |
| E2E-CRM-05 | Manager | Crear producto o configurar organización según alcance. |
| E2E-CRM-06 | Manager/web-admin | Crear vacante → consultar postulante → revisar CV. |
| E2E-CRM-07 | Perfil sin permiso | Intentar ruta protegida y confirmar redirección/ausencia de acción. |

### Criterio de salida

Los journeys principales pasan en un ambiente reproducible y el reporte HTML identifica claramente cualquier fallo, screenshot y trace.

### Fase 9 — Cerrar cobertura y hacer el gate de calidad

**Objetivo:** alcanzar y demostrar la meta del 80% del código crítico.

**Duración estimada:** 1–2 días después de completar las fases anteriores.

### Actividades

1. Ejecutar toda la suite unit/component.
2. Ejecutar cobertura con el `include` final.
3. Revisar líneas no cubiertas del conjunto crítico.
4. Priorizar ramas de seguridad, ownership, límites y estados.
5. Eliminar tests duplicados o dependientes de implementación interna.
6. Añadir el umbral mínimo para el conjunto crítico.
7. Confirmar que los tests fallan cuando se introduce un defecto controlado, si el equipo puede hacerlo sin dejar cambios en la rama final.
8. Ejecutar lint, typecheck y build.
9. Guardar artifacts.
10. Actualizar la matriz y el registro de evidencia.

### Gate propuesto

| Métrica | Gate final |
|---|---:|
| Tests unit/component críticos | 100% deben pasar |
| Cobertura de líneas del conjunto crítico | ≥ 80% |
| Reglas de decisión crítica | Casos válidos, inválidos y no autorizados cubiertos |
| Lint | Sin errores |
| Typecheck | Sin errores |
| Build | Exitoso |
| E2E mínimos | Todos pasan en ambiente de prueba |

El porcentaje global puede reportarse como información adicional, pero no reemplaza el gate del conjunto crítico.

### Fase 10 — Evidencia para informe, manual y rúbrica

**Objetivo:** convertir los resultados en evidencia académica reproducible.

**Duración estimada:** 1–2 días.

### Evidencia mínima por ejecución

- Repositorio y commit SHA.
- Fecha y hora.
- Sistema operativo, Node y npm.
- Ambiente y URL base sin secretos.
- Comando ejecutado.
- Resultado de tests.
- Porcentaje de cobertura y archivos incluidos.
- Artifact HTML/LCOV.
- Screenshots, video o exportación de casos de aceptación.
- Defecto, fix SHA y retest, si existió.

### Cadena de trazabilidad

Cada caso debe poder seguir la cadena:

```text
Riesgo → Requisito → Caso de prueba → Resultado observado → Evidencia → Retest
```

### Entregables finales

- `MATRIZ_CASOS_PRUEBA_CRM.md` actualizado.
- `REGISTRO_EVIDENCIA_CRM.md` con ejecuciones reales.
- Reporte HTML/LCOV de cobertura.
- Reporte de pruebas basado en riesgos.
- Capítulo de testing del informe final.
- Manual de usuario con escenarios que sí fueron ejecutados.
- Runbook de demostración.

## 6. Técnicas de diseño de pruebas

### Particiones de equivalencia

Aplicar a correos, RUC, estados, roles, permisos, tipos de archivo, filtros y formularios:

- válido;
- vacío;
- inválido;
- duplicado;
- no autorizado;
- fuera de alcance.

### Valores límite

Probar siempre:

- 0, 1, máximo y máximo + 1;
- fechas iguales, anterior y posterior;
- archivo vacío, justo en el límite y sobre el límite;
- observación vacía y longitud máxima;
- primera y última página.

### Tabla de decisión

Usar combinaciones de usuario, rol, permiso, propietario, estado y acción. Esto es obligatorio para auth/RBAC y ownership.

### Transiciones de estado

Documentar transiciones válidas e inválidas para negociaciones, documentos y postulaciones. Probar que el historial se actualice una sola vez y que un error no deje un estado parcial.

### Tests parametrizados

Usar `it.each` para roles, permisos, estados, extensiones y límites cuando el comportamiento sea el mismo.

### Arrange–Act–Assert

Cada caso debe separar preparación, ejecución y aserciones observables. Evitar afirmar únicamente que una función interna fue llamada.

## 7. Fixtures y datos de prueba

### Usuarios

- `admin-test`.
- `manager-test`.
- `supervisor-test`.
- `advisor-test`.
- `coordinator-test`.
- `web-admin-test` cuando el ambiente lo soporte.

### Datos

- Clientes con estados activo/inactivo.
- Clientes asignados a diferentes asesores.
- Asesores bajo el mismo supervisor y fuera de su alcance.
- Negociaciones en cada estado.
- Documentos pendientes, aprobados y rechazados.
- Tipos documentales obligatorios y opcionales.
- Vacantes publicadas y borrador.
- Postulaciones en cada estado.

### Archivos

- `valid-document.pdf`.
- `valid-image.jpg`.
- `invalid-extension.exe`.
- `empty-file.pdf`.
- archivo de exactamente 50 MB.
- archivo mayor a 50 MB.
- CV PDF válido.

No se deben versionar archivos de clientes, credenciales, tokens ni bases de datos de producción.

## 8. CI y calendario de ejecución

### Pull request

Ejecutar:

```bash
npm ci
npm run lint
npx tsc -b --noEmit
npm run test:coverage
npm run build
```

El artifact debe incluir:

- resumen de consola;
- `coverage/lcov.info`;
- `coverage/index.html`;
- reportes de fallos si existen.

### Ejecución nocturna o manual

Ejecutar Playwright contra un ambiente de prueba estable. No depender de producción para hacer que el CI pase.

### Release candidate

Ejecutar unit/component, integración API, E2E, smoke de `/health`, validación de despliegue y revisión manual de los escenarios del reporte.

## 9. Riesgos y bloqueos

| Riesgo | Consecuencia | Mitigación |
|---|---|---|
| No hay cuentas de prueba | No se pueden cerrar RBAC ni E2E. | Crear cuentas temporales y rotar secretos. |
| API o storage no disponible | Falla la integración aunque el componente sea correcto. | Mocks para unit/component y ambiente de integración separado. |
| GPS requiere dispositivo | No se demuestra geolocalización solo con jsdom. | Prueba manual en navegador/dispositivo y caso de permiso denegado. |
| Permisos API/frontend diferentes | Manual y E2E pueden describir accesos contradictorios. | Validar cada rol en ambos repositorios y documentar la diferencia. |
| Datos sensibles en capturas | Riesgo de exposición académica/operativa. | Fixtures anonimizadas y revisión antes de subir artifacts. |
| Cobertura inicial limitada a cuatro archivos | Porcentaje engañoso. | La Fase 1 dejó registrada la línea base y amplió `coverage.include` a 10 archivos críticos antes del gate final. |
| Tests frágiles por textos o implementación | Falsos negativos en cambios visuales. | Consultas accesibles y aserciones de comportamiento. |

## 10. Criterios de terminado

El plan completo se considera terminado cuando:

- [ ] El conjunto crítico está definido y justificado.
- [ ] La línea base tiene SHA, fecha y comandos reproducibles.
- [ ] Auth/RBAC/API boundary tienen pruebas completas.
- [ ] El flujo cliente → negociación → visita está cubierto.
- [ ] Documentos, archivos y cierre con documentos están cubiertos.
- [ ] Reportes y exportación tienen datos esperados conocidos.
- [ ] Los módulos administrativos tienen pruebas de sus validaciones principales.
- [ ] La API confirma ownership y permisos.
- [ ] Los E2E mínimos pasan en un ambiente de prueba.
- [ ] La cobertura del código crítico es ≥80%.
- [ ] Lint, typecheck y build pasan.
- [ ] El CI conserva artifacts.
- [ ] Cada caso del informe tiene evidencia actual.
- [ ] Las limitaciones, descopes y casos bloqueados están declarados.

## 11. Orden recomendado de ejecución

1. Fase 0: alcance, cuentas y fixtures.
2. Fase 1: baseline y runner.
3. Fase 2: auth/API boundary.
4. Fase 3: clientes, negociaciones y visitas.
5. Fase 4: documentos y matriz limitada.
6. Fase 5: reportes.
7. Fase 6: catálogo, organización y empleabilidad.
8. Fase 7: integración API/RBAC.
9. Fase 8: E2E.
10. Fase 9: cobertura y gates.
11. Fase 10: evidencia y rúbrica.

No se debe empezar por Playwright si todavía no existe una línea base, fixtures y cuentas de prueba. El navegador valida el journey, pero no sustituye las pruebas unitarias de reglas y permisos.
