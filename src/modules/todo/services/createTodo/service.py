from injector import inject

from src.modules.todo.contracts.dtos.createTodo_dto import CreateTodoDto
from src.modules.todo.entities.todo import Todo
from src.modules.todo.repositories.todo import TodoRepository


class CreateTodoService:
    @inject
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository

    async def handle(self, data: CreateTodoDto) -> Todo:
        todo = await self.todo_repository.create(data)
        return todo
