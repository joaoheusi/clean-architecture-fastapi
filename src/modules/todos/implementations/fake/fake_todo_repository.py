from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.contracts.repositories.todo import TodoRepository
from src.modules.todos.entities.todo import Todo


class FakeTodoRepository(TodoRepository):
    __todos: list[Todo] = []

    async def create(self, data: CreateTodoDto, user_id: str) -> Todo:
        todo = Todo(
            **data.model_dump(),
            userId=user_id,
            isDone=False,
        )
        self.__todos.append(todo)
        return todo

    async def find_by_user_id(self, user_id: str) -> list[Todo]:
        return list(filter(lambda todo: todo.userId == user_id, self.__todos))

    async def find_by_id(self, todo_id: str) -> Todo | None:
        return next(filter(lambda todo: todo.id == todo_id, self.__todos))

    async def delete(self, todo_id: str) -> None:
        todo = await self.find_by_id(todo_id)
        if todo:
            self.__todos.remove(todo)
        return None
