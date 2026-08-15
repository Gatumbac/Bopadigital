# Plan: Consolidate the BOPADIGITAL final-report chapter map

**Date:** 2026-08-15  
**Status:** Completed  
**Context:** The report structure existed in the active LaTeX source and the rubric was distributed across several Markdown files, but there was no single document describing the purpose, evidence, and completion condition of each chapter.

## Objectives

- [x] Map every current chapter and appendix to its intended content.
- [x] Link chapters to the corresponding rubric criteria and evidence sources.
- [x] Record the current status of each chapter and the recommended writing sequence.
- [x] Preserve the agreed LaTeX, scope, and evidence standards.

## Steps of implementation

1. **Inspect the source structure** — Review the active LaTeX chapter headings, rubric, final-delivery plan, tracker, requirements, and historical references.
2. **Define chapter responsibilities** — Document purpose, content, evidence, readiness condition, and status for Chapters 1–8.
3. **Define appendix responsibilities** — Map manuals, installation, deployment, communications, presentation, and testing artifacts to their evidence.
4. **Add rubric traceability and submission gates** — Make mandatory points, penalties, and final verification conditions visible.
5. **Create the repository document** — Save the consolidated plan in 06-project2p/final-report-chapter-plan.md.

## Files affected

- 06-project2p/final-report-chapter-plan.md — New chapter-by-chapter report plan.
- .opencode/plans/final-report-chapter-plan.md — Completed planning record for this documentation task.

## Risks and considerations

- Historical reports and reference reports may contain obsolete features or facts; current repository and execution evidence take precedence.
- The final PDF still requires Overleaf compilation and visual inspection.
- Mobile, deployment, frontend testing, and acceptance claims must remain limited to verified evidence.
- The matrix module remains outside the final scope by client decision.

## References

- 06-project2p/Rubric_2.txt
- 06-project2p/02FinalProjectSpec_en.md
- 06-project2p/final-delivery-plan.md
- 06-project2p/final-delivery-tracker.md
- 06-project2p/rubric-must-have-plan.md
- 06-project2p/latex-working-directory.md
- BOPADIGITAL/mainETS_english_se2.tex
- 02-requirements/BOPADIGITAL_REQUIREMENTS_SPECIFICATION_DOCUMENT.md

## Cambios al plan

- La narrativa del informe se ajustó para representar la entrega final: las evidencias faltantes se gestionan como tareas pendientes de cierre y no como afirmaciones de ausencia dentro de los capítulos.
- Se añadió una tarea explícita para consolidar las cartas de aceptación de todos los sprints y la aceptación final en el paquete de comunicaciones.
