from flask import jsonify, render_template, session, request
from datetime import date, timedelta, datetime

from . import admin
from .auth import login_required
from App.models import Booking, Order, Mydb, Room

@admin.route("/board")
@login_required
def board():
    today = date.today()

    new_orders = Order.query.filter(
        Order.create_datetime.between(today-timedelta(days=6), today)
    ).filter(
        Order.status != "CANCEL"
    )

    pending_orders = Order.query.filter_by(
        status="PENDING"
    ).filter(
        Order.detail!=None
    )

    today_checkin_count = 0
    for i in Booking.query.filter_by(date=today):
        if i.o.status.value=="PAID":
            today_checkin_count+=1

    try:
        mydb = Mydb()
        calendar = mydb.getCalendar(today, today+timedelta(days=6))
    except Exception as e:
        print(e)

    return render_template(
        "admin_board.html", 
        current_user = session.get("user")[1],
        calendar = calendar, 
        rooms = Room.query.filter(Room.is_available==1),
        counts = {"new": new_orders.count(), "pending": pending_orders.count(), "arrival": today_checkin_count}
    )
