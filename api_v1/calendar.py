from flask import make_response, request
import json
from datetime import datetime, timedelta

from model.db import Mydb
from . import api

@api.route("/calendar/<search_sting>")
def get_calendar(search_sting):
    status_code = 0
    booking_list = []
    dateFormatter = "%Y-%m-%d"
    slist = search_sting.split("&")
    check_in_date = (slist[0].split("="))[1]

    start_date = datetime.strptime(check_in_date, dateFormatter)
    if start_date<datetime.today():
        start_date = datetime.today()+timedelta(days=1)
        check_in_date = datetime.strftime(start_date, dateFormatter) # 轉字串

    end_date = start_date+timedelta(days=6)
    end_date = datetime.strftime(end_date, dateFormatter) # 轉字串
    try:
        mydb = Mydb()
        booking_list = mydb.getBookingByDate(check_in_date, end_date)
            
    except Exception as e:
        print("資料庫出錯了：", e)

    body = json.dumps({
        "list": booking_list
    }, ensure_ascii=False, indent=2)

    resp = make_response(body, 200)
    resp.headers["Content-Type"] = "application/json"
    return resp