from injector import inject

from src.modules.todos.contracts.repositories.todo import TodoRepository
from src.modules.todos.entities.todo import Todo
from src.modules.todos.implementations.beanie.document import TodoDocument
from src.shared.server.errors.app_exceptions import AppExceptions


class MarkTodoAsDoneService:
    @inject
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository

    async def execute(self, todo_id: str, user_id: str) -> Todo:
        todo = await self.todo_repository.find_by_id(todo_id=todo_id)
        if not todo:
            raise AppExceptions.resource_not_found()
        if not todo.userId == user_id:
            raise AppExceptions.resource_not_yours()
        todo.isDone = True
        if type(todo) == TodoDocument:
            await todo.save_changes()
        return todo
