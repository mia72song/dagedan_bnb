from flask import jsonify
from flask_jwt_extended import jwt_required
from datetime import datetime

from . import auth
from models import Orders
from constants import DATE_FORMATTER, DATETIME_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

# 將由db取得的訂單資料，整理成dict格式
def orderFormatter(result):
    cols = [
            "order_id", "create_datetime", "booker_name", "booker_gender", "booker_phone",
            "check_in_date", "check_out_date", "nights", "guests", "amount", "order_status",
            "add_on_order_id", "payment_id"
        ]
    data_dict = dict(zip(cols, result))
    data_dict["create_datetime"] = datetime.strftime(data_dict["create_datetime"], DATETIME_FORMATTER)
    data_dict["check_in_date"] = datetime.strftime(data_dict["check_in_date"], DATE_FORMATTER)
    data_dict["check_out_date"] = datetime.strftime(data_dict["check_out_date"], DATE_FORMATTER)
    data_dict["amount"] = float(data_dict["amount"])
    return data_dict

@auth.route("/order/<int:order_id>")
@jwt_required()
def get_order_by_id(order_id):
    try:
        mydb = OrderDB()
        data_dict = orderFormatter(mydb.getOrderById(order_id))
        body = jsonify({"data": [data_dict, ]})
        status_code = 200

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code

@auth.route("/orders/<data_type>=<keyword>")
@jwt_required()
def get_orders_by_keyword(data_type, keyword):
    # data_type: status, phone, check_in_date
    try:
        mydb = OrderDB()
        data_list = []
        for r in mydb.getOrdersByDataType([data_type, keyword.upper()]):
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
def get_all_orders():
    try:
        mydb = OrderDB()
        data_list = []
        for r in mydb.getOrdersByDataType():
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

