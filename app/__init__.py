import os
from flask import Flask
from flask_restx import Api

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.update(
        SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL'),
        PRESERVE_CONTEXT_ON_EXCEPTION = True
    )
    from . import db_command
    db_command.init_app(app)

    api  = Api(app,prefix="/api/", doc="/api/")
    
    app.api = api

    return app