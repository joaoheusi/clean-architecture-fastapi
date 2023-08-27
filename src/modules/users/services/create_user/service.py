from injector import inject
from src.modules.users.contracts.dtos.create_user import CreateUserDto

from src.modules.users.contracts.repositories.users import UsersRepository
from src.modules.users.entities.user import User
from src.shared.server.errors.app_exceptions import AppExceptions


class CreateUserService:
    @inject
    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    async def perform(self, data: CreateUserDto) -> User:
        email_exists = await self.user_repository.find_one_by_email(data.email)
        if email_exists:
            raise AppExceptions.email_in_use()
        user = await self.user_repository.create(data)
        return user
