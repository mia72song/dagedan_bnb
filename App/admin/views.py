from flask import render_template, redirect, session, url_for, request, flash, abort
import os

from . import admin
from App.constants import TEMPLATES_DIR
from .auth import login_required

# 管理後台頁面
@admin.route("/<html_filename>")
@login_required
def get_views(html_filename):
    html_filename = f"admin_{html_filename}.html"

    if not os.path.exists(f"{TEMPLATES_DIR}/{html_filename}"):
        abort(404)

    return render_template(html_filename, current_user=session.get("user")[1])