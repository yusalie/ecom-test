from tests.test_base import BaseTest
from market.__init__ import db
from market.models import User
from flask_login import current_user
from flask import request
from market.models import User, Item

class testForms(BaseTest):
    def test_username(self):
        with self.app:
            response = self.app.post('/register', data=dict(username='test', email_address='strive@gg.com', password1='pasword', password2='password'))
            user = db.session.query(User).filter_by(username='test').first()
            self.assertTrue(user)
            message = 'Username already exists! Please try a different username'
            self.assertTrue(message, response.data)
    
    def test_email(self):
        with self.app:
            response = self.app.post('/register', data=dict(username='test', email_address='strive@gg.com', password1='pasword', password2='password'))
            user = db.session.query(User).filter_by(email_address='strive@gg.com').first()
            self.assertTrue(user)
            message = 'Email Address already exists! Please try a different email address'
            self.assertTrue(message, response.data)
    
    