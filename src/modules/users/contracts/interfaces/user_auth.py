from pydantic import BaseModel

from src.modules.users.entities.user import User


class UserAuthInterface(BaseModel):
    user: User
    token: str
