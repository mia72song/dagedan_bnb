from flask import *
from config import envs

from flask_jwt_extended import JWTManager
jwt = JWTManager()

app = Flask(__name__)

# 先載入config 再 init_app(app)
env_config = envs.get("dev")  #dev, pro, test
app.config.from_object(env_config)
jwt.init_app(app)

from cms import admin
app.register_blueprint(admin, url_prefix = "/admin")
from auth import auth
app.register_blueprint(auth, url_prefix = "/auth")
from api_v1 import api
app.register_blueprint(api, url_prefix = "/api")

# 前台頁面
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/booking")
def booking():    
    return render_template("booking.html")

#Rroduction Environment：app.run(host="0.0.0.0", port=3000)

#Development Environment:
app.run() #default port=5000