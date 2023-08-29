from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from src.modules.users.contracts.dtos.authenticate_user import AuthenticateUserDto
from src.modules.users.contracts.dtos.create_user import CreateUserDto
from src.modules.users.contracts.interfaces.user_auth import UserAuthInterface
from src.modules.users.entities.user import User
from src.modules.users.services.authenticate_user.controller import (
    AuthenticateUserController,
)
from src.modules.users.services.create_user.controller import CreateUserController
from src.providers.container import container
from src.shared.contracts.enums.application_scope import ApplicationScope
from src.shared.contracts.enums.security_scope import SecurityScope
from src.shared.server.dependencies.authorization import Authorization

users_router = APIRouter(
    prefix="/users",
    tags=["users"],
)

create_user_authorization = container.get(Authorization)
create_user_authorization.set_scopes(
    security_scope=SecurityScope.SINGLE,
    application_scope=ApplicationScope.ADMIN,
)


@users_router.post("", response_model=User)
async def create_user(
    data: CreateUserDto, user: User = Depends(create_user_authorization)
) -> JSONResponse:
    response = await CreateUserController.handle(data)
    return JSONResponse(response)


@users_router.post("/auth", response_model=UserAuthInterface)
async def authenticate_user(data: AuthenticateUserDto) -> JSONResponse:
    response = await AuthenticateUserController.handle(data)
    return JSONResponse(response)
