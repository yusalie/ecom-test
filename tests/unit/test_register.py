from unittest import TestCase
from market import app

class TestRegister(TestCase):
    def test_home(self):
        with app.test_client() as client:
            response = client.get('/home')
            
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'/home', response.get_data())