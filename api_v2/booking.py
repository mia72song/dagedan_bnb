from flask import jsonify, request
from datetime import datetime, timedelta

from . import api
from models_v2 import Bookings
from constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

@api.route("/booking/calendar/from<start_date_string>")
def get_booking_calendar(start_date_string):
    start_date = datetime.strptime(start_date_string, DATE_FORMATTER)
    end_date = start_date+timedelta(days=6)
    end_date_string = datetime.strftime(end_date, DATE_FORMATTER)
    try:
        mydb = Bookings()
        if request.args.get("guests"):
            types = mydb.getRoomTypes(request.args.get("guests"))
        else:
            types = mydb.getRoomTypes()
        
        data_list = []
        week = mydb.getCalendar(start_date_string, end_date_string)
        for d in week:
            data_dict = {}
            date = datetime.strftime(d[0], DATE_FORMATTER)

            rooms = {}
            if not (d[4]==1):
                for t in types:
                    type = t[0]
                    rooms[type] = [item[0] for item in mydb.getAvailableRoomNos(type, date)]
            
            data_dict["date"] = date
            data_dict["weekday"] = d[1]
            data_dict["is_holiday"] = (d[2]==1)
            data_dict["note"] = d[3]
            data_dict["is_closed"] = (d[4]==1)
            data_dict["available_rooms"] = rooms

            data_list.append(data_dict)

        body = jsonify({"data": data_list})
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