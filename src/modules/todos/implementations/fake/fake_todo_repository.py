from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.contracts.repositories.todo import TodoRepository
from src.modules.todos.entities.todo import Todo


class FakeTodoRepository(TodoRepository):
    __todos: list[Todo] = []

    async def create(self, data: CreateTodoDto) -> Todo:
        todo = Todo(
            **data.model_dump(),
        )
        self.__todos.append(todo)
        return todo
