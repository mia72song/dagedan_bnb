from flask import jsonify
from datetime import datetime, timedelta

from . import api
from models import BookingDB
from constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

@api.route("/booked_calendar/start=<start_date_string>")
def get_booked_calendar(start_date_string):
    '''data_dict = {
        date: {
            "weekday": "日",
            "is_holiday": bool, 
            "booked": [],
            "is_closed": bool
        }
    }'''
    start_date = datetime.strptime(start_date_string, DATE_FORMATTER)
    end_date = start_date+timedelta(days=6)
    end_date_string = datetime.strftime(end_date, DATE_FORMATTER)
    try:
        mydb = BookingDB()
        data_dict = {}
        for b in mydb.getBookedCalendar(start_date_string, end_date_string):
            date = datetime.strftime(b[0], DATE_FORMATTER)
            booked = []
            if date in data_dict:
                booked = data_dict[date]["booked"]
                booked.append(b[3])
                continue
            if b[3]:
                booked.append(b[3])

            data_dict[date] = {
                "weekday": b[1],
                "is_holiday": (b[2]==1),
                "booked": booked,
                "is_closed": (b[4]==1)
            }

        body = jsonify({"data": data_dict})
        status_code = 200

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code

@api.route("/boking", methods=["POST"])
def create_new_booking():
    pass