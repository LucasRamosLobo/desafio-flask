from flask_restful import Resource
from flask import jsonify
from models import Task
from db import db
from serializers import TaskSerializer

class TaskResource(Resource):
    def get(self, task_id=None):
        if task_id:
            task = Task.query.get_or_404(task_id)
            return jsonify({'id': task.id, 'title': task.title, 'description': task.description})
        tasks = Task.query.all()
        return jsonify([{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks])

    def post(self):
        data = TaskSerializer.validate_data()
        task = Task(title=data['title'], description=data['description'])
        db.session.add(task)
        db.session.commit()
        return jsonify({'message': 'Tarefa criada com sucesso!', 'id': task.id})

    def put(self, task_id):
        task = Task.query.get_or_404(task_id)
        data = TaskSerializer.validate_data()
        task.title = data['title']
        task.description = data['description']
        db.session.commit()
        return jsonify({'message': 'Tarefa atualizada com sucesso!'})

    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Tarefa deletada com sucesso!'})

def initialize_routes(api):
    api.add_resource(TaskResource, '/tasks', '/tasks/<int:task_id>')