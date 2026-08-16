# Chapter 4 — Runbook de evidencia de código y capturas

## Decisión de presentación

Chapter 4 usa dos tipos de evidencia, cada uno en el formato que mejor lo representa:

- Los fragmentos de configuración y código se insertan directamente en
  `BOPADIGITAL/mainETS_english_se2.tex` mediante bloques `lstlisting` estilizados. Solo se muestra el
  fragmento que demuestra la regla explicada.
- Las salidas de comandos, los Git hooks y el diff del refactor se insertan como capturas PNG. No se
  fotografía un archivo completo ni una terminal con contenido irrelevante.

El documento ya contiene un recuadro temporal para cada captura pendiente. Cuando guardes el PNG con
el nombre indicado en `BOPADIGITAL/appendices/images/`, el recuadro se sustituirá automáticamente por
la imagen.

No se muestran fechas, tokens, contraseñas, cookies, valores de `.env`, URLs privadas ni datos
personales. La trazabilidad se mantiene con el repositorio, el SHA corto, la ruta del archivo, el
comando y el resultado validado.

## Mapa de evidencia usado en Chapter 4

| Elemento LaTeX | Repositorio fuente | Archivo, comando o captura | Evidencia |
|---|---|---|---|
| `lst:chapter4_ci_pipeline` | `../bopacorp-api` | `.github/workflows/ci.yml` | Secuencia de CI: instalación, lint, tipos, pruebas y build |
| `lst:chapter4_biome` | `../bopacorp-api` | `biome.json` | Reglas de lint y formato |
| `lst:chapter4_tsconfig` | `../bopacorp-api` | `tsconfig.json` | Compilación estricta |
| `fig:chapter4_hooks_commitlint` | `../bopacorp-api` | `chapter4_hooks_commitlint.png` | Hook `pre-commit`, hook `commit-msg` y `lint-staged` |
| `fig:chapter4_quality_output_part1` | `../bopacorp-api` | `chapter4_quality_output_part1.png` | SHA, lint y validación TypeScript |
| `fig:chapter4_quality_output_part2` | `../bopacorp-api` | `chapter4_quality_output_part2.png` | Pruebas y build de producción |
| `fig:chapter4_refactor_diff` | `../bopacorp-api` | `chapter4_refactor_diff.png` | Extracción de utilidades compartidas |

Los demás repositorios aparecen en las tablas comparativas del capítulo. El API se usa como ejemplo
visual porque el patrón se repite en CRM, Web, Mobile y Shared; Deploy conserva su validación
operativa específica. El archivo de evidencia del proyecto se documenta fuera de este capítulo.

## Guardar las capturas

Después de limpiar la terminal y dejar visible solo el resultado relevante, usa la selección de
área del sistema. Los comandos siguientes guardan directamente en la carpeta que ya utiliza el
LaTeX:

~~~bash
gnome-screenshot -a -f /home/gabrieltumbaco/code/BOPACORP/Bopadigital/BOPADIGITAL/appendices/images/chapter4_hooks_commitlint.png
gnome-screenshot -a -f /home/gabrieltumbaco/code/BOPACORP/Bopadigital/BOPADIGITAL/appendices/images/chapter4_quality_output_part1.png
gnome-screenshot -a -f /home/gabrieltumbaco/code/BOPACORP/Bopadigital/BOPADIGITAL/appendices/images/chapter4_quality_output_part2.png
gnome-screenshot -a -f /home/gabrieltumbaco/code/BOPACORP/Bopadigital/BOPADIGITAL/appendices/images/chapter4_refactor_diff.png
~~~

Ejecuta un comando, selecciona la región de la terminal y repite con el siguiente nombre. No
incluyas el escritorio completo; la captura debe contener solo la terminal y el resultado.

## Comandos para obtener los fragmentos de código

Ejecutar los siguientes comandos dentro del repositorio fuente. El SHA corto sirve para asociar la
evidencia con el estado revisado y no contiene fechas.

### API: CI

~~~bash
cd /home/gabrieltumbaco/code/BOPACORP/bopacorp-api
git rev-parse --short HEAD
sed -n '1,180p' .github/workflows/ci.yml
~~~

El listing del capítulo reproduce el workflow completo, compactado únicamente mediante la eliminación
de líneas vacías de presentación. No se exponen valores de secretos; únicamente aparece la referencia
segura `secrets.NPM_TOKEN` utilizada por GitHub Actions.

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

Este elemento ahora es una captura. La terminal debe mostrar únicamente los tres hooks/reglas que
demuestran la protección local. La evidencia será una verificación real de commit, no una captura de
los archivos de configuración.

