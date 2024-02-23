from fastapi import Request
from injector import inject

from src.modules.users.contracts.repositories.users import UsersRepository
from src.modules.users.entities.user import User
from src.providers.token.contracts.interfaces.token import TokenProvider
from src.shared.contracts.enums.application_scope import ApplicationScope
from src.shared.contracts.enums.security_scope import SecurityScope
from src.shared.errors.app_exceptions import AppExceptions
from src.shared.utils.get_authorization_scheme_param import (
    get_authorization_scheme_param,
)


class Authorization:
    @inject
    def __init__(
        self,
        token_url: str,
        token_provider: TokenProvider,
        users_repository: UsersRepository,
    ):
        self.token_url = token_url
        self.security_scope = SecurityScope.SINGLE.value
        self.application_scope = ApplicationScope.USER.value
        self.token_provider = token_provider
        self.users_repository = users_repository

    def set_scopes(
        self, security_scope: SecurityScope, application_scope: ApplicationScope
    ) -> None:
        self.security_scope = security_scope
        self.application_scope = application_scope

    async def __call__(self, request: Request) -> User:
        authorization: str | None = request.headers.get("Authorization")
        scheme, param = get_authorization_scheme_param(authorization)

        if not authorization:
            raise AppExceptions.no_authentication_provided()
        if scheme == "" or param == "":
            raise AppExceptions.invalid_authentication_method()

        if scheme.lower() != "bearer":
            raise AppExceptions.invalid_authentication_method()

        token_payload = await self.token_provider.get(param)

        if not token_payload:
            raise AppExceptions.invalid_or_expired_token()

        if token_payload.securityScope != self.security_scope:
            raise AppExceptions.insufficient_security_clearance()

        user = await self.users_repository.find_one_by_id(token_payload.owner)

        if not user:
            raise AppExceptions.invalid_or_expired_token()

        if not user.isActive or not user.isEmailConfirmed:
            raise AppExceptions.invalid_or_expired_token()

        if self.application_scope not in user.applicationScopes:
            raise AppExceptions.insufficient_application_clearance()

        return user
