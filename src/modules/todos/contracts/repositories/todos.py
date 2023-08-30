from abc import ABC, abstractmethod

from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.entities.todo import Todo


class TodosRepository(ABC):
    @abstractmethod
    async def create(self, data: CreateTodoDto, user_id: str) -> Todo:
        raise Exception("Not implemented")

    @abstractmethod
    async def find_by_user_id(self, user_id: str) -> list[Todo]:
        raise Exception("Not implemented")

    @abstractmethod
    async def find_by_id(self, todo_id: str) -> Todo | None:
        raise Exception("Not implemented")

    @abstractmethod
    async def delete(self, todo_id: str) -> None:
        raise Exception("Not implemented")

    @abstractmethod
    async def save(self, todo: Todo) -> None:
        raise Exception("Not implemented")
