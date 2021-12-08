from flask import render_template
from flask_jwt_extended import jwt_required

from . import admin

@admin.route("/")
def index():
    return render_template("admin.html")

@jwt_required()
@admin.route("/board")
def board():
    return render_template("board.html")