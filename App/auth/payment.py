from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

from . import auth
from App.models import Authdb
from App.constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

@auth.route("/payment/<pid>")
@jwt_required()
def get_payment(pid):
    cols = ["pid", "bank", "account_no", "name", "amount", "update_datetime", "current_user", "transfer_date"]
    try:
        mydb = Authdb()
        result = mydb.getPaymentById(pid)
        data_dict = dict(zip(cols, result))
        data_dict["amount"] = float(data_dict["amount"])
        data_dict["transfer_date"] = datetime.strftime(data_dict["transfer_date"], DATE_FORMATTER)
        del data_dict["update_datetime"]
        del data_dict["current_user"]

        body = jsonify({"data": data_dict})
        status_code = 200
        
    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code

@auth.route("/payment/<int:order_id>", methods=["POST"])
@jwt_required()
def create_payment(order_id):
    if get_jwt_identity():
        current_username = get_jwt_identity()
        data = request.get_json()
    else:
        body = jsonify({
            "error": True,
            "message": {"login": False}
        })
        status_code = 403
        return body, status_code

    if data:
        try:
            mydb = Authdb()
            pid, msg = mydb.createPayment(current_username, order_id, data["bank"], data["account_no"], data["name"], data["amount"], data["transfer_date"])
            if msg=="ok":
                body = jsonify({
                    "ok": (msg=="ok"),
                    "pid": pid
                    })
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

@auth.route("/payment/<pid>", methods=["PUT"])
@jwt_required()
def update_payment(pid):
    if get_jwt_identity():
        current_username = get_jwt_identity()
        data = request.get_json()
    else:
        body = jsonify({
            "error": True,
            "message": {"login": False}
        })
        status_code = 403
        return body, status_code
        
    if data:
        try:
            mydb = Authdb()
            msg = mydb.updatePayment(current_username, pid, bank=data.get("bank"), account_no=data.get("account_no"), name=data.get("name"), amount=data.get("amount"), transfer_date=data.get("transfer_date"))            
            if msg=="ok":            
                body = jsonify({
                    "ok": (msg=="ok")
                })
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