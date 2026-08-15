# BOPADIGITAL — Plan de cumplimiento obligatorio de la rúbrica

**Parcial:** Software Engineering II — Final Project / Project 2P  
**Equipo:** T2  
**Fecha base:** 2026-08-14  
**Puntaje base:** 100 puntos + 3 puntos extra opcionales

## Cómo usar este documento

Este archivo es el checklist operativo de entrega. No se debe marcar una tarea como `Verificado` solamente porque exista código o una captura antigua. Para verificarla debe existir evidencia actual, asociada a una revisión conocida del código, y una persona del equipo debe abrir el artefacto y confirmar que es correcto.

Fuentes principales:

- [`02FinalProjectSpec_en.md`](./02FinalProjectSpec_en.md)
- [`Rubric_2.txt`](./Rubric_2.txt)
- [`final-delivery-tracker.md`](./final-delivery-tracker.md)
- [`requirements-test-traceability.md`](./requirements-test-traceability.md)

Estados permitidos: `No iniciado` · `En progreso` · `Listo para revisión` · `Verificado`.

Referencia específica de testing y riesgos: [software1-risk-to-testing-plan.md](./software1-risk-to-testing-plan.md).

## 1. Requisitos críticos y penalizaciones

Estos puntos se deben cerrar antes de pulir detalles secundarios. La ausencia de uno puede anular una gran parte del trabajo.

| ID | Requisito crítico | Consecuencia indicada en la especificación | Evidencia mínima | Estado | Próxima acción |
|---|---|---:|---|---|---|
| G-01 | Sistema desplegado en producción | **-100 puntos** si falta | URLs actuales de Web, CRM y API; respuesta `/health`; fecha y commit desplegado; capturas | No iniciado | Verificar el entorno final y guardar evidencia reproducible |
| G-02 | Formulario de aceptación firmado por el cliente | **-100 puntos** si falta | Formulario legible, fecha, firmas y enlace en el informe | Listo para revisión | Confirmar que corresponde a la revisión final |
| G-03 | Comunicaciones con el cliente durante el proyecto | **-30 puntos** si falta | README/index actualizado, mensajes, reuniones, entregas y aceptación | Listo para revisión | Revisar que cubra hasta el despliegue final |
| G-04 | Informe autocontenido en inglés y con formato solicitado | Hasta **-100%** por incumplimiento de entrega | PDF `T2BOPADIGITAL.pdf`, fuente final, índice, enlaces accesibles y anexos | No iniciado | Crear la versión final sin sobrescribir el informe anterior |
| G-05 | Coevaluaciones individuales | **-50 puntos** si falta | Confirmación de entrega de cada integrante en Aula Virtual | No iniciado | Asignar responsable y fecha a cada integrante |
| G-06 | Repositorios y herramientas accesibles | **-50 puntos** si el repositorio no tiene acceso | Permisos verificados y enlaces probados desde una cuenta evaluadora | No iniciado | Revisar permisos antes de entregar |
| G-07 | Video de presentación | Requisito de entrega | Video en inglés, aproximadamente 13 minutos, participación equilibrada y enlace funcional | No iniciado | Preparar runbook, grabar y verificar el enlace |

### Política de retraso

La especificación indica penalización por retraso: hasta 12 horas `-10%`, de 12 a 24 horas `-20%`, de 24 a 48 horas `-30%` y más de 48 horas `-100%`. La fecha límite y el canal de entrega deben confirmarse con el docente.

## 2. Checklist de los 100 puntos

