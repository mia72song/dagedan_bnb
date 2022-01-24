from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

jwt = JWTManager()
mail = Mail()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    from config import envs
    #dev, pro, test，配置文件因運行環境而異
    env_config = envs.get("dev")
    app.config.from_object(env_config)

    jwt.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from App.utils import ReConverter
    app.url_map.converters["re"] = ReConverter

    from App.view import view
    app.register_blueprint(view, url_prefix = "/")
    from App.auth import auth
    app.register_blueprint(auth, url_prefix = "/auth")
    from App.api_v2 import api
    app.register_blueprint(api, url_prefix = "/api")

    return app
