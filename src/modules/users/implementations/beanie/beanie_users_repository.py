from src.modules.users.contracts.dtos.create_user import CreateUserDto
from src.modules.users.contracts.repositories.users import UsersRepository
from src.modules.users.entities.user import User
from src.modules.users.implementations.beanie.document import UserDocument


class BeanieUsersRepository(UsersRepository):
    async def create(self, data: CreateUserDto) -> User:
        user = UserDocument(**data.model_dump())
        await user.insert()
        return user

    async def find_one_by_email(self, email: str) -> User | None:
        user = await UserDocument.find_one(UserDocument.email == email)
        return user

    async def find_one_by_id(self, id: str) -> User | None:
        user = await UserDocument.find_one(UserDocument.id == id)
        return user
