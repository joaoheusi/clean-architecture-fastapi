from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.entities.todo import Todo
from src.modules.todos.repositories.todo import TodoRepository


class FakeTodoRepository(TodoRepository):
    __todos = []

    async def create(self, data: CreateTodoDto) -> Todo:
        todo = Todo(
            id="1239874",
            title=data.title,
            description=data.description,
            is_done=False,
        )
        self.__todos.append(todo)
        return todo
