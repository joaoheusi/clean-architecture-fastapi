from uuid import uuid4

from beanie import Document
from pydantic import Field

from src.modules.todos.entities.todo import Todo


class TodoDocument(Document, Todo):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")  # type: ignore

    class Settings:
        name = "todos"
