from flask import *
from flask_jwt_extended import JWTManager
import os

jwt = JWTManager()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
app.config["PERMANENT_SESSION_LIFETIME"] = 86400
app.config["JSON_AS_ASCII"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True

# JWT設置
jwt.init_app(app)
app.config['JWT_SECRET_KEY'] = os.urandom(24).hex()
app.config['JWT_TOKEN_LOCATION'] = ['headers','query_string']
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']

from admin import admin
app.register_blueprint(admin, url_prefix = "/admin")
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

app.run(debug=True)