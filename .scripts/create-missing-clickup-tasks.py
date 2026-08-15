#!/usr/bin/env python3
"""Create missing BOPADIGITAL ClickUp tasks for Sprints 5–7 incrementally."""

import argparse
import json
import os
import sys
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import requests


REPO_ROOT = Path(__file__).resolve().parents[1]
ENV_FILES = (
    REPO_ROOT / ".env",
    REPO_ROOT.parent / "bopacorp-api" / ".env",
)

SPACE_ID = "90176024370"
FOLDER_ID = "90179341245"
LISTS = {
    "Sprint 5": "901716103979",
    "Sprint 6": "901716103981",
    "Sprint 7": "901716103982",
}

ACCEPTANCE_DATES = {
    "Sprint 5": "2026-07-14",
    "Sprint 6": "2026-07-21",
    "Sprint 7": "2026-07-28",
}

M = {
    "GT": 101235845,
    "ND": 216131439,
    "SM": 101235842,
    "SA": 101235844,
    "AN": 101235843,
}

PRIO = {"urgent": 1, "high": 2, "normal": 3, "low": 4}
STATUSES = ("completadas", "en curso", "pendiente")
DEFAULT_STATUS = "completadas"
DEFAULT_DELAY = 3.0
BASE = "https://api.clickup.com/api/v2"
RATE_LIMITED = False


def load_repo_env():
    """Load only CLICKUP_API_TOKEN from the local project env files."""
    for env_file in ENV_FILES:
        if not env_file.is_file():
            continue

        for raw_line in env_file.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("export "):
                line = line[7:].lstrip()

            key, separator, value = line.partition("=")
            if separator and key.strip() == "CLICKUP_API_TOKEN":
                value = value.strip()
                if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                    value = value[1:-1]
                os.environ.setdefault("CLICKUP_API_TOKEN", value)


load_repo_env()
TOKEN = os.getenv("CLICKUP_API_TOKEN")
HEADERS = {
    "Authorization": TOKEN or "",
    "Content-Type": "application/json",
}


def ms(date_value):
    return int(
        datetime.strptime(date_value, "%Y-%m-%d")
        .replace(tzinfo=timezone.utc)
        .timestamp()
        * 1000
    )


def normalize(value):
    """Normalize names for safe duplicate detection without changing display names."""
    plain = unicodedata.normalize("NFKD", value)
    plain = "".join(char for char in plain if not unicodedata.combining(char))
    return " ".join(plain.casefold().split())


def api(method, path, data=None, params=None):
    """Call ClickUp once; never sleep through a long rate-limit window."""
    global RATE_LIMITED

    if not TOKEN:
        raise SystemExit(
            "CLICKUP_API_TOKEN is required; add it to a local .env file or export it."
        )

    try:
        response = requests.request(
            method,
            f"{BASE}{path}",
            headers=HEADERS,
            json=data,
            params=params,
            timeout=30,
        )
    except requests.RequestException as error:
        print(f"  ERR network: {error}")
        return None

    if response.status_code == 429:
        RATE_LIMITED = True
        retry_after = response.headers.get("Retry-After", "desconocido")
        print(
            "  ERR 429: ClickUp mantiene el límite de solicitudes. "
            f"Retry-After: {retry_after}. Se detiene la corrida."
        )
        return None

    if response.status_code >= 400:
        print(f"  ERR {response.status_code}: {response.text[:300]}")
        return None

    if not response.content:
        return {}

    try:
        return response.json()
    except ValueError:
        print("  ERR: ClickUp devolvió una respuesta no JSON")
        return None


def fetch_tasks(list_id):
    result = api(
        "get",
        f"/list/{list_id}/task",
        params={
            "include_closed": "true",
            "subtasks": "true",
            "page": 0,
        },
    )
    if result is None:
        return None
    return result.get("tasks", [])


def description(sprint_name, task_name, status):
    return (
        f"Actividad: {task_name}.\n\n"
        f"Alcance: {sprint_name}.\n"
        f"Fecha de aceptación: {ACCEPTANCE_DATES[sprint_name]}.\n\n"
        "Criterio de cierre: registrar un resultado verificable, responsable y "
        "referencia al artefacto o ejecución correspondiente.\n\n"
        f"Estado administrativo: {status} para la entrega del proyecto."
    )


