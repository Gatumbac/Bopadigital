# BOPADIGITAL — Guía para crear las tareas de ClickUp de los Sprints 4–7

**Fecha de preparación:** 2026-08-15  
**Propósito:** servir como handoff para el agente que inspeccionará el estado actual de ClickUp y completará las tareas históricas de los Sprints 4, 5, 6 y 7.  
**Responsable de la ejecución:** otro agente autorizado por el equipo.  
**Responsable de la orquestación:** equipo BOPADIGITAL.

Esta guía define qué debe crear el agente, qué debe verificar antes de escribir en ClickUp y qué evidencia debe devolver. El agente ejecutor debe trabajar con el token mediante `CLICKUP_API_TOKEN`; nunca debe copiar el token en este repositorio, en capturas ni en logs.

## 1. Objetivo y límites

El objetivo es completar la planificación de ClickUp para los Sprints 4, 5, 6 y 7 dentro de la carpeta existente de BOPADIGITAL, manteniendo intactas las tareas históricas de los Sprints 1–3. Sprint 4 comenzó con el tiempo limitado del primer parcial y tuvo una ventana extendida para la entrega final.

El agente ejecutor debe:

- inspeccionar primero el espacio, la carpeta, las listas y las tareas existentes;
- reutilizar la carpeta y las listas existentes cuando ya estén creadas;
- crear únicamente tareas de los Sprints 4–7 que puedan trazarse a una fuente del proyecto;
- conservar la jerarquía de tarea padre y subtareas usada por el script original;
- devolver un reporte de ejecución con IDs, tareas omitidas, errores y pendientes de evidencia.

El agente ejecutor no debe:

- ejecutar nuevamente el script completo de Sprints 1–4;
- sobrescribir o duplicar tareas de Sprint 4 que ya existan en ClickUp;
- crear una segunda carpeta llamada `BOPADIGITAL` sin resolver primero si ya existe una;
- borrar tareas, carpetas, listas o evidencias existentes;
- marcar una tarea como completada solo porque aparezca en una carta de aceptación;
- reintroducir el módulo de matrices o funcionalidades descartadas;
- modificar el informe LaTeX, el código de aplicación de los repositorios o los manuales como parte de esta operación; la adaptación del script de orquestación se permite únicamente si es necesaria y queda registrada;
- inventar fechas de inicio, resultados de pruebas, porcentajes de cobertura o despliegues.

## 2. Fuentes de verdad y prioridad

Usar las fuentes en este orden:

| Prioridad | Fuente | Uso correcto |
|---|---|---|
| 1 | Repositorios actuales y sus artefactos verificables | Determinar si una tarea está realmente implementada, probada o documentada. |
| 2 | [`CARTAS.md`](./CARTAS.md) | Definir el alcance aceptado por el cliente y las fechas de aceptación de cada sprint. |
| 3 | [`mainETS_english_se2_legacy.tex`](../BOPADIGITAL/mainETS_english_se2_legacy.tex) | Recuperar el backlog ampliado de Sprint 4 que se planificó durante el primer parcial. |
| 4 | [`rubric-must-have-plan.md`](./rubric-must-have-plan.md) y [`final-delivery-tracker.md`](./final-delivery-tracker.md) | Relacionar cada tarea con la rúbrica y con la evidencia de entrega. |
| 5 | [`requirements-test-traceability.md`](./requirements-test-traceability.md) y [`software1-risk-to-testing-plan.md`](./software1-risk-to-testing-plan.md) | Construir tareas de pruebas, riesgos, trazabilidad, defectos y retests. |
| 6 | [`create-clickup-tasks.py`](../../bopacorp-api/.scripts/create-clickup-tasks.py) y [`BOPADIGITAL_Scrum_Final_Corregido.md`](../03-scrum/BOPADIGITAL_Scrum_Final_Corregido.md) | Usar como plantilla histórica de nombres, responsables y jerarquía; no como fuente final de alcance. |

### Advertencias sobre las fuentes históricas

