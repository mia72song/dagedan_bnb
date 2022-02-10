from flask import jsonify, request
from datetime import date, datetime

from . import api
from App.models import Order, PaymentAtm, Mydb
from App import db

# 初始化response content
body = "" #json
status_code = 0

@api.route("/payment/<oid>", methods=["POST"])
def createPayment(oid):
    data = request.get_json()
    if data:
        try:
            order = Order.query.get(oid)
            if order and order.payment_id is None:
                pid = f"A{int(datetime.timestamp(datetime.now()))}"
                payment = PaymentAtm(pid=pid)
                payment.bank = data["bank"]
                payment.account_no = data["account_no"]
                payment.name = data["account_name"]
                payment.amount = data["amount"]
                payment.transfer_date = data["transfer_date"]

                order.payment = payment                
                order.status = "PENDING"
                order.update_user = payment.update_user = "guest"
                
                db.session.commit()

                body = jsonify({"ok": True})
                status_code = 200
            else:
                body = jsonify({
                    "error": True,
                    "message": "Invalid Order"
                })
                status_code = 400
        except Exception as e:
            body = jsonify({
                "error": True,
                "message": f"伺服器內部錯誤：{e}"
            })
            status_code = 500
    else:
        body = jsonify({
            "error": True,
            "message": "No Json Data"
        })
        status_code = 400
        
    return body, status_code

@api.route("/payment/<oid>", methods=["GET"])
def getPayment(oid):
    try:
        order = Order.query.get(oid)
        if not order:
            body = jsonify({
                "error": True,
                "message": "Invalid Order"
            })
            status_code = 404

        # 未過超過付款期限，回應：付款連結有效
        elif date.today()<=order.payment_deadline and order.status.value=="NEW" and order.payment_id is None:
            body = jsonify({"ok": True})
            status_code = 200        
        
        else:
            #超過付款期限，更新狀態為「CANCEL」
            if date.today()>order.payment_deadline and order.status.value=="NEW" and order.payment_id is None:
                mydb = Mydb()
                mydb.updateStatus()
                mydb.cancelBooking()
                del mydb            
            #回應：付款連結無效
            body = jsonify({
                "expired":True, 
                "message": "Expired Order"
            })
            status_code = 403

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code