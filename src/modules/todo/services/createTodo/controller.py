from fastapi.encoders import jsonable_encoder

from src.modules.todo.contracts.dtos.createTodo_dto import CreateTodoDto
from src.modules.todo.entities.todo import Todo
from src.modules.todo.services.createTodo.service import CreateTodoService
from src.providers.container import container


class CreateTodoController:
    @staticmethod
    async def handle(data: CreateTodoDto) -> Todo:
        create_todo_service = container.get(CreateTodoService)
        response = await create_todo_service.handle(data)
        return jsonable_encoder(response)