El script original solo define Sprints 1–4. Además, crea una carpeta nueva en cada ejecución y no tiene modo `dry-run`, detección de duplicados ni rollback. Por eso no debe ejecutarse sin modificarlo o sin preparar una ejecución equivalente y segura.

El archivo legacy planifica Sprint 4 como una iteración ampliada de 25 tareas, con un cierre inicial el 24 de junio. La carta posterior del Sprint 4, fechada el 5 de julio, confirma formalmente el bloque de frontend testing y evidencia SCRUM. Para el reporte final se deben conservar ambos hechos: el legacy explica el alcance planificado y la carta establece la aceptación del cliente.

El backlog histórico contiene tareas de matrices y otros elementos que ya no representan el alcance final. La decisión vigente del proyecto es mantener el módulo de matrices fuera del producto entregado.

La carta específica de Sprint 6 se concentra en calidad y mantenibilidad, mientras que el resumen de aceptación final agrupa también la guía de instalación, el manual, la documentación API y la presentación en Sprint 6. El agente debe conservar ambas referencias en la descripción de las tareas y marcar como pendiente cualquier evidencia que no pueda localizar.

## 3. Fechas aceptadas

Las siguientes fechas son fechas de aceptación, no necesariamente fechas de inicio:

| Sprint | Fecha de aceptación | Fuente |
|---|---|---|
| Sprint 4 | 2026-07-05 | `CARTAS.md`, carta de aceptación del Sprint 4 |
| Sprint 5 | 2026-07-14 | `CARTAS.md`, carta de aceptación del Sprint 5 |
| Sprint 6 | 2026-07-21 | `CARTAS.md`, carta de aceptación del Sprint 6 |
| Sprint 7 | 2026-07-28 | `CARTAS.md`, carta de aceptación del Sprint 7 |
| Cierre final | 2026-08-07 | `CARTAS.md`, carta de aceptación final |

No se debe inventar una fecha de inicio. Si la configuración de ClickUp exige `start_date`, el agente debe:

1. buscar una fecha respaldada por el historial de comunicaciones o por ClickUp;
2. si no existe, dejarla vacía cuando la API lo permita; o
3. detenerse y reportar la decisión requerida, en vez de asignar una fecha arbitraria.

## 4. Alcance que debe representarse en ClickUp

Los nombres pueden conservar el estilo en español del script original. Los identificadores técnicos como `Vitest`, `React Testing Library`, `IEEE 29119`, `Biome`, `CI/CD` y `Gherkin` deben escribirse exactamente.

### Sprint 4 — Alcance ampliado del legacy y aceptación final

Fechas de referencia: **2026-06-24** para el cierre inicial descrito en el legacy y **2026-07-05** para la carta de aceptación del cliente.

El documento legacy (`mainETS_english_se2_legacy.tex`, líneas 701–767) presenta Sprint 4 como una iteración de transición entre el primer parcial y la entrega final. El agente debe representar estos ocho grupos como tareas padre, pero marcar cada una según la evidencia actual:

1. **Suite de pruebas frontend — Vitest y React Testing Library**
   - Configurar o verificar Vitest + RTL en `bopacorp-web`.
   - Probar landing page, autenticación y CMS.
   - Configurar o verificar Vitest + RTL en `bopacorp-crm`.

2. **Compilación de evidencia SCRUM**
   - Capturas de ClickUp de los sprints.
   - Evidencia de comunicaciones.
   - Índice con archivos, fechas y participantes.
   - Sprint reviews y retrospectivas.

3. **Inicio del informe final del proyecto**
   - Consolidar introducción, alcance, arquitectura, Scrum, testing y despliegue.
   - Registrar capítulos y evidencias faltantes.
   - Tratar la redacción posterior como continuación, no como una tarea duplicada.

4. **Carta de aceptación del cliente**
   - Coordinar la revisión con el cliente.
   - Registrar la carta de aceptación del Sprint 4 y su ubicación.
   - No sustituir la carta del Sprint 4 por la aceptación final del 7 de agosto.

