# Chapter 4 — Estandarización pendiente por repositorio

**Fecha del inventario:** 2026-08-15  
**Alcance:** BOPACORP y repositorios hermanos ubicados en `../`  
**Modo de levantamiento:** inspección estática de archivos, configuraciones, historial y estado Git. No se ejecutaron comandos de calidad en esta revisión.

## Objetivo

Unificar las configuraciones de desarrollo, calidad y CI/CD para que todos los repositorios tengan un estándar comparable y evidencia reproducible para Chapter 4. Los tests se consideran un requisito común para todos los repositorios; su implementación o ampliación no debe usarse como motivo para detener la normalización.

## Estado base observado

| Repositorio | HEAD observado | Estado del worktree | Estado de estandarización |
|---|---:|---|---|
| `../bopacorp-api` | `4018bd5` | Limpio | Parcial, es la referencia más completa |
| `../bopacorp-crm` | `5011dc4` | Sucio | Parcial; conservar cambios locales antes de editar |
| `../bopacorp-web` | `f527679` | Sucio | Parcial; conservar cambios locales antes de editar |
| `../bopacorp-mobile` | `4638ea1` | Limpio | Parcial; usa una variante Expo propia |
| `../bopacorp-shared` | `4cbf3d4` | Limpio | Parcial; contratos claros, sin tests/hooks propios |
| `../deploy` | `b6f2f6f` | Limpio | No aplica el estándar TypeScript; requiere estándar operativo |
| `../communications` | `369ae94` | Limpio | Repositorio documental; requiere validación documental |
| `../bopacorp` | Sin Git | Legacy | Excluir del producto actual o archivarlo formalmente |
| Este repositorio `Bopadigital` | `06eaf13` | Limpio | Coordinador documental; debe actualizarse al cerrar los agentes |

Los archivos modificados o no rastreados de CRM y Web no deben citarse como evidencia final hasta que exista una revisión comprometida y registrada.

## Estándar objetivo común

### Repositorios JavaScript/TypeScript

API, CRM, Web, Mobile y Shared deben converger en lo siguiente, adaptando únicamente lo necesario por framework:

- Node.js 22 fijado y documentado; npm y lockfile reproducibles.
- Scripts explícitos y equivalentes: `lint`, `format:check`, `typecheck`, `check`, `test`, `test:run`, `test:coverage` y `build` cuando el repositorio produzca un artefacto.
- `check` debe ser no mutante. No debe usar `--write`; la escritura queda para `format` o para el hook de archivos staged.
- Biome con configuración explícita y consistente: 2 espacios, ancho 100, comillas simples, punto y coma, trailing commas ES5, reglas recomendadas, imports/variables no usados como error y `noExplicitAny` como error.
- TypeScript con `strict: true` explícito y reglas de no-unused/no-fallthrough. Las excepciones del framework deben quedar documentadas y ser mínimas.
- Husky y Commitlint con el mismo contrato de hooks. El pre-commit valida archivos staged y el commit-msg valida Conventional Commits.
- CI con la misma secuencia: instalación reproducible, lint, formato, typecheck, tests con coverage, build y publicación del reporte de coverage cuando corresponda.
- Una única estrategia para consumir `@bopacorp/shared`. No mezclar indefinidamente dependencia publicada con `file:../bopacorp-shared`; la opción objetivo es el paquete publicado, alineado con Deploy.
- No leer, imprimir, versionar ni hardcodear secretos o archivos `.env`.

### Repositorios no TypeScript

- Deploy debe validar Compose, imágenes, variables requeridas y configuración de proxy en CI.
- Communications y Bopadigital deben validar Markdown, enlaces internos y estructura documental en CI.
- Legacy no debe recibir cambios de producto hasta confirmar si sigue dentro del alcance.

## Pendientes y prompt por repositorio

### 1. `../bopacorp-api` — prioridad P1

**Ya está bien encaminado:** TypeScript estricto, Biome, Husky, Commitlint, Vitest, coverage, build y CI completo.

**Pendientes:**

- Añadir o normalizar `typecheck` y `format:check` como scripts públicos.
- Separar `check` de cualquier operación `--write`.
- Fijar Node/npm y documentar el contrato común de scripts.
- Hacer que la política de auditoría de dependencias sea explícita: bloqueo o excepción justificada, no un `|| true` silencioso.
- Confirmar que CI y hooks ejecutan exactamente las mismas reglas de calidad.
- Registrar una ejecución real sobre la revisión final.

**Prompt para el agente de API:**

