import unittest
from app import app, db
from models import Task

class TaskAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()
            self.task1 = Task(title='Task 1', description='Description of Task 1')
            db.session.add(self.task1)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_task(self):
        response = self.app.post('/tasks', json={'title': 'New Task', 'description': 'New task description'})
        self.assertEqual(response.status_code, 201)

    def test_update_task(self):
        response = self.app.put(f'/tasks/{self.task1.id}', json={'title': 'Task 1 Atualizada', 'description': 'Descrição atualizada da task 1'})
        self.assertEqual(response.status_code, 200)

    def test_delete_task(self):
        response = self.app.delete(f'/tasks/{self.task1.id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
