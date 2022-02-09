from flask import render_template, redirect, session, request

from . import admin
from .auth import login_required
from App.models import Order

@admin.route("/order")
@login_required
def get_orders():
    # 請求網址：/admin/order?page=1
    # 請求網址：/admin/order?status=new&page=1
    limit = 10
    try:
        page = request.args.get("page", 1)
        end_index = limit*int(page)

    except ValueError:
        return render_template("404.html"), 404

    if request.args.get("status"):
        orders = Order.query.filter_by(status=request.args["status"]).order_by(Order.create_datetime.desc()).all()
    else:
        orders = Order.query.order_by(Order.create_datetime.desc()).all()
    
    return render_template(
        "admin_order.html", 
        current_user=session.get("user")[1],
        orders = orders[end_index-limit:end_index+1]
    )

@admin.route("/order/<oid>")
@login_required
def get_order_by_id(oid):
    # 請求網址：/admin/order/XXXXX
    order = Order.query.get(oid)
    return render_template(
        "admin_order.html", 
        current_user = session.get("user")[1],
        order = order
    )

@admin.route("/order/<oid>", methods=["PUT"])
@login_required
def update_order_by_id(oid):
    order = Order.query.get(oid)
    print(order)
    return redirect(f"/admin/order/{oid}")
    
