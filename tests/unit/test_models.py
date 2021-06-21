from unittest import TestCase
from market.models import User, Item
from market import bcrypt
from 

class TestModels(TestCase):
    # test user model creates user object
    def test_user(self):
        user = User(username='qwerty', email_address='test@gmail.com', password_hash='password', budget=1100)
        
        self.assertEqual(user.username, 'qwerty', "this the username")
        self.assertEqual(user.email_address, 'test@gmail.com', "testing email")
        self.assertEqual(user.password_hash, 'password', "test password")
        self.assertEqual(user.budget, 1100)
    
    def test_prettier_budget(self):
        budget = User(username='qwerty', email_address='test@gmail.com', password_hash='password', budget=1100).prettier_budget
        self.assertEqual(budget, "1,100$")
        
    def test_password(self):
        passw = User(username='qwerty', email_address='test@gmail.com', password_hash='password', budget=1100).password
        self.assertEqual(passw, 'password')
    
    def test_password_verification(self):
        password = 'qwerty'
        pw_hash = bcrypt.generate_password_hash(password)
        ps_hash = bcrypt.check_password_hash(pw_hash, 'qwerty')
        self.assertTrue(ps_hash)
        
    def test_can_purchase(self):
        user = User(username='qwert', email_address='test@gmail.com', password_hash='passwords', budget=2000).can_purchase(Item(
          name='paper', price=1000, barcode='white', description='test'  
        ))
        self.assertTrue(user)    
    
    def test_item(self):
        item = Item(name='paper', price=15, barcode='white', description='test')
        
        self.assertEqual(item.name, 'paper', "this the name")
        self.assertEqual(item.price, 15)
        self.assertEqual(item.barcode, 'white')
        self.assertEqual(item.description, 'test')

    def test_repr(self):
        item = Item(name='car', price=15, barcode='white', description='test')
        
        self.assertEqual(item.__repr__(), "Item car")