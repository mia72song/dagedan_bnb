import csv
from re import M

from App import db, create_app
from App.models import Calendar, User, RoomType, Booking, Room
from App.mydb import Mydb

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
    from datetime import datetime
    DATE_FORMATTER = "%Y-%m-%d"
    #app = create_app()
    #app.app_context().push()
    try:
        mydb = Mydb()
        data = mydb.getAvailableRoomNos("Double", "2022-01-30")
        print(data)
    except Exception as e:
        print(e)