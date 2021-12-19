import csv
from datetime import datetime

import sys
sys.path.append("..")

from models.db import Mydb
from constants import DATE_FORMATTER

class CalendarDB(Mydb):
    def getCalendar(self, start_date_string, end_date_string):
        cols = ["date", "weekday", "is_holiday", "note"]
        sql = f"SELECT * FROM calendar WHERE date<='{end_date_string}' AND date>='{start_date_string}'"
        self.cur.execute(sql)
        results = self.cur.fetchall()
        if results:
            data_list = []
            for r in results:
                data_dict = dict(zip(cols, r))
                data_dict["date"] = datetime.strftime(data_dict["date"], DATE_FORMATTER)
                data_list.append(data_dict)
            return data_list
        else:
            return None

    def updateCalendarFromCSV(self, csv_file_mane):
        with open(csv_file_mane, "r") as f:
            rows = csv.DictReader(f)
            for row in rows:
                sql = ""
                date = row['西元日期'][:4]+"-"+row['西元日期'][4:6]+"-"+row['西元日期'][6:8]
                is_holiday = 0
                if row['是否放假']=="2":
                    is_holiday = 1
                sql = f"INSERT INTO calendar VALUES ('{date}', '{row['星期']}',{is_holiday}, '{row['備註']}')"
                self.cur.execute(sql)
                self.conn.commit()

'''用於更新日曆'''
# 中華民國政府行政機關辦公日曆表(csv檔)：https://data.gov.tw/dataset/14718
csv_file_mane = "111年中華民國政府行政機關辦公日曆表.csv"

if __name__=="__main__": 
    import pymysql
    try:
        mydb = CalendarDB()
        mydb.updateCalendarFromCSV(csv_file_mane)
        print(f"{csv_file_mane}已更新入資料庫")
    except pymysql.err.IntegrityError:
        print(f"Woop!!!{csv_file_mane}已存在資料庫中")
    except Exception as e:
        print(f"其他資料庫錯誤：", e)
    finally:
        del mydb