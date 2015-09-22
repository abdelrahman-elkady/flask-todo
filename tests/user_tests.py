import unittest

from app import create_app
from app.models import db
from app.models.user import User

from .config_test import TestConfig

app = create_app(TestConfig)


class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

        # FIXME should we really do our db interaction with the test_context ?
        with app.test_request_context():
            db.create_all()

    def tearDown(self):
        with app.test_request_context():
            db.session.remove()
            db.drop_all()


class UserTest(TestCase):

    def login(self, email, password):
        """ helper for loggin in a user """
        return self.app.post('/login',
                             data={'email': email, 'password': password},
                             follow_redirects=True
                             )

    def logout(self):
        """helper for loggin out a user """
        return self.app.get('/logout', follow_redirects=True)

    def test_login_reachable(self):
        """ testing login page is reachable """
        result = self.app.get('/login')
        assert 'Sign in' in result.data

    def test_login_valid(self):
        """ testing logging in with a valid user """
        user = User('test_user', 'test_password', 'testmail@testprovider.com')
        with app.test_request_context():
            db.session.add(user)
            db.session.commit()

        res = self.login('testmail@testprovider.com', 'test_password')
        assert 'Logged in successfully' in res.data
