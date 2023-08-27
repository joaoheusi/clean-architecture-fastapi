from pydantic import BaseModel


class AuthenticateUserDto(BaseModel):
    email: str
    password: str
