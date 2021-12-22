from flask import jsonify
from datetime import datetime, timedelta

from . import api
from models import BookingDB
from constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0
@api.route("/booked_calendar/start=<start_date_string>&guests=<int:num_of_guests>")
def get_booked_calendar(start_date_string, num_of_guests):
    start_date = datetime.strptime(start_date_string, DATE_FORMATTER)
    end_date = start_date+timedelta(days=6)
    end_date_string = datetime.strftime(end_date, DATE_FORMATTER)
    if 0<num_of_guests<=2:
        num_of_guests = 2
    else:
        num_of_guests = 4
    try:
        mydb = BookingDB()
        data_dict = {}
        results = mydb.getBookedCalendarByRoomAccommodate(start_date_string, end_date_string, num_of_guests)
        for r in results:
            booked = []
            date = datetime.strftime(r[0], DATE_FORMATTER)
            if date in data_dict:
                booked = data_dict[date]["booked"]
                booked.append(r[3])
                continue
            
            if r[3]:
                booked.append(r[3])
            
            data_dict[date] = {
                "weekday": r[1],
                "is_holiday": (r[2]==1),
                "booked": booked,
                "is_closed": (r[4]==1)
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