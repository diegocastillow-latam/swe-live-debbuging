import uuid
from datetime import datetime
from app.database import load_tasks, save_tasks


def get_all_tasks(status: str = "all") -> list[dict]:
    tasks = load_tasks()
    if status == "completed":
        return [t for t in tasks if t["completed"]]
    elif status == "pending":
        return [t for t in tasks if not t["completed"]]
    return tasks


def create_task(title: str, description: str = "") -> dict:
    tasks = load_tasks()
    task = {
        "id": str(uuid.uuid4())[:8],
        "title": title,
        "description": description,
        "completed": False,
        "created_at": datetime.now().isoformat(),
    }
    tasks.append(task)
    save_tasks(tasks)
    return task


def complete_task(task_id: str) -> dict | None:
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            return task
    return None


def get_stats(tasks: list[dict]) -> dict:
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed
    # BUG 3: se calcula el porcentaje de tareas PENDIENTES en lugar de COMPLETADAS
    percentage = round((pending / total) * 100, 1) if total > 0 else 0
    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "percentage": percentage,
    }
