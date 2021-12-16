from flask import jsonify
from datetime import datetime
from flask_jwt_extended import jwt_required

from . import auth
from models import BookingDB
from constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

# 將由db取得的預約日曆，整理成dict格式
def calendarFormatter(result, cols):
    cols = cols[:3]+cols[6:]
    result = result[:3]+result[6:]
    order_dict = dict(zip(cols, result))
    order_dict["date"] = datetime.strftime(order_dict["date"], DATE_FORMATTER)
    
    data_dict = {}
    data_dict["bid"] = order_dict["date"]+"-"+order_dict["room_no"]
    data_dict.update(order_dict)

    return data_dict

@auth.route("/booking/start=<start_date_string>&end=<end_date_string>")
@jwt_required()
def get_booking_by_date(start_date_string, end_date_string):
    try:
        mydb = BookingDB()
        data, cols = mydb.getBookingListByDate(start_date_string, end_date_string)
        order_calendar = []
        if data:
            for d in data:
                order_calendar.append(calendarFormatter(d, cols))
        
        body = jsonify({"data": order_calendar})
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
def get_booking_list_by_oid(oid):
    # cols = ["date", "room_no", "room_name", "room_type"]
    try:
        mydb = BookingDB()
        results, cols = mydb.getBookingListByOrderId(oid)
        data = []
        if results:            
            for r in results:
                data_dict = dict(zip(cols, r))
                data_dict["date"] = datetime.strftime(data_dict["date"], DATE_FORMATTER)
                data.append(data_dict)
        body = jsonify({"data": data})
        status_code = 200

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code