import csv
from random import random
import sys
import os
from datetime import datetime, date, timedelta

from App.api_v2.captcha import captcha

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from App import create_app, db
from App.models import Calendar, User, Booking, Order, Room, RoomType, PaymentAtm, Mydb

def updateCalendarFromCSV(csv_file_mane):    
    with open(csv_file_mane, "r") as f:
        rows = csv.DictReader(f)
        for row in rows:
            date = row['西元日期'][:4]+"-"+row['西元日期'][4:6]+"-"+row['西元日期'][6:8]
            is_holiday = 0
            if row['是否放假']=="2":
                is_holiday = 1

            c = Calendar(date=date, day=row['星期'], is_holiday=is_holiday, note=row['備註'])
            db.session.add(c)
            db.session.commit()

'''用於更新日曆'''
# 中華民國政府行政機關辦公日曆表(csv檔)：https://data.gov.tw/dataset/14718
csv_file_mane = "111年中華民國政府行政機關辦公日曆表.csv"

if __name__=="__main__": 
    app = create_app()
    app.app_context().push()
    #db.create_all()
    today = date.today()
    mydb = Mydb()
    calendar = mydb.getCalendar(today, today+timedelta(days=6))
    print(calendar)
    