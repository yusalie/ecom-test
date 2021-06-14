from tests.test_base import BaseTest
from market.__init__ import db
from market.models import User
from flask_login import current_user
from flask import request
from market.routes import register_page

class TestForms(BaseTest):
# testing register route post(sucessful register)
    def test_register_username(self):
        with self.app:
            with self.app_context():
                # correct details
                response = self.app.post('/register', data=dict(username='test', email_address='test@test.com', password1='password', password2='password'), follow_redirects=True)
                user = db.session.query(User).filter_by(email_address='test@test.com').first()
                self.assertTrue(user)
                self.assertIn(b'Account created successfully! You are now logged in as test', response.data)
                self.assertEqual(current_user.get_id(), '1')
    
    def test_login(self):
        with self.app:
            with self.app_context():
                response = self.app.post('/register', data=dict(username='test2', email_address='test2@test.com', password1='password', password2='password'), follow_redirects=True)
                user = db.session.query(User).filter_by(email_address='test2@test.com').first()
                self.assertTrue(user)
                self.assertIn(b'Account created successfully! You are now logged in as test2', response.data)
                self.assertEqual(current_user.get_id(), '1')
                
                response = self.app.post('/login', data=dict(username='test2', email_address='test2@test.com', password='password'), follow_redirects=True)
                user = db.session.query(User).filter_by(username='test2').first()
                self.assertTrue(user)
                self.assertIn(b'Success! You are logged in as: test2', response.data)
    
    def logout(self):
        with self.app:
            with self.app_context():
                response = self.app.post('/register', data=dict(username='test3', email_address='test3@test.com', password1='password', password2='password'), follow_redirects=True)
                user = db.session.query(User).filter_by(email_address='test3@test.com').first()
                self.assertTrue(user)
                self.assertIn(b'Account created successfully! You are now logged in as test3', response.data)
                self.assertEqual(current_user.get_id(), '3')
                
                response = self.app.post('/login', data=dict(username='test3', email_address='test3@test.com', password='password'), follow_redirects=True)
                self.assertTrue(user)
            
                response = self.app.get('/log-out', follow_redirects=True)
                self.assertEqual(response.status_code, 200)
        
                self.assertIn('/log-in', request.url)
                self.assertFalse(current_user.is_active)