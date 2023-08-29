from fastapi.encoders import jsonable_encoder

from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.entities.todo import Todo
from src.modules.todos.services.create_todo.service import CreateTodoService
from src.modules.users.entities.user import User
from src.providers.container import container


class CreateTodoController:
    @staticmethod
    async def handle(data: CreateTodoDto, user: User) -> Todo:
        create_todo_service = container.get(CreateTodoService)
        response = await create_todo_service.execute(data, user_id=user.id)
        return jsonable_encoder(
            response.model_dump(by_alias=False, exclude={"revision_id"})
        )