```text
Trabaja en ../bopacorp-api para normalizar su configuración al estándar de BOPACORP.

Baseline: inspecciona primero git status --short y git rev-parse HEAD. No borres ni sobrescribas cambios existentes, no leas archivos .env, no expongas secretos y no hagas push.

Objetivos:
1. Mantener TypeScript strict, Biome, Husky, Commitlint, Vitest, coverage y build.
2. Añadir scripts explícitos typecheck y format:check.
3. Hacer que check, lint y format:check sean no mutantes; deja --write únicamente para format o lint-staged.
4. Alinear Node/npm, formato Biome, lint-staged y Conventional Commits con el estándar común.
5. Revisar el audit de dependencias y dejar una política explícita y auditable.
6. Mantener la arquitectura route -> middleware -> controller -> service -> db y no mezclar esta tarea con refactors funcionales.

Verifica con npm ci, npm run check, npm run test:coverage, npm run build y git diff --check. Reporta archivos cambiados, comandos, resultado, HEAD probado y cualquier excepción justificada.
```

### 2. `../bopacorp-crm` — prioridad P0

**Ya está bien encaminado:** Biome, Vitest, coverage, build, hooks, CI y primitivas CRUD reutilizables.

**Pendientes:**

- Declarar `strict: true` explícitamente en la configuración efectiva de TypeScript y resolver los errores resultantes.
- Cambiar `check` para que no escriba archivos mediante `biome check --write .`.
- Añadir `format:check` y alinear el formato con API/Web/Shared.
- Normalizar el hook `commit-msg` y el uso de argumentos de Husky.
- Alinear el workflow con la secuencia común y conservar el artifact de coverage.
- Validar la configuración sin destruir los cambios actuales del worktree.

**Prompt para el agente de CRM:**

```text
Trabaja en ../bopacorp-crm para normalizar su configuración al estándar de BOPACORP.

Antes de editar, revisa git status --short y protege todos los cambios locales existentes. No uses git reset, git checkout, clean ni comandos destructivos; no leas .env, no expongas secretos y no hagas push.

Objetivos:
1. Hacer explícito TypeScript strict en la configuración efectiva y corregir los errores sin cambiar comportamiento funcional.
2. Eliminar --write de check/lint de CI; crear format:check y dejar la escritura para format o lint-staged.
3. Mantener Vitest, test:run, test:coverage, build y artifact de coverage.
4. Alinear Biome, Node/npm, Husky, lint-staged y Commitlint con API, Web y Shared.
5. Mantener la estructura modular y las abstracciones existentes usePaginatedList, useUnsavedGuard y PaginationFooter.

Ejecuta npm ci, npm run check, npm run test:coverage, npm run build y git diff --check. Reporta qué errores ya existían, qué cambios hiciste, resultados y HEAD probado. No incluyas en el reporte como evidencia final archivos aún no comprometidos.
```

### 3. `../bopacorp-web` — prioridad P0

**Ya está bien encaminado:** módulos por funcionalidad, servicios/hooks separados, Vitest, Biome y hooks.

**Pendientes:**

- Declarar `strict: true` explícitamente y corregir la deuda de tipos.
- Activar `noExplicitAny` como error, con excepciones puntuales documentadas solo si son inevitables.
- Separar validación de formato de comandos mutantes.
- Añadir tests y coverage a CI, además de publicar el artifact correspondiente.
- Eliminar el paso de depuración que imprime `package.json` y consultas de dependencias en CI.
- Actualizar `AGENTS.md`, que todavía afirma que no existe runner de tests.
- Alinear Node/npm, Biome, hooks y Commitlint.

**Prompt para el agente de Web:**

```text
Trabaja en ../bopacorp-web para normalizar su configuración al estándar de BOPACORP.

Primero inspecciona git status --short y preserva todos los cambios locales. No borres, resetees ni leas .env; no imprimas secretos, no hagas push y no cambies contratos funcionales.

Objetivos:
1. Activar TypeScript strict explícito y resolver errores de tipado.
2. Activar Biome noExplicitAny como error y mantener reglas de accesibilidad apropiadas para React.
3. Crear format:check y hacer que check/lint de CI sean no mutantes.
4. Mantener y ejecutar test:run/test:coverage; añadir ambos pasos al workflow y publicar coverage.
5. Quitar pasos de debug innecesarios del workflow.
6. Actualizar AGENTS.md para reflejar la existencia real de Vitest y los comandos vigentes.
7. Conservar la separación de feature module, service y hook visible en el refactor CMS.

Verifica npm ci, npm run check, npm run test:coverage, npm run build y git diff --check. Reporta archivos, resultados, HEAD probado y excepciones.
```

### 4. `../bopacorp-mobile` — prioridad P1

