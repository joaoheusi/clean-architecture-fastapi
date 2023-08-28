from uuid import uuid4
from pydantic import BaseModel, Field
from datetime import datetime, timezone


class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    username: str
    email: str
    password: str
    firstName: str
    lastName: str
    isActive: bool = False
    isEmailConfirmed: bool = False
    applicationScopes: list[str] = []
    securityScopes: list[str] = []
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
