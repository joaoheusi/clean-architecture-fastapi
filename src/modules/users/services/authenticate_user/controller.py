from fastapi.encoders import jsonable_encoder
from src.modules.users.contracts.dtos.authenticate_user import AuthenticateUserDto
from src.modules.users.entities.user import User
from src.modules.users.services.authenticate_user.service import AuthenticateUserService
from src.providers.container import container


class AuthenticateUserController:
    @staticmethod
    async def handle(data: AuthenticateUserDto) -> User:
        authenticate_user_service = container.get(AuthenticateUserService)
        response = await authenticate_user_service.execute(data)
        return jsonable_encoder(response)
