from datetime import datetime, timezone
from uuid import uuid4

from pydantic import BaseModel, Field


class Todo(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    title: str
    description: str
    isDone: bool
    userId: str
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    completedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
