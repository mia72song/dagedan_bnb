from os import access
from flask import make_response, session, request
from datetime import datetime, timedelta
import json
from flask_jwt_extended import jwt_required

from . import admin
from model.db import Mydb
from flask import session

# 將由資料庫取得的預約日曆資料，整理成dict格式
def calendarFormatter(result):
    data_dict = {}
    dateFormatter = "%Y-%m-%d"
    date = datetime.strftime(result[0], dateFormatter)
    bid = date+"-"+result[1]
    order_data = list(result[2:])
    cols = ["order_id", "booker_name", "gender", "phone"]    
    order_dict = dict(zip(cols, order_data))

    gender = "先生"
    if order_dict["gender"]=="F":
        gender = "小姐"
    order_dict["gender"] = gender

    data_dict["bid"] = bid
    data_dict.update(order_dict)

    return data_dict


@admin.route("/orders/start=<start_date_string>&end=<end_date_string>")
@jwt_required()
def get_orders_by_date(start_date_string, end_date_string):
    body = ""
    status_code = 0
    try:
        mydb = Mydb()
        data = mydb.getOrdersByDate(start_date_string, end_date_string)
        order_calendar = []
        for d in data:
            order_calendar.append(calendarFormatter(d))
        
        body = json.dumps({
            "data": order_calendar
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

@admin.route("/order/<int:order_id>")
@jwt_required()
def get_order_by_id(order_id):
    pass

@admin.route("/orders")
@jwt_required()
def get_orders():
    pass

