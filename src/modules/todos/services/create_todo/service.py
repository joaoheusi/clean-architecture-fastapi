from injector import inject

from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.entities.todo import Todo
from src.modules.todos.repositories.todo import TodoRepository


class CreateTodoService:
    @inject
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository

    async def handle(self, data: CreateTodoDto) -> Todo:
        todo = await self.todo_repository.create(data)
        return todo
