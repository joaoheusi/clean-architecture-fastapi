from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.contracts.repositories.todos import TodosRepository
from src.modules.todos.entities.todo import Todo
from src.modules.todos.implementations.beanie.document import TodoDocument


class BeanieTodosRepository(TodosRepository):
    async def create(self, data: CreateTodoDto, user_id: str) -> Todo:
        todo = TodoDocument(
            **data.model_dump(),
            userId=user_id,
            isDone=False,
        )
        response = await todo.insert()
        return response

    async def find_by_user_id(self, user_id: str) -> list[Todo]:
        todos = (
            await TodoDocument.find(TodoDocument.userId == user_id)
            .project(Todo)
            .to_list()
        )
        return todos

    async def find_by_id(self, todo_id: str) -> Todo | None:
        todo = await TodoDocument.find_one(TodoDocument.id == todo_id)
        if not todo:
            return None
        return todo

    async def delete(self, todo_id: str) -> None:
        todo = await self.find_by_id(todo_id)
        if not todo:
            return None
        if not type(todo) == TodoDocument:
            return None
        await todo.delete()
