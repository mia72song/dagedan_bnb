from flask import make_response
from datetime import datetime
import json
from flask_jwt_extended import jwt_required

from . import auth
from model.db import Mydb
from constants import DATE_FORMATTER

# 將由資料庫取得的預約日曆，整理成dict格式
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
    body = ""
    status_code = 0
    try:
        mydb = Mydb()
        data, cols = mydb.getBookingListByDate(start_date_string, end_date_string)
        order_calendar = []
        if data:
            for d in data:
                order_calendar.append(calendarFormatter(d, cols))
        
        body = json.dumps({
            "data": order_calendar
        }, ensure_ascii=False, indent=2)
        status_code = 200

    except Exception as e:
        body = json.dumps({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        }, ensure_ascii=False, indent=2)
        status_code = 500

    resp = make_response(body, status_code)
    resp.headers["Content-Type"] = "application/json"
    return resp