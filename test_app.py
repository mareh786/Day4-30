import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the Web App!", response.data)

    def test_greet(self):
        name = "Alice"
        response = self.client.get(f'/greet/{name}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, Alice!", response.data)

    def test_greet_edge_case(self):
        name = "123"
        response = self.client.get(f'/greet/{name}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, 123!", response.data)

if __name__ == '__main__':
    unittest.main()

