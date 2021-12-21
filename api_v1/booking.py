from flask import jsonify
from datetime import datetime, timedelta

from . import api
from models import BookingDB
from constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0
@api.route("/booking_calendar/start=<start_date_string>&guests=<int:num_of_guests>")
def get_available_booking_calendar(start_date_string, num_of_guests):
    start_date = datetime.strptime(start_date_string, DATE_FORMATTER)
    end_date = start_date+timedelta(days=6)
    end_date_string = datetime.strftime(end_date, DATE_FORMATTER)
    if 0<num_of_guests<=2:
        num_of_guests = 2
    else:
        num_of_guests = 4
    try:
        mydb = BookingDB()
        rooms = [item[0] for item in mydb.getRoomsByAccommodate(2)]

        data_dict = {}
        results = mydb.getBookingCalendarByRoomAccommodate(start_date_string, end_date_string, num_of_guests)
        for b in results:
            date = datetime.strftime(b[0], DATE_FORMATTER)
            available_rooms = rooms.copy()
            if b[4]==1:
                available_rooms = []
            else:
                if date in data_dict:
                    available_rooms = data_dict[date]["available_rooms"]
                    available_rooms.remove(b[3])
                    continue
                
                if b[3]:
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