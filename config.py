import secrets

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
    JWT_TOKEN_LOCATION = ["headers", "cookies"]
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access"]

class DevConfig(Config):
    ENV = "development"
    DEBUG = True

class ProConfig(Config):
    ENV = "production"
    DEBUG = False

class TestingConfig(ProConfig):
    TESTING = True

envs = {
    "dev": DevConfig,
    "pro": ProConfig,
    "test": TestingConfig
}