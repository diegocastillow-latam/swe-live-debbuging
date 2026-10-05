from pydantic import BaseModel


class Task(BaseModel):
    id: str
    title: str
    description: str = ""
    completed: bool = False
    created_at: str


class TaskCreate(BaseModel):
    title: str
    description: str = ""
