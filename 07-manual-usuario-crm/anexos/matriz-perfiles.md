# Matriz de perfiles y acceso

Este anexo sirve para preparar las versiones del manual por perfil. La regla práctica es documentar solamente las acciones que aparecen para el usuario autenticado.

## Grupos de acceso del frontend

| Grupo | Perfiles incluidos | Uso |
|---|---|---|
| `ORG_ROLES` | `admin`, `manager` | Catálogo y organización. |
| `DOC_ROLES` | `admin`, `manager`, `coordinator` | Cola documental y tipos de documento. |
| `SALES_MANAGEMENT_ROLES` | `admin`, `manager`, `supervisor` | Reportes y métricas de gestión. |

## Acceso observable en el CRM

| Sección | Admin | Manager | Supervisor | Asesor | Coordinador | Web-admin |
|---|---:|---:|---:|---:|---:|---:|
| Inicio/métricas | Sí | Sí | Sí | Sí, propios | No como página inicial | No |
| Clientes | Sí | Sí | Sí | Sí, propios | Sí, lectura | No |
| Negociaciones | Sí | Sí | Sí | Sí, propias | Sí, lectura | No |
| Documentación global | Sí | Sí | Validar en instalación | Acciones dentro de negociación | Sí | No |
| Tipos de documento | Sí | Sí | No por ruta del frontend | Lectura | Sí | No |
| Reportes | Sí | Sí | Sí | No por guard de ruta | No | No |
| Catálogo CRM | Sí | Sí | No | No | No | API sí, ruta CRM bloqueada |
| Solicitudes de contacto | Sí | Sí | No por ruta del frontend | No | No por ruta del frontend | Validar CMS |
| Organización | Sí | Sí | No | No | No | No |
| Vacantes | Sí | Sí | No | No | No | Sí |
| Postulantes | Sí | Sí | No | No | No | Sí |

## Acciones de negocio

### Asesor

- Crear, consultar y editar clientes propios.
- Crear, consultar y actualizar negociaciones propias.
- Cambiar el estado de sus negociaciones cuando el permiso esté disponible.
- Registrar y consultar visitas propias.
- Subir documentos desde los flujos permitidos.
- Crear y administrar matrices propias.
- Consultar sus métricas en Inicio.

### Supervisor

- Consultar y administrar clientes y negociaciones dentro del alcance asignado.
- Registrar visitas y verificarlas.
- Consultar métricas de los asesores supervisados.
- Generar exportaciones de reportes.
- Validar documentación desde las superficies que la instalación exponga.

### Manager

- Operar el ciclo comercial completo.
- Configurar metas de ventas.
- Administrar catálogo y tablas auxiliares.
- Administrar empleados, departamentos y roles organizacionales.
- Desbloquear cuentas de usuario.
- Administrar vacantes y revisar postulantes.

### Coordinador

- Consultar clientes y negociaciones en modo lectura.
- Revisar documentos pendientes.
- Aprobar o rechazar documentos con motivo.
- Crear, editar y desactivar tipos de documento.

## Alcance de datos

| Perfil | Alcance |
|---|---|
| Asesor | Registros propios de clientes, negociaciones, visitas y documentos. |
| Supervisor | Registros de los asesores relacionados en la configuración organizacional. |
| Manager | Alcance general de la operación. |
| Coordinador | Documentación disponible para revisión y consultas de apoyo. |
| Administrador | Sin restricción funcional prevista. |

## Discrepancias que deben validarse antes de la publicación

1. La API concede algunos permisos de documentación al supervisor, pero las rutas globales del frontend usan `DOC_ROLES`, que no incluye supervisor.
2. El asesor tiene permiso de lectura de reportes en la API, pero la ruta `/reportes` usa `SALES_MANAGEMENT_ROLES` y actualmente no le permite entrar.
3. `web-admin` tiene permisos de catálogo en la API, pero las rutas CRM de catálogo usan `ORG_ROLES`.
4. La documentación de planificación describe un acceso a Overview para más perfiles que el comportamiento actual de `SalesOnly`.

Para el manual final, estas diferencias deben resolverse con una cuenta de cada perfil o convertirse en una nota de configuración de la instalación.
