from flask import make_response, session
from datetime import datetime, timedelta
import json

from . import api
from model.db import Mydb
from .utils import dateFormatter

@api.route("/booking/start=<start_date_string>&end=<end_date_string>")
def get_booking_by_date(start_date_string, end_date_string):
    body = ""
    status_code = 0
    try:
        mydb = Mydb()
        data = mydb.getBookingByDate(start_date_string, end_date_string)
        if data:
            data = list(data)
            for i in range(len(data)):
                d = list(data[i])
                d[0] = datetime.strftime(d[0], dateFormatter)
                del d[2]
                
                data[i] = d
        
        body = json.dumps({
            "data": data
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

@api.route("/boking", methods=["POST"])
def create_new_booking():
    pass