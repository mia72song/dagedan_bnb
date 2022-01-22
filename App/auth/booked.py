from flask import jsonify
from flask_jwt_extended import jwt_required
from datetime import datetime

from . import auth
from App.models import Authdb
from App.constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

@auth.route("/booked/<oid>")
@jwt_required()
def getBookedListByOrderId(oid):
    try:
        mydb = Authdb()
        results = mydb.getBookingByOrderId(oid)
        data_list = []
        for r in results:
            cols = ["date", "room_name", "room_no", "order_id"]
            data_dict = dict(zip(cols, r))
            data_dict["date"] = datetime.strftime(data_dict["date"], DATE_FORMATTER)
            data_list.append(data_dict)
        
        body = jsonify({"data": data_list})
        status_code = 200

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code