from flask import make_response
import json
from datetime import datetime, timedelta

from model.db import Mydb
from . import api
from .utils import dateFormatter, bookingDateFormatter, roomFormatter

body = None
status_code = 0

@api.route("/calendar/<search_sting>")
def get_calendar(search_sting):
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
        results = mydb.getBookingByDate(start_date_string, end_date_string)
        data_list = []
        if results:
            for r in results:
                data = bookingDateFormatter(r)
                data_list.append(data)
        
        body = json.dumps({
            "start_date":start_date_string,
            "end_date":end_date_string,
            "list": data_list
        }, ensure_ascii=False, indent=2)
        status_code = 200
            
    except Exception as e:
        body = json.dumps({
            "error": True,
            "message": f"Server Error：{e}"
        }, ensure_ascii=False, indent=2)
        status_code = 500
    
    resp = make_response(body, status_code)
    resp.headers["Content-Type"] = "application/json"
    return resp

@api.route("/rooms")
def get_rooms():
    try:
        mydb = Mydb()
        rooms = mydb.getRooms()
        room_list = []
        if rooms:
            for r in rooms:
                room_info = roomFormatter(r)
                room_list.append(room_info)
            body = json.dumps({
                "list":room_list
            }, ensure_ascii=False, indent=2)
            status_code = 200
        
        else:
            body = json.dumps({
            "error": True,
            "message": "All Rooms are Not Available"
            }, ensure_ascii=False, indent=2)
            status_code = 500
    
    except Exception as e:
        body = json.dumps({
            "error": True,
            "message": f"Server Error：{e}"
        }, ensure_ascii=False, indent=2)
        status_code = 500

    resp = make_response(body, status_code)
    resp.headers["Content-Type"] = "application/json"
    return resp