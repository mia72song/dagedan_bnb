from flask import make_response
import json

from model.db import Mydb
from . import api

# 將由資料庫取得的房間資訊，整理成dict格式
def roomFormatter(result):
    cols = ["room_no", "name", "type", "accommodate", "rate_weekday", "rate_holiday", "single_discount"]
    data_dict = dict(zip(cols, result))
    data_dict["rate_weekday"] = float(data_dict["rate_weekday"])
    data_dict["rate_holiday"] = float(data_dict["rate_holiday"])
    return data_dict

body = None
status_code = 0

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