**Ya está bien encaminado:** Expo, TypeScript strict, tests, lint y typecheck en CI.

**Pendientes:**

- Alinear Biome con el estándar común: comillas simples, `noExplicitAny` como error y reglas de imports/variables no usados como error.
- Añadir scripts explícitos `typecheck`, `format:check` y `test:coverage`.
- Incorporar coverage y build web/Expo a CI cuando el entorno lo permita.
- Añadir Husky y Commitlint si se confirma que Mobile comparte el mismo ciclo de commits; si Expo lo impide, documentar la excepción y validar en CI.
- Unificar la estrategia de instalación de `@bopacorp/shared` con los demás consumidores.
- Revisar `docs/ARCHITECTURE.md`: sustituir afirmaciones de “SOLID estricto” por evidencia concreta y rutas relativas válidas.

**Prompt para el agente de Mobile:**

```text
Trabaja en ../bopacorp-mobile para normalizar su configuración Expo al estándar de BOPACORP.

Inspecciona primero git status --short y git rev-parse HEAD. No leas .env, no expongas secretos, no borres archivos y no hagas push.

Objetivos:
1. Mantener Expo funcional y TypeScript strict explícito.
2. Alinear Biome con el estándar común sin romper archivos generados ni convenciones obligatorias de Expo.
3. Crear typecheck, format:check y test:coverage; mantener tests existentes.
4. Añadir coverage y build verificable a CI, documentando cualquier limitación del entorno.
5. Evaluar Husky/Commitlint; implementarlos si son compatibles y, si no, dejar una excepción verificable en CI.
6. Reemplazar file:../bopacorp-shared por la estrategia publicada común cuando la versión requerida esté disponible; no dejar dos estrategias sin documentar.
7. Corregir ARCHITECTURE.md para que sus afirmaciones SOLID y sus rutas correspondan al código actual.

Verifica npm ci, npm run check, npm run test:coverage, typecheck y build web si el proyecto lo soporta. Reporta evidencia, excepciones y HEAD probado.
```

### 5. `../bopacorp-shared` — prioridad P1

**Ya está bien encaminado:** TypeScript strict, Biome, declaraciones, exports por dominio y patrón Zod de cuatro archivos.

**Pendientes:**

- Incorporar tests unitarios de schemas y coverage, como requisito común.
- Añadir `typecheck`, `format:check`, `test:run` y `test:coverage`.
- Hacer `check` no mutante.
- Añadir hooks y Commitlint si se mantiene como paquete versionado del mismo producto.
- Publicar el artifact de coverage en CI.
- Documentar versionado y publicación para que API, CRM, Web y Mobile consuman una única fuente de `@bopacorp/shared`.

**Prompt para el agente de Shared:**

```text
Trabaja en ../bopacorp-shared para normalizar el paquete de contratos al estándar de BOPACORP.

Inspecciona git status --short y el HEAD actual. No leas .env, no expongas secretos, no borres archivos, no hagas push y no cambies contratos sin actualizar consumidores o documentar compatibilidad.

Objetivos:
1. Mantener strict, Biome, declaraciones y el patrón index/enums/request/response por dominio.
2. Añadir framework y tests para schemas Zod, inferencia de tipos y casos inválidos; producir coverage.
3. Añadir typecheck, format:check, test:run y test:coverage.
4. Hacer check/lint de CI no mutantes.
5. Alinear hooks, Commitlint, Node/npm y CI con los repositorios consumidores.
6. Documentar publicación/versionado y dejar una única estrategia de consumo del paquete.

Verifica npm ci, npm run check, npm run test:coverage y npm run build. Reporta archivos, resultados, coverage, HEAD probado y cambios de contrato.
```

### 6. `../deploy` — prioridad P1

**Ya está bien encaminado:** Docker Compose, Caddy, servicios y puertos documentados.

**Pendientes:**

- Añadir validación automatizada de `docker compose config`.
- Validar que todas las imágenes tengan tags explícitos y, cuando sea viable, digest.
- Añadir validación de variables requeridas sin imprimir valores.
- Añadir healthchecks o smoke checks de los servicios cuando el entorno CI permita levantarlos.
- Crear workflow propio de validación de infraestructura.
- Documentar rollback y compatibilidad de la versión publicada de Shared.

**Prompt para el agente de Deploy:**

