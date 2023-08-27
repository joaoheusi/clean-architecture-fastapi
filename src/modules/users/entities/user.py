from uuid import uuid4
from pydantic import BaseModel, Field
from datetime import datetime, timezone

from src.shared.contracts.enums.application_scope import ApplicationScope
from src.shared.contracts.enums.security_scope import SecurityScope


class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    username: str
    email: str
    password: str
    firstName: str
    lastName: str
    isActive: bool = False
    isEmailConfirmed: bool = False
    applicationScopes: list[ApplicationScope] = []
    securityScopes: list[SecurityScope] = []
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
