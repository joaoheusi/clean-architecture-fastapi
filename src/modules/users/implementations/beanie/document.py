from uuid import uuid4

from beanie import Document
from pydantic import Field

from src.modules.users.entities.user import User


class UserDocument(Document, User):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")  # type: ignore

    class Settings:
        name = "users"
