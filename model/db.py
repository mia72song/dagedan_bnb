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
    
    def getBookingByDate(self, start_date, end_date):
        '''
        Parameters
        ----------
        start_date : String，格式yyyy-mm-dd
        end_date : String，格式yyyy-mm-dd
        '''
        sql = f"""SELECT c.date, b.room_no, b.order_id, c.weekday, c.is_holiday, c.note 
            FROM calendar AS c
            LEFT JOIN booking AS b ON c.date=b.date
            WHERE c.date<='{end_date}' AND c.date>='{start_date}'
            ORDER BY c.date, b.room_no"""
        self.cur.execute(sql)
        data = self.cur.fetchall()

        print(f"搜尋{start_date}到{end_date}的預約")
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

if __name__=="__main__":
    # 中華民國政府行政機關辦公日曆表(csv檔)：https://data.gov.tw/dataset/14718
    lastest_csv = "111年中華民國政府行政機關辦公日曆表.csv"
    
    mydb = Mydb()
    data = mydb.getBookingByDate('2021-12-28', '2022-01-02')
    print(data)
    del mydb
