from flask import jsonify, render_template, session, request, abort

from . import admin
from .auth import login_required
from App.models import Order, Mydb
from App import db

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
        abort(404)

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
        orders = orders[end_index-limit:end_index]
    )

@admin.route("/order/<oid>", methods=["GET", "PUT", "DELETE"])
@login_required
def get_order_by_id(oid):
    # 請求網址：/admin/order/XXXXX
    order = Order.query.get(oid)
    print(order.status.value)
    print(order.booked)
    print(order.payment)
    
    # 修改訂單狀態為：PAID，及修改付款資料
    if request.method == "PUT":
        update_data = request.get_json()
        update_user = session.get("user")[0]

        if order.payment and order.status.value=="PENDING":
            pass
        elif order.payment is None and order.status.value=="NEW":
            pass
        
        print(order)

    # 修改訂單狀態為：CANCEL
    elif request.method == "DELETE":
        if order.status.value=="NEW" or order.status.value=="PENDING":
            try:
                order.status = "CANCEL"
                order.update_user = session.get("user")[0]
                mydb = Mydb()
                mydb.cancelBooking()
            
            except Exception as e:
                print("資料庫錯誤：", e)
            
            finally:
                db.session.commit()
                del mydb
                
        else:
            return jsonify({"error": True, "message": f"Can Not Cancel Order:{oid}"}), 403
    
    return render_template(
        "admin_order.html", 
        current_user = session.get("user")[1],
        orders = [order, ]
    )
