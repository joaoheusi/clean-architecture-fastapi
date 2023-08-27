from pydantic import BaseModel


class CreateUserDto(BaseModel):
    username: str
    email: str
    password: str
    firstName: str
    lastName: str