5. **Preparación de la guía de instalación y despliegue**
   - Documentar Docker, variables de entorno y base de datos.
   - Preparar manual por rol y documentación API como entregables relacionados.
   - Marcar como continuación las versiones definitivas de Sprint 6 o Sprint 7.

6. **Preparación de presentación y video demostrativo**
   - Preparar diapositivas con la plantilla de ESPOL.
   - Definir demo por rol, arquitectura, decisiones y resultados de pruebas.
   - Registrar el video final únicamente cuando exista el enlace y la revisión del equipo.

7. **Perfilamiento de la aplicación**
   - Verificar si existe una medición reproducible del API Node.js.
   - Registrar herramienta, escenario, resultado y bottlenecks.
   - Mantener pendiente lo que solo exista como planificación histórica.

8. **Polish final y QA**
   - Revisar responsive, navegadores, seguridad y comportamiento de sesión.
   - Asociar cada hallazgo a una corrección y un retest.

La carta del Sprint 4 confirma expresamente los grupos 1 y 2. Los grupos 3–8 provienen del plan legacy y deben quedar como iniciados, continuados o completados únicamente con evidencia actual. Si los Sprints 5–7 contienen la finalización de uno de estos grupos, usar nombres como `Continuación`, `Finalización` o `Versión definitiva` para no crear dos tareas que parezcan el mismo trabajo.

### Sprint 5 — Pruebas, riesgos y métricas

Fecha de aceptación: **2026-07-14**.

Crear las siguientes tareas padre y subtareas:

1. **Pruebas de aceptación automatizadas y escenarios Gherkin**
   - Confirmar la herramienta y la configuración realmente presentes en Web y CRM.
   - Definir escenarios Gherkin por historia y por rol.
   - Implementar o registrar los escenarios de aceptación ejecutables.
   - Guardar reportes, capturas, videos o logs de las ejecuciones.

2. **Ejecución de pruebas de aceptación por rol**
   - Visitante/candidato en el portal público.
   - Administrador en CMS y catálogo.
   - Asesor en clientes, negociaciones, visitas y documentos.
   - Supervisor/coordinador en revisión y aprobación de documentos.
   - Manager en reportes y filtros.
   - Mobile únicamente si el repositorio, el flujo y la evidencia actual están disponibles.

3. **Plan de pruebas basado en riesgos e IEEE 29119**
   - Consolidar riesgos actuales desde Software Engineering I.
   - Mapear `Riesgo → Requisito → Caso de prueba → Resultado → Evidencia → Retest`.
   - Priorizar autenticación, RBAC, ownership, transiciones de estado, documentos, clientes, visitas y reportes.
   - Identificar explícitamente los riesgos descartados por el cambio de alcance de matrices.

4. **Pruebas de sistema e integración**
   - Validar flujos completos frontend → API → base de datos.
   - Validar integración entre CRM, Documentos, Supervisión y Reportes.
   - Registrar precondiciones, datos de prueba, respuesta esperada y respuesta observada.
   - Asociar cada ejecución con el SHA de los repositorios y el ambiente utilizado.

5. **Métricas de calidad y cobertura**
   - Registrar cobertura por repositorio y por módulo usando la ejecución actual.
   - Documentar qué métricas están disponibles y cómo se calculan.
   - No confundir cobertura global con el requisito de cobertura del código crítico.
   - Guardar URL de CI, SHA, fecha y artifact cuando exista.

6. **Registro de defectos y retests**
   - Crear un registro con defecto, severidad, pasos, ambiente, evidencia y responsable.
   - Asociar cada corrección con su commit o pull request.
   - Ejecutar y registrar el retest después de cada corrección.

7. **Pruebas de flujo de datos**
   - Seleccionar variables críticas de los módulos principales.
   - Validar entrada, transformación, persistencia y salida.
   - Registrar datos inválidos, límites y errores esperados.

8. **Perfilamiento de la aplicación**
   - Confirmar si existe una medición reproducible de rendimiento.
   - Registrar herramienta, escenario, entorno, resultado y conclusión.
   - Mantener la tarea como pendiente si solo existe una intención histórica y no un artifact verificable.

