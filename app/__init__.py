# This file intializes a Python module. Without it, Python will not recognize the app directory as a module.

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
