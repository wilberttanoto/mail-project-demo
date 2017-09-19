#  This file contains all the routes for our application. This will tell Flask what to display on which path

from flask import render_template,request

from app import app

@app.route('/')
def index():
    return render_template("index.html")