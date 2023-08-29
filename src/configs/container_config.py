from injector import Module, provider, singleton

from src.modules.todos.contracts.repositories.todos import TodosRepository
from src.modules.todos.implementations.beanie.beanie_todos_repository import (
    BeanieTodosRepository,
)
from src.modules.users.contracts.repositories.users import UsersRepository
from src.modules.users.implementations.beanie.beanie_users_repository import (
    BeanieUsersRepository,
)


class BeanieUsersRepositoryModule(Module):
    @singleton
    @provider
    def provide_beanie_user_repository(self) -> UsersRepository:
        return BeanieUsersRepository()


class BeanieTodoRepositoryModule(Module):
    @singleton
    @provider
    def provide_beanie_todo_repository(self) -> TodosRepository:
        return BeanieTodosRepository()
