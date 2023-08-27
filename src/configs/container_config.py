from injector import Module, provider, singleton
from src.modules.todos.implementations.beanie.beanie_todo_repository import (
    BeanieTodoRepository,
)

from src.modules.todos.implementations.fake.fake_todo_repository import (
    FakeTodoRepository,
)
from src.modules.todos.repositories.todo import TodoRepository


class FakeTodoRepositoryModule(Module):
    @singleton
    @provider
    def provide_fake_todo_repository(self) -> TodoRepository:
        return FakeTodoRepository()


class BeanieTodoRepositoryModule(Module):
    @singleton
    @provider
    def provide_beanie_todo_repository(self) -> TodoRepository:
        return BeanieTodoRepository()
