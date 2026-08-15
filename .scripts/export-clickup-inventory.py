#!/usr/bin/env python3
"""Export the current ClickUp task inventory for BOPADIGITAL Sprints 1–7."""

import argparse
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import requests


REPO_ROOT = Path(__file__).resolve().parents[1]
ENV_FILES = (
    REPO_ROOT / ".env",
    REPO_ROOT.parent / "bopacorp-api" / ".env",
)

SPACE_ID = "90176024370"
FOLDER_ID = "90179341245"
BASE = "https://api.clickup.com/api/v2"
LOCAL_ZONE = ZoneInfo("America/Guayaquil")

LISTS = {
    "Sprint 1": "901714510299",
    "Sprint 2": "901714510300",
    "Sprint 3": "901714510301",
    "Sprint 4": "901714510302",
    "Sprint 5": "901716103979",
    "Sprint 6": "901716103981",
    "Sprint 7": "901716103982",
}

ACCEPTANCE_DATES = {
    "Sprint 4": "2026-07-05",
    "Sprint 5": "2026-07-14",
    "Sprint 6": "2026-07-21",
    "Sprint 7": "2026-07-28",
    "Cierre final": "2026-08-07",
}


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
if not TOKEN:
    raise SystemExit(
        "CLICKUP_API_TOKEN is required; add it to a local .env file or export it."
    )

HEADERS = {"Authorization": TOKEN, "Content-Type": "application/json"}


def api_get(path, params=None):
    response = requests.get(
        f"{BASE}{path}",
        headers=HEADERS,
        params=params,
        timeout=30,
    )
    if response.status_code >= 400:
        raise RuntimeError(f"ClickUp GET {response.status_code}: {response.text[:300]}")
    return response.json()


def fetch_tasks(list_id):
    tasks = []
    page = 0

    while True:
        data = api_get(
            f"/list/{list_id}/task",
            {
                "include_closed": "true",
                "subtasks": "true",
                "archived": "false",
                "page": page,
            },
        )
        page_tasks = data.get("tasks", [])
        tasks.extend(page_tasks)

        if data.get("last_page", True) or len(page_tasks) < 100:
            return tasks

        page += 1
        time.sleep(0.25)


def date_label(timestamp):
    if not timestamp:
        return "—"
    try:
        value = int(timestamp) / 1000
        return datetime.fromtimestamp(value, LOCAL_ZONE).strftime("%Y-%m-%d")
    except (TypeError, ValueError, OverflowError):
        return str(timestamp)


def text_label(value):
    return str(value or "—").replace("|", "\\|").replace("\n", " ")


def status_label(task):
    status = task.get("status")
    if isinstance(status, dict):
        return text_label(status.get("status"))
    return text_label(status)


def assignees_label(task):
    assignees = task.get("assignees") or []
    labels = []
    for assignee in assignees:
        username = assignee.get("username")
        user_id = assignee.get("id")
        labels.append(username or str(user_id))
    return ", ".join(labels) if labels else "—"


def task_rows(tasks):
    by_id = {str(task["id"]): task for task in tasks}
    order = {str(task["id"]): index for index, task in enumerate(tasks)}
    children = {}
    roots = []

    for task in tasks:
        task_id = str(task["id"])
        parent_id = task.get("parent")
        if parent_id and str(parent_id) in by_id:
            children.setdefault(str(parent_id), []).append(task)
        else:
            roots.append(task)

    roots.sort(key=lambda task: order[str(task["id"])])
    for values in children.values():
        values.sort(key=lambda task: order[str(task["id"])])

    rows = []

    def visit(task, depth):
        task_id = str(task["id"])
        rows.append((task, depth))
        for child in children.get(task_id, []):
            visit(child, depth + 1)

    for root in roots:
        visit(root, 0)

    return rows


def render_sprint(sprint_name, tasks):
    parents = sum(1 for task in tasks if not task.get("parent"))
    subtasks = len(tasks) - parents
    lines = [
        f"## {sprint_name}",
        "",
        f"- Lista: `{LISTS[sprint_name]}`",
        f"- Fecha de aceptación registrada: `{ACCEPTANCE_DATES.get(sprint_name, '—')}`",
        f"- Total: **{len(tasks)}** ({parents} padres, {subtasks} subtareas)",
        "",
        "| Tipo | Tarea | ClickUp ID | Estado | Responsables | Fecha límite | Fecha de cierre | Enlace |",
        "|---|---|---|---|---|---|---|---|",
    ]

    for task, depth in task_rows(tasks):
        kind = "Padre" if depth == 0 else "Subtarea"
        name = ("↳ " * depth) + text_label(task.get("name"))
        url = task.get("url") or "—"
        link = f"[abrir]({url})" if url != "—" else "—"
        lines.append(
            "| "
            + " | ".join(
                [
                    kind,
                    name,
                    f"`{task.get('id', '—')}`",
                    status_label(task),
                    text_label(assignees_label(task)),
                    date_label(task.get("due_date")),
                    date_label(task.get("date_closed")),
                    link,
                ]
            )
            + " |"
        )

    return lines


def render_document(inventory):
    generated = datetime.now(LOCAL_ZONE).isoformat(timespec="seconds")
    total = sum(len(tasks) for tasks in inventory.values())
    lines = [
        "# Inventario actual de ClickUp — BOPADIGITAL",
        "",
        f"- Generado: `{generated}`",
        "- Método: lectura directa de la API de ClickUp en modo solo lectura.",
        f"- Workspace: `{SPACE_ID}`",
        f"- Carpeta: `BOPADIGITAL` (`{FOLDER_ID}`)",
        f"- Total de tareas inventariadas: **{total}**",
        "- Este archivo sirve como snapshot de comparación; no es una fuente para crear duplicados.",
        "",
        "## Fechas de aceptación de referencia",
        "",
        "| Sprint | Fecha |",
        "|---|---|",
    ]
    for name, date_value in ACCEPTANCE_DATES.items():
        lines.append(f"| {name} | `{date_value}` |")
    lines.extend(["", "## Resumen", "", "| Sprint | Tareas | Padres | Subtareas |", "|---|---:|---:|---:|"])

    for sprint_name, tasks in inventory.items():
        parents = sum(1 for task in tasks if not task.get("parent"))
        lines.append(f"| {sprint_name} | {len(tasks)} | {parents} | {len(tasks) - parents} |")

    lines.extend(["", "---", ""])
    for sprint_name, tasks in inventory.items():
        lines.extend(render_sprint(sprint_name, tasks))
        lines.extend(["", "---", ""])

    return "\n".join(lines).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        default=str(REPO_ROOT / "06-project2p" / "clickup-sprints-1-7-current-inventory.md"),
        help="Ruta del Markdown de salida.",
    )
    args = parser.parse_args()

    inventory = {}
    for sprint_name, list_id in LISTS.items():
        tasks = fetch_tasks(list_id)
        inventory[sprint_name] = tasks
        print(f"{sprint_name}: {len(tasks)} tareas")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_document(inventory), encoding="utf-8")
    print(f"Inventario escrito en: {output}")


if __name__ == "__main__":
    main()
