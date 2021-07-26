# flask_restful사용해서

from datetime import datetime

from flask import Flask, request
from flask_restful import Resource, Api

from model.todo import TodoModel


app = Flask(__name__)
app.db = []
todo_id = 0

api = Api(app)

class ListTodoView(Resource):
    def get(self):
        result = []
        for todo in app.db:
            result.append(todo.to_dict())
        return result, 200


class CreateTodoView(Resource):
    def post(self):
        global todo_id
        todo = TodoModel(
            todo_id = todo_id,
            title=request.json.get("title"),
            body=request.json.get("body"),
            is_completed=False,
            created_at=datetime.now(),
            priority=request.json.get("priority", 5)
        )
        app.db.append(todo)
        todo_id += 1
        return "", 201

class TodoView(Resource):
    def get(self, todo_id):
        result = None
        for todo in app.db:
            if todo.todo_id == todo_id:
                result = todo
                break
        if result is None:
            return "", 404
        
        return result.to_dict(), 200
    
    def delete(self, todo_id):
        for todo in app.db:
            if todo.todo_id == todo_id:
                app.db.remove(todo)
                break
        
        return "", 204
    
    def patch(self, todo_id):
        target = None
        for todo in app.db:
            if todo.todo_id == todo_id:
                target = todo
                break
        if target is None:
            return "", 404
        
        title = request.json.get("title")
        if title is not None:
            target.title = title
        
        body = request.json.get("body")
        if body is not None:
            target.body = body
        
        is_completed = request.json.get("is_completed")
        if is_completed is not None:
            target.is_completed = is_completed
        
        priority = request.json.get("priority")
        if priority is not None:
            target.priority = priority
        
        return "", 200


api.add_resource(ListTodoView, "/todos")
api.add_resource(CreateTodoView, "/todo")
api.add_resource(TodoView, "/todo/<int:todo_id>")

if __name__ == "__main__":
    app.run(debug=True)
