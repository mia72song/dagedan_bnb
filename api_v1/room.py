from flask import jsonify

from . import api
from models import RoomDB

# 初始化response content
body = "" #json
status_code = 0

@api.route("/rooms")
def get_all_rooms():
    try:
        mydb = RoomDB()
        body = jsonify({"data": mydb.getRooms()})
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
