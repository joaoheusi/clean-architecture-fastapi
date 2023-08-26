from uuid import uuid4
from pydantic import Field
from beanie import Document

from src.modules.todo.entities.todo import Todo


class TodoDocument(Document, Todo):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")

    class Settings:
        name = "todos"
