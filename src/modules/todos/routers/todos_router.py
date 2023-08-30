from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.entities.todo import Todo
from src.modules.todos.services.create_todo.controller import CreateTodoController
from src.modules.todos.services.find_user_todos.controller import (
    FindUserTodosController,
)
from src.modules.todos.services.mark_todo_as_done.controller import (
    MarkTodoAsDoneController,
)
from src.modules.todos.services.mark_todo_as_undone.controller import (
    MarkTodoAsUndoneController,
)
from src.modules.users.entities.user import User
from src.providers.container import container
from src.shared.contracts.enums.application_scope import ApplicationScope
from src.shared.contracts.enums.security_scope import SecurityScope
from src.shared.server.dependencies.authorization import Authorization

todos_router = APIRouter(
    prefix="/todos",
    tags=["todos"],
)

todos_authorization = container.get(Authorization)
todos_authorization.set_scopes(
    security_scope=SecurityScope.SINGLE,
    application_scope=ApplicationScope.USER,
)


@todos_router.post("", response_model=Todo)
async def create_todo(
    data: CreateTodoDto, user: User = Depends(todos_authorization)
) -> JSONResponse:
    response = await CreateTodoController.handle(data=data, user=user)
    return JSONResponse(response)


@todos_router.get("", response_model=list[Todo])
async def find_user_todos(user: User = Depends(todos_authorization)) -> JSONResponse:
    response = await FindUserTodosController.handle(user_id=user.id)
    return JSONResponse(response)


@todos_router.patch("/{todo_id}/done", response_model=Todo)
async def mark_todo_as_done(
    todo_id: str, user: User = Depends(todos_authorization)
) -> JSONResponse:
    response = await MarkTodoAsDoneController.handle(todo_id=todo_id, user_id=user.id)
    return JSONResponse(response)


@todos_router.patch("/{todo_id}/undone", response_model=Todo)
async def mark_todo_as_undone(
    todo_id: str, user: User = Depends(todos_authorization)
) -> JSONResponse:
    response = await MarkTodoAsUndoneController.handle(todo_id=todo_id, user_id=user.id)
    return JSONResponse(response)
