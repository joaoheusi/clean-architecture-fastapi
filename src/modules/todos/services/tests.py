import asyncio
import unittest

from fastapi import HTTPException

from src.modules.todos.contracts.dtos.create_todo import CreateTodoDto
from src.modules.todos.implementations.fake.fake_todo_repository import (
    FakeTodoRepository,
)
from src.modules.todos.services.create_todo.service import CreateTodoService
from src.modules.todos.services.find_user_todos.service import FindUserTodosService
from src.modules.todos.services.mark_todo_as_done.service import MarkTodoAsDoneService


class TestTodosServices(unittest.TestCase):
    fake_todo_repository = FakeTodoRepository()
    create_todo_service = CreateTodoService(fake_todo_repository)
    find_user_todos_service = FindUserTodosService(fake_todo_repository)
    mark_todo_as_done_service = MarkTodoAsDoneService(fake_todo_repository)

    def test_create_todo(self) -> None:
        data = CreateTodoDto(
            **{
                "title": "title",
                "description": "description",
            }
        )
        user_id = "123456"
        response = asyncio.run(
            self.create_todo_service.execute(data=data, user_id=user_id)
        )
        assert response.title == data.title

    def test_get_user_todos(self) -> None:
        user_id = "123456"
        response = asyncio.run(self.find_user_todos_service.execute(user_id=user_id))
        assert len(response) == 1
        assert response[0].userId == user_id

    def test_mark_todo_as_done(self) -> None:
        user_id = "123456"
        response = asyncio.run(self.find_user_todos_service.execute(user_id=user_id))
        todo_id = response[0].id
        done_response = asyncio.run(
            self.mark_todo_as_done_service.execute(user_id=user_id, todo_id=todo_id)
        )
        assert done_response.isDone is True

    def test_mark_todo_as_other_user(self) -> None:
        wrong_user_id = "122222"
        original_user_id = "123456"
        response = asyncio.run(
            self.find_user_todos_service.execute(user_id=original_user_id)
        )
        todo_id = response[0].id
        with self.assertRaises(HTTPException) as context:
            asyncio.run(
                self.mark_todo_as_done_service.execute(
                    user_id=wrong_user_id, todo_id=todo_id
                )
            )
        assert context.exception.status_code == 403
