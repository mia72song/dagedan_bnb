from flask import jsonify, request, session
from datetime import datetime

from . import admin
from App.models import Booking, Order, Mydb
from App.constants import DATETIME_FORMATTER, DATE_FORMATTER
from .auth import login_required
from App import db

@admin.route("/api/booked")
@login_required
def get_booked_list():
    if request.args.get("start") and request.args.get("end"):
        booked = Booking.query.filter(Booking.date.between(request.args.get("start"), request.args.get("end")))
        data = []
        for b in booked:
            if b.o.status.value=="PAID":
                data_dict = {}
                data_dict["date"] = datetime.strftime(b.date, DATE_FORMATTER)
                data_dict["room_no"] = b.room_no
                data_dict["order_id"] = b.order_id
                od = b.o.detail
                data_dict["booker"] = od.booker_name +" "+od.booker_gender.value
                data_dict["phone"] = od.booker_phone
                data_dict["arrival_datetime"] = datetime.strftime(od.arrival_datetime, DATETIME_FORMATTER)
                data.append(data_dict)
        
        return jsonify({"data": data})

    else:
        return jsonify({"data": None})


@admin.route("/api/order/<oid>", methods=["DELETE"])
@login_required
def cancel_order_by_id(oid):
    order = Order.query.get(oid)
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

            return jsonify({"ok": True})
        
        except Exception as e:
            return jsonify({"error": True, "message": f"伺服器內部錯誤：{e}"}), 500   
            
    else:
        return jsonify({"error": True, "message": f"拒絕「取消」。原因：編號{oid} 訂單 已付款、或已取消。"}), 400


@admin.route("/api/payment/<oid>", methods=["GET", "POST", "PUT"])
@login_required
def get_payment_by_oid(oid):
    order = Order.query.get(oid)
    if request.method=="GET": 
        if order.payment:
            payment_info = order.payment.getDataDict()
            payment_info["transfer_date"] = datetime.strftime(payment_info["transfer_date"], DATE_FORMATTER)
            return jsonify({"data": payment_info})
        
        else:
            return jsonify({"data": None})

    elif request.method=="POST":
        if order.payment:
            return jsonify({"error": True, "message": f"拒絕「新增」。原因：編號{oid} 訂單已有匯款資料。"}), 400
        else:
            pass

    elif request.method=="PUT":
        if not order.payment:
            return jsonify({"error": True, "message": f"拒絕「修改」。原因：編號{oid} 訂單尚無匯款資料。"}), 400
        else:
            pass
