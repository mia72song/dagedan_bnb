from flask import jsonify
from datetime import datetime, timedelta

from model.db import Mydb
from . import api

dateFormatter = "%Y-%m-%d"

@api.route("/calendar/<search_sting>")
def get_calendar(search_sting):
    status_code = 0
    booking_list = []

    slist = search_sting.split("&")
    start_date_string = (slist[0].split("="))[1]
    
    # 檢查start_date是否早於今天日期，是則以明天為start_date
    start_date = datetime.strptime(start_date_string, dateFormatter)
    if datetime.strptime(start_date_string, dateFormatter)<=datetime.today():
        start_date = datetime.today()+timedelta(days=1)
        start_date_string = datetime.strftime(start_date, dateFormatter)

    end_date = start_date+timedelta(days=6)
    end_date_string = datetime.strftime(end_date, dateFormatter)
    try:
        mydb = Mydb()
        booking_list = mydb.getBookingByDate(start_date_string, end_date_string)
        status_code = 200
        body = {
            "list": booking_list
        }
            
    except Exception as e:
        status_code = 500
        body = {
            "error": True,
            "message": f"Server Error：{e}"
        }
    
    return jsonify(body), status_code