| ID | Criterio | Puntos | Qué debemos entregar | Evidencia que debe quedar | Estado |
|---|---|---:|---|---|---|
| R-01 | Project information | 3 | Cliente, problema, objetivos, alcance, actores, escenarios, cantidad de historias y sprints | Capítulo del informe, diapositivas y fuentes actuales | En progreso |
| R-02 | Architectural decisions | 3 | Diagrama de componentes/despliegue y justificación de tecnologías | Diagrama actualizado, tabla de decisiones y referencias a repositorios | En progreso |
| R-03 | Feature demonstration | 10 | Demostración funcional en inglés con participación equilibrada | Video, diapositivas, runbook y capturas de los escenarios | No iniciado |
| R-04 | Testing management and documentation | 4 | Estrategia, niveles de prueba, responsables, calendario y resultados | `test-execution-log.md`, comandos, resultados y defectos/retests | No iniciado |
| R-05 | User manual | 10 | Manual por rol con prerrequisitos, pasos numerados, clics y resultados esperados | `user-manual.md`, capturas actuales y versión PDF | No iniciado |
| R-06 | Installation guide | 10 | Instalación local/producción, variables, paquetes, base de datos, Docker, Caddy y troubleshooting | `installation-guide.md`, comandos verificados y capturas | No iniciado |
| R-07 | Project, communication and architecture evidence | 10 | Evidencia indexada del cliente, aceptación, repositorios, herramientas y arquitectura | `communications`, formularios, URLs, diagramas y anexos | En progreso |
| R-08 | Risk-based testing | 10 | Riesgos, probabilidad, impacto, control, casos asociados, resultados y retests | `risk-based-test-report.md` y matriz requisito-prueba | No iniciado |
| R-09 | SCRUM adherence | 5 | Backlog, historias, planificación, revisiones, gráficos y aceptación por sprint | `03-scrum/`, capturas de la herramienta y anexos | Listo para revisión |
| R-10 | Coding standards and diagnostics | 10 | Biome, TypeScript estricto, hooks, lint, typecheck y diagnóstico preventivo | Configuración, comandos y resultados de la revisión final | En progreso |
| R-11 | CI with quality data | 10 | CI con instalación, lint, typecheck, tests, coverage, build y artifacts | URLs de runs, SHA, fechas, coverage y archivos descargables | En progreso |
| R-12 | Acceptance-testing tool | 10 | Escenarios automatizados de aceptación ejecutables y reproducibles | Playwright, reportes HTML, capturas/videos y artifacts de CI | No iniciado |
| R-13 | SOLID, patterns and refactoring | 5 | Ejemplos concretos del código y al menos un refactor documentado | Comparación antes/después, archivos, commit y explicación | No iniciado |

**Total obligatorio: 100 puntos.**

### Extras opcionales

Se pueden intentar después de cerrar los 100 puntos base:

- `X-01` GUI test automation: 1 punto.
- `X-02` Application profiling: 1 punto.
- `X-03` Load testing: 1 punto.

No se deben priorizar los extras mientras falte evidencia de los criterios obligatorios.

## 3. Escenarios de aceptación que deben cubrirse

Estos escenarios conectan la funcionalidad, las pruebas, el manual, la demo y el informe.

| ID | Rol | Flujo mínimo | Aplicación |
|---|---|---|---|
| AT-01 | Visitante público — Web | Filtrar catálogo, consultar servicio y enviar solicitud de contacto | `bopacorp-web/e2e/public-catalog-and-contact.spec.ts` |
| AT-02 | Candidato — Web | Consultar vacante, probar validación y enviar CV PDF válido | `bopacorp-web/e2e/job-application.spec.ts` |
| AT-03 | Administrador CMS — Web/CRM | Editar bloque CMS, crear/actualizar producto y verificar resultado público | `bopacorp-crm/e2e/admin-cms-catalog.spec.ts` |
| AT-04 | Asesor comercial — CRM | Registrar cliente, crear negociación, registrar visita y subir documento | `bopacorp-crm/e2e/advisor-commercial-workflow.spec.ts` |
| AT-05 | Supervisor/coordinador — CRM | Filtrar trabajo, revisar datos y aprobar/rechazar documento con motivo | `bopacorp-crm/e2e/supervision-and-documents.spec.ts` |
| AT-06 | Manager — CRM | Consultar reportes, filtrar período/asesor y exportar resultado | `bopacorp-crm/e2e/manager-reports.spec.ts` |
| AT-07 | Asesor — Mobile | Login, clientes, negociación y documentos | Solo si existe el repositorio y el flujo es estable |

Para cada ejecución se debe registrar: ambiente/base URL, SHA de cada repositorio, tester, fecha, precondiciones, pasos, resultado esperado, resultado observado, Pass/Fail/Blocked, evidencia y retest.

## 4. Orden recomendado de trabajo

### Fase 1 — Cerrar alcance y riesgos

- [ ] Elegir los escenarios AT-01 a AT-06 que se mostrarán en la demo.
- [ ] Asignar responsable y fecha a cada criterio R-01 a R-13.
- [ ] Alinear la versión de `@bopacorp/shared` en API, CRM y Web antes de probar integración.
- [ ] Confirmar cuentas de prueba, datos semilla, URLs y ambiente controlado.
- [ ] Mantener Matrices fuera del alcance funcional por decisión del cliente; reconciliar el código residual del API y documentarlo como limitación técnica si permanece.
- [ ] Localizar/verificar Mobile antes de incluirlo en la demo; si no existe evidencia actual, declararlo como futuro trabajo.

