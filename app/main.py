from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import app.services as services

app = FastAPI(title="Task Manager")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def index(request: Request, status: str = "all"):
    tasks = services.get_all_tasks(status)
    all_tasks = services.get_all_tasks()
    stats = services.get_stats(all_tasks)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "tasks": tasks,
            "stats": stats,
            "current_filter": status,
        },
    )


@app.post("/tasks")
async def create_task(
    title: str = Form(...),
    description: str = Form(""),
):
    if not title.strip():
        return RedirectResponse(url="/", status_code=303)
    services.create_task(title.strip(), description.strip())
    return RedirectResponse(url="/", status_code=303)


@app.post("/tasks/{task_id}/complete")
async def complete_task(task_id: str):
    services.complete_task(task_id)
    return RedirectResponse(url="/", status_code=303)
