from flask import jsonify, request
from datetime import datetime

from . import api
from App.models import RoomType, Calendar
from App.constants import DATE_FORMATTER
from App.mydb import Mydb

# 初始化response content
body = "" #json
status_code = 0

@api.route("/rooms")
def get_rooms():
    try:
        if request.args.get("guests"):
            try:
                num_of_guests = int(request.args.get("guests"))
                if num_of_guests<=0:
                    body = jsonify({
                        "error": True,
                        "message": f"invalid args: must greater than 0"
                    })
                    status_code = 400
                    return body, status_code

                if num_of_guests<=2:
                    num_of_guests = 2

            except ValueError:
                body = jsonify({
                    "error": True,
                    "message": f"invalid args: must be int"
                })
                status_code = 400
                return body, status_code
            
            rts = RoomType.query.filter(RoomType.accommodate<=num_of_guests).all()
        else:
            rts = RoomType.query.all()

        rooms = {}
        for rt in rts:
            room = rt.getDataDict()

            type = room["type"]
            del room["type"]

            if room["images"]:
                room["images"] = room["images"].split(", ")[:-1]

            rooms[type] = room
                 
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
    try:
        rts = RoomType.query.filter_by(type=room_type.capitalize()).all()
        rooms = {}
        for rt in rts:
            room = rt.getDataDict()

            type = room["type"]
            del room["type"]

            if room["images"]:
                room["images"] = room["images"].split(", ")[:-1]
                
            rooms[type] = room
                 
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
        week = Calendar.query.filter(Calendar.date.between(start_date_string, end_date_string))
        data_list = []
        min_quantity = 100
        for d in week:
            data_dict = {}
            date = datetime.strftime(d.date, DATE_FORMATTER)

            rooms = []
            if not (d.is_closed):
                mydb = Mydb()
                rooms = mydb.getAvailableRoomNos(room_type, date)
                min_quantity = min(min_quantity, len(rooms))
            else:
                min_quantity = 0
            
            data_dict["date"] = date
            data_dict["weekday"] = d.day
            data_dict["is_holiday"] = d.is_holiday
            data_dict["note"] = d.note
            data_dict["is_closed"] = d.is_closed
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