~~~bash
cd /home/gabrieltumbaco/code/BOPACORP/bopacorp-api
git status --short
git switch -c evidence/chapter4-hooks
printf '%s\n' 'export const chapter4HookCheck = true;' > src/chapter4-hook-check.ts
git add src/chapter4-hook-check.ts
git commit -m 'verify hooks'
git commit -m 'docs: verify commit hooks'
git show -s --format='%h %s' HEAD
~~~

El primer commit debe ser rechazado por Commitlint porque no tiene formato Conventional Commits.
Después ejecuta el segundo comando de commit; debe pasar por Husky, ejecutar `lint-staged`, validar
el mensaje y crear el commit. El último comando muestra el commit real sin imprimir la fecha.

Si el repositorio no está limpio, no cambies de rama ni mezcles la prueba con trabajo pendiente.
Realiza esta verificación en una rama temporal separada. Cuando termines la captura, puedes conservar
la rama hasta cerrar el PDF y eliminarla después si ya no la necesitas.

Guarda la captura como `BOPADIGITAL/appendices/images/chapter4_hooks_commitlint.png`. Recorta solo
la secuencia del rechazo, la ejecución exitosa de Husky y el commit final; no incluyas el escritorio,
el prompt con tu nombre ni fechas.

## Comandos de calidad por repositorio

Las dos figuras del capítulo usan la salida del API como ejemplo visual. Los demás repositorios se
mantienen en la tabla comparativa; no hace falta una captura por repositorio.

### API

#### Parte 1: SHA, lint y TypeScript

~~~bash
cd /home/gabrieltumbaco/code/BOPACORP/bopacorp-api
clear
git rev-parse --short HEAD
npm run lint
npx tsc --noEmit && printf '%s\n' 'TypeScript check: passed'
~~~

Toma esta primera salida y guárdala como
`BOPADIGITAL/appendices/images/chapter4_quality_output_part1.png`.

#### Parte 2: pruebas y build

~~~bash
cd /home/gabrieltumbaco/code/BOPACORP/bopacorp-api
clear
npm run test:run
npm run build && printf '%s\n' 'Build: passed'
~~~

Toma esta segunda salida y guárdala como
`BOPADIGITAL/appendices/images/chapter4_quality_output_part2.png`. No incluyas prompts con el nombre
de usuario, rutas personales, timestamps ni variables de entorno.
La revisión esperada es `4018bd58c6856e9258b7e79b0b91eeaa852a5459`; su referencia está disponible en
el [commit de cobertura de reports en GitHub](https://github.com/Bopacorp/bopacorp-api/commit/4018bd58c6856e9258b7e79b0b91eeaa852a5459).

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

## Refactor antes/después

La evidencia del refactor corresponde exactamente al commit
`ed79e6b99dc8341766fe34e21af3466745a861bb`, titulado
`refactor(shared): extract duplicated utilities to shared modules`. Su padre es
`4a258d601730aca3166bb84812669b4dd8adb80c`. Puedes abrir el
[commit del refactor en GitHub](https://github.com/Bopacorp/bopacorp-api/commit/ed79e6b99dc8341766fe34e21af3466745a861bb)
o el [diff entre el padre y el refactor](https://github.com/Bopacorp/bopacorp-api/compare/4a258d601730aca3166bb84812669b4dd8adb80c...ed79e6b99dc8341766fe34e21af3466745a861bb).

La captura debe ser recortada; no fotografíes el diff completo del repositorio. La salida siguiente
incluye el helper `fetchPermissionCodes`, el uso de `BCRYPT_SALT_ROUNDS` y los nuevos módulos
compartidos que se mencionan en el capítulo.

~~~bash
cd /home/gabrieltumbaco/code/BOPACORP/bopacorp-api
git diff --stat 4a258d601730aca3166bb84812669b4dd8adb80c ed79e6b99dc8341766fe34e21af3466745a861bb
git diff --no-ext-diff --unified=3 4a258d601730aca3166bb84812669b4dd8adb80c ed79e6b99dc8341766fe34e21af3466745a861bb -- \
  src/modules/auth/auth.service.ts \
  src/shared/constants/auth.ts \
  src/shared/utils/format.ts \
  src/shared/utils/query.ts \
  src/shared/utils/request.ts
~~~

Toma una captura donde se lean la extracción de `fetchPermissionCodes`, la constante
`BCRYPT_SALT_ROUNDS` y el resumen de archivos modificados. Guarda la captura como
`BOPADIGITAL/appendices/images/chapter4_refactor_diff.png`.

## Regla de edición del LaTeX

Los listings de código deben permanecer cortos, con caption y label; el estilo `chaptercode` ya
aplica fondo tenue, marco, colores para palabras clave, cadenas y comentarios, y saltos de línea
controlados. Las cuatro figuras de captura deben conservar exactamente sus nombres y labels. Si una
salida produce demasiadas líneas, se recorta la terminal al fragmento que prueba la afirmación.
