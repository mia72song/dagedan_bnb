from flask import jsonify, request
from datetime import datetime, timedelta

from . import api
from models import Guests
from models import Orders
from constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

@api.route("/orders", methods=["POST"])
def create_new_order():
    data = request.get_json()
    if data:
        try:
            g = Guests()
            gender = "M"
            if data["gender"]=="female" : gender = "F"
            g.createGuest(data["name"], gender, data["phone"], data["email"])

            o = Orders()
            oid = o.createOrder(data["check_in_date"], data["check_out_date"], data["nights"], data["num_of_guests"], data["amount"], data["phone"], data["arrival_datetime"], booking=data["booking"])
            
            body = jsonify({
                "ok": True,
                "oid": oid
                })
            status_code = 200
        
        except Exception as e:
            body = jsonify({
                "error": True,
                "message": f"伺服器內部錯誤：{e}"
            })
            status_code = 500
        
        finally:
            del g
            del o
    
    else:
        body = jsonify({
            "error": True,
            "message": "No Json Data"
        })
        status_code = 400

    return body, status_code

@api.route("/order/<oid>")
def getOrderById(oid):
    try:
        o = Orders()
        data = o.getOrderById(oid)
        amount = data[2]
        deadline = datetime.strftime(data[-1], DATE_FORMATTER)
        
        body = jsonify({
            "data": {
                "amount": amount,
                "deadline": deadline
            }
        })
        status_code = 200

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code