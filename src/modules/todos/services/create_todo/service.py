from injector import inject

from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.contracts.repositories.todo import TodoRepository
from src.modules.todos.entities.todo import Todo


class CreateTodoService:
    @inject
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository

    async def execute(self, data: CreateTodoDto) -> Todo:
        todo = await self.todo_repository.create(data)
        return todo
