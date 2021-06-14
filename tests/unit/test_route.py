from unittest import TestCase
from market import app

class TestRoute(TestCase):
    def test_home(self):
        with app.test_client() as client:
            response = client.get('/home')
            
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'/home', response.get_data())

    def test_register(self):
        with app.test_client() as client:
            response = client.get('/register')
            
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'/register', response.get_data())

    def test_login(self):
        with app.test_client() as client:
            response = client.get('/login')
            
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'/login', response.get_data())

    def test_logout(self):
        with app.test_client() as client:
            response = client.get('/logout')
            self.assertEqual(response.status_code, 302)