from injector import inject

from src.modules.todos.contracts.repositories.todo import TodoRepository
from src.modules.todos.entities.todo import Todo


class FindUserTodosService:
    @inject
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository

    async def execute(self, user_id: str) -> list[Todo]:
        user_todos = await self.todo_repository.find_by_user_id(user_id)
        return user_todos