9. **Inicio de consolidación del informe final**
   - Relacionar resultados de pruebas, riesgos, defectos y métricas con el reporte.
   - Identificar evidencias faltantes para capítulos, anexos y rúbrica.

### Sprint 6 — Calidad preventiva, mantenibilidad y documentación

Fecha de aceptación: **2026-07-21**.

Crear las siguientes tareas padre y subtareas:

1. **Revisión de principios SOLID y refactorización**
   - Seleccionar ejemplos reales por repositorio.
   - Documentar problema, cambio aplicado y resultado.
   - Asociar los ejemplos con archivos y commits actuales.

2. **Aplicación de patrones de diseño**
   - Identificar patrones realmente presentes en el código.
   - Explicar el problema que resuelve cada patrón.
   - No registrar un patrón solo porque aparezca en una lista teórica.

3. **Refactorización del código base**
   - Registrar mejoras de legibilidad, modularidad, duplicación o mantenibilidad.
   - Verificar que los tests y el build sigan pasando después de cada cambio.

4. **Análisis estático y estándares de codificación**
   - Verificar las herramientas configuradas actualmente en cada repositorio.
   - Para este proyecto, comprobar especialmente Biome, TypeScript y hooks existentes.
   - La carta histórica menciona `ESLint/PMD`; no marcar PMD como ejecutado si no existe evidencia real.
   - Registrar comandos, revisión, fecha y resultado.

5. **Integración continua con datos de calidad**
   - Verificar jobs de instalación, lint, typecheck, tests, coverage y build.
   - Guardar URL del pipeline, SHA, fecha y artifacts descargables.
   - Registrar fallos y correcciones relevantes.

6. **Pruebas cross-browser**
   - Definir navegadores, versión, ambiente y escenarios.
   - Ejecutar y guardar resultados para Chrome, Firefox y Edge cuando estén disponibles.
   - No convertir una revisión manual aislada en una prueba automatizada sin evidencia.

7. **Revisión de seguridad**
   - Revisar autenticación, autorización, manejo de secretos, validación de entradas y exposición de datos.
   - Asociar hallazgos con riesgo, severidad, corrección y retest.

8. **Accesibilidad y diseño responsive**
   - Registrar viewport, navegador, flujo y criterios revisados.
   - Guardar capturas o reportes de los hallazgos y correcciones.

9. **Documentación y material de presentación**
   - Verificar la guía de instalación y despliegue.
   - Verificar los manuales de usuario por rol.
   - Verificar la documentación de API.
   - Verificar el material de presentación y su correspondencia con el informe final.

### Sprint 7 — Cierre, validación y entrega final

Fecha de aceptación: **2026-07-28**. El cierre final del proyecto fue aceptado el **2026-08-07**.

Crear las siguientes tareas padre y subtareas:

1. **Despliegue final en producción**
   - Verificar Web, CRM y API en el entorno final.
   - Registrar URL, fecha, SHA desplegado y respuesta de salud.
   - Guardar capturas sin secretos ni datos personales innecesarios.

2. **Guía definitiva de instalación y despliegue**
   - Confirmar prerrequisitos, variables, instalación, base de datos, despliegue y validación.
   - Incluir troubleshooting y rollback solo cuando estén realmente verificados.

3. **Manual final de usuario por rol**
   - Verificar los roles Asesor, Supervisor, Administrador y Candidato.
   - Confirmar pasos numerados, acciones de clic, resultados esperados y capturas actuales.
   - Adjuntar los PDF finales como anexos cuando corresponda.

4. **Informe final del proyecto**
   - Verificar capítulos, objetivos, alcance, arquitectura, sprints, testing, riesgos y contribuciones.
   - Reemplazar TODOs por evidencia actual o limitaciones explícitas.
   - Compilar y revisar visualmente el PDF final en Overleaf.

5. **Validación final de requisitos**
   - Ejecutar los escenarios de aceptación seleccionados.
   - Confirmar requisitos funcionales y no funcionales con resultado y evidencia.
   - Resolver o declarar los defectos restantes.

