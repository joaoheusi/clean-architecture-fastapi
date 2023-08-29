import asyncio
import unittest

from fastapi.exceptions import HTTPException

from src.modules.users.contracts.dtos.authenticate_user import AuthenticateUserDto
from src.modules.users.contracts.dtos.create_user import CreateUserDto
from src.modules.users.implementations.fake.fake_users_repository import (
    FakeUsersRepository,
)
from src.modules.users.services.authenticate_user.service import AuthenticateUserService
from src.modules.users.services.create_user.service import CreateUserService
from src.providers.hash.implementations.fake.fake_hash_provider import FakeHashProvider
from src.providers.token.implementations.fake.fake_token_provider import (
    FakeTokenProvider,
)


class TestCreateUserService(unittest.TestCase):
    users_repository = FakeUsersRepository()
    hash_provider = FakeHashProvider()
    create_user_service = CreateUserService(users_repository, hash_provider)
    token_provider = FakeTokenProvider()
    authenticate_user_service = AuthenticateUserService(
        users_repository, hash_provider, token_provider
    )

    def test_correct(self) -> None:
        data = CreateUserDto(
            email="email@email.com",
            username="username",
            password="password",
            firstName="first_name",
            lastName="last_name",
        )
        response = asyncio.run(self.create_user_service.execute(data))
        assert response.email == data.email
        assert response.username == data.username
        assert response.firstName == data.firstName
        assert response.lastName == data.lastName

    def test_email_in_use(self) -> None:
        data = CreateUserDto(
            email="email@email.com",
            username="username",
            password="password",
            firstName="first_name",
            lastName="last_name",
        )
        with self.assertRaises(HTTPException) as context:
            asyncio.run(self.create_user_service.execute(data))
        assert context.exception.status_code == 400

    def test_authenticate(self) -> None:
        create_data = CreateUserDto(
            email="email@emailauth.com",
            username="username",
            password="password",
            firstName="first_name",
            lastName="last_name",
        )
        response = asyncio.run(self.create_user_service.execute(create_data))
        assert response.email == create_data.email

        auth_data = AuthenticateUserDto(
            email="email@emailauth.com",
            password="password",
        )
        auth_response = asyncio.run(self.authenticate_user_service.execute(auth_data))
        assert auth_response.user.email == auth_data.email

    def test_email_not_found(self) -> None:
        data = AuthenticateUserDto(
            email="nonexistentemail@email.com",
            password="password",
        )
        with self.assertRaises(HTTPException) as context:
            asyncio.run(self.authenticate_user_service.execute(data))
        assert context.exception.status_code == 400

    def test_invalid_password(self) -> None:
        create_data = CreateUserDto(
            email="invalidPass@email.com",
            username="username",
            password="password",
            firstName="first_name",
            lastName="last_name",
        )
        response = asyncio.run(self.create_user_service.execute(create_data))
        assert response.email == create_data.email
        invalid_data = AuthenticateUserDto(
            email="invalidPass@email.com",
            password="invalidPassword",
        )
        with self.assertRaises(HTTPException) as context:
            asyncio.run(self.authenticate_user_service.execute(invalid_data))
        assert context.exception.status_code == 400
