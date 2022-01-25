from flask_mail import Message
from threading import Thread
from flask import current_app, render_template

from App import mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(order_query):
    msg = Message(
        subject = f"打個蛋海旅來信：訂房編號{order_query.oid}內容及匯款通知", 
        recipients = [order_query.booker_email, ],
        sender = ("DagedanBooking", "noreply@dagedan.com"),
        reply_to = "dagedanhouse@gmail.com"
    )
    msg.html = render_template("email.html", data=order_query)

    Thread(
        target=send_async_email, 
        args=[current_app._get_current_object(), msg]
    ).start()
