from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.entities.todo import Todo
from src.modules.todos.contracts.repositories.todo import TodoRepository
from src.modules.todos.implementations.beanie.document import TodoDocument


class BeanieTodoRepository(TodoRepository):
    async def create(self, data: CreateTodoDto) -> Todo:
        todo = TodoDocument(
            **data.model_dump(),
        )
        await todo.insert()
        return todo
