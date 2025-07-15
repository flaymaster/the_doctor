import unittest
from app.main import app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200, 'Status code is not 200')
        try:
            data = response.get_json()
        except Exception as e:
            self.fail(f'Response is not valid JSON: {e}')
        self.assertIsInstance(data, dict, 'Response JSON is not a dictionary')
        self.assertIn('status', data, 'Missing "status" in response')
        self.assertEqual(data['status'], 'healthy', 'Status is not "healthy"')
        self.assertIn('container', data, 'Missing "container" in response')
        self.assertIn('project', data, 'Missing "project" in response')


if __name__ == '__main__':
    unittest.main()
