from flask import make_response
from datetime import datetime
import json
from flask_jwt_extended import jwt_required

from . import auth
from model.db import Mydb

from constants import DATE_FORMATTER

# 將由資料庫取得的預約日曆資料，整理成dict格式
def calendarFormatter(result):
    data_dict = {}
    date = datetime.strftime(result[0], DATE_FORMATTER)
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

@auth.route("/order/<int:order_id>")
@jwt_required()
def get_order_by_id(order_id):
    pass

@auth.route("/orders")
@jwt_required()
def get_orders():
    pass

