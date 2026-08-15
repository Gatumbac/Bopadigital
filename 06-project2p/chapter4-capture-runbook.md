# Chapter 4 — Runbook de evidencia de código

## Decisión de presentación

Chapter 4 no necesita capturas de pantalla de archivos completos. La evidencia técnica se inserta
directamente en `BOPADIGITAL/mainETS_english_se2.tex` mediante bloques `lstlisting` breves. Cada bloque
muestra únicamente el fragmento que demuestra la regla explicada; no se copia un archivo completo.

No se muestran fechas, tokens, contraseñas, cookies, valores de `.env`, URLs privadas ni datos
personales. La trazabilidad se mantiene con el repositorio, el SHA corto, la ruta del archivo, el
comando y el resultado validado.

## Listings usados en Chapter 4

| Listing LaTeX | Repositorio fuente | Archivos o comando | Evidencia |
|---|---|---|---|
| `lst:chapter4_ci_pipeline` | `../bopacorp-api` | `.github/workflows/ci.yml` | Secuencia de CI: instalación, lint, tipos, pruebas y build |
| `lst:chapter4_biome` | `../bopacorp-api` | `biome.json` | Reglas de lint y formato |
| `lst:chapter4_tsconfig` | `../bopacorp-api` | `tsconfig.json` | Compilación estricta |
| `lst:chapter4_hooks_commitlint` | `../bopacorp-api` | `.husky/*`, `package.json` | Hook `pre-commit`, hook `commit-msg` y `lint-staged` |
| `lst:chapter4_quality_output` | `../bopacorp-api` | Comandos de calidad | Resultado representativo sin timestamps |
| `lst:chapter4_refactor_diff` | `../bopacorp-api` | Diff de `ed79e6b` | Extracción de utilidades compartidas |

Los demás repositorios aparecen en las tablas comparativas del capítulo. El API se usa como ejemplo
visual porque el patrón se repite en CRM, Web, Mobile y Shared; Deploy y Communications conservan
sus validaciones específicas.

## Comandos para obtener los fragmentos

Ejecutar los siguientes comandos dentro del repositorio fuente. El SHA corto sirve para asociar la
evidencia con el estado revisado y no contiene fechas.

### API: CI

~~~bash
cd /home/gabrieltumbaco/code/BOPACORP/bopacorp-api
git rev-parse --short HEAD
sed -n '1,180p' .github/workflows/ci.yml
~~~

Usar únicamente el bloque de pasos de Node, `npm ci`, lint, typecheck, tests con coverage y build.
No insertar el workflow completo.

### API: Biome y TypeScript

~~~bash
cd /home/gabrieltumbaco/code/BOPACORP/bopacorp-api
git rev-parse --short HEAD
sed -n '1,180p' biome.json
sed -n '1,180p' tsconfig.json
~~~

Seleccionar las opciones que demuestran la política: reglas recomendadas, `noExplicitAny`, imports y
variables no usados, `strict`, `noUncheckedIndexedAccess`, ancho de línea, indentación, comillas,
punto y coma y trailing commas.

### API: hooks y Commitlint

~~~bash
cd /home/gabrieltumbaco/code/BOPACORP/bopacorp-api
git rev-parse --short HEAD
sed -n '1,80p' .husky/pre-commit
sed -n '1,80p' .husky/commit-msg
sed -n '1,140p' commitlint.config.js
npm pkg get lint-staged
~~~

El listing debe mostrar solo la ejecución de `lint-staged`, la ejecución de Commitlint y la regla de
archivos staged. Este es el hook que demuestra cómo se bloquea una modificación que no cumple la
política antes del commit.

## Comandos de calidad por repositorio

No hace falta tomar una captura de la terminal. Ejecutar los comandos, conservar el resultado de la
validación y resumirlo en la matriz del capítulo sin incluir timestamps.

### API

~~~bash
cd /home/gabrieltumbaco/code/BOPACORP/bopacorp-api
git rev-parse --short HEAD
npm run lint
npx tsc --noEmit
npm run test:coverage
npm run build
~~~

Para el listing representativo se puede usar `npm run test:run` cuando se necesita el conteo breve
de archivos y pruebas, siempre que el resultado provenga de la misma revisión.

### CRM

~~~bash
cd /home/gabrieltumbaco/code/BOPACORP/bopacorp-crm
git rev-parse --short HEAD
npm run check
npm run test:coverage
npm run build
~~~

### Web

~~~bash
cd /home/gabrieltumbaco/code/BOPACORP/bopacorp-web
git rev-parse --short HEAD
npm run check
npm run test:coverage
npm run build
~~~

### Mobile

~~~bash
cd /home/gabrieltumbaco/code/BOPACORP/bopacorp-mobile
git rev-parse --short HEAD
npm run check
npm run test:coverage
npm run build:web
~~~

### Shared

~~~bash
cd /home/gabrieltumbaco/code/BOPACORP/bopacorp-shared
git rev-parse --short HEAD
npm run check
npm run test:coverage
npm run build
~~~

### Deploy

~~~bash
cd /home/gabrieltumbaco/code/BOPACORP/deploy
git rev-parse --short HEAD
docker compose config --quiet
docker compose config
~~~

### Communications

~~~bash
cd /home/gabrieltumbaco/code/BOPACORP/communications
git rev-parse --short HEAD
npm run check
~~~

## Refactor antes/después

La evidencia del refactor se obtiene como texto, no como captura de un diff completo:

~~~bash
cd /home/gabrieltumbaco/code/BOPACORP/bopacorp-api
git diff --stat ed79e6b^ ed79e6b
git diff --no-ext-diff --unified=20 ed79e6b^ ed79e6b -- \
  src/shared/constants/auth.ts \
  src/shared/utils/format.ts \
  src/shared/utils/query.ts \
  src/shared/utils/request.ts
~~~

En LaTeX se conserva solo el cambio representativo: la extracción de `fetchPermissionCodes`, la
constante `BCRYPT_SALT_ROUNDS` y el resumen de archivos modificados. No se inserta el diff completo.

## Regla de edición del LaTeX

Los listings deben permanecer cortos, con caption y label. Si un comando produce demasiadas líneas,
seleccionar el fragmento que prueba la afirmación y mantener el resultado resumido en una tabla.
Chapter 4 no depende de archivos PNG nuevos; los PNG históricos no se referencian en el documento.
