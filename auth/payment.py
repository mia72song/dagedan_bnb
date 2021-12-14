from flask import jsonify
from datetime import datetime
from flask_jwt_extended import jwt_required

from . import auth
from model.db import Mydb
from constants import DATE_FORMATTER, DATETIME_FORMATTER

payment_dict = {
    "pid": "", 
    "bank": "",
    "account_no": "",
    "name": "",
    "amount": 0,
    "transfer_date": "",
    "current_user": ""
}

def paymentFormatter(result):
    cols = ["pid", "bank", "account_no", "name", "amount", "update_datetime", "current_user", "transfer_date"]
    data_dict = dict(zip(cols, result))
    data_dict["amount"] = float(data_dict["amount"])
    del data_dict["update_datetime"]
    del data_dict["current_user"]

    return data_dict    

@auth.route("/payment/<pid>")
#@jwt_required()
def getPayment(pid):
    body = ""
    status_code = 0
    try:
        mydb = Mydb()
        data = list(mydb.getPaymentById(pid))
        body = jsonify({"data": paymentFormatter(data)})
        status_code = 200
    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code

@auth.route("/payment/<pid>", methods=["POST"])
#@jwt_required()
def createPayment(pid):
    pass

@auth.route("/payment/<pid>", methods=["PUT"])
#@jwt_required()
def updatePayment(pid):
    pass