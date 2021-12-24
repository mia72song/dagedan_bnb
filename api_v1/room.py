from flask import jsonify, request

from . import api
from models import RoomDB

# 初始化response content
body = "" #json
status_code = 0

@api.route("/rooms")
def get_rooms():
    cols = ["room_type", "name", "accommodate", "images", "description", "rate_weekday", "rate_holiday", "single_discount"]
    try:
        mydb = RoomDB()
        if request.args.get("type"):
            results = mydb.getRoomTypes(request.args.get("type"))
        else:
            results = mydb.getRoomTypes()

        rooms = {}
        for r in results:
            room_type_string = r[0]
            room_type = dict(zip(cols[1:], r[1:]))
            if room_type["images"]:
                room_type["images"] = room_type["images"].split(", ")

            room_type["rate_weekday"] = format(int(room_type["rate_weekday"]), ",")
            room_type["rate_holiday"] = format(int(room_type["rate_holiday"]), ",")
            room_type["room_nos"] = [item[0] for item in mydb.getRoomNos(room_type=room_type_string)]
                        
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

