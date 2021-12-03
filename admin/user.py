from flask import render_template, request, redirect, session, flash

from model.db import Mydb
from . import admin

@admin.route("/")
def index():
    if session.get("user"):
        return redirect("/admin/board")
    
    return render_template("admin.html")

@admin.route("/login", methods=["POST",])
def login():
    if request.method=="POST":
        if request.form.get("username") and request.form.get("password"):
            mydb = Mydb()
            user_info = mydb.getUser(request.form.get("username"), request.form.get("password"))
            if user_info:
                session["user"] = user_info
                return redirect("/admin/board")
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