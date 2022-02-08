from flask import render_template, redirect, session, url_for, request, flash

from . import admin
from App.models import User

# 判斷user帳號是否登入，否則重定向至登入頁面
def login_required(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("user"):
            return func(*args, **kwargs)
        else:
            flash("請先登入")
            return redirect(url_for("admin.index"))
    return wrapper

# 登入
@admin.route("/", methods=["GET", "POST"])
def index():
    if session.get("user"):
        return redirect("/admin/board")

    if request.method == "POST":
        if request.form.get("username") and request.form.get("password"):
            user = User.query.filter_by(username=request.form.get("username")).first()
            if (user is None) or (not user.checkPassword(request.form.get("password"))):
                flash("帳號或密碼錯誤")
            else:
                session["user"] = (user.username, user.name)
                return redirect("/admin/board")
        else:
            flash("帳號及密碼皆不得為空值")
    
    return render_template("admin.html")

# 登出
@admin.route("/logout")
def logout():
    if session.get("user"):
        del session["user"]

    return redirect(url_for("admin.index"))