### Fase 2 — Ejecutar pruebas y corregir bloqueadores

- [ ] Ejecutar la cobertura existente del API y CRM.
- [ ] Crear pruebas de componentes y flujos críticos de Web.
- [ ] Crear pruebas Playwright para Web y CRM.
- [ ] Ejecutar AT-01 a AT-06 en una revisión conocida.
- [ ] Corregir únicamente defectos que bloqueen una demo, una prueba, un criterio de la rúbrica o una evidencia obligatoria.
- [ ] Registrar cada defecto, fix SHA y resultado del retest.

### Fase 3 — Capturar calidad y despliegue

- [ ] Ejecutar lint, typecheck, tests, coverage y build en CI.
- [ ] Guardar URL del run, SHA, fecha y artifacts.
- [ ] Capturar `/health`, Web, CRM y API del entorno desplegado.
- [ ] Confirmar que las capturas no exponen contraseñas, tokens ni datos personales reales.
- [ ] Actualizar comunicaciones y solicitar/confirmar aceptación correspondiente a la versión final.

### Fase 4 — Crear manuales y anexos

- [ ] Escribir el manual de usuario a partir de AT-01 a AT-06.
- [ ] Preparar capturas reales con flechas, rectángulos, números y leyendas consistentes.
- [ ] Escribir la guía de instalación a partir de comandos realmente verificados.
- [ ] Crear el log de ejecución de pruebas.
- [ ] Crear el informe de pruebas basado en riesgos.
- [ ] Crear el documento de evidencia de calidad y CI.

### Fase 5 — Informe y presentación

- [ ] Actualizar arquitectura, alcance, historias, sprints y limitaciones.
- [ ] Documentar estándares, SOLID, patrones y refactorización con ejemplos reales.
- [ ] Preparar el runbook de 13 minutos en inglés con participación equilibrada.
- [ ] Grabar y revisar el video completo.
- [ ] Compilar el PDF final dos veces y revisar índice, enlaces, figuras, tablas, gramática y nombre del archivo.
- [ ] Verificar permisos de todos los repositorios, herramientas, video y documentos.
- [ ] Confirmar formularios de aceptación y coevaluaciones.

## 5. Definición de terminado para cualquier afirmación

Una funcionalidad solo puede aparecer como `implemented and tested` en el informe cuando se cumplen todas estas condiciones:

- [ ] Existe una ruta de código actual en el repositorio responsable.
- [ ] El rol correspondiente puede ejecutar el flujo en el ambiente definido.
- [ ] Existe una prueba unitaria, de integración o de aceptación cuando sea razonable.
- [ ] El log registra un resultado Pass sobre una revisión conocida.
- [ ] Existe screenshot, video, reporte o archivo exportado utilizable en el informe/manual/demo.
- [ ] Las limitaciones conocidas están declaradas como limitaciones o trabajo futuro.

## 6. Línea base observada el 2026-08-15

- API: tiene 59 archivos de tests registrados y coverage configurado en CI; todavía falta registrar evidencia final de ejecución y porcentaje de cobertura.
- CRM: tiene tests de autenticación y coverage configurado en CI; todavía faltan los escenarios de aceptación completos.
- Web: tiene CI de lint/typecheck/build, pero no tiene suite automatizada de aceptación ni tests registrados.
- Shared: tiene CI de lint/typecheck/build, pero no tiene suite de tests registrada.
- Deploy: existe Compose y README, pero la prueba actual de producción debe capturarse y asociarse a un SHA.
- Communications: existe índice y aceptación final; se debe confirmar que la evidencia corresponde a la versión final.
- Mobile: no se encontró el checkout `bopacorp-mobile` en la ubicación esperada; no se debe afirmar funcionalidad mobile sin localizarlo y verificarlo.
- Matrices: están descoped por decisión del cliente; no deben aparecer como feature de demo ni como riesgo activo de cálculos de subsidios.

## 7. Regla final del equipo

La evidencia ejecutada manda sobre la documentación anterior. Si una función no puede demostrarse, probarse y documentarse en la revisión final, debe presentarse como limitación o futuro trabajo, no como funcionalidad terminada.
