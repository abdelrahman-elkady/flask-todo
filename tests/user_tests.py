from flask.ext.testing import TestCase

from app import create_app
from app.models import db
from app.models.user import User

from .config_test import TestConfig

class BaseTestCase(TestCase):

    SQLALCHEMY_DATABASE_URI = "postgresql:///todo_test"
    TESTING = True

    def create_app(self):
        app = create_app(TestConfig)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class UserTest(BaseTestCase):

    def login(self, email, password):
        """ helper for loggin in a user """
        return self.client.post('/login',
                             data={'email': email, 'password': password},
                             follow_redirects=True
                             )

    def logout(self):
        """helper for loggin out a user """
        return self.client.get('/logout', follow_redirects=True)

    def test_login_reachable(self):
        """ testing login page is reachable """
        result = self.client.get('/login')
        assert 'Sign in' in result.data

    def test_login_valid(self):
        """ testing logging in with a valid user """
        user = User('test_user', 'test_password', 'testmail@testprovider.com')

        db.session.add(user)
        db.session.commit()

        res = self.login('testmail@testprovider.com', 'test_password')
        assert 'Logged in successfully' in res.data
        assert 'Hi test_user!' in res.data
