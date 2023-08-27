from fastapi.encoders import jsonable_encoder

from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.entities.todo import Todo
from src.modules.todos.services.create_todo.service import CreateTodoService
from src.providers.container import container


class CreateTodoController:
    @staticmethod
    async def handle(data: CreateTodoDto) -> Todo:
        create_todo_service = container.get(CreateTodoService)
        response = await create_todo_service.handle(data)
        return jsonable_encoder(response)