6. **Correcciones finales derivadas del Sprint 6**
   - Registrar cada corrección, responsable, commit y retest.
   - No crear tareas genéricas sin criterio de aceptación.

7. **Repositorio y paquete final de evidencias**
   - Revisar permisos y enlaces de todos los repositorios.
   - Consolidar comunicaciones, cartas firmadas, capturas, videos, manuales y guías.
   - Congelar revisión, fecha y artefactos usados en el informe.

8. **Video demostrativo y reunión de cierre**
   - Verificar duración, idioma, participación y escenarios demostrados.
   - Guardar el enlace final y una lista breve de lo demostrado.

9. **Aceptación final del cliente**
   - Confirmar carta firmada del 2026-08-07.
   - Registrar ubicación de la evidencia y su inclusión en el reporte.

## 5. Responsables, prioridades y estados

El script histórico usa los siguientes identificadores. El agente debe confirmarlos mediante la API antes de crear tareas:

| Alias | Persona | Uso sugerido |
|---|---|---|
| `GT` | Gabriel Tumbaco — `101235845` | Coordinación, API, DevOps, integración y reporte |
| `ND` | Nahim Díaz — `216131439` | Backend, testing API, calidad y DevOps |
| `SM` | Salvador Muñoz — `101235842` | Backend y frontend/CRM |
| `SA` | Shirley Aragón — `101235844` | Frontend, CRM, Web y documentación visual |
| `AN` | Anthony Navarrete — `101235843` | Frontend y Mobile |

Asignar por responsabilidad técnica actual y confirmar la participación con el equipo. No reasignar una tarea basándose únicamente en el comentario histórico del script.

### Prioridad sugerida

- `urgent`: despliegue final, aceptación, defectos bloqueantes y requisitos con penalización.
- `high`: pruebas de aceptación, integración, riesgos, CI, seguridad y documentación obligatoria.
- `normal`: refactorización, estándares, cross-browser, accesibilidad y preparación de evidencias.
- `low`: extras opcionales, perfilamiento adicional o mejoras que no bloqueen la entrega.

### Estados

Antes de crear tareas, consultar los estados reales de la lista en ClickUp. Usar el nombre exacto configurado en el workspace, aunque el script original use `completadas`, `en curso` y `pendiente`.

- **Completada:** existe implementación o documento actual, resultado verificable y evidencia enlazable.
- **En curso:** existe trabajo parcial, pero falta ejecución, revisión, evidencia o retest.
- **Pendiente:** no existe implementación o evidencia suficiente.
- **Bloqueada:** no puede continuar por una dependencia externa; describir la dependencia.

No usar `completada` para tareas sustentadas únicamente por una carta o una captura antigua.

## 6. Protocolo seguro de ejecución en ClickUp

### Fase A — Preflight de solo lectura

1. Confirmar que `CLICKUP_API_TOKEN` está disponible sin imprimirlo.
2. Consultar el Space `90176024370`.
3. Buscar todas las carpetas llamadas `BOPADIGITAL`.
4. Si no existe ninguna, reportarlo y crear una solo después de confirmar el objetivo.
5. Si existe una única carpeta, reutilizarla.
6. Si existen varias, detenerse y pedir selección; no adivinar.
7. Consultar las listas y las tareas actuales de esa carpeta.
8. Exportar un inventario temporal con IDs, nombres, estados y fechas, excluyendo tokens.

### Fase B — Preview y deduplicación

1. Preparar un plan local de Sprints 4–7 sin hacer `POST`.
2. Normalizar nombres para detectar duplicados por `(sprint, tarea padre/subtarea)`.
3. Comparar el plan con las tareas existentes.
4. Mostrar qué se reutilizará, qué se creará y qué quedará pendiente.
5. Revisar que las tareas no incluyan matrices ni claims sin evidencia.
6. Confirmar las fechas de inicio antes de enviarlas.

### Fase C — Escritura controlada