```text
Trabaja en ../deploy para crear un estándar operativo reproducible para BOPACORP.

Inspecciona git status --short y la configuración actual. No leas ni imprimas secretos, no subas imágenes, no hagas deploy real, no borres recursos y no hagas push.

Objetivos:
1. Crear validaciones automatizadas para Docker Compose, Caddy, nombres de servicios, puertos, variables requeridas y dependencias.
2. Mantener docker compose config como validación obligatoria y no mutante.
3. Revisar tags/digests de imágenes y documentar excepciones.
4. Añadir smoke/health checks seguros para CI, sin depender de credenciales reales.
5. Añadir workflow de CI y un reporte claro de pass/fail.
6. Documentar rollback y la fuente/versionado de @bopacorp/shared.

Verifica la configuración sin hacer despliegue real. Reporta archivos, comandos, resultados y riesgos pendientes.
```

### 7. `../communications` — prioridad P2

**Ya está bien encaminado:** contiene documentación e inventario histórico.

**Pendientes:**

- Definirlo formalmente como repositorio documental, no como repositorio de aplicación.
- Añadir Markdown lint y verificación de enlaces internos.
- Añadir CI para detectar enlaces rotos, archivos huérfanos y formato inválido.
- Identificar documentos históricos frente a documentación vigente.
- No forzar Biome, TypeScript ni Husky de aplicaciones si no existe código ejecutable.

**Prompt para el agente de Communications:**

```text
Trabaja en ../communications para establecer un estándar de calidad documental.

Inspecciona git status --short. No borres documentos históricos, no leas secretos, no hagas push y no cambies contenido funcional sin conservar trazabilidad.

Objetivos:
1. Inventariar Markdown vigente, histórico y obsoleto.
2. Añadir lint Markdown y validación de enlaces internos.
3. Añadir CI reproducible para esas validaciones.
4. Detectar archivos huérfanos y referencias rotas.
5. Documentar por qué no aplican Biome/TypeScript/build de aplicación.

Ejecuta las validaciones disponibles y reporta archivos, resultados, enlaces rotos y excepciones.
```

### 8. `../bopacorp` — prioridad P2, decisión de alcance

Este directorio no tiene Git y solo contiene material legacy Java. No debe recibir una “normalización” automática porque podría pertenecer a una etapa anterior del proyecto.

**Pendiente:** confirmar si se archiva, se excluye del producto actual o se incorpora formalmente con un agente separado.

**Prompt de clasificación:**

```text
Inspecciona ../bopacorp únicamente para clasificar su vigencia. No edites, no borres, no migres y no ejecutes comandos destructivos.

Determina si BOPADIGITAL_JAVA pertenece al producto actual. Entrega inventario, fecha/revisión disponible, dependencias, riesgos de conservarlo y recomendación: archivar, excluir o planificar migración.
```

### 9. `Bopadigital` — repositorio coordinador

**Pendientes:**

- Actualizar `00-architecture/repos-architecture.md` con los repositorios y módulos actuales.
- Corregir referencias antiguas a `../proy/` y a Mobile inexistente.
- Actualizar el tracker para reflejar que los tests son requisito común y que cada agente debe entregar evidencia.
- Añadir a Chapter 4 la matriz final de estándares y las refactorizaciones verificadas.
- Mantener una tabla de SHA, fecha, entorno y artifact para cada resultado.
- Validar Markdown/enlaces del propio repositorio documental.

**Prompt para el agente documental:**

```text
Trabaja en /home/gabrieltumbaco/code/BOPACORP/Bopadigital como agente de consolidación documental.

No cambies Chapter 3 ya cerrado ni reescribas decisiones aprobadas sin evidencia. No leas secretos ni modifiques repositorios hermanos.

Cuando los agentes terminen, actualiza arquitectura, README, tracker y Chapter 4 usando únicamente SHA, rutas, outputs y artifacts verificables. Distingue claramente estándar objetivo, estado observado y resultado ejecutado. Ejecuta validación Markdown/enlaces y reporta las fuentes utilizadas.
```

## Criterio de cierre por repositorio

Cada agente debe entregar, como mínimo:

1. `git status --short` inicial y final.
2. SHA probado con `git rev-parse HEAD`.
3. Archivos de configuración modificados.
4. Resultado de lint, format check, typecheck, tests con coverage y build cuando aplique.
5. URL de CI o artifact de coverage, si existe.
6. Lista de excepciones al estándar y su justificación.
7. `git diff --check` limpio.

La evidencia de una ejecución local no debe presentarse como evidencia de CI, y una captura histórica no debe presentarse como resultado actual.

## Orden recomendado de ejecución

1. API y Shared, porque fijan contratos y la referencia técnica.
2. CRM y Web, preservando sus worktrees actuales.
3. Mobile, adaptando el estándar a Expo.
4. Deploy y Communications, con sus validadores específicos.
5. Bopadigital, para consolidar la matriz y redactar Chapter 4.

