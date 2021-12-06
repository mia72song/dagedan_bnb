from flask import render_template

from . import admin

@admin.route("/")
def index():
    return render_template("admin.html")

@admin.route("/board")
def board():
    return render_template("board.html")