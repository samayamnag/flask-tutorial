import os
from utils import getenv


class BaseConfig(object):
    """Base configuration."""

    APP_NAME = os.getenv("APP_NAME")
    BCRYPT_LOG_ROUNDS = 4
    DEBUG_TB_ENABLED = False
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_BINDS = {
        "swachh_manch": f'mysql+pymysql://'
        f'{getenv("SWACHHATA_MYSQL_DB_USERNAME")}:{getenv("SWACHHATA_MYSQL_DB_PASSWORD")}'
        f'@{getenv("SWACHHATA_MYSQL_DB_HOST")}/{getenv("SWACHHATA_MYSQL_DB_NAME")}',
        "icmyc": f'mysql+pymysql://'
        f'{getenv("ICMYC_MYSQL_DB_USERNAME")}:{getenv("ICMYC_MYSQL_DB_PASSWORD")}'
        f'@{getenv("ICMYC_MYSQL_DB_HOST")}/{getenv("ICMYC_MYSQL_DB_NAME")}',
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MONGODB_SETTINGS = {
        'db': getenv("SWACHHATA_MONGO_DB_NAME"),
        'host': getenv("SWACHHATA_MONGO_DB_HOST"),
        'port': int(getenv("SWACHHATA_MONGO_DB_PORT")),
        'username': getenv("SWACHHATA_MONGO_DB_USERNAME"),
        'password': getenv("SWACHHATA_MONGO_DB_PASSWORD"),
    }


class TestingConfig(BaseConfig):
    """Testing configuration."""

    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL", "sqlite:///")
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration."""

    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    WTF_CSRF_ENABLED = True

