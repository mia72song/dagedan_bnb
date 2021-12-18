from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

from . import auth
from models import PaymentDB
from constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

@auth.route("/payment/<pid>")
@jwt_required()
def get_payment(pid):
    cols = ["pid", "bank", "account_no", "name", "amount", "update_datetime", "current_user", "transfer_date"]
    try:
        mydb = PaymentDB()
        result = mydb.getPaymentById(pid)
        data_dict = dict(zip(cols, result))
        data_dict["amount"] = float(data_dict["amount"])
        data_dict["transfer_date"] = datetime.strftime(data_dict["transfer_date"], DATE_FORMATTER)
        del data_dict["update_datetime"]
        del data_dict["current_user"]

        body = jsonify({"data": [data_dict, ]})
        status_code = 200
        
    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code

@auth.route("/payment", methods=["POST"])
@jwt_required()
def create_payment():
    if get_jwt_identity():
        current_username = get_jwt_identity()
        create_data = request.get_json()
    else:
        body = jsonify({
            "error": True,
            "message": {"login": False}
        })
        status_code = 403
        return body, status_code

    if create_data:
        try:
            mydb = PaymentDB()
            result, msg = mydb.createPayment(create_data, current_username)
            if result:
                body = jsonify({"ok": True})
                status_code = 200
            else:
                body = jsonify({
                    "error": True,
                    "message": msg
                })
                status_code = 500
        except Exception as e:
            body = jsonify({
                "error": True,
                "message": f"伺服器內部錯誤：{e}"
            })
            status_code = 500
        finally:
            del mydb
    else:
        body = jsonify({
            "error": True,
            "message": "No Json Data"
        })
        status_code = 400

    return body, status_code

@auth.route("/payment", methods=["PUT"])
@jwt_required()
def update_payment():
    if get_jwt_identity():
        current_username = get_jwt_identity()
        update_data = request.get_json()
    else:
        body = jsonify({
            "error": True,
            "message": {"login": False}
        })
        status_code = 403
        return body, status_code
        
    if update_data:
        try:
            mydb = PaymentDB()
            mydb.updatePayment(update_data, current_username)
            body = jsonify({"ok": True})
            status_code = 200
        except Exception as e:
            body = jsonify({
                "error": True,
                "message": f"伺服器內部錯誤：{e}"
            })
            status_code = 500
        finally:
            del mydb
    else:
        body = jsonify({
            "error": True,
            "message": "No Json Data"
        })
        status_code = 400
    
    return body, status_code