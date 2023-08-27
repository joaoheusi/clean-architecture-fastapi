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
        return jsonable_encoder(response)

        # POSSIBLE TO REMOVE SOME OF THE ATTRIBUTES USING THE EXCLUDE PARAMETER
        # create_user_service_result = await create_user_service.perform(data)
        # response = jsonable_encoder(
        #     create_user_service_result.model_dump(exclude={"password"})
        # )
        # return jsonable_encoder(response)
