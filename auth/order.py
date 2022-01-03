from flask import jsonify, request
from flask_jwt_extended import jwt_required
from datetime import datetime

from . import auth
from models import Authdb
from constants import DATE_FORMATTER, DATETIME_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

# 將由db取得的訂單資料，整理成dict格式
def orderFormatter(result):
    cols = [
        "order_id", "create_datetime", "check_in_date", "check_out_date", "nights", "guests", "amount", 
        "booker_name", "booker_gender", "booker_phone", "pid", "order_status"
    ]
    data_dict = dict(zip(cols, result))
    data_dict["create_datetime"] = datetime.strftime(data_dict["create_datetime"], DATETIME_FORMATTER)
    data_dict["check_in_date"] = datetime.strftime(data_dict["check_in_date"], DATE_FORMATTER)
    data_dict["check_out_date"] = datetime.strftime(data_dict["check_out_date"], DATE_FORMATTER)
    data_dict["amount"] = int(data_dict["amount"])
    return data_dict

@auth.route("/order/<int:order_id>")
@jwt_required()
def get_order_by_id(order_id):
    try:
        mydb = Authdb()
        data_list = []
        results = mydb.getOrderById(order_id)
        for r in results:
            data_list.append(orderFormatter(r))

        body = jsonify({"data": data_list})
        status_code = 200
    
    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code

@auth.route("/orders")
@jwt_required()
def get_orders():
    try:
        mydb = Authdb()
        data_list = []
        # with data_type: phone, check_in_date
        if request.args.get("phone"):
            results = mydb.getOrdersByKeyword("phone", request.args.get("phone"))                     
        elif request.args.get("check_in_date"):
            results = mydb.getOrdersByKeyword("check_in_date", request.args.get("check_in_date"))
        else:
            results = mydb.getOrdersByStatus(status="ALL")

        for r in results:
            data_list.append(orderFormatter(r))
        body = jsonify({"data": data_list})
        status_code = 200

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code

@auth.route("/orders/<status>")
@jwt_required()
def get_orders_by_status(status):
    try:
        mydb = Authdb()
        data_list = []
        results = mydb.getOrdersByStatus(status=status.upper())

        for r in results:
            data_list.append(orderFormatter(r))
        body = jsonify({"data": data_list})
        status_code = 200

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code