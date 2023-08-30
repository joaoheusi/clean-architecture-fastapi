from fastapi.encoders import jsonable_encoder

from src.modules.todos.entities.todo import Todo
from src.modules.todos.services.mark_todo_as_undone.service import (
    MarkTodoAsUndoneService,
)
from src.providers.container import container


class MarkTodoAsUndoneController:
    @staticmethod
    async def handle(todo_id: str, user_id: str) -> Todo:
        mark_todo_as_undone_service = container.get(MarkTodoAsUndoneService)
        todo = await mark_todo_as_undone_service.execute(
            todo_id=todo_id, user_id=user_id
        )
        return jsonable_encoder(todo)
