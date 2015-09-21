import unittest

from app import create_app
from app.models import db

from .config_test import TestConfig

app = create_app(TestConfig)

class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        with app.test_request_context():
            db.create_all()

    def tearDown(self):
        with app.test_request_context():
            db.session.remove()
            db.drop_all()


class UserTest(TestCase):
    
    def test_index_exists(self):
        result = self.app.get('/')
        assert 'INDEX' in result.data
