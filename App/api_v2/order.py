from flask import jsonify, request, current_app, render_template, session
from datetime import date, datetime, timedelta

from . import api
from App.models import Order, Booking, OrderDetail
from App import db, mail
from App.constants import DATE_FORMATTER

# 寄送訂房付款通知
def send_email(order_query):
    from flask_mail import Message
    from threading import Thread

    msg = Message(
        subject = f"打個蛋海旅來信：訂房編號{order_query.oid}內容及匯款通知", 
        recipients = [order_query.detail.booker_email, ],
        sender = ("DagedanBooking", "dagedanbooking@gmail.com"),
        reply_to = "dagedanbooking@gmail.com"
    )
    payment_page = f"{request.url_root}payment?oid={order_query.oid}"
    msg.html = render_template("email.html", data=order_query, link=payment_page)

    def send_async_email(app, msg):
        with app.app_context():
            mail.send(msg)

    Thread(
        target=send_async_email, 
        args=[current_app._get_current_object(), msg]
    ).start()

# 初始化response content
body = "" #json
status_code = 0

@api.route("/orders", methods=["POST"])
def create_new_order():
    data = request.get_json()
    if data:
        if session.get("captcha") is None or session.get("captcha")[0]!=data["email"] or session.get("captcha")[1]!=data["captcha"]:
            body = jsonify({
                "error": True,
                "message": "Captcha Error"
            })
            status_code = 403
            return body, status_code

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

        finally:
            del session["captcha"]
    
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