1. Reutilizar listas `Sprint 4`, `Sprint 5`, `Sprint 6` y `Sprint 7` si existen.
2. Crear únicamente las listas faltantes dentro de la carpeta correcta.
3. Crear tareas padre y, después, sus subtareas.
4. Incluir en cada descripción la fuente, el criterio de terminado y la evidencia esperada.
5. Registrar el ID devuelto por ClickUp inmediatamente después de cada creación.
6. Si ocurre un error, detener la ejecución o continuar solo con una lista explícita de tareas independientes; no repetir toda la corrida.
7. No borrar automáticamente tareas creadas parcialmente. Preparar una lista de IDs para revisión manual.

### Fase D — Verificación posterior

1. Consultar nuevamente cada lista y verificar nombres, jerarquía, responsables, estados y fechas.
2. Confirmar que los Sprints 1–3 no fueron modificados y que las tareas existentes de Sprint 4 no fueron duplicadas.
3. Confirmar que no se creó una carpeta duplicada.
4. Comparar el número de tareas planificadas, creadas, reutilizadas, omitidas y fallidas.
5. Devolver un reporte con IDs y enlaces de ClickUp.
6. Capturar las vistas de cada sprint para el anexo SCRUM del informe.

## 7. Reglas para adaptar el script

Si se reutiliza [`create-clickup-tasks.py`](../../bopacorp-api/.scripts/create-clickup-tasks.py), el agente debe adaptar el flujo antes de ejecutar:

- agregar selección explícita de sprints, por ejemplo `Sprint 4`, `Sprint 5`, `Sprint 6` y `Sprint 7`;
- permitir `--dry-run`;
- permitir recibir un `folder_id` existente;
- consultar carpetas y listas antes de crear;
- hacer deduplicación por nombre normalizado y sprint;
- generar un log JSON sin secretos;
- aceptar estados reales del workspace;
- evitar fechas de inicio inventadas;
- preservar el plan histórico de Sprints 1–3 sin reejecutarlo y usar el legacy para completar Sprint 4;
- no agregar tareas de matrices, cálculos de subsidios ni funcionalidades fuera del alcance final.

No es necesario modificar el script si el agente puede implementar el mismo protocolo de manera segura en una ejecución separada. En cualquier caso, debe reportar qué archivo o comando usó y qué revisión del repositorio ejecutó.

## 8. Reporte que debe devolver el agente ejecutor

El resultado de la ejecución debe contener:

- fecha y hora de ejecución;
- Space, folder y list IDs utilizados;
- revisión del script o archivo de plan utilizado;
- número de tareas encontradas, reutilizadas, creadas, omitidas y fallidas;
- tabla de tarea → ClickUp ID → estado → responsable → fecha;
- errores completos sin incluir secretos;
- tareas que requieren decisión humana;
- enlaces de ClickUp para cada sprint;
- confirmación de que no se tocó S1–S3 ni se duplicaron las tareas existentes de Sprint 4;
- capturas o indicación exacta de las capturas que faltan para el informe.

## 9. Criterios de aceptación de esta guía

La operación se considera correctamente orquestada cuando:

- [ ] Sprints 4–7 existen dentro de la carpeta correcta o se reportó claramente por qué no se crearon.
- [ ] Todas las tareas tienen una fuente y un criterio de terminado.
- [ ] Las tareas padre tienen responsables y subtareas coherentes.
- [ ] Los estados reflejan evidencia actual, no solo planificación histórica.
- [ ] No se duplicó la carpeta ni se reejecutó S1–S3.
- [ ] No se incluyó el módulo de matrices.
- [ ] Se registraron las incertidumbres sobre fechas, herramientas y evidencia.
- [ ] Se entregó el inventario final de IDs y enlaces.
- [ ] Se identificaron las capturas necesarias para actualizar el capítulo SCRUM y los anexos.

Esta guía es un plan de orquestación. La creación efectiva en ClickUp, la validación de los resultados y la captura de evidencias pertenecen al agente ejecutor y deben quedar respaldadas por su reporte final.
