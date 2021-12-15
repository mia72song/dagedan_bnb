from flask import make_response
from datetime import datetime, timedelta
import json

from . import api
from model.db import Mydb
from constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

# 將由db取得的已預約日曆，整理成dict格式
def calendarFormatter(result, cols):
    data_dict = dict(zip(cols[:5], result[:5]))
    data_dict["date"] = datetime.strftime(data_dict["date"], DATE_FORMATTER)

    is_holiday = False
    if data_dict["is_holiday"]:
        is_holiday = True
    data_dict["is_holiday"] = is_holiday

    return data_dict

@api.route("/booking/start=<start_date_string>")
def get_booking_by_weekly_calendar(start_date_string):
    start_date = datetime.strptime(start_date_string, DATE_FORMATTER)
    end_date = start_date+timedelta(days=6)
    end_date_string = datetime.strftime(end_date, DATE_FORMATTER)
    try:
        mydb = Mydb()
        data, cols = mydb.getBookingListByDate(start_date_string, end_date_string)
        booked_calendar = None
        if data:
            booked_calendar = []
            for d in data:
                data_dict = calendarFormatter(d, cols)
                booked_calendar.append(data_dict)

        body = json.dumps({
            "data": booked_calendar
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

@api.route("/boking", methods=["POST"])
def create_new_booking():
    pass