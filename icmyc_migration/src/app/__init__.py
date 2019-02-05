import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine
from flask_migrate import Migrate


# instantiate the extensions
db = SQLAlchemy()
migrate = Migrate()
mongo = MongoEngine()


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv(
        "APP_SETTINGS", "src.app.config.DevelopmentConfig"
    )
    app.config.from_object(app_settings)

    # set up extensions
    mongo.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
