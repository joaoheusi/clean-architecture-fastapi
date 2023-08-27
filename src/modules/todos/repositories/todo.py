from abc import ABC, abstractmethod

from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.entities.todo import Todo


class TodoRepository(ABC):
    @abstractmethod
    async def create(self, data: CreateTodoDto) -> Todo:
        raise Exception("Not implemented")
