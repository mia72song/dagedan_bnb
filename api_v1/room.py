import re
from flask import jsonify

from . import api
from models import RoomDB

cols = [
    "room_no", "room_name", "room_type", 
    "accommodate", "rate_weekday", "rate_holiday", "single_discount", "discribe", "images", "is_available"
]
# 初始化response content
body = "" #json
status_code = 0

@api.route("/rooms")
def get_all_rooms():
    try:
        mydb = RoomDB()
        results = mydb.getRooms()
        room_list = []
        for r in results:
            data_dict = dict(zip(cols, r))
            data_dict["rate_weekday"] = float(data_dict["rate_weekday"])
            data_dict["rate_holiday"] = float(data_dict["rate_holiday"])
            room_list.append(data_dict)
        
        body = jsonify({"data": room_list})
        status_code = 200
    
    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code

@api.route("/available_rooms/<date_type>")
# route params: "holiday", "weekday"
def get_available_rooms(date_type):
    try:
        mydb = RoomDB()
        if date_type=="holiday":
            results = mydb.getAvailableRoomsByDateType(is_holiday=True)
        elif date_type=="weekday":
            results = mydb.getAvailableRoomsByDateType(is_holiday=False)
        else:
            return jsonify({"data": None}), 404

        room_list = []
        for r in results:
            cols = [
                "room_no", "room_name", "room_type", 
                "accommodate", "rate", "single_discount", "discribe", "images", "is_available"
            ]
            data_dict = dict(zip(cols, r))
            data_dict["rate"] = float(data_dict["rate"])
            del data_dict["is_available"]
            room_list.append(data_dict)
                 
        body = jsonify({"data": room_list})
        status_code = 200
        
    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code

@api.route("/room/<type>")
def get_room(type):
    pass
