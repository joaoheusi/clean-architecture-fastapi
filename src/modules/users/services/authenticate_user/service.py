from injector import inject

from src.modules.users.contracts.dtos.authenticate_user import AuthenticateUserDto
from src.modules.users.contracts.interfaces.user_auth import UserAuthInterface
from src.modules.users.contracts.repositories.users import UsersRepository
from src.providers.hash.contracts.interfaces.hash import HashProvider
from src.providers.token.contracts.dtos.create_token import CreateTokenDto
from src.providers.token.contracts.enums.token_type import TokenType
from src.providers.token.contracts.interfaces.token import TokenProvider
from src.providers.token.contracts.interfaces.token_payload import TokenPayload
from src.shared.contracts.enums.security_scope import SecurityScope
from src.shared.server.errors.app_exceptions import AppExceptions


class AuthenticateUserService:
    @inject
    def __init__(
        self,
        user_repository: UsersRepository,
        hash_provider: HashProvider,
        token_provider: TokenProvider,
    ):
        self.user_repository = user_repository
        self.token_provider = token_provider
        self.hash_provider = hash_provider

    async def execute(self, data: AuthenticateUserDto) -> UserAuthInterface:
        user = await self.user_repository.find_one_by_email(data.email)
        if not user:
            raise AppExceptions.invalid_user_password_combination()
        password_match = await self.hash_provider.compare(data.password, user.password)
        if not password_match:
            raise AppExceptions.invalid_user_password_combination()

        token_payload = TokenPayload(
            type=TokenType.USER_AUTHENTICATION.value,
            owner=user.id,
            securityScope=SecurityScope.SINGLE.value,
        )

        token = await self.token_provider.create(
            CreateTokenDto(
                payload=token_payload,
                ttl=3600,
            )
        )
        user_auth = UserAuthInterface(
            user=user,
            token=token,
        )
        return user_auth