def subtask(name, assignees):
    return {"name": name, "assignees": assignees}


def parent(name, assignees, priority, subtasks):
    return {
        "name": name,
        "assignees": assignees,
        "priority": priority,
        "subtasks": subtasks,
    }


PLAN = {
    "Sprint 5": [
        parent(
            "Pruebas de aceptación automatizadas y escenarios Gherkin",
            [M["ND"], M["SA"], M["AN"]],
            PRIO["high"],
            [
                subtask("Confirmar herramienta y configuración de pruebas en Web y CRM", [M["SA"], M["AN"]]),
                subtask("Definir escenarios Gherkin por historia y rol", [M["ND"], M["SA"]]),
                subtask("Implementar o registrar escenarios de aceptación ejecutables", [M["SA"], M["AN"], M["ND"]]),
                subtask("Guardar reportes, capturas, videos o logs de ejecución", [M["ND"]]),
            ],
        ),
        parent(
            "Ejecución de pruebas de aceptación por rol",
            [M["ND"], M["SA"], M["AN"]],
            PRIO["high"],
            [
                subtask("Visitante/candidato en el portal público", [M["SA"], M["AN"]]),
                subtask("Administrador en CMS y catálogo", [M["SM"], M["SA"]]),
                subtask("Asesor en clientes, negociaciones, visitas y documentos", [M["AN"], M["SM"]]),
                subtask("Supervisor/coordinador en revisión y aprobación de documentos", [M["ND"], M["SM"]]),
                subtask("Manager en reportes y filtros", [M["ND"], M["SA"]]),
                subtask("Mobile cuando el flujo y la evidencia estén disponibles", [M["AN"]]),
            ],
        ),
        parent(
            "Plan de pruebas basado en riesgos e IEEE 29119",
            [M["GT"], M["ND"]],
            PRIO["high"],
            [
                subtask("Consolidar riesgos de calidad actuales", [M["ND"]]),
                subtask("Mapear riesgo, requisito, caso de prueba, resultado, evidencia y retest", [M["GT"], M["ND"]]),
                subtask("Priorizar autenticación, RBAC, ownership, estados, documentos, clientes, visitas y reportes", [M["GT"], M["SM"], M["ND"]]),
                subtask("Identificar riesgos fuera del alcance vigente", [M["ND"]]),
            ],
        ),
        parent(
            "Pruebas de sistema e integración",
            [M["GT"], M["ND"], M["SM"]],
            PRIO["high"],
            [
                subtask("Validar flujos completos frontend, API y base de datos", [M["GT"], M["SM"]]),
                subtask("Validar integración entre CRM, Documentos, Supervisión y Reportes", [M["GT"], M["SM"]]),
                subtask("Registrar precondiciones, datos, respuesta esperada y observada", [M["ND"]]),
                subtask("Asociar cada ejecución con SHA y ambiente utilizado", [M["GT"], M["ND"]]),
            ],
        ),
        parent(
            "Métricas de calidad y cobertura",
            [M["GT"], M["ND"]],
            PRIO["high"],
            [
                subtask("Registrar cobertura actual por repositorio y módulo", [M["ND"]]),
                subtask("Definir las métricas disponibles y su cálculo", [M["GT"], M["ND"]]),
                subtask("Diferenciar cobertura global de cobertura de código crítico", [M["ND"]]),
                subtask("Guardar URL de CI, SHA, fecha y artifact cuando exista", [M["ND"]]),
            ],
        ),
        parent(
            "Registro de defectos y retests",
            [M["GT"], M["ND"]],
            PRIO["high"],
            [
                subtask("Registrar defecto, severidad, pasos, ambiente, evidencia y responsable", [M["ND"]]),
                subtask("Asociar cada corrección con commit o pull request", [M["GT"], M["ND"]]),
                subtask("Ejecutar y registrar el retest después de cada corrección", [M["ND"]]),
            ],
        ),
        parent(
            "Pruebas de flujo de datos",
            [M["GT"], M["ND"], M["SM"]],
            PRIO["high"],
            [
                subtask("Seleccionar variables críticas de los módulos principales", [M["ND"], M["SM"]]),
                subtask("Validar entrada, transformación, persistencia y salida", [M["GT"], M["ND"]]),
                subtask("Registrar datos inválidos, límites y errores esperados", [M["ND"]]),
            ],
        ),
        parent(
            "Perfilamiento de la aplicación",
            [M["ND"]],
            PRIO["low"],
            [
                subtask("Confirmar medición reproducible de rendimiento", [M["ND"]]),
                subtask("Registrar herramienta, escenario, entorno, resultado y conclusión", [M["ND"]]),
            ],
        ),
        parent(
            "Inicio de consolidación del informe final",
            [M["ND"], M["SA"]],
            PRIO["high"],
            [
                subtask("Relacionar resultados de pruebas, riesgos, defectos y métricas", [M["ND"]]),
                subtask("Identificar evidencias faltantes para capítulos, anexos y rúbrica", [M["SA"], M["ND"]]),
            ],
        ),
    ],
    "Sprint 6": [
        parent(
            "Revisión de principios SOLID y refactorización",
            [M["GT"], M["SM"]],
            PRIO["normal"],
            [
                subtask("Seleccionar ejemplos reales por repositorio", [M["GT"], M["SM"]]),
                subtask("Registrar problema, cambio aplicado y resultado", [M["GT"], M["SM"]]),
                subtask("Asociar los ejemplos con commits actuales", [M["GT"]]),
            ],
        ),
        parent(
            "Aplicación de patrones de diseño",
            [M["GT"], M["SM"]],
            PRIO["normal"],
            [
                subtask("Identificar patrones realmente presentes en el código", [M["GT"], M["SM"]]),
                subtask("Explicar el problema que resuelve cada patrón", [M["SM"]]),
                subtask("Validar cada patrón con su implementación actual", [M["GT"]]),
            ],
        ),
        parent(
            "Refactorización del código base",
            [M["GT"], M["SM"]],
            PRIO["normal"],
            [
                subtask("Registrar mejoras de legibilidad, modularidad y duplicación", [M["GT"], M["SM"]]),
                subtask("Ejecutar tests y build después de cada cambio", [M["GT"], M["ND"]]),
                subtask("Confirmar el resultado de cada refactorización", [M["GT"], M["SM"]]),
            ],
        ),
        parent(
            "Análisis estático y estándares de codificación",
            [M["GT"], M["ND"], M["SM"]],
            PRIO["high"],
            [
                subtask("Verificar las herramientas configuradas actualmente", [M["GT"], M["SM"]]),
                subtask("Comprobar Biome, TypeScript y hooks existentes", [M["GT"]]),
                subtask("Registrar comandos, revisión, fecha y resultado", [M["ND"], M["GT"]]),
            ],
        ),
        parent(
            "Integración continua con datos de calidad",
            [M["GT"], M["ND"]],
            PRIO["high"],
            [
                subtask("Verificar jobs de instalación, lint, typecheck, tests, coverage y build", [M["GT"], M["ND"]]),
                subtask("Guardar URL del pipeline, SHA, fecha y artifacts descargables", [M["ND"]]),
                subtask("Registrar fallos y correcciones relevantes", [M["GT"], M["ND"]]),
            ],
        ),
        parent(
            "Pruebas cross-browser",
            [M["SA"], M["AN"], M["SM"]],
            PRIO["normal"],
            [
                subtask("Definir navegadores, versiones, ambiente y escenarios", [M["SA"], M["AN"]]),
                subtask("Ejecutar escenarios en Chrome", [M["SA"], M["AN"]]),
                subtask("Ejecutar escenarios en Firefox", [M["SA"], M["AN"]]),
                subtask("Ejecutar escenarios en Edge", [M["SA"], M["SM"]]),
            ],
        ),
        parent(
            "Revisión de seguridad",
            [M["GT"], M["ND"]],
            PRIO["high"],
            [
                subtask("Revisar autenticación, autorización, secretos, entradas y datos expuestos", [M["GT"], M["ND"]]),
                subtask("Asociar hallazgos con riesgo, severidad y corrección", [M["ND"]]),
                subtask("Ejecutar retest de los hallazgos corregidos", [M["ND"], M["GT"]]),
            ],
        ),
        parent(
            "Accesibilidad y diseño responsive",
            [M["SA"], M["AN"]],
            PRIO["normal"],
            [
                subtask("Registrar viewport, navegador, flujo y criterios revisados", [M["SA"], M["AN"]]),
                subtask("Guardar hallazgos y correcciones de accesibilidad", [M["SA"]]),
                subtask("Verificar las correcciones responsive", [M["SA"], M["AN"]]),
            ],
        ),
        parent(
            "Documentación y material de presentación",
            [M["ND"], M["SA"]],
            PRIO["high"],
            [
                subtask("Verificar la guía de instalación y despliegue", [M["ND"]]),
                subtask("Verificar los manuales de usuario por rol", [M["SA"]]),
                subtask("Verificar la documentación de API", [M["ND"]]),
                subtask("Verificar el material de presentación y su correspondencia con el informe", [M["SA"], M["ND"]]),
            ],
        ),
    ],
    "Sprint 7": [
        parent(
            "Despliegue final en producción",
            [M["GT"], M["ND"]],
            PRIO["urgent"],
            [
                subtask("Verificar Web, CRM y API en el entorno final", [M["GT"], M["ND"]]),
                subtask("Registrar URL, fecha, SHA desplegado y respuesta de salud", [M["GT"]]),
                subtask("Guardar capturas sin secretos ni datos personales innecesarios", [M["SA"], M["GT"]]),
            ],
        ),
        parent(
            "Guía definitiva de instalación y despliegue",
            [M["ND"], M["SA"]],
            PRIO["high"],
            [
                subtask("Confirmar prerrequisitos, variables, instalación, base de datos y validación", [M["ND"]]),
                subtask("Confirmar el procedimiento de despliegue", [M["ND"], M["GT"]]),
                subtask("Incluir troubleshooting y rollback solo cuando estén verificados", [M["ND"]]),
            ],
        ),
        parent(
            "Manual final de usuario por rol",
            [M["SA"], M["AN"]],
            PRIO["high"],
            [
                subtask("Verificar los roles Asesor, Supervisor, Administrador y Candidato", [M["SA"]]),
                subtask("Confirmar pasos numerados, acciones de clic y resultados esperados", [M["SA"], M["AN"]]),
                subtask("Adjuntar los PDF finales como anexos cuando corresponda", [M["SA"]]),
            ],
        ),
        parent(
            "Informe final del proyecto",
            [M["ND"], M["SA"]],
            PRIO["urgent"],
            [
                subtask("Verificar capítulos, objetivos, alcance, arquitectura, sprints, testing y riesgos", [M["ND"], M["SA"]]),
                subtask("Reemplazar TODOs por evidencia actual o limitaciones explícitas", [M["SA"], M["ND"]]),
                subtask("Compilar y revisar visualmente el PDF final", [M["ND"], M["SA"]]),
            ],
        ),
        parent(
            "Validación final de requisitos",
            [M["GT"], M["ND"]],
            PRIO["urgent"],
            [
                subtask("Ejecutar los escenarios de aceptación seleccionados", [M["ND"], M["SA"]]),
                subtask("Confirmar requisitos funcionales y no funcionales con resultado y evidencia", [M["GT"], M["ND"]]),
                subtask("Resolver o declarar los defectos restantes", [M["GT"], M["ND"]]),
            ],
        ),
        parent(
            "Correcciones finales derivadas del Sprint 6",
            [M["GT"], M["ND"], M["SM"], M["SA"], M["AN"]],
            PRIO["high"],
            [
                subtask("Registrar cada corrección, responsable, commit y retest", [M["GT"], M["ND"]]),
                subtask("Verificar que no queden tareas genéricas sin criterio de aceptación", [M["SA"], M["ND"]]),
            ],
        ),
        parent(
            "Repositorio y paquete final de evidencias",
            [M["GT"], M["ND"], M["SA"]],
            PRIO["high"],
            [
                subtask("Revisar permisos y enlaces de todos los repositorios", [M["GT"], M["ND"]]),
                subtask("Consolidar comunicaciones, cartas, capturas, videos, manuales y guías", [M["SA"], M["ND"]]),
                subtask("Congelar revisión, fecha y artifacts usados en el informe", [M["GT"], M["ND"]]),
            ],
        ),
        parent(
            "Video demostrativo y reunión de cierre",
            [M["GT"], M["ND"], M["SM"], M["SA"], M["AN"]],
            PRIO["high"],
            [
                subtask("Verificar duración, idioma, participación y escenarios demostrados", [M["SA"], M["GT"]]),
                subtask("Guardar el enlace final y una lista breve de lo demostrado", [M["ND"], M["SA"]]),
            ],
        ),
        parent(
            "Aceptación final del cliente",
            [M["GT"], M["ND"]],
            PRIO["urgent"],
            [
                subtask("Confirmar la aceptación final del 2026-08-07", [M["GT"], M["ND"]]),
                subtask("Registrar la evidencia de aceptación e inclusión en el reporte", [M["ND"], M["SA"]]),
            ],
        ),
    ],
}


def index_tasks(tasks):
    parents = {}
    children = set()
    for existing in tasks:
        name = normalize(existing.get("name", ""))
        parent_id = existing.get("parent")
        if parent_id:
            children.add((str(parent_id), name))
        else:
            parents[name] = existing
    return parents, children


def build_actions(selected_sprints, inventories):
    actions = []
    existing_count = 0

    for sprint_name in selected_sprints:
        parents, children = inventories[sprint_name]
        for planned_parent in PLAN[sprint_name]:
            parent_task = parents.get(normalize(planned_parent["name"]))
            if not parent_task:
                actions.append(
                    {
                        "kind": "parent",
                        "sprint": sprint_name,
                        "name": planned_parent["name"],
                        "assignees": planned_parent["assignees"],
                        "priority": planned_parent["priority"],
                    }
                )
                continue

            existing_count += 1
            parent_id = str(parent_task["id"])
            for planned_subtask in planned_parent["subtasks"]:
                key = (parent_id, normalize(planned_subtask["name"]))
                if key in children:
                    existing_count += 1
                    continue
                actions.append(
                    {
                        "kind": "subtask",
                        "sprint": sprint_name,
                        "name": planned_subtask["name"],
                        "assignees": planned_subtask["assignees"],
                        "priority": None,
                        "parent_id": parent_id,
                        "parent_name": planned_parent["name"],
                    }
                )

    return actions, existing_count


