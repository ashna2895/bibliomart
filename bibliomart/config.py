DEBUG = True

import os
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# SQL ALCHEMY Config
DATABASE = 'site.db'
DATABASE_PATH = os.path.join(basedir, DATABASE)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "this is some kind of secret"

SECRET_KEY = 'super-secret'
SERVE_URL = 'http://0.0.0.0:8000'
SERVE_HOST = '0.0.0.0'
SERVE_PORT = 8000
MEINHELD = False
THREADED = False

PROPAGATE_EXCEPTIONS = True

# Flask Security Configs
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = 'Thi$ s@lt'
SECURITY_TRACKABLE = True
SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
WTF_CSRF_ENABLED = False
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
SECURITY_POST_REGISTER_VIEW = '/'
SECURITY_REGISTER_URL = '/signup'
SECURITY_EMAIL_SENDER = 'ashna.abdul2895@gmail.com'
SECURITY_RESET_URL = '/user/password-reset'
SECURITY_CHANGE_URL = '/user/password-change'
SECURITY_POST_CHANGE_VIEW = '/user/password-change'
SECURITY_POST_RESET_VIEW = '/user/password-reset'


# Mail Settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'frezbotech@gmail.com'
MAIL_PASSWORD = '#Frezbo123'
