# Manual de usuario — BOPACORP CRM

Documentación de usuario del CRM web de BOPACORP, preparada a partir del comportamiento actual del frontend, la API REST, los contratos de `@bopacorp/shared`, la documentación del proyecto y las capturas disponibles en el repositorio de contexto.

## Contenido

- [`MANUAL_USUARIO_CRM.md`](./MANUAL_USUARIO_CRM.md): manual principal para usuarios no técnicos.
- [`anexos/matriz-perfiles.md`](./anexos/matriz-perfiles.md): acceso por perfil y acciones disponibles.
- [`anexos/trazabilidad-funcional.md`](./anexos/trazabilidad-funcional.md): relación entre funciones documentadas y archivos fuente.
- [`anexos/validacion-y-capturas.md`](./anexos/validacion-y-capturas.md): inventario de capturas, datos de evidencia y pendientes de validación en ejecución.
- [`manual_usuario_crm.tex`](./manual_usuario_crm.tex): plantilla LaTeX con portada y estilo de procedimientos inspirado en `Manual_docente.pdf`.
- [`imagenes/`](./imagenes/): capturas del CRM reutilizadas para el manual.

## Alcance

Este manual documenta el CRM web actual: acceso, clientes, negociaciones, visitas, documentación, matrices, reportes, catálogo, organización y empleabilidad.

La API y la arquitectura se utilizan como fuentes de trazabilidad, pero no se presentan como pasos de uso para el usuario final.

## Fuente de verdad

Cuando existe una diferencia entre un documento de planificación y el sistema implementado, este manual sigue la interfaz y las rutas actuales del CRM. Las diferencias conocidas se registran en los anexos para que puedan corregirse o validarse antes de publicar una versión final.

## Estado del documento

- Versión: 0.1 — borrador completo basado en código y documentación.
- Fecha de elaboración: 14 de agosto de 2026.
- Capturas disponibles: reutilizadas desde `Bopadigital/BOPADIGITAL`.
- Pendiente: validación de los procedimientos con cuentas reales o de prueba, datos anonimizados y sesión de aceptación.

## Generación de una versión PDF

La fuente principal es el archivo Markdown. La plantilla LaTeX contiene la portada, la estructura visual y los estilos de procedimiento. Antes de entregar el PDF final se deben revisar las imágenes, completar las capturas pendientes y compilar/renderizar la versión seleccionada.

No se deben incluir contraseñas, tokens, RUC reales, teléfonos reales ni información personal de clientes o postulantes.
