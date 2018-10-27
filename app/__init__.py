from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(config_class)

    db.init_app(application)
    migrate.init_app(application, db)

    from app.main import bp as main_bp
    application.register_blueprint(main_bp)
    from app.auth import bp as auth_bp
    application.register_blueprint(auth_bp)

    return application


from app import models