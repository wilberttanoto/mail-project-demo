# This file contains the configuration variables for your app, such as database details.

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'super secret key'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
