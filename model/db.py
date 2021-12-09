import pymysql
import os
from werkzeug.security import generate_password_hash, check_password_hash
import csv
from dotenv import load_dotenv
load_dotenv()

db_info = {
    "host": os.getenv("DB_HOST", default="localhost"),
    "port": 3306,
    "user": os.getenv("DB_USER", default="root"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASE"),
    "charset": "utf8"
}

class Mydb:
    def __init__(self, db_info=db_info):
        try:
            self.conn = pymysql.connect(
                host=db_info["host"],
                port=db_info["port"],
                user=db_info["user"],
                password=db_info["password"],
                database=db_info["database"],
                charset=db_info["charset"]
            )
        except Exception as e:
            print("資料庫連線發生錯誤囉，", e)

        self.cur = self.conn.cursor()
        print("資料庫已開啟…")

    def getUser(self, username, password):
        sql = f"SELECT username, password, staff_name FROM users WHERE username='{username}' and is_del=0"
        self.cur.execute(sql)
        data = self.cur.fetchone()
        if data and check_password_hash(data[1], password):
            return data[0], data[2]
        else:
            return None

    '''密碼加密儲存用
    def updatePassword(self, username, password):
        password_hash = generate_password_hash(password)
        sql = f"UPDATE users SET password='{password_hash}' WHERE username='{username}'"
        self.cur.execute(sql)
        self.conn.commit()
        print("密碼已更新")
    '''
    def __getBookedList(self, data):
        data = list(data)
        for i in range(len(data)):
            data[i] = list(data[i])
            d = data[i]
            del d[2]
            booked = []
            if d[0]==data[i-1][0]:
                booked = data[i-1][1]
                booked.append(d[1])
                d[1] = booked
                data[i-1] = None
                continue
            
            if d[1] :                
                booked.append(d[1])
                d[1] = booked         
                                
        return data

    def getBookingByDate(self, start_date, end_date, opendata=True):
        '''
        Parameters
        ----------
        start_date : String，格式yyyy-mm-dd
        end_date : String，格式yyyy-mm-dd
        '''
        sql = f"""
            SELECT c.date, b.room_no, b.order_id, c.weekday, c.is_holiday, c.note FROM calendar AS c
            LEFT JOIN booking AS b ON b.date=c.date
            WHERE c.date<='{end_date}' AND c.date>='{start_date}'
            ORDER BY c.date, b.room_no
            """
        self.cur.execute(sql)
        data = self.cur.fetchall()
        if opendata:
            return self.__getBookedList(data)
        else:
            return data

    def getOrdersByDate(self, start_date, end_date):
        sql = f"""
            SELECT b.date, b.room_no, b.order_id, o.name, o.gender, o.phone
            FROM booking AS b
            INNER JOIN orders AS o ON b.order_id=o.order_id
            WHERE b.date<='{end_date}' AND b.date>='{start_date}'
            ORDER BY b.date, b.room_no
            """
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def getCalendar(self, start_date, end_date):
        sql = f"SELECT * FROM calendar WHERE date<='{end_date}' AND date>='{start_date}'"
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data
    
    def getRooms(self):
        sql = f"""SELECT r.room_no, r.name, r.room_type, 
            rt.accommodate, rt.rate_weekday, rt.rate_holiday, rt.single_discount,
            rt.discribe, rt.images
            FROM rooms AS r
            INNER JOIN room_type AS rt ON rt.type=r.room_type
            WHERE is_available=1"""
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def updateCalendar(self, csv_file_mane):
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
            print(f"{csv_file_mane}已寫入資料庫")

    def __del__(self):
        self.cur.close()
        self.conn.close()
        print("資料庫已關閉!!")

# 將由資料庫取得的預約日曆資料，整理成dict格式
def calendarFormatter(result):
    from datetime import datetime, timedelta

    data_dict = {}
    dateFormatter = "%Y-%m-%d"
    date = datetime.strftime(result[0], dateFormatter)
    bid = date+"-"+result[1]
    order_data = list(result[2:])
    cols = ["order_id", "booker_name", "gender", "phone"]    
    order_dict = dict(zip(cols, order_data))

    gender = "先生"
    if order_dict["gender"]=="F":
        gender = "小姐"
    order_dict["gender"] = gender

    data_dict[bid] = order_dict

    return data_dict

if __name__=="__main__":
    # 中華民國政府行政機關辦公日曆表(csv檔)：https://data.gov.tw/dataset/14718
    lastest_csv = "111年中華民國政府行政機關辦公日曆表.csv"
    
    mydb = Mydb()
    data = mydb.getOrdersByDate("2021-12-28", "2022-01-02")
    del mydb

    for d in data:
        d = calendarFormatter(d)
        print(d)

    print(data)
