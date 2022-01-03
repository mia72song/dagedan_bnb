from flask import jsonify, request
from datetime import datetime

from . import api
from models import Apidb
from constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

@api.route("/rooms")
def get_rooms():
    cols = ["room_type", "name", "accommodate", "images", "description", "rate_weekday", "rate_holiday", "single_discount"]
    try:
        mydb = Apidb()
        if request.args.get("guests"):
            results = mydb.getRoomInfoByType(num_of_guests=request.args.get("guests"))
        else:
            results = mydb.getRoomInfoByType()

        rooms = {}
        for r in results:
            room_type_string = r[0]
            room_type = dict(zip(cols[1:], r[1:]))
            if room_type["images"]:
                room_type["images"] = room_type["images"].split(", ")

            room_type["rate_weekday"] = int(room_type["rate_weekday"])
            room_type["rate_holiday"] = int(room_type["rate_holiday"])
                        
            rooms[room_type_string] = room_type
                 
        body = jsonify({"data": rooms})
        status_code = 200
        
    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code

@api.route("/rooms/<room_type>")
def get_rooms_by_type(room_type):
    cols = ["room_type", "name", "accommodate", "images", "description", "rate_weekday", "rate_holiday", "single_discount"]
    try:
        mydb = Apidb()
        results = mydb.getRoomInfoByType(room_type=room_type)
        rooms = {}
        for r in results:
            room_type_string = r[0]
            room_type = dict(zip(cols[1:], r[1:]))
            if room_type["images"]:
                room_type["images"] = room_type["images"].split(", ")

            room_type["rate_weekday"] = int(room_type["rate_weekday"])
            room_type["rate_holiday"] = int(room_type["rate_holiday"])
                        
            rooms[room_type_string] = room_type
                 
        body = jsonify({"data": rooms})
        status_code = 200
        
    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code

@api.route("/rooms/<room_type>/available/from<start_date_string>to<end_date_string>")
def check_available_room_by_type(start_date_string, end_date_string, room_type):
    try:
        mydb = Apidb()
        data_list = []
        week = mydb.getCalendar(start_date_string, end_date_string)
        min_quantity = 100
        for d in week:
            data_dict = {}
            date = datetime.strftime(d[0], DATE_FORMATTER)

            rooms = []
            if not (d[4]==1):
                rooms = [item[0] for item in mydb.getAvailableRoomNos(room_type, date)]
                min_quantity = min(min_quantity, len(rooms))
            else:
                min_quantity = 0
            
            data_dict["date"] = date
            data_dict["weekday"] = d[1]
            data_dict["is_holiday"] = (d[2]==1)
            data_dict["note"] = d[3]
            data_dict["is_closed"] = (d[4]==1)
            data_dict["available_rooms"] = rooms

            data_list.append(data_dict)

        body = jsonify({
            "room_type": room_type.capitalize(),
            "min_quantity": min_quantity,
            "data": data_list
            })
        status_code = 200

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code