import unittest
from client import Client

class testClient(unittest.TestCase):
    def setUp(self):
        self.client = Client("Alex", "pass123")
    
    def test_inst(self):
        self.assertIsInstance(self.client, Client, "The client was not initiated properly")

    def test_eq(self):
        self.assertEqual(self.client, Client("Alex", "pass123"), "The two clients are not equal")
        self.assertNotEqual(self.client, Client("Nelly", "pass123"), "The two clients are equal")
        self.assertNotEqual(self.client, Client("Alex", "pass12"), "The two clients are equal")

if __name__ == '__main__':
    unittest.main()
    