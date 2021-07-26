from datetime import datetime
import unittest

from model.todo import TodoModel
from main import app


class TestListTodo(unittest.TestCase):
    def setUp(self) -> None:
        self.test_app = app.test_client()
        app.db = []
    
    def test_success_list_todo(self):
        app.db.append(
            TodoModel(
                0, 
                "title", 
                "body", 
                False, 
                datetime.now(), 
                1
            )
        )
        app.db.append(
            TodoModel(
                1, 
                "title1", 
                "body1", 
                False, 
                datetime.now(), 
                2
            )
        )
        app.db.append(
            TodoModel(
                2, 
                "title2", 
                "body2", 
                True, 
                datetime.now(), 
                3
            )
        )

        response = self.test_app.get("/todos")

        self.assertEqual(200, response.status_code)
        self.assertEqual(3, len(response.json))


class TestCreateTodo(unittest.TestCase):
    def setUp(self) -> None:
        self.test_app = app.test_client()
        app.db = []
    
    def test_success_create_todo(self):
        response = self.test_app.post(
            "/todo",
            json={
                "title": "할일1",
                "body": "난 강의를 해야한다.",
                "priority": 1
            }
        )

        self.assertEqual(201, response.status_code)
        created_todo = app.db[0]
        self.assertEqual("할일1", created_todo.title)
        self.assertEqual("난 강의를 해야한다.", created_todo.body)
        self.assertFalse(created_todo.is_completed)
        self.assertEqual(1, created_todo.priority)

unittest.main()