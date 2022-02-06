from flask import jsonify, request, current_app, session

from . import api

# 寄送驗證碼
def send_captcha(recipient, captcha):
    from flask_mail import Message
    from threading import Thread
    from App import mail

    msg = Message(
        subject = f"打個蛋海旅來信：訂房驗證碼", 
        recipients = [recipient, ],
        sender = ("DagedanBooking", "dagedanbooking@gmail.com"), 
        reply_to = "dagedanbooking@gmail.com"
    )
    msg.body = f"您的訂房驗證碼為：{captcha}"

    def send_async_captcha(app, msg):
        with app.app_context():
            mail.send(msg)

    Thread(
        target=send_async_captcha, 
        args=[current_app._get_current_object(), msg]
    ).start()

# 生成驗證碼
def generate_captcha(n):
    import string, random
    samples = list(string.ascii_letters+string.digits)
    captcha = random.choices(samples, k=n)
    return "".join(captcha)

# 初始化response content
body = "" #json
status_code = 0

@api.route("/captcha")
def captcha():
    if request.args["email"]:
        email = request.args["email"]
        captcha = generate_captcha(6)
        session["captcha"] = (email, captcha)
        send_captcha(recipient=email, captcha=captcha)
        body = jsonify({"ok": True})
        status_code = 200
    else:
        body = jsonify({
            "error": True,
            "message": "No EMail"
        })
        status_code = 400

    return body, status_code