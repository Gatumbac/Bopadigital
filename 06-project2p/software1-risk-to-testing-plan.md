# BOPADIGITAL — Puente entre riesgos de Software I y testing de Software II

**Proyecto:** BOPADIGITAL — BOPACORP S.A.  
**Uso:** Plan de pruebas basado en riesgos para el segundo parcial  
**Fecha base:** 2026-08-14

## 1. Propósito

Este documento convierte el análisis de riesgos definido en el proyecto final de Software I en una estrategia de pruebas verificable para Software II.

La relación que debe mantenerse para cada riesgo es:

~~~
Riesgo → Requisito → Caso de prueba → Resultado observado → Evidencia → Retest
~~~

El análisis original se encuentra en [`mainETS_english.tex`](../BOPADIGITAL/mainETS_english.tex:168), sección RISK MANAGEMENT, SPRINT BACKLOGS, AND PROJECT SCHEDULING. El documento posterior de Software II contiene una tabla histórica de casos TC01–TC20 y una primera sección de tests unitarios en [`mainETS_english_se2.tex`](../BOPADIGITAL/mainETS_english_se2.tex:1348), pero sus resultados deben volver a verificarse sobre la revisión actual del código.

### Decisión de alcance vigente

El cliente decidió descartar el módulo de Matrices como funcionalidad del producto final. Por eso no se debe planificar testing de cálculos de subsidios, precios, cantidades, aprobación de matrices ni indicadores comerciales de matrices.

El código todavía contiene un residuo técnico del módulo: el API mantiene src/modules/matrices/ y createNegotiation inserta una fila en offer_matrices. Esto debe tratarse como una inconsistencia de implementación pendiente, no como una funcionalidad que se presentará en la demo.

Para el segundo parcial:

- [ ] Marcar MAT/SUP como descoped por decisión del cliente.
- [ ] Excluir la lógica de subsidios y aprobación de matrices del conjunto de código crítico.
- [ ] Confirmar si se eliminará el insert automático de matriz al crear una negociación o si quedará como compatibilidad interna.
- [ ] Si el residuo permanece en la revisión final, cubrir solamente su efecto de regresión sobre la creación de negociaciones y declararlo como limitación técnica.

## 2. Regla de cobertura

La rúbrica del segundo parcial no exige 100% de cobertura global. Sin embargo, el requisito no funcional RNF-021 establece que los tests unitarios deben cubrir al menos el **80% del código crítico**: BOPADIGITAL_REQUIREMENTS_SPECIFICATION_DOCUMENT.md, línea 685.

Por lo tanto, la meta de este plan es:

- [ ] Definir y documentar el conjunto de código crítico.
- [ ] Alcanzar al menos 80% en ese conjunto.
- [ ] Medir cobertura de líneas y revisar también ramas importantes.
- [ ] Ejecutar todos los tests en CI.
- [ ] Guardar el reporte HTML/LCOV, el SHA, la fecha y la URL del CI.
- [ ] Relacionar los tests con requisitos y riesgos.

El 100% puede ser una meta interna para módulos pequeños o reglas críticas, pero no debe reemplazar una estrategia basada en riesgo ni justificar tests frágiles o puramente mecánicos.

## 3. Riesgos heredados de Software I

| ID original | Riesgo | Probabilidad original | Impacto original | Respuesta original | Traducción a testing |
|---|---|---|---|---|---|
| 001 | Field Connectivity Failures | Very High | Critical | Offline-first, almacenamiento local y sincronización | Probar timeout, pérdida de red, reintentos, duplicación de solicitudes e idempotencia. Si no existe offline-first, documentarlo como limitación. |
| 002 | Geolocation Inaccuracy | High | High | Tolerancias y corrección manual supervisada | Probar coordenadas inválidas, valores fuera de rango, ubicación ausente, permiso denegado y corrección solo por roles autorizados. |
| 003 | Subsidy Calculation Complexity | Descoped | Descoped | Decisión del cliente: no se implementa el módulo de matrices ni el cálculo de subsidios | Mantener como riesgo histórico únicamente. No crear nuevos tests ni presentarlo como funcionalidad final. |
| 004 | Sales Staff Resistance to Change | High | Moderate | UX intuitiva y capacitación | Validar mediante pruebas de aceptación, tareas por rol y observación de usabilidad; no es principalmente un riesgo de unit testing. |
| 005 | Storage Overload | Low | High | Compresión, almacenamiento escalable y retención | Probar tipo, tamaño, formato, archivo corrupto, error del proveedor, limpieza y permisos de descarga. |
| 006 | Approval Role and Permission Changes | Moderate | Moderate | RBAC flexible y configurable | Probar RBAC, ownership y permisos sobre documentos, usuarios y negociaciones; no probar aprobación de matrices descoped. |

