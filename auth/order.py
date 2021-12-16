from flask import jsonify
from datetime import datetime
from flask_jwt_extended import jwt_required

from . import auth
from models import OrderDB

# 初始化response content
body = "" #json
status_code = 0

@auth.route("/order/<int:order_id>")
@jwt_required()
def get_order_by_id(order_id):
    try:
        mydb = OrderDB()
        data_list = mydb.getOrderById(order_id)        
        body = jsonify({"data": data_list})
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
        data_list = mydb.getOrdersByDataType([data_type, keyword.upper()])
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
        data_list = mydb.getOrdersByDataType()
        body = jsonify({"data": data_list})
        status_code = 200

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code

