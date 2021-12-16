from flask import jsonify
from datetime import datetime, timedelta

from . import api
from models import CalendarDB
from constants import DATE_FORMATTER

@api.route("/weekly_calendar/start=<start_date_string>")
def get_weekly_calendar(start_date_string):
    body = ""
    status_code = 0

    start_date = datetime.strptime(start_date_string, DATE_FORMATTER)
    end_date = start_date+timedelta(days=6)
    end_date_string = datetime.strftime(end_date, DATE_FORMATTER)
    try:
        mydb = CalendarDB()
        weekly_calendar = mydb.getCalendar(start_date_string, end_date_string)
        body = jsonify({"data": weekly_calendar})
        status_code = 200

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code