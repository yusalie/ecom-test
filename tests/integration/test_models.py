from tests.test_base import BaseTest
from market.__init__ import db
from market.models import User
from flask_login import current_user
from flask import request
from market.models import User, Item

class somethingModel(BaseTest):
    def test_user_crud(self):
        with self.app_context():
            user = User(username='something', email_address='somethings@gmail.com', password_hash='123456')
            result = db.session.query(User).filter_by(username="something").first()
            self.assertIsNone(result)
            
            db.session.add(user)
            db.session.commit()
            
            result = db.session.query(User).filter_by(username="something").first()
            self.assertIsNotNone(result)
            # assert user in db.session
            
            db.session.delete(user)
            db.session.commit()
            
            result = db.session.query(User).filter_by(username="something").first()
            self.assertIsNone(result)
            
    def test_item_crud(self):
        with self.app_context():
            item = Item(name='RTX 3080', price=1200, barcode='8555632047963', description='description')
            result = db.session.query(Item).filter_by(name="RTX 3080").first()
            self.assertIsNone(result)
            
            db.session.add(item)
            db.session.commit()
            
            result = db.session.query(Item).filter_by(name="RTX 3080").first()
            self.assertIsNotNone(result)
            
            db.session.delete(item)
            db.session.commit()
            
            result = db.session.query(Item).filter_by(name="RTX 3080").first()
            self.assertIsNone(result)
            
    def test_password_setter(self):
        with self.app_context():
            self.app.post('/register', data=dict(username='test', email_address='strive@gg.com', password1='password', password2='password'))
            user = db.session.query(User).filter_by(username='test').first()
            # assert user.password not equals 'password' 
            self.assertNotEqual(user.password, 'password')
            print(user.password)
    
    def test_password_correction(self):
        with self.app_context():
            self.app.post('/register', data=dict(username='manga', email_address='anime@anime.com', password1='password', password2='password'), follow_redirects=True)
            user = db.session.query(User).filter_by(username='manga').first()
            
            password_hash = User.check_password_correction(user, 'password')
            self.assertTrue(password_hash)
            
            password_hash1 = User.check_password_correction(user, "passwords")
            self.assertFalse(password_hash1)
            
    def test_buy_method(self):
         with self.app:
            with self.app_context():
                response = self.app.post('/register',
                                         data=dict(username="user", email_address="user@gmail.com",
                                                   password1="password", password2="password",), follow_redirects=True)
                user1 = db.session.query(User).filter_by(email_address="user@gmail.com").first()
                self.assertTrue(user1)

                item = Item(name="RTX 2080ti", price=250, barcode=5284176390, description="graphics card")
                db.session.add(item)
                db.session.commit()

                a = db.session.query(Item).filter_by(name="RTX 2080ti")
                self.assertTrue(a)

                buy = item.buy(user1)
                self.assertEqual(user1.budget, 750)
                self.assertEqual(item.owner, 1)

                sell = item.sell(user1)
                self.assertEqual(user1.budget, 1050)
                self.assertEqual(item.owner, None)