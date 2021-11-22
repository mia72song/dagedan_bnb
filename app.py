from flask import *

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# 前台頁面
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/booking")
def booking():
    return render_template("booking.html")

# 管理後台頁面
@app.route("/admin/")
def admin():
    return render_template("admin.html")

def logout():
    pass

@app.route("/admin/room")
def room():
    return render_template("room.html")

@app.route("/admin/order")
def order():
    return render_template("order.html")

@app.route("/admin/guest")
def guest():
    return render_template("guest.html")

@app.route("/admin/user")
def user():
    return render_template("/user.html")

app.run()