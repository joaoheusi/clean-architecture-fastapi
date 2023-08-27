from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from src.modules.users.contracts.dtos.create_user import CreateUserDto

from src.modules.users.entities.user import User
from src.modules.users.services.create_user.controller import CreateUserController

users_router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@users_router.post("", response_model=User)
async def create_user(data: CreateUserDto) -> JSONResponse:
    response = await CreateUserController.handle(data)
    return JSONResponse(response)
