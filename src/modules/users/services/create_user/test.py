import asyncio
import unittest

from fastapi.exceptions import HTTPException
from src.modules.users.contracts.dtos.create_user import CreateUserDto

from src.modules.users.implementations.fake.fake_users_repository import (
    FakeUsersRepository,
)
from src.modules.users.services.create_user.service import CreateUserService
from src.providers.hash.implementations.fake.fake_hash_provider import FakeHashProvider


class TestCreateUserService(unittest.TestCase):
    users_repository = FakeUsersRepository()
    hash_provider = FakeHashProvider()
    create_user_service = CreateUserService(users_repository, hash_provider)

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
