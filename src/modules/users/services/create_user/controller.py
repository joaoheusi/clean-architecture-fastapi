from fastapi.encoders import jsonable_encoder
from src.modules.users.contracts.dtos.create_user import CreateUserDto
from src.modules.users.entities.user import User
from src.modules.users.services.create_user.service import CreateUserService
from src.providers.container import container


class CreateUserController:
    @staticmethod
    async def handle(data: CreateUserDto) -> User:
        create_user_service = container.get(CreateUserService)
        response = await create_user_service.execute(data)
        return jsonable_encoder(
            response.model_dump(by_alias=False, exclude={"revision_id", "password"})
        )
