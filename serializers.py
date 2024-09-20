from flask import request
from werkzeug.exceptions import BadRequest

class TaskSerializer:
    @staticmethod
    def validate_data():
        json_data = request.get_json()
        if not json_data:
            raise BadRequest("Nenhum dado enviado.")
        
        title = json_data.get('title')
        description = json_data.get('description')

        if not title or not title.strip():
            raise BadRequest("O título não pode estar vazio.")
        
        if not description or not description.strip():
            raise BadRequest("A descrição não pode estar vazia.")
        
        return {
            'title': title.strip(),
            'description': description.strip()
        }