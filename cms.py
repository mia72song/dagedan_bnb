from flask import Blueprint, render_template

admin = Blueprint("admin", __name__)

# 管理後台頁面
@admin.route("/<re(r'.*'):html_filename>")
def index(html_filename):
    if not html_filename:
        html_filename = "admin.html"
    else:
        html_filename = f"admin_{html_filename}.html"
        
    return render_template("admin.html")
