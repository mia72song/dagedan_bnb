from flask import make_response
import json

from . import api
from model.db import Mydb

# 將由資料庫取得的房間，整理成dict格式
def roomFormatter(result):
    cols = ["room_no", "name", "type", "accommodate", "rate_weekday", "rate_holiday", "single_discount", "discribe", "images"]
    data_dict = dict(zip(cols, result))
    data_dict["rate_weekday"] = float(data_dict["rate_weekday"])
    data_dict["rate_holiday"] = float(data_dict["rate_holiday"])
    return data_dict

@api.route("/rooms")
def get_all_rooms():
    body = ""
    status_code = 0
    try:
        mydb = Mydb()
        data = mydb.getRooms()
        room_list = []
        for d in data:
            room = roomFormatter(d)
            room_list.append(room)
        
        body = json.dumps({
            "data":room_list
        }, ensure_ascii=False, indent=2)
        status_code = 200
    
    except Exception as e:
        body = json.dumps({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        }, ensure_ascii=False, indent=2)
        status_code = 500

    resp = make_response(body, status_code)
    resp.headers["Content-Type"] = "application/json"
    return resp

@api.route("/room/<type>")
def get_room(type):
    pass
