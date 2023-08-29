from injector import inject

from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.contracts.repositories.todos import TodosRepository
from src.modules.todos.entities.todo import Todo


class CreateTodoService:
    @inject
    def __init__(self, todo_repository: TodosRepository):
        self.todo_repository = todo_repository

    async def execute(self, data: CreateTodoDto, user_id: str) -> Todo:
        todo = await self.todo_repository.create(data, user_id=user_id)
        return todo