## 4. Riesgos prioritarios para la API

### Prioridad crítica

#### Auth, RBAC y ownership

Debe probarse como tabla de decisión:

| Usuario autenticado | Permiso | Propietario del recurso | Resultado esperado |
|---|---|---|---|
| No | Cualquiera | Cualquiera | 401 Unauthorized |
| Sí | No tiene permiso | Cualquiera | 403 Forbidden |
| Sí | Sí | No es propietario y el rol no permite supervisión | 403 o resultado no visible |
| Sí | Sí | Es propietario | Operación permitida |
| Sí | Sí | No es propietario, pero es supervisor/manager autorizado | Operación permitida según alcance |

Casos mínimos:

- [ ] Login válido e inválido.
- [ ] Ruta sin token.
- [ ] Token inválido o expirado.
- [ ] Rol insuficiente.
- [ ] Acceso a cliente o negociación de otro asesor.
- [ ] Supervisor con alcance de equipo.
- [ ] Manager con acceso a reportes permitidos.
- [ ] Usuario bloqueado y usuario desbloqueado.

#### Estados comerciales y aprobaciones

Aplicar pruebas de transición de estados:

- [ ] Transición válida.
- [ ] Transición inválida.
- [ ] Cambio al mismo estado como no-op.
- [ ] Historial creado una sola vez.
- [ ] Rechazo con motivo obligatorio.
- [ ] Aprobación solo para el rol autorizado.
- [ ] Error cuando la entidad no existe.
- [ ] Fallo de persistencia sin dejar estado parcial.

### Prioridad alta

#### Documentos y almacenamiento

- [ ] PDF válido.
- [ ] Tipo MIME no permitido.
- [ ] Archivo mayor al límite.
- [ ] Archivo vacío o corrupto.
- [ ] Documento sin negociación o tipo documental.
- [ ] Fallo del storage.
- [ ] Rechazo y aprobación con persistencia correcta.
- [ ] Descarga individual y descarga masiva con permisos.

#### Clientes, negociaciones y visitas

- [ ] Creación válida.
- [ ] RUC duplicado.
- [ ] Actualización de un recurso inexistente.
- [ ] Filtros combinados.
- [ ] Propiedad del asesor.
- [ ] Registro de visita con coordenadas válidas.
- [ ] Coordenadas ausentes o fuera de rango.
- [ ] Error de base de datos.

#### Reportes y cálculos

- [ ] Dataset pequeño con totales calculados manualmente.
- [ ] Sin datos.
- [ ] Fechas en los límites del período.
- [ ] Filtros por asesor, supervisor y fecha.
- [ ] Estados comerciales contados correctamente.
- [ ] Exportación con contenido esperado.
- [ ] Restricción de acceso según rol.

## 5. Código crítico que debe cubrirse

La definición final debe ajustarse al código actual, pero inicialmente se consideran críticos:

- [ ] Autenticación, JWT, bloqueo de cuenta y middleware de autorización.
- [ ] Roles, permisos y relaciones asesor-supervisor.
- [ ] Clientes empresariales.
- [ ] Negociaciones, visitas y cambios de estado; no incluir flujo de matrices.
- [ ] Validación y subida de documentos.
- [ ] Aplicaciones laborales y solicitudes públicas.
- [ ] Cálculos y filtros de reportes que sigan en alcance.
- [ ] Validaciones compartidas de Zod que controlan contratos API.

Se pueden excluir, con justificación documentada:

- Tipos sin lógica ejecutable.
- Archivos generados.
- Configuración simple.
- Seeds y scripts operativos que no participan en el flujo de negocio probado.
- El módulo de Matrices, cálculos de subsidios y flujo de aprobación descoped. Si el código residual sigue siendo alcanzable desde negociaciones, se debe documentar y probar solo como regresión técnica.

## 6. Técnicas de prueba que se deben aplicar

### Equivalence partitioning

Separar entradas en clases válidas, inválidas, vacías, duplicadas, expiradas y no autorizadas. Aplicar a emails, RUC, estados, filtros, permisos y archivos.

