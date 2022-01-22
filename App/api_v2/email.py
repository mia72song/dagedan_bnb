from flask_mail import Mail, Message
from threading import Thread
from flask import current_app

mail = Mail()

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(recipient, order_data):
    subject = "test"
    msg = Message(
        subject = subject, 
        recipients = [recipient, ],
        reply_to = "noreply@dagedan.com"
    )
    msg.body = order_data

    Thread(
        target=send_async_email, 
        args=[current_app._get_current_object(), msg]
    ).start()