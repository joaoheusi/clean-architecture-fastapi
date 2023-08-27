from src.modules.users.contracts.dtos.create_user import CreateUserDto
from src.modules.users.contracts.repositories.users import UsersRepository
from src.modules.users.entities.user import User


class FakeUsersRepository(UsersRepository):
    __users: list[User] = []

    async def create(self, data: CreateUserDto) -> User:
        user = User(
            **data.model_dump(),
        )
        self.__users.append(user)
        return user

    async def find_one_by_email(self, email: str) -> User | None:
        for user in self.__users:
            if user.email == email:
                return user
        return None
