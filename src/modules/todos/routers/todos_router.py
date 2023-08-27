from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.entities.todo import Todo
from src.modules.todos.services.create_todo.controller import (
    CreateTodoController,
)

todos_router = APIRouter(
    prefix="/todos",
    tags=["todos"],
)


@todos_router.post("", response_model=Todo)
async def create_todo(data: CreateTodoDto) -> JSONResponse:
    response = await CreateTodoController.handle(data)
    return JSONResponse(response)
