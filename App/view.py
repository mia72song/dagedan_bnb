from flask import Blueprint, render_template
import os

from App import csrf

view = Blueprint("view", __name__)
csrf.exempt(view)

templates_dir = f"{os.path.dirname(os.path.abspath(__file__))}/templates"

# 前台頁面
@view.route("/<re(r'.*'):html_filename>")
def get_views(html_filename):
    status_code = 200
    if not html_filename:
        html_filename = "index.html"
    else:
        html_filename += ".html"

    if not os.path.exists(f"{templates_dir}/{html_filename}"):
        html_filename = "404.html"
        status_code = 404       

    return render_template(html_filename), status_code
