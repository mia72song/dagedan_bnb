import secrets
import os
from dotenv import load_dotenv
load_dotenv()

# flask_sqlalchemy設置
DB_HOST = os.getenv("DB_HOST", default="localhost")
DB_PORT = 3306
DB_USER = os.getenv("DB_USER", default="root")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

class Config:
    SECRET_KEY = secrets.token_hex()
    PERMANENT_SESSION_LIFETIME = 86400
    TEMPLATES_AUTO_RELOAD = True

    # jsonify設置，取代json.dumps(data_dict, ensure_ascii=False, indent=2)
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    # JSONIFY_MIMETYPE = "application/json" #default

    # JWT設置
    JWT_SECRET_KEY = secrets.token_hex()
    JWT_TOKEN_LOCATION = ["headers", "cookies"] #"headers", "cookies", "json", "query_string"
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access"]
    PROPAGATE_EXCEPTIONS = True

    # flask-mail設置
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

    # flask_sqlalchemy設置
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevConfig(Config):
    ENV = "development"
    DEBUG = True

class ProConfig(Config):
    ENV = "production"
    DEBUG = False

    HOST = "0.0.0.0"
    PORT = 80

    # If true this will only allow the cookies that contain your JWTs to be sent over https.
    # In production, this should always be set to True
    JWT_COOKIE_SECURE = True
    JWT_TOKEN_LOCATION = ["headers"] #"headers", "cookies", "json", "query_string"

class TestingConfig(ProConfig):
    TESTING = True

envs = {
    "dev": DevConfig,
    "pro": ProConfig,
    "test": TestingConfig
}