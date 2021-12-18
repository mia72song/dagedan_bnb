from flask import jsonify
from datetime import datetime, timedelta

from . import api
from models import BookingDB
from constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

@api.route("/booked/start=<start_date_string>")
def get_booked_by_weekly_calendar(start_date_string):
    start_date = datetime.strptime(start_date_string, DATE_FORMATTER)
    end_date = start_date+timedelta(days=6)
    end_date_string = datetime.strftime(end_date, DATE_FORMATTER)
    try:
        mydb = BookingDB()
        booked_list = []
        for r in mydb.getBookedByDate(start_date_string, end_date_string):
            cols = ["date", "is_holiday", "room_no"]
            data_dict = dict(zip(cols, r))
            data_dict["date"] = datetime.strftime(data_dict["date"], DATE_FORMATTER)
            booked_list.append(data_dict)

        body = jsonify({
            "search_string": {
                "start_date": start_date_string,
                "end_date": end_date_string
            },
            "data": booked_list
            })
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