import pymysql
import os

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

    def getAvailableRoomNos(self, room_type, date):
        sql = f"""
            SELECT room_no FROM rooms 
            WHERE is_available=1 AND room_type='{room_type}' 
            AND room_no NOT IN(SELECT room_no FROM booking WHERE date='{date}')
        """
        self.cur.execute(sql)
        return list(item[0] for item in self.cur.fetchall())

    def __del__(self):
        self.cur.close()
        self.conn.close()
        print("資料庫已關閉!!")