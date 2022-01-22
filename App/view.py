from flask import Blueprint, render_template

view = Blueprint("view", __name__)

# 前台頁面
@view.route("/<re(r'.*'):html_filename>")
def index(html_filename):
    if not html_filename:
        html_filename = "index.html"
    else:
        html_filename += ".html"
        
    return render_template(html_filename)

# 管理後台頁面
@view.route("/admin/<re(r'.*'):html_filename>")
def admin(html_filename):
    if not html_filename:
        html_filename = "admin.html"
    else:
        html_filename = f"admin_{html_filename}.html"

    return render_template(html_filename)