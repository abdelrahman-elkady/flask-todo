from flask.ext.testing import TestCase
from flask import url_for
from flask.ext.login import current_user

from app import create_app
from app.models import db
from app.models.user import User


from .config_test import TestConfig


class BaseTestCase(TestCase):

    def create_app(self):
        app = create_app(TestConfig)
        return app

    def setUp(self):
        db.create_all()

        user = User('test_user', 'test_password', 'testmail@testprovider.com')
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class UserTest(BaseTestCase):

    def login(self, email, password):
        """ helper for loggin in a user """
        return self.client.post('/login',
                                data={'email': email, 'password': password},
                                follow_redirects=False
                                )

    def logout(self):
        """helper for loggin out a user """
        return self.client.get('/logout', follow_redirects=False)

    def test_login_reachable(self):
        """ testing login page is reachable """
        res = self.client.get('/login')
        self.assert200(res)
        assert 'Sign in' in res.data

    def test_login_valid(self):
        """ testing logging in with a valid user """

        res = self.login('testmail@testprovider.com', 'test_password')
        self.assert_redirects(res, '/')

        res = self.client.get(url_for('user.index'))
        self.assert200(res)
        assert 'Logged in successfully' in res.data
        assert 'Hi test_user!' in res.data

    def test_login_invalid(self):
        """ testing logging in with an invalid user """

        # Wrong password
        res = self.login('testmail@testprovider.com', 'fail_you_test')
        self.assert_redirects(res, '/login')

        res = self.client.get('/login')
        self.assert200(res)
        assert 'Username or password is not correct' in res.data

        # Wrong username
        res = self.login('fail_you_test', 'test_password')
        self.assert_redirects(res, '/login')

        res = self.client.get('/login')
        self.assert200(res)
        assert 'Username or password is not correct' in res.data

    def test_logout(self):
        """ testing logging out !"""
        with self.client:
            self.login('testmail@testprovider.com', 'test_password')
            self.assertTrue(current_user.is_authenticated())

            res = self.client.get(url_for('user.logout'))
            self.assert_redirects(res, url_for('user.index'))
            self.assertFalse(current_user.is_authenticated())

    def test_logout_without_login(self):
        """ testing logging out while not logged in """
        res = self.client.get(url_for('user.logout'))
        self.assert_redirects(res, url_for('user.index'))
        self.assertFalse(current_user.is_authenticated())

    
