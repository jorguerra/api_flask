"app modules"
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from . import create_app

app = create_app()
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = app.api

from .api.my_model import api as ns_object

api.add_namespace(ns_object,'/objects')

@app.route('/')
def index():
    return 'I am the homepage'