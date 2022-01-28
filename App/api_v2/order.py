from flask import jsonify, request
from datetime import date, datetime, timedelta

from . import api
from App.models import Order, Booking, OrderDetail
from App import db
from App.constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

@api.route("/orders", methods=["POST"])
def create_new_order():
    data = request.get_json()
    if data:
        try:
            oid = int(datetime.timestamp(datetime.now()))
            order = Order(oid=oid)
            
            detail = OrderDetail()
            detail.check_in_date = data["check_in_date"]
            detail.check_out_date = data["check_out_date"]
            detail.nights = data["nights"]
            detail.num_of_guests = data["num_of_guests"]
            detail.room_type = data["room_type"]
            detail.room_quantity = data["quantity"]
            detail.booker_name = data["name"]

            gender = "M"
            if data["gender"]=="female" : gender = "F"
            detail.booker_gender = gender

            detail.booker_phone = data["phone"]
            detail.booker_email = data["email"]
            detail.arrival_datetime = data["arrival_datetime"]

            order.detail = detail
            order.amount = data["amount"]
            order.payment_deadline = date.today()+timedelta(days=1)
            order.update_user = "guest"
            
            for b in data["booking"]:
                booking_list = b.split("_")
                booking = Booking(date=booking_list[0], room_no=booking_list[1])
                order.booked.append(booking)
                
            db.session.add(order)  
            db.session.commit()

            from .email import send_email
            send_email(order)
            
            body = jsonify({
                "ok": True,
                "oid": oid
                })
            status_code = 200
        
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

@api.route("/order/<oid>")
def getOrderById(oid):
    try:
        order = Order.query.get(oid)
        if not order:
            body = jsonify({
                "error": True,
                "message": "Invalid Order"
            })
            status_code = 403
        else:           
            body = jsonify({
                "ok": True, 
                "data": {
                    "amount": order.amount,
                    "deadline": datetime.strftime(order.payment_deadline, DATE_FORMATTER)
                }
            })
            status_code = 200

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code
