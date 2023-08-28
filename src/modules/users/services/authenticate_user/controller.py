from fastapi.encoders import jsonable_encoder

from src.modules.users.contracts.dtos.authenticate_user import AuthenticateUserDto
from src.modules.users.contracts.interfaces.user_auth import UserAuthInterface
from src.modules.users.services.authenticate_user.service import AuthenticateUserService
from src.providers.container import container


class AuthenticateUserController:
    @staticmethod
    async def handle(data: AuthenticateUserDto) -> UserAuthInterface:
        authenticate_user_service = container.get(AuthenticateUserService)
        response = await authenticate_user_service.execute(data)
        return jsonable_encoder(response.model_dump(by_alias=False))
