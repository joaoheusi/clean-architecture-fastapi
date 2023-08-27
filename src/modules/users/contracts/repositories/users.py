from abc import ABC, abstractmethod

from src.modules.users.contracts.dtos.create_user import CreateUserDto
from src.modules.users.entities.user import User


class UsersRepository(ABC):
    @abstractmethod
    async def create(self, data: CreateUserDto) -> User:
        raise Exception("Not implemented")

    @abstractmethod
    async def find_one_by_email(self, email: str) -> User | None:
        raise Exception("Not implemented")
