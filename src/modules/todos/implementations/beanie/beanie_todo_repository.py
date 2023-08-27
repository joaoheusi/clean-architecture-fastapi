from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.entities.todo import Todo
from src.modules.todos.repositories.todo import TodoRepository
from src.modules.todos.implementations.beanie.document import TodoDocument


class BeanieTodoRepository(TodoRepository):
    async def create(self, data: CreateTodoDto) -> Todo:
        todo = TodoDocument(
            title=data.title,
            description=data.description,
            is_done=False,
        )
        await todo.insert()
        return todo
