import unittest
from app import app, users, tasks

class TaskFlowTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Intelligent Task Management', response.data)

    def test_login_success(self):
        response = self.app.post('/login', data={
            'email': 'manager@company.com',
            'password': 'securepass123'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your Dashboard', response.data)

    def test_create_task(self):
        initial_count = len(tasks)
        self.app.post('/create-task?user=manager@company.com', data={
            'title': 'Test Task',
            'description': 'Test Description',
            'deadline': '2023-12-31',
            'auto_assign': 'on'
        })
        self.assertEqual(len(tasks), initial_count + 1)

if __name__ == '__main__':
    unittest.main()
