from flask import *
from flask_jwt_extended import JWTManager

from config import envs

jwt = JWTManager()

app = Flask(__name__)

# 先載入config 再 init_app(app)
env_config = envs.get("dev")  #dev, pro, test，配置文件因運行環境而異
app.config.from_object(env_config)

jwt.init_app(app)

from utils import ReConverter
#為flask添加自定義的轉換器 (要在藍圖之前導入)
app.url_map.converters["re"] = ReConverter

from auth import auth
app.register_blueprint(auth, url_prefix = "/auth")
from api_v2 import api
app.register_blueprint(api, url_prefix = "/api")

# 前台頁面
@app.route("/<re(r'.*'):html_filename>")
def index(html_filename):
    if not html_filename:
        html_filename = "index.html"
    else:
        html_filename += ".html"
        
    return render_template(html_filename)

# 管理後台頁面
@app.route("/admin/<re(r'.*'):html_filename>")
def admin(html_filename):
    if not html_filename:
        html_filename = "admin.html"
    else:
        html_filename = f"admin_{html_filename}.html"

    return render_template(html_filename)

#Rroduction Environment：app.run(host="0.0.0.0", port=3000)

#Development Environment:
app.run() #default host="127.0.0.1" port=5000