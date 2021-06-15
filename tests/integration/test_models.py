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