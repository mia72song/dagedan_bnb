from flask import render_template, session, request, abort

from . import admin
from .auth import login_required
from App.models import Order, OrderDetail

@admin.route("/orders")
@login_required
def get_all_orders():
    limit = 10
    try:
        page = request.args.get("page", 1)
        end_index = limit*int(page)
    except ValueError:
        abort(404)

    orders = Order.query.filter(
        Order.detail != None
    ).order_by(
        Order.create_datetime.desc()
    ).all()

    return render_template(
        "admin_order.html", 
        current_user = session.get("user")[1],
        orders = orders[end_index-limit:end_index],
        page = page
    )


@admin.route("/orders/<status>")
@login_required
def get_orders_by_status(status):
    limit = 10
    try:
        page = request.args.get("page", 1)
        end_index = limit*int(page)
    except ValueError:
        abort(404)

    status_list = ["new", "pending", "paid"]
    if status in status_list:
        orders = Order.query.filter_by(
            status=status
        ).filter(
            Order.detail != None
        ).order_by(
            Order.create_datetime.desc()
        ).all()

        return render_template(
            "admin_order.html", 
            current_user = session.get("user")[1],
            orders = orders[end_index-limit:end_index],
            page = page
        )
    else:
        abort(404)


@admin.route("/orders/search")
@login_required
def search_orders_by_keyword():
    limit = 10
    try:
        page = request.args.get("page", 1)
        end_index = limit*int(page)
    except ValueError:
        abort(404)

    orders = []
    if request.args.get("id"):
        order = Order.query.get(request.args.get("id"))
        orders = [order, ]

    elif request.args.get("phone"):
        ods = OrderDetail.query.filter_by(booker_phone=request.args.get("phone"))
        for od in ods:
            orders.insert(0, od.o)      

    elif request.args.get("checkin"):
        ods = OrderDetail.query.filter_by(check_in_date=request.args.get("checkin"))
        for od in ods:
            orders.insert(0, od.o)

    return render_template(
        "admin_order.html", 
        current_user = session.get("user")[1],
        orders = orders[end_index-limit:end_index],
        page = page
    )