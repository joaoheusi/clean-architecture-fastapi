from src.modules.todo.contracts.dtos.createTodo_dto import CreateTodoDto
from src.modules.todo.entities.todo import Todo
from src.modules.todo.repositories.todo import TodoRepository


class FakeTodoRepository(TodoRepository):
    async def create(self, data: CreateTodoDto) -> Todo:
        return Todo(
            id="1239874",
            title=data.title,
            description=data.description,
            is_done=False,
        )
