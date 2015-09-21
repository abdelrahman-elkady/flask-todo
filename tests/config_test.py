class TestConfig(object):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql:///todo_test'
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'aV3rySEcr3tK3yJustForT3sT'
