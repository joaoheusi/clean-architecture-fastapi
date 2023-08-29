from fastapi.encoders import jsonable_encoder

from src.modules.todos.entities.todo import Todo
from src.modules.todos.services.find_user_todos.service import FindUserTodosService
from src.providers.container import container


class FindUserTodosController:
    @staticmethod
    async def handle(user_id: str) -> list[Todo]:
        find_user_todos_service = container.get(FindUserTodosService)
        response = await find_user_todos_service.execute(user_id)
        return jsonable_encoder(response)
