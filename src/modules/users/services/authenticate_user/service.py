from injector import inject
from src.modules.users.contracts.dtos.authenticate_user import AuthenticateUserDto

from src.modules.users.contracts.repositories.users import UsersRepository
from src.modules.users.entities.user import User
from src.providers.hash.contracts.interfaces.hash import HashProvider
from src.shared.server.errors.app_exceptions import AppExceptions


class AuthenticateUserService:
    @inject
    def __init__(self, user_repository: UsersRepository, hash_provider: HashProvider):
        self.user_repository = user_repository
        self.hash_provider = hash_provider

    async def execute(self, data: AuthenticateUserDto) -> User:
        user = await self.user_repository.find_one_by_email(data.email)
        if not user:
            raise AppExceptions.invalid_user_password_combination()
        password_match = await self.hash_provider.compare(data.password, user.password)
        if not password_match:
            raise AppExceptions.invalid_user_password_combination()
        return user
