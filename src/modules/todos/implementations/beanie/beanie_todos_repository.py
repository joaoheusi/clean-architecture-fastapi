from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.contracts.repositories.todos import TodosRepository
from src.modules.todos.entities.todo import Todo
from src.modules.todos.implementations.beanie.document import TodoDocument
from src.shared.utils.update_beanie_document_from_pydantic import (
    update_beanie_document_from_pydantic,
)


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
        todo = await TodoDocument.find_one(TodoDocument.id == todo_id).project(Todo)
        if not todo:
            return None
        return todo

    async def delete(self, todo_id: str) -> None:
        todo = await TodoDocument.find_one(TodoDocument.id == todo_id)
        if not todo:
            return None
        await todo.delete()

    async def save(self, todo: Todo) -> None:
        document = await TodoDocument.find_one(TodoDocument.id == todo.id)
        if not document:
            return None
        await update_beanie_document_from_pydantic(document, todo)
        await document.save_changes()
