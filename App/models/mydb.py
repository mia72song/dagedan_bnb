from time import monotonic
import pymysql
import os
from datetime import date, datetime

from dotenv import load_dotenv
load_dotenv()

from App.constants import DATE_FORMATTER

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

    def __getColumns(self, table_name):
        sql = f"desc {table_name}"
        self.cur.execute(sql)
        return list(item[0] for item in self.cur.fetchall())

    def getAllByPk(self, table_name, pk:tuple):
        # pk = (pk_col, pk_value)
        pk_col = pk[0]
        pk_value = pk[1]
        cols = self.__getColumns(table_name)
        
        sql = f"SELECT * FROM {table_name} WHERE {pk_col}='{pk_value}'"
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return dict(zip(cols, result))

    def getCalendar(self, start_date, end_date):
        cols = self.__getColumns("calendar")

        start_date_string =  datetime.strftime(start_date, DATE_FORMATTER)
        end_date_string =  datetime.strftime(end_date, DATE_FORMATTER)

        sql = f"SELECT * FROM calendar WHERE date between '{start_date_string}' AND '{end_date_string}'"
        self.cur.execute(sql)
        results = self.cur.fetchall()
        data = []
        year = ""
        for r in results:
            data_dict = dict(zip(cols, r))
            date_string = datetime.strftime(data_dict["date"], DATE_FORMATTER)
            if not year:
                year = date_string[:4]

            data_dict["date"] = date_string[5:]

            data.append(data_dict)
            
        return {"year": year, "days": data}

    # 將超過期限未付款的訂單，修改狀態為「取消」
    def updateStatus(self):
        today = date.today()
        date_string =  datetime.strftime(today, DATE_FORMATTER)
        sql = f"""
            UPDATE orders SET status='CANCEL', update_user='system' 
            WHERE payment_id IS NULL AND status='NEW' AND payment_deadline<'{date_string}'
        """
        self.cur.execute(sql)
        self.conn.commit()

    # 邏輯刪除 已「取消」的訂單的訂房明細
    def cancelBooking(self):
        sql = f"""
            UPDATE booking SET is_del=1 
            WHERE order_id IN(SELECT oid FROM orders WHERE status='CANCEL') 
            OR order_id NOT IN(SELECT oid FROM orders)
        """
        self.cur.execute(sql)
        self.conn.commit()

    def getAvailableRoomNos(self, room_type, date):
        # 自動取消過期訂單及釋出空房
        self.updateStatus()
        self.cancelBooking()
        
        sql = f"""
            SELECT room_no FROM rooms 
            WHERE is_available=1 AND room_type='{room_type}' 
            AND room_no NOT IN(SELECT room_no FROM booking WHERE date='{date}' AND is_del=0)
        """
        self.cur.execute(sql)
        return list(item[0] for item in self.cur.fetchall())



    def __del__(self):
        self.cur.close()
        self.conn.close()
        print("資料庫已關閉!!")