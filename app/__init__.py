from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

login = LoginManager()
login.login_view = 'auth.index'

def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(config_class)

    db.init_app(application)
    migrate.init_app(application, db)
    ma.init_app(application)

    login.init_app(application, db)

    from app.main import bp as main_bp
    application.register_blueprint(main_bp)
    from app.api import bp as api_bp
    application.register_blueprint(api_bp, url_prefix='/api')
    from app.auth import bp as auth_bp
    application.register_blueprint(auth_bp)

    return application


from app import models