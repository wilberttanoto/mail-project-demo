# This file contains the configuration variables for your app, such as database details.

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'super secret key'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'wilbert.social@gmail.com'
MAIL_PASSWORD = 'w1lbert_social'
MAIL_DEFAULT_SENDER = 'wilbert.social@gmail.com'

# Celery configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

accept_content=['json','pickle']