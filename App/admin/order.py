from flask import render_template, session, request

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
        orders = Order.query.filter_by(
            status=request.args["status"]
        ).filter(
            Order.detail != None
        ).order_by(
            Order.create_datetime.desc()
        ).all()
    else:
        orders = Order.query.filter(
            Order.detail != None
        ).order_by(
            Order.create_datetime.desc()
        ).all()
    
    return render_template(
        "admin_order.html", 
        current_user=session.get("user")[1],
        orders = orders[end_index-limit:end_index+1]
    )

@admin.route("/order/<oid>", methods=["GET", "PUT", "DELETE"])
@login_required
def get_order_by_id(oid):
    # 請求網址：/admin/order/XXXXX
    order = Order.query.get(oid)
    print(order.status.value)
    print(order.booked)
    print(order.payment)
    
    # 修改訂單狀態為：PAID，及付款資料
    if request.method == "PUT":
        update_data = request.get_json()
        update_user = session.get("user")[0]
        print(order)

    # 修改訂單狀態為：CANCEL
    elif request.method == "DELETE":
        pass
    
    return render_template(
        "admin_order.html", 
        current_user = session.get("user")[1],
        orders = [order, ]
    )
