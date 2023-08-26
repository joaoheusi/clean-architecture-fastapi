from src.modules.todo.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todo.entities.todo import Todo
from src.modules.todo.repositories.todo import TodoRepository
from src.modules.todo.implementations.beanie.document import TodoDocument


class BeanieTodoRepository(TodoRepository):
    async def create(self, data: CreateTodoDto) -> Todo:
        todo = TodoDocument(
            title=data.title,
            description=data.description,
            is_done=False,
        )
        await todo.insert()
        return todo
