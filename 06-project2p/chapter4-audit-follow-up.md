# Chapter 4 — Audit follow-up

**Fecha de auditoría:** 2026-08-15  
**Alcance:** estructura, redacción, evidencia, CI, scripts y hooks relacionados con Chapter 4.  
**Modo:** inspección estática de LaTeX, runbook, repositorios, workflows, `package.json` e historial Git.

## Conclusión ejecutiva

La redacción de Chapter 4 está completa: no contiene `TODO`, placeholders textuales ni secciones sin
desarrollar. La estructura del capítulo, sus tablas, listings, figuras y cierre conceptual están
integrados.

La alineación técnica todavía no debe considerarse cerrada. El capítulo presenta una estandarización
común como resultado final, pero las revisiones auditadas de Web, Mobile y Shared no ejecutan toda la
secuencia de CI ni comparten el mismo contrato de hooks descrito en el texto. Esta diferencia se
conserva aquí como seguimiento separado para no convertir la redacción final en una lista de tareas.

## Lo que quedó validado

- Chapter 4 comienza en `mainETS_english_se2.tex:1691` y Chapter 5 comienza en `:2076`; no quedan
  capítulos falsos generados por la macro de capturas.
- La macro de capturas usa el nombre válido `\chaptercapture`.
- Las capturas de calidad están protegidas con `\FloatBarrier` antes de SOLID y la captura del
  refactor tiene una barrera antes del texto posterior.
- Los listings de CI, Biome y TypeScript están contenidos en bloques indivisibles.
- Las rutas largas del texto usan `\path` para permitir cortes en `/` y `.`.
- `git diff --check` pasó.
- `chktex` no reportó advertencias en el rango de Chapter 4.
- No se detectaron labels duplicados en el documento.
- El workflow completo del API coincide con el workflow existente en la revisión `4018bd5`.
- El refactor `ed79e6b` corresponde al commit real `refactor(shared): extract duplicated utilities
  to shared modules` y su resumen de 16 archivos coincide con el repositorio.

## Evidencia de capturas

En el workspace auditado todavía no están estos archivos:

```text
BOPADIGITAL/appendices/images/chapter4_hooks_commitlint.png
BOPADIGITAL/appendices/images/chapter4_quality_output_part1.png
BOPADIGITAL/appendices/images/chapter4_quality_output_part2.png
BOPADIGITAL/appendices/images/chapter4_refactor_diff.png
```

Si ya fueron cargados directamente en Overleaf, deben copiarse también al workspace para que el
handoff sea reproducible. Si no, las figuras continuarán mostrando el recuadro temporal definido por
`\chaptercapture`.

## Baseline de evidencia y HEAD actual

Los SHAs de la tabla de Chapter 4 existen y son revisiones válidas, pero algunos repositorios ya
avanzaron después de esa baseline.

| Repositorio | SHA usado en Chapter 4 | HEAD observado en la auditoría | Lectura |
|---|---:|---:|---|
| API | `4018bd5` | `4018bd5` | Coincide |
| CRM | `5011dc4` | `98db999` | El repositorio avanzó después de la baseline |
| Web | `f527679` | `11c5a3e` | El repositorio avanzó después de la baseline |
| Mobile | `4638ea1` | `c0c4a4a` | El repositorio avanzó después de la baseline |
| Shared | `4cbf3d4` | `55c4711` | El repositorio avanzó después de la baseline |
| Deploy | `b6f2f6f` | `b6f2f6f` | Coincide |

Esto no es un error si Chapter 4 se presenta como baseline de evidencia. Para evitar ambigüedad, las
capturas y resultados deben ejecutarse sobre el SHA que aparece en la tabla, o la tabla debe
actualizarse junto con una nueva validación completa.

## Desalineaciones técnicas detectadas

### Secuencia común de calidad

El texto de `mainETS_english_se2.tex:1699-1705` presenta esta secuencia:

```text
npm ci -> format:check -> lint -> typecheck -> test:coverage -> build
```

En los `package.json` auditados no existe un script público `format:check` ni un script público
`typecheck` común. Algunos workflows llaman directamente a `npx tsc`; otros llaman a `npm run check`.

### `check` como comando no mutante

El texto de `mainETS_english_se2.tex:1707-1710` describe `check` como no mutante. Sin embargo, en
las revisiones baseline de API, CRM, Web y Shared aparece `biome check --write` dentro de `check`.
Eso puede modificar el workspace y contradice la explicación del capítulo.

### Tests y coverage

El texto de `mainETS_english_se2.tex:1712-1716` afirma que todos los repositorios de aplicación
ejecutan tests y generan coverage. Los workflows auditados muestran:

| Repositorio | Workflow en la baseline | Diferencia con el texto |
|---|---|---|
| API | lint, audit, coverage y build; el build ejecuta TypeScript | Compatible en lo esencial |
| CRM | lint, typecheck, coverage y build | Compatible |
| Web | `check` y build | No ejecuta tests ni coverage en CI |
| Mobile | lint, TypeScript y tests | No ejecuta coverage ni build en CI |
| Shared | `check` y build | No ejecuta tests/schema coverage en esa baseline |

### Contrato de hooks

La redacción y la Tabla 4.4 indican que API, CRM, Web, Mobile y Shared usan Husky, lint-staged y
Commitlint (`mainETS_english_se2.tex:1922-1949`). En la inspección:

- API, CRM y Web sí tienen `.husky/pre-commit`, `.husky/commit-msg` y `lint-staged`.
- Mobile no tiene `.husky` ni `prepare`/Commitlint en su `package.json`.
- Shared no tiene `.husky` ni `prepare`/Commitlint en la revisión baseline.
- Incluso entre API, CRM y Web el `commit-msg` no es textual o paramétricamente idéntico.

## Decisión pendiente para el cierre futuro

Hay dos formas coherentes de cerrar este seguimiento:

1. **Mantener la redacción final actual:** estandarizar los repositorios para que scripts, CI, tests,
   coverage y hooks coincidan con Chapter 4; luego registrar nuevos SHAs y evidencias.
2. **Mantener el estado real actual:** ajustar las tablas y los párrafos para describir las
   diferencias existentes por repositorio, dejando la estandarización como objetivo futuro.

La primera opción conserva la decisión de redactar el informe como si el estándar estuviera listo.
En ambos casos, no debe mezclarse una captura de un `HEAD` posterior con una tabla que identifica una
baseline anterior.

## Criterios de aceptación posteriores

- Cada repositorio cubierto por la tabla tiene scripts y workflow documentados con el mismo nombre
  que usa el capítulo, o la excepción está escrita explícitamente.
- `check` es no mutante en todos los repositorios donde el capítulo lo describe así.
- Web, Mobile y Shared tienen la cobertura/validación que sus filas de Chapter 4 declaran, o las filas
  se corrigen.
- Mobile y Shared tienen el contrato de hooks descrito, o dejan de aparecer como si ya lo tuvieran.
- Las cuatro capturas existen bajo `BOPADIGITAL/appendices/images/`.
- Overleaf compila el proyecto y se revisan visualmente saltos de tabla, listings, figuras y barreras
  de sección.

## Documentos relacionados

- `06-project2p/chapter4-standardization-pending-by-repo.md`: prompts y plan de normalización por
  repositorio.
- `06-project2p/chapter4-capture-runbook.md`: comandos y nombres de capturas.
- `BOPADIGITAL/mainETS_english_se2.tex`: fuente activa del informe.

