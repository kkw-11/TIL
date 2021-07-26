from datetime import datetime

from flask import Flask, Response, request, jsonify
from flaks_restful import Resource, Api
from model.todo import TodoModel

app = Flask(__name__)
app.db = []

api = Api(app)


class listTodoView(Resource):
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
        priority= request.json.get("priority", 5)
        )
        app.db.append(todo)
        todo_id += 1
        return "", 201




@app.route("/todos/<int:todo_id>", methods=["PATCH"])
def update_todo(todo_id):
    target = None
    for todo in app.db:
        if todo.todo_id == todo_id:
            target = todo
            break
    if target is None:
        return Response(status=404)
    
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
    
    return Response(status=200)


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    for todo in app.db:
        if todo.todo_id == todo_id:
            app.db.remove(todo)
            break
    
    return Response(status=204)


@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    result = None
    for todo in app.db:
        if todo.todo_id == todo_id:
            result = todo
            break
    if result is None:
        return Response(status=404)
    
    return jsonify(result.to_dict())


if __name__ == "__main__":
    app.run(debug=True)
