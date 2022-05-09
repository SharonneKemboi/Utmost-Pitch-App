import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = "app/static/photos"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

    #email 
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USERNAME")
    MAIL_PASSWORD  = os.environ.get("EMAIL_PASSWORD")
   


class DevConfig(Config):
    """
    This is the class which we will use to set the configurations during development stage of the app
    Args:
        COnfig - this is the parent config class from which we inherit its properties
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Atara@localhost/pitches'
    DEBUG = True


class ProdConfig(Config):
    """
    This is the class which we will use to set the configurations during production stage of the app
    Args:
        Config - this is the parent config class from which we inherit its properties
    """
    pass
   


class TestConfig(Config):
    """
    This is the class which we will use to set the configurations during testing stage of the app
    Args:
        Config - this is the parent config class from which we inherit its properties
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Atara@localhost/pitches_test'


config_options = {
    "test": TestConfig,
    "production": ProdConfig,
    "development": DevConfig
} 