from flask import render_template, request, redirect, url_for, session, flash

from model.db import Mydb
from . import admin

@admin.route("/")
def admin_index():
    if session.get("user"):
        return redirect("/admin/user")
    
    return render_template("admin.html")

@admin.route("/login", methods=["POST",])
def login():
    user_info = None
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username and password:
            mydb = Mydb()
            user_info = mydb.getUser(username, password)
            if user_info:
                session["user"] = user_info
                return redirect("/admin/user")
            else:
                flash("帳號或密碼輸入錯誤!!!")
        else:
            flash("帳號及密碼皆不得為空")    
    
    return redirect("/admin")

@admin.route("/logout")
def logout():
    if session.get("user") :
        del session["user"]

    return redirect("/admin")

@admin.route("/user")
def user():
    if session.get("user") :
        return render_template("user.html", user = (session.get("user"))[1])
    else:
        return redirect("/admin")
