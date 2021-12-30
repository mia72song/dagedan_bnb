from flask import jsonify
from flask_jwt_extended import jwt_required
from datetime import datetime

from . import auth
from models import Bookings
from constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

@auth.route("/booked/start=<start_date_string>&end=<end_date_string>")
@jwt_required()
def get_booker_info_by_date(start_date_string, end_date_string):
    cols = [
        "date", "room_no", "rate", "order_id", "guest_id", 
        "booker_name", "booker_gender", "booker_phone"
    ]
    try:
        mydb = Bookings()
        booked_list = []
        for r in mydb.getBookedByDateWithBookerInfo(start_date_string, end_date_string):
            data_dict = dict(zip(cols, r))
            data_dict["date"] = datetime.strftime(data_dict["date"], DATE_FORMATTER)
            data_dict["rate"] = float(data_dict["rate"])
            booked_list.append(data_dict)

        print(booked_list)

        body = jsonify({"data": booked_list})
        status_code = 200

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code

@auth.route("/booked/oid=<int:oid>")
@jwt_required()
def get_booked_by_oid(oid):
    cols = ["date", "room_no", "room_name", "order_id"]
    try:
        mydb = BookingDB()
        booked_list = []
        for r in mydb.getBookedByOrderIdWithRoomInfo(oid):
            data_dict = dict(zip(cols, r))
            data_dict["date"] = datetime.strftime(data_dict["date"], DATE_FORMATTER)
            booked_list.append(data_dict)
        
        body = jsonify({"data": booked_list})
        status_code = 200

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code