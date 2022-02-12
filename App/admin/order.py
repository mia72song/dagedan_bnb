from flask import render_template, session, request, abort

from . import admin
from .auth import login_required
from App.models import Order, OrderDetail

@admin.route("/orders")
@login_required
def get_all_orders():
    limit = 10
    try:
        page = request.args.get("page", 1)
        end_index = limit*int(page)
    except ValueError:
        abort(404)

    orders = Order.query.filter(
        Order.detail != None
    ).order_by(
        Order.create_datetime.desc()
    ).all()

    return render_template(
        "admin_order.html", 
        current_user = session.get("user")[1],
        orders = orders[end_index-limit:end_index]
    )

@admin.route("/orders/<status>")
@login_required
def get_orders_by_status(status):
    limit = 10
    try:
        page = request.args.get("page", 1)
        end_index = limit*int(page)
    except ValueError:
        abort(404)

    status_list = ["new", "pending", "paid"]
    if status in status_list:
        orders = Order.query.filter_by(
            status=status
        ).filter(
            Order.detail != None
        ).order_by(
            Order.create_datetime.desc()
        ).all()

        return render_template(
            "admin_order.html", 
            current_user = session.get("user")[1],
            orders = orders[end_index-limit:end_index]
        )
    else:
        abort(404)
'''
@admin.route("/orders/id=<oid>", methods=["GET", "DELETE"])
@login_required
def get_order_by_id(oid):
    # 請求網址：/admin/order/XXXXX
    order = Order.query.get(oid)
    if not order:
        abort(404)
    
    # 修改訂單狀態為：CANCEL
    if request.method == "DELETE":
        if order.status.value=="NEW" or order.status.value=="PENDING":
            try:
                order.status = "CANCEL"
                order.update_user = session.get("user")[0]
                if order.payment:
                    order.payment.is_del = 1
                
                mydb = Mydb()
                mydb.cancelBooking()                
                del mydb
                
                db.session.commit()
            
            except Exception as e:
                return jsonify({"error": True, "message": f"伺服器內部錯誤：{e}"}), 500   
                
        else:
            return jsonify({"error": True, "message": f"拒絕「取消」。原因：編號{oid} 訂單 已付款、或已取消。"}), 400
    
    return render_template(
        "admin_order.html", 
        current_user = session.get("user")[1],
        orders = [order, ]
    )
'''
@admin.route("/orders/search")
@login_required
def search_orders_by_keyword():
    orders = []
    if request.args.get("id"):
        order = Order.query.get(request.args.get("id"))
        orders = [order, ]

    elif request.args.get("phone"):
        ods = OrderDetail.query.filter_by(booker_phone=request.args.get("phone"))
        for od in ods:
            orders.insert(0, od.o)      

    elif request.args.get("checkin"):
        ods = OrderDetail.query.filter_by(check_in_date=request.args.get("checkin"))
        for od in ods:
            orders.insert(0, od.o)

    return render_template(
        "admin_order.html", 
        current_user = session.get("user")[1],
        orders = orders
    )