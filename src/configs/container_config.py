from injector import Module, provider, singleton
from src.modules.todos.implementations.beanie.beanie_todo_repository import (
    BeanieTodoRepository,
)

from src.modules.todos.implementations.fake.fake_todo_repository import (
    FakeTodoRepository,
)
from src.modules.todos.contracts.repositories.todo import TodoRepository
from src.modules.users.contracts.repositories.users import UsersRepository
from src.modules.users.implementations.beanie.beanie_users_repository import (
    BeanieUsersRepository,
)
from src.modules.users.implementations.fake.fake_users_repository import (
    FakeUsersRepository,
)


class FakeTodoRepositoryModule(Module):
    @singleton
    @provider
    def provide_fake_todo_repository(self) -> TodoRepository:
        return FakeTodoRepository()


class FakeUsersRepositoryModule(Module):
    @singleton
    @provider
    def provide_fake_user_repository(self) -> UsersRepository:
        return FakeUsersRepository()


class BeanieUsersRepositoryModule(Module):
    @singleton
    @provider
    def provide_beanie_user_repository(self) -> UsersRepository:
        return BeanieUsersRepository()


class BeanieTodoRepositoryModule(Module):
    @singleton
    @provider
    def provide_beanie_todo_repository(self) -> TodoRepository:
        return BeanieTodoRepository()
