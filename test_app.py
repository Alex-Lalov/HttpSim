import unittest
from app import App
from client import Client

class testApp(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.app.app.config['TESTING'] = True
        self.client = self.app.app.test_client()
    
    def test_auth(self):
        json_client = {
            "client_id": "0123456",
            "client_pass": "pass123"
        }
        response = self.client.post('/auth', json=json_client)

        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.get_json())
    
    def test_noauth(self):
        json_client = {
            "client_id": "01234",
            "client_pass": "123"
        }
        response = self.client.post('/auth', json=json_client)

        self.assertEqual(response.status_code, 401)
    
    def test_resource(self):
        response = self.client.get('/resource')

        self.assertEqual(response.status_code, 403)

if __name__ == "__main__":
    unittest.main()