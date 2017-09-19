# This file intializes a Python module. Without it, Python will not recognize the app directory as a module.

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
Bootstrap(app)

from app import views, models
