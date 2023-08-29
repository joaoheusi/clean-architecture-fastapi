from pydantic import BaseModel


class CreateTodoDto(BaseModel):
    title: str
    description: str
