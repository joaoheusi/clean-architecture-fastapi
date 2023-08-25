from pydantic import BaseModel


class Todo(BaseModel):
    id: str
    title: str
    description: str
    is_done: bool