### Boundary value analysis

Probar 0, 1, máximo permitido, máximo + 1, fechas inicial/final, tamaño máximo de archivo y límites de paginación.

### Decision tables

Usar combinaciones de rol, permiso, propietario, estado y operación para evitar probar solo el camino feliz.

### State-transition testing

Representar las transiciones permitidas y prohibidas de negociaciones, documentos y aprobaciones.

### Parameterized tests

Usar it.each para repetir una misma regla sobre roles, permisos, estados y entradas límite sin duplicar código.

### Mocks, fakes y fixtures

- Mockear la base de datos, storage, correo y servicios externos en unit tests.
- Usar fixtures deterministas o builders de datos.
- Limpiar mocks y estado entre tests.
- Reservar Supertest para probar rutas, middleware, validación y respuestas HTTP integradas.

### Arrange–Act–Assert

Cada test debe separar preparación, ejecución y verificación. Las aserciones deben validar el resultado observable, no únicamente que una función interna fue llamada.

## 7. Organización recomendada de tests en el API

Cada módulo crítico debe cubrir servicio y controlador cuando corresponda:

~~~
src/modules/<module>/<module>.service.test.ts
src/modules/<module>/<module>.controller.test.ts
~~~

Nombres recomendados:

~~~
auth-rbac
resource-ownership
negotiation-state-transitions
document-upload-validation
report-calculations
public-application-validation
~~~

Los tests deben describir comportamiento:

~~~
it('rejects an advisor who tries to access another advisor client')
it('does not create a second history entry for the current negotiation state')
it('rejects a resume larger than the configured limit')
~~~

## 8. Evidencia que debe entregarse

Para cada ejecución importante guardar:

- [ ] Nombre del test o comando ejecutado.
- [ ] Repositorio y commit SHA.
- [ ] Ambiente y versión de Node.
- [ ] Fecha, responsable y duración.
- [ ] Resultado total y casos fallidos.
- [ ] Resumen de cobertura.
- [ ] Reporte HTML/LCOV descargable.
- [ ] Defecto, fix SHA y retest cuando aplique.
- [ ] Relación con requisito, user story y riesgo.

La evidencia debe alimentar:

- 06-project2p/test-execution-log.md.
- 06-project2p/risk-based-test-report.md.
- 06-project2p/requirements-test-traceability.md.
- El capítulo de testing del informe final.

## 9. Criterio de terminado de esta fase

La fase de testing unitario del API está terminada cuando:

- [ ] Los módulos críticos están definidos y justificados.
- [ ] Los riesgos críticos tienen casos de prueba asociados.
- [ ] Existen casos exitosos, negativos, de seguridad y de límites.
- [ ] La cobertura del código crítico es al menos 80%.
- [ ] Todos los tests pasan localmente y en CI.
- [ ] La cobertura se publica como artifact.
- [ ] Cada afirmación de Passed tiene SHA, fecha y evidencia.
- [ ] Las limitaciones conocidas están declaradas y no se presentan como funcionalidades verificadas.

## 10. Estado actual observado el 2026-08-15

- API: 59 archivos de tests registrados. Los commits recientes amplían cobertura en organización, CRM, catálogo, empleabilidad, documentos, notificaciones y usuarios. Aún falta conservar el resultado de ejecución y el porcentaje de cobertura asociado a una revisión final.
- CRM: 6 archivos de tests registrados, concentrados en AuthContext, guards de autenticación/permisos y cliente API. No cubre todavía los flujos completos de asesor, supervisor, coordinador, manager o CMS.
- Web: no tiene archivos de tests registrados ni suite automatizada.
- Frontends: todavía faltan tests de formularios, validaciones, estados de carga/error, permisos y flujos de aceptación.
- Matrices: existen código, rutas y tests en el API, pero el módulo está fuera del alcance funcional decidido con el cliente. Debe reconciliarse el código residual antes de afirmar que está completamente descartado.
- Esta revisión fue estática; no se deben reportar los tests como Pass hasta guardar la ejecución real, SHA, fecha y artifact.

## 11. Advertencia sobre documentación histórica

El documento de Software I y el borrador de Software II son fuentes de contexto y diseño. Las frases históricas como Passed, deployed o verified no son evidencia actual por sí solas. Para el segundo parcial se deben volver a ejecutar los escenarios seleccionados sobre la revisión final y conservar los artifacts correspondientes.
