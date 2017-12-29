# -*- coding: utf-8 -*-
"""
    mod: api
    version: v2
"""
from flask import (
    Flask, Blueprint, request, session, g,
    redirect, url_for, abort, render_template,
    flash, current_app, make_response
)
from flask_restful import reqparse, abort, Resource, Api

bp = Blueprint(__name__, __name__, url_prefix='/api')
api = Api(prefix='/v2', app=bp)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


# show a single todos item and lets you delete them
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


# Actually setup the Api resource routing here
# api.add_resource(TodoList, 'todos', endpoint='todos')
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')