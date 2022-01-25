from flask import Blueprint, render_template
import os

view = Blueprint("view", __name__)

templates_dir = f"{os.path.dirname(os.path.abspath(__file__))}/templates"

# 前台頁面
@view.route("/<re(r'.*'):html_filename>")
def index(html_filename):
    status_code = 200
    if not html_filename:
        html_filename = "index.html"
    else:
        html_filename += ".html"

    if not os.path.exists(f"{templates_dir}/{html_filename}"):
        html_filename = "404.html"
        status_code = 404       

    return render_template(html_filename), status_code


# 管理後台頁面
@view.route("/admin/<re(r'.*'):html_filename>")
def admin(html_filename):
    status_code = 200
    if not html_filename:
        html_filename = "admin.html"
    else:
        html_filename = f"admin_{html_filename}.html"

    if not os.path.exists(f"{templates_dir}/{html_filename}"):
        html_filename = "404.html"
        status_code = 404

    return render_template(html_filename), status_code