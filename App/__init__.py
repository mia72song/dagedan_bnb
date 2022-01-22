from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mail import Mail

jwt = JWTManager()
mail = Mail()

def create_app(env):
    app = Flask(__name__)

    from config import envs
    #dev, pro, test，配置文件因運行環境而異
    env_config = envs.get(env)
    app.config.from_object(env_config)

    jwt.init_app(app)
    mail.init_app(app)

    from App.utils import ReConverter
    app.url_map.converters["re"] = ReConverter

    from App.view import view
    app.register_blueprint(view, url_prefix = "/")
    from App.auth import auth
    app.register_blueprint(auth, url_prefix = "/auth")
    from App.api_v2 import api
    app.register_blueprint(api, url_prefix = "/api")

    return app
