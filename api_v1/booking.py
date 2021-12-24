from sys import prefix
from flask import jsonify, request
from datetime import datetime, timedelta

from . import api
from models import BookingDB
from constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

def roomNosGroupByType(room_nos):
    mydb = BookingDB()
    data_dict = {}
    for r in mydb.roomNosGetType(tuple(room_nos)):
        if r[0] not in data_dict:
            data_dict[r[0]] = [r[1], ]
        else:
            data_dict[r[0]].append(r[1])
    return data_dict   

@api.route("/booking/calendar/from<start_date_string>")
def get_booking_calendar(start_date_string):
    start_date = datetime.strptime(start_date_string, DATE_FORMATTER)
    end_date = start_date+timedelta(days=6)
    end_date_string = datetime.strftime(end_date, DATE_FORMATTER)
    try:
        mydb = BookingDB()
        data_dict = {}
        if request.args.get("guests"):
            num_of_guests = int(request.args.get("guests"))
            if 0<num_of_guests<=2:
                num_of_guests = 2
            else:
                num_of_guests = 4
            room_nos = mydb.getRoomNos(num_of_guests=num_of_guests)
        else:            
            room_nos = mydb.getRoomNos()

        booked = mydb.getBookedCalendar(start_date_string, end_date_string)
        for b in booked:
            date = datetime.strftime(b[0], DATE_FORMATTER)
            if b[4]==1:
                available_rooms = []
            else:
                if date in data_dict:
                    available_rooms = data_dict[date]["available_rooms"]
                else:
                    available_rooms = [item[0] for item in room_nos]

                if b[3] in available_rooms:
                    available_rooms.remove(b[3])

            data_dict[date] = {
                "weekday": b[1],
                "is_holiday": (b[2]==1),
                "available_rooms": available_rooms,
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