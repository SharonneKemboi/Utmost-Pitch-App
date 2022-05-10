from flask import Flask
from flask_mail import Mail
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager


login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"

#initialize extensions
mail = Mail()
bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet("photos", IMAGES)

def create_app(config_name):
    """
    This is a function that will initialize the Flask instance
    """
    #instantiate Flask
    app = Flask(__name__)
   
    

    #add the configurations
    app.config.from_object(config_options[config_name])

    #initialize the extensions
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    #initialize the uploads
    configure_uploads(app,photos)

    #initialize blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    

    return app