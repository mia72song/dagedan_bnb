from flask import Blueprint, render_template

admin = Blueprint("admin", __name__)

# 管理後台頁面
@admin.route("/")
def index():
    return render_template("admin.html")

@admin.route("/board")
def board():
    return render_template("board.html")

@admin.route("/rooms")
def get_room_list():
    return render_template("admin_room.html")

@admin.route("/orders")
def get_order_list():
    return render_template("admin_order.html")

@admin.route("/guests")
def get_guest_list():
    return render_template("admin_guest.html")