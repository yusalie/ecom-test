from unittest import TestCase
from market import app
from flask import request

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

    def test_route(self):
        with self.app:
            response = self.app.get('/', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
    
    def test_login(self):
        with self.app:
            response = self.app.get('/login', follow_redirects=True)
            self.assertIn('/login', request.url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Please Login', response.data)