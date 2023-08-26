from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.modules.todo.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todo.entities.todo import Todo
from src.modules.todo.services.create_todo.controller import (
    CreateTodoController,
)

todo_router = APIRouter(
    prefix="/todo",
    tags=["todo"],
)


@todo_router.post("", response_model=Todo)
async def create_todo(data: CreateTodoDto) -> JSONResponse:
    response = await CreateTodoController.handle(data)
    return JSONResponse(response)
