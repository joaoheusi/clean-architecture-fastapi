from abc import ABC, abstractmethod

from src.modules.todo.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todo.entities.todo import Todo


class TodoRepository(ABC):
    @abstractmethod
    async def create(self, data: CreateTodoDto) -> Todo:
        raise Exception("Not implemented")
