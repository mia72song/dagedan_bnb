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
        status_list = ["new", "pending", "paid"]
        if request.args.get("status") in status_list:
            orders = Order.query.filter_by(
                status=request.args["status"]
            ).filter(
                Order.detail != None
            ).order_by(
                Order.create_datetime.desc()
            ).all()
        else:
            abort(404)
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

@admin.route("/order/<oid>", methods=["GET", "DELETE"])
@login_required
def get_order_by_id(oid):
    # 請求網址：/admin/order/XXXXX
    order = Order.query.get(oid)        
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
