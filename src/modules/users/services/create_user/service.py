from injector import inject
from src.modules.users.contracts.dtos.create_user import CreateUserDto

from src.modules.users.contracts.repositories.users import UsersRepository
from src.modules.users.entities.user import User
from src.providers.hash.contracts.interfaces.hash import HashProvider
from src.shared.server.errors.app_exceptions import AppExceptions


class CreateUserService:
    @inject
    def __init__(self, user_repository: UsersRepository, hash_provider: HashProvider):
        self.user_repository = user_repository
        self.hash_provider = hash_provider

    async def execute(self, data: CreateUserDto) -> User:
        email_exists = await self.user_repository.find_one_by_email(data.email)
        if email_exists:
            raise AppExceptions.email_in_use()
        hashed_password = await self.hash_provider.hash(data.password)
        data.password = hashed_password
        user = await self.user_repository.create(data)
        return user
