# Validación, capturas y criterios de aceptación

## Evidencia visual incluida

Las siguientes capturas fueron copiadas desde `Bopadigital/BOPADIGITAL` a `imagenes/` para que el manual sea autocontenido:

| Archivo | Pantalla |
|---|---|
| `crm_login.png` | Inicio de sesión |
| `crm_overview.png`, `crm_overview2.png` | Inicio y métricas |
| `crm_clients.png`, `crm_client_detail.png` | Clientes y detalle |
| `crm_negotiations_table.png` | Negociaciones en tabla |
| `crm_negotiations_kanban.png` | Negociaciones en kanban |
| `crm_negotiation_detail.png` | Detalle de negociación |
| `crm_negotiation_visits.png` | Visitas |
| `crm_negotiation_documents.png` | Documentos de negociación |
| `crm_negotiation_matrix.png` | Matriz de oferta |
| `crm_documents.png` | Cola documental |
| `crm_document_upload.png` | Carga de documento |
| `crm_document_types.png` | Tipos de documento |
| `crm_reports.png`, `crm_reports2.png` | Reportes y exportaciones |
| `crm_catalog.png` | Catálogo |
| `crm_catalog_requests.png` | Solicitudes de contacto |
| `crm_vacancies.png` | Vacantes |
| `crm_applicants.png` | Postulantes |
| `crm_team.png` | Equipo |
| `crm_org_settings.png` | Configuración organizacional |

## Capturas que conviene completar

Para una versión final con el estilo del manual de referencia se recomienda añadir capturas anotadas de:

1. Formulario de creación de cliente.
2. Formulario de creación de negociación.
3. Diálogo de cambio de estado.
4. Mensaje de documentos obligatorios al cerrar.
5. Formulario de registro de visita con permiso GPS.
6. Diálogo de verificación de visita.
7. Diálogo de aprobación y rechazo documental.
8. Creación de matriz y carga de cada adjunto.
9. Edición de metas en reportes.
10. Formulario completo de producto por tipo técnico.
11. Creación de empleado.
12. Desbloqueo de usuario.
13. Detalle de postulante y descarga del CV.
14. Campana de notificaciones abierta.

## Protocolo de captura

1. Usar una base de prueba.
2. Crear registros con nombres como `CLIENTE DEMO`, `ASESOR DEMO` y `VACANTE DEMO`.
3. No utilizar contraseñas reales ni tokens.
4. Ocultar correos, teléfonos, identificaciones y documentos personales.
5. Tomar una captura antes de la acción y otra después de guardar.
6. Mantener la misma resolución y escala del navegador.
7. Colocar números y flechas azules sobre los controles relevantes, siguiendo el estilo de `Manual_docente.pdf`.

## Criterios de aceptación del manual

### Acceso

- El usuario puede identificar cómo entrar y salir.
- Se explica qué hacer ante credenciales inválidas o cuenta bloqueada.

### Operación

- Cada procedimiento tiene objetivo, perfil, pasos y resultado esperado.
- Los campos obligatorios y restricciones aparecen en un bloque IMPORTANTE.
- Los estados están explicados en lenguaje no técnico.

### Permisos

- El manual no promete una acción que el perfil no puede ejecutar.
- Las diferencias entre API y frontend están registradas como validaciones.

### Evidencia

- Cada flujo importante tiene una captura real o una marca de pendiente.
- Las capturas no exponen información personal.

### Entrega

- Se revisa el PDF exportado página por página.
- El índice y las referencias de imágenes funcionan.
- La versión y la fecha aparecen en portada y pie de página.
