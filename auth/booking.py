from flask import jsonify
from datetime import datetime
from flask_jwt_extended import jwt_required

from . import auth
from models import BookingDB
from constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

@auth.route("/booking/start=<start_date_string>&end=<end_date_string>")
@jwt_required()
def get_booking_by_date(start_date_string, end_date_string):
    try:
        mydb = BookingDB()
        data_list = mydb.getBookingByDateToAdmin(start_date_string, end_date_string)
        body = jsonify({"data": data_list})
        status_code = 200

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code

@auth.route("/booking/oid=<oid>")
@jwt_required()
def get_booking_by_oid(oid):
    try:
        mydb = BookingDB()
        data_list = mydb.getBookingByOrderId(oid)
        body = jsonify({"data": data_list})
        status_code = 200

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code