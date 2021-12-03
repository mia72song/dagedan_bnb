from flask import make_response, request
import json
from datetime import datetime, timedelta

from model.db import Mydb
from . import api

@api.route("/calendar/<search_sting>")
def get_calendar(search_sting):
    status_code = 0
    data = ""
    dateFormatter = "%Y-%m-%d"
    slist = search_sting.split("&")
    check_in_date = (slist[0].split("="))[1]
    check_out_date = (slist[1].split("="))[1]
    adults = int((slist[2].split("="))[1])
    kids = int((slist[3].split("="))[1])

    today = datetime.today()

    start_date = datetime.strptime(check_in_date, dateFormatter)
    end_date = start_date+timedelta(days=6)
    end_date = datetime.strftime(end_date, dateFormatter) # 轉字串
    try:
        mydb = Mydb()
        data = mydb.getBookingByDate(check_in_date, end_date)
            
    except Exception as e:
        print("資料庫出錯了：", e)


    body = json.dumps({
        "list": data
    }, ensure_ascii=False, indent=2)

    resp = make_response(body, 200)
    resp.headers["Content-Type"] = "application/json"
    return resp