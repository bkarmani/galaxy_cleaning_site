from config import config
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_login import LoginManager
from flask_ckeditor import CKEditor
import pymysql



db = SQLAlchemy()
bootstrap = Bootstrap()
email = Mail()
time = Moment()
ckeditor = CKEditor()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
pymysql.install_as_MySQLdb()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    email.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)
    

    # blueprpints
    from .main import main as main_blueprint
    from .auth import auth as auth_bp
    from .admin import admin as admin_bp

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app
