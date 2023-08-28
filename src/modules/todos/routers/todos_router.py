from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.entities.todo import Todo
from src.modules.todos.services.create_todo.controller import CreateTodoController
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
    security_scope=SecurityScope.SINGLE.value,
    application_scope=ApplicationScope.USER.value,
)


@todos_router.post("", response_model=Todo)
async def create_todo(
    data: CreateTodoDto, user: User = Depends(todos_authorization)
) -> JSONResponse:
    response = await CreateTodoController.handle(data)
    return JSONResponse(response)
