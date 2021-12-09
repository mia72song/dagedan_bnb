from flask import Blueprint, render_template

admin = Blueprint("admin", __name__)

# 管理後台頁面
@admin.route("/")
def index():
    return render_template("admin.html")

@admin.route("/board")
def board():
    return render_template("board.html")

@admin.route("/room")
def room():
    return render_template("room.html")

@admin.route("/order")
def order():
    return render_template("order.html")