from uuid import uuid4
from pydantic import BaseModel, Field


class Todo(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    title: str
    description: str
    is_done: bool
