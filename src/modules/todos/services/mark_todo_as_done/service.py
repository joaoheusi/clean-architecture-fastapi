from injector import inject

from src.modules.todos.contracts.repositories.todos import TodosRepository
from src.modules.todos.entities.todo import Todo
from src.shared.errors.app_exceptions import AppExceptions


class MarkTodoAsDoneService:
    @inject
    def __init__(self, todos_repository: TodosRepository):
        self.todos_repository = todos_repository

    async def execute(self, todo_id: str, user_id: str) -> Todo:
        todo = await self.todos_repository.find_by_id(todo_id=todo_id)
        if not todo:
            raise AppExceptions.resource_not_found()
        if not todo.userId == user_id:
            raise AppExceptions.resource_not_yours()
        todo.isDone = True
        await self.todos_repository.save(todo)
        return todo
