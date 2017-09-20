# This file intializes a Python module. Without it, Python will not recognize the app directory as a module.

# third-party imports
from flask import Flask
from celery import Celery
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
Bootstrap(app)
mail = Mail(app)

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

from app import views, models
