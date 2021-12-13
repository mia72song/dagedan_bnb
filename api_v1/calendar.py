from flask import make_response
from datetime import datetime, timedelta
import json

from . import api
from model.db import Mydb
from constants import DATE_FORMATTER

# 將由資料庫取得的預約日曆，整理成dict格式
def calendarFormatter(result):
    cols = ["date", "weekday", "is_holiday", "note"]
    data_dict = dict(zip(cols, result))
    data_dict["date"] = datetime.strftime(data_dict["date"], DATE_FORMATTER)

    is_holiday = False
    if data_dict["is_holiday"]:
        is_holiday = True
    data_dict["is_holiday"] = is_holiday

    return data_dict

@api.route("/weekly_calendar/start=<start_date_string>")
def get_weekly_calendar(start_date_string):
    body = ""
    status_code = 0

    start_date = datetime.strptime(start_date_string, DATE_FORMATTER)
    end_date = start_date+timedelta(days=6)
    end_date_string = datetime.strftime(end_date, DATE_FORMATTER)
    try:
        mydb = Mydb()
        data = mydb.getCalendar(start_date_string, end_date_string)
        weekly_calendar = []
        for d in data:
            weekly_calendar.append(calendarFormatter(d))

        body = json.dumps({
            "data": weekly_calendar
        }, ensure_ascii=False, indent=2)
        status_code = 200

    except Exception as e:
        print(e)
        body = json.dumps({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        }, ensure_ascii=False, indent=2)
        status_code = 500

    resp = make_response(body, status_code)
    resp.headers["Content-Type"] = "application/json"
    return resp