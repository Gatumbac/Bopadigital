#!/usr/bin/env python3
"""Update the descriptions of the ClickUp tasks created for Sprint 5."""

import argparse
import os
import sys
from pathlib import Path

import requests


REPO_ROOT = Path(__file__).resolve().parents[1]
ENV_FILES = (
    REPO_ROOT / ".env",
    REPO_ROOT.parent / "bopacorp-api" / ".env",
)


def load_repo_env():
    """Load only the ClickUp token from the local project env files."""
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
if not TOKEN:
    raise SystemExit(
        "CLICKUP_API_TOKEN is required; add it to a local .env file or export it."
    )

HEADERS = {"Authorization": TOKEN, "Content-Type": "application/json"}
BASE = "https://api.clickup.com/api/v2"

# These are the seven Sprint 5 parent tasks created before the API rate limit.
TASKS = {
    "86e2uvdcb": "Pruebas de aceptación automatizadas y escenarios Gherkin",
    "86e2uvdce": "Ejecución de pruebas de aceptación por rol",
    "86e2uvdcg": "Plan de pruebas basado en riesgos e IEEE 29119",
    "86e2uvdck": "Pruebas de sistema e integración",
    "86e2uvdcn": "Métricas de calidad y cobertura",
    "86e2uvdcp": "Registro de defectos y retests",
    "86e2uvdct": "Pruebas de flujo de datos",
}

CLOSURE_DATE = "15 de agosto de 2026"
RATE_LIMITED = False


def api(method, path, data=None):
    """Call ClickUp without retrying for an extended rate-limit window."""
    global RATE_LIMITED

    response = requests.request(
        method,
        f"{BASE}{path}",
        headers=HEADERS,
        json=data,
        timeout=30,
    )

    if response.status_code == 429:
        RATE_LIMITED = True
        retry_after = response.headers.get("Retry-After", "desconocido")
        print(
            "  ERR 429: ClickUp mantiene el límite de solicitudes. "
            f"Retry-After: {retry_after}. No se reintentará automáticamente."
        )
        return None

    if response.status_code >= 400:
        print(f"  ERR {response.status_code}: {response.text[:300]}")
        return None

    return response.json() if response.content else {}


def description(name):
    return (
        f"Actividad: {name}.\n\n"
        f"Fecha de cierre: {CLOSURE_DATE}.\n\n"
        "Estado de cierre: completada para la entrega del proyecto.\n\n"
        "La evidencia y la revisión correspondiente quedan bajo responsabilidad del equipo."
    )


def update_task(task_id, name, dry_run=False):
    payload = {"description": description(name)}
    if dry_run:
        print(f"  DRY-RUN {task_id}: {name}")
        return True

    result = api("put", f"/task/{task_id}", payload)
    if result is None:
        print(f"  FAILED {task_id}: {name}")
        return False

    print(f"  UPDATED {task_id}: {name}")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Limpia las descripciones de las tareas Sprint 5 en ClickUp."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Muestra las tareas seleccionadas sin llamar a ClickUp.",
    )
    parser.add_argument(
        "--task-id",
        action="append",
        choices=TASKS,
        help="Actualiza solo este ID; puede repetirse. Por defecto usa los siete.",
    )
    args = parser.parse_args()

    selected = args.task_id or list(TASKS)
    print("BOPADIGITAL — actualización de descripciones ClickUp")
    print(f"Tareas seleccionadas: {len(selected)}")

    updated = 0
    failed = 0
    for index, task_id in enumerate(selected):
        if update_task(task_id, TASKS[task_id], dry_run=args.dry_run):
            updated += 1
        else:
            failed += 1
            if RATE_LIMITED:
                skipped = len(selected) - index - 1
                failed += skipped
                if skipped:
                    print(f"  SKIPPED: {skipped} tarea(s) para evitar más llamadas durante el límite.")
                break

    print(f"DONE. Updated: {updated} | Failed: {failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