def create_task(list_id, sprint_name, name, assignees, priority, status, parent_id=None):
    payload = {
        "name": name,
        "description": description(sprint_name, name, status),
        "assignees": assignees,
        "status": status,
        "due_date": ms(ACCEPTANCE_DATES[sprint_name]),
        "due_date_time": False,
    }
    if priority is not None:
        payload["priority"] = priority
    if parent_id:
        payload["parent"] = parent_id
    return api("post", f"/list/{list_id}/task", payload)


def positive_int(value):
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("debe ser mayor que cero")
    return parsed


def non_negative_float(value):
    parsed = float(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("no puede ser negativo")
    return parsed


def write_report(path, report):
    if not path:
        return
    report_path = Path(path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Reporte: {report_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Crea tareas faltantes de ClickUp para Sprints 5–7, una por vez."
    )
    parser.add_argument(
        "--sprint",
        action="append",
        choices=tuple(LISTS),
        help="Limita la corrida a uno o más sprints. Por defecto usa 5–7.",
    )
    parser.add_argument(
        "--limit",
        type=positive_int,
        default=1,
        help="Máximo de tareas nuevas por ejecución (por defecto: 1).",
    )
    parser.add_argument(
        "--delay",
        type=non_negative_float,
        default=DEFAULT_DELAY,
        help="Segundos entre creaciones cuando limitas más de una tarea.",
    )
    parser.add_argument(
        "--status",
        choices=STATUSES,
        default=DEFAULT_STATUS,
        help="Estado para las tareas nuevas (por defecto: completadas).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Consulta y muestra las tareas faltantes sin crear nada.",
    )
    parser.add_argument(
        "--report-file",
        help="Escribe un reporte JSON sin secretos en esta ruta.",
    )
    args = parser.parse_args()

    selected_sprints = args.sprint or list(LISTS)
    print("BOPADIGITAL — creación incremental de tareas ClickUp")
    print(f"Sprints: {', '.join(selected_sprints)}")
    print(f"Límite de creación: {args.limit} | Estado: {args.status}")

    inventories = {}
    for sprint_name in selected_sprints:
        tasks = fetch_tasks(LISTS[sprint_name])
        if tasks is None:
            report = {
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                "space_id": SPACE_ID,
                "folder_id": FOLDER_ID,
                "lists": LISTS,
                "selected_sprints": selected_sprints,
                "error": f"No se pudo leer {sprint_name}",
                "rate_limited": RATE_LIMITED,
            }
            write_report(args.report_file, report)
            return 1
        inventories[sprint_name] = index_tasks(tasks)
        print(f"  {sprint_name}: {len(tasks)} tareas inspeccionadas")

    actions, existing_count = build_actions(selected_sprints, inventories)
    selected_actions = actions[: args.limit]

    print(f"Encontradas/reutilizadas: {existing_count}")
    print(f"Pendientes en el plan: {len(actions)}")
    print(f"En esta corrida: {len(selected_actions)}")

    if args.dry_run:
        for action in selected_actions:
            parent_label = (
                f" -> {action['parent_name']}" if action["kind"] == "subtask" else ""
            )
            print(f"  DRY-RUN [{action['sprint']}] {action['kind']}: {action['name']}{parent_label}")
        report = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "space_id": SPACE_ID,
            "folder_id": FOLDER_ID,
            "lists": {name: LISTS[name] for name in selected_sprints},
            "selected_sprints": selected_sprints,
            "dry_run": True,
            "existing_count": existing_count,
            "planned_missing": len(actions),
            "selected_count": len(selected_actions),
            "created": [],
            "failed": [],
            "rate_limited": False,
        }
        write_report(args.report_file, report)
        return 0

    created = []
    failed = []
    for index, action in enumerate(selected_actions):
        if index and args.delay:
            time.sleep(args.delay)

        result = create_task(
            LISTS[action["sprint"]],
            action["sprint"],
            action["name"],
            action["assignees"],
            action["priority"],
            args.status,
            action.get("parent_id"),
        )
        if result and result.get("id"):
            created.append(
                {
                    "id": result["id"],
                    "sprint": action["sprint"],
                    "kind": action["kind"],
                    "name": action["name"],
                    "parent_id": action.get("parent_id"),
                    "status": args.status,
                }
            )
            print(f"  CREATED {result['id']}: [{action['sprint']}] {action['name']}")
        else:
            failed.append(action)
            print(f"  FAILED: [{action['sprint']}] {action['name']}")
            if RATE_LIMITED:
                break

    report = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "space_id": SPACE_ID,
        "folder_id": FOLDER_ID,
        "lists": {name: LISTS[name] for name in selected_sprints},
        "selected_sprints": selected_sprints,
        "dry_run": False,
        "limit": args.limit,
        "delay_seconds": args.delay,
        "status": args.status,
        "existing_count": existing_count,
        "planned_missing": len(actions),
        "created": created,
        "failed": [
            {
                "sprint": action["sprint"],
                "kind": action["kind"],
                "name": action["name"],
                "parent_id": action.get("parent_id"),
            }
            for action in failed
        ],
        "rate_limited": RATE_LIMITED,
    }
    write_report(args.report_file, report)
    print(f"DONE. Created: {len(created)} | Failed: {len(failed)}")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
