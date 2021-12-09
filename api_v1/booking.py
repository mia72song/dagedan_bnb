from flask import make_response
from datetime import datetime, timedelta
import json

from . import api
from model.db import Mydb
from utils import dateFormatter

# 將由資料庫取得的預約日曆資料，整理成dict格式
def calendarFormatter(result):
    cols = ["date", "booked", "weekday", "is_holiday", "note"]
    data_dict = dict(zip(cols, result))
    data_dict["date"] = datetime.strftime(data_dict["date"], dateFormatter)

    is_holiday = False
    if data_dict["is_holiday"]:
        is_holiday = True
    data_dict["is_holiday"] = is_holiday

    return data_dict

@api.route("/booking/start=<start_date_string>")
def get_booking_by_weekly_calendar(start_date_string):
    start_date = datetime.strptime(start_date_string, dateFormatter)
    end_date = start_date+timedelta(days=6)
    end_date_string = datetime.strftime(end_date, dateFormatter)
    body = ""
    status_code = 0
    try:
        mydb = Mydb()
        data = mydb.getBookingByDate(start_date_string, end_date_string)
        booked_calendar = []
        for d in data:
            if d:
                date_dict = calendarFormatter(d)
                booked_calendar.append(date_dict)

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