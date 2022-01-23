from flask import current_app, render_template
from flask_mail import Message
from threading import Thread

from App import mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(oid, order_data:dict, booked_list:list):
    subject = f"打個蛋海旅來信：訂房編號：{oid}內容及匯款通知"
    msg = Message(
        subject = subject, 
        recipients = [order_data.get("booker_email")],
        sender = ("noreply", "noreply@dagedan.com"), 
        reply_to = "dagedanhouse@gmail.com"
    )
    msg.html = render_template("email.html", oid=oid, data=order_data, booked_list=booked_list)

    Thread(
        target = send_async_email, 
        args = [current_app._get_current_object(), msg]
    ).start()