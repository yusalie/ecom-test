from unittest import TestCase
from market.models import User, Item

class TestModels(TestCase):
    def test_user(self):
        user = User(username='something', email_address='something@email.com', password_hash='123456')
        
        self.assertEqual(user.username, 'something', 'username')
        self.assertEqual(user.email_address, 'something@email.com', 'email')
        self.assertEqual(user.password_hash, '123456', 'password')
    
    def test_item(self):
        item = Item(name='PS5', price=250, barcode='258741369000', description='description')
        
        self.assertEqual(item.name, 'PS5', 'console')
        self.assertEqual(item.price, 250, 'price')
        self.assertEqual(item.barcode, '258741369000', 'barcode')
        self.assertEqual(item.description, 'description', 'description')