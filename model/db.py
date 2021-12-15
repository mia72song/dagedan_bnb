from datetime import datetime
import pymysql
import os
from werkzeug.security import generate_password_hash, check_password_hash
import csv
import sys
sys.path.append("..")

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
    def __orderIsNull(self, order_id, col_name):
        sql = f"SELECT * FROM orders WHERE order_id={order_id} AND {col_name} IS NULL"
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data

    def createPayment(self, payment_dict, current_user):
        '''
        payment_dict = {
            'oid': int, 
            'bank': value,
            'account_no': value,
            'name': value,
            'amount': value,
            'transfer_date': value
        }
        '''
        order_id = payment_dict["oid"]
        #是則該筆訂單沒有付款資料，表示未付款過
        data = self.__orderIsNull(order_id, "payment_id")
        if data: 
            pid = "A" + str(int(datetime.now().timestamp()))
            now = datetime.now()
            sql_p = f'''
                INSERT INTO payment_atm 
                (id, bank, account_no, name, amount, transfer_date, update_datetime, update_user) 
                VALUES 
                ("{pid}", "{payment_dict['bank']}", "{payment_dict['account_no']}", "{payment_dict['name']}", 
                "{payment_dict['amount']}", "{payment_dict['transfer_date']}", "{now}", "{current_user}")
            '''
            sql_o = f'''
                UPDATE orders 
                SET payment_id="{pid}", update_datetime="{now}", update_user="{current_user}", status="PAID"
                WHERE order_id={order_id} AND payment_id IS NULL
            '''
            self.cur.execute(sql_p)
            self.cur.execute(sql_o)
            self.conn.commit()
            message = "ok"
            return True, message
        else:
            message = f"訂單編號：{order_id}已有付款資料{data[11]}"
            return False, message

    def updatePayment(self, payment_dict, current_user):
        '''
        payment_dict = {pid: value, key :value, ...}
        data_string = "data_dict[key]=data_dict[value],"
        '''
        pid = payment_dict["pid"]
        data_string = ""
        for k, v in payment_dict.items():
            if k=="pid":
                continue
            data_string += f"{k}='{v}', "
        sql = f'''
            UPDATE payment_atm SET {data_string}
            update_datetime="{datetime.now()}", update_user="{current_user}" 
            WHERE id="{pid}"
        '''
        self.cur.execute(sql)
        self.conn.commit()
        print(f"付款編號：{pid} 資料已修改")

    def getPaymentById(self, pid):
        sql = f"SELECT * FROM payment_atm WHERE id='{pid}'"
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data

    def getOrderById(self, order_id):
        sql = f"""
            SELECT o.order_id,  o.create_datetime, 
            g.last_name, g.gender, g.phone,
            o.check_in_date, o.check_out_date, o.nights, o.guests,
            o.amount, o.status,
            o.add_on_order_id, payment_id
            FROM orders AS o
            INNER JOIN guests AS g ON o.guest_id=g.guest_id 
            WHERE order_id={order_id}
        """
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data

    def getOrdersByDataType(self, search_list=[]):
        '''
        search_list = [data_type, keyword]
        None則，調用所有訂單
        '''
        sql = f"""
            SELECT o.order_id,  o.create_datetime, 
            g.last_name, g.gender, g.phone AS phone,
            o.check_in_date, o.check_out_date, o.nights, o.guests,
            o.amount, o.status,
            o.add_on_order_id, payment_id
            FROM orders AS o
            INNER JOIN guests AS g ON o.guest_id=g.guest_id
        """
        if search_list:
            sql += f" WHERE {search_list[0]}='{search_list[1]}'"

        # 訂單建立時間 由近到遠
        sql += f" ORDER BY o.create_datetime DESC"
        
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def getBookingListByDate(self, start_date_string, end_date_string, filter_none=True):
        cols = [
            "date", "room_no", "order_id", "weekday", "is_holiday", "holiday_note", 
            "booker_name", "booker_gender", "booker_phone"
        ]
        filter_string = "INNER"
        
        if not filter_none:
            filter_string = "LEFT"
        sql = f"""
            SELECT c.date, b.room_no, b.order_id, 
            c.weekday, c.is_holiday, c.note, 
            g.last_name, g.gender, g.phone 
            FROM calendar AS c
            {filter_string} JOIN booking AS b ON b.date=c.date
            {filter_string} JOIN orders AS o ON o.order_id=b.order_id
            {filter_string} JOIN guests AS g ON g.guest_id=o.guest_id
            WHERE c.date<='{end_date_string}' AND c.date>='{start_date_string}'
            ORDER BY c.date, b.room_no
        """
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data, cols

    def getRooms(self, type=None, room_no=None):
        sql = f"""SELECT r.room_no, r.name, r.room_type, 
            rt.accommodate, rt.rate_weekday, rt.rate_holiday, rt.single_discount,
            rt.discribe, rt.images
            FROM rooms AS r
            INNER JOIN room_type AS rt ON rt.type=r.room_type
            WHERE r.is_available=1"""

        if type:
            sql += f" AND r.room_type='{type}'"
        
        if room_no:
            sql += f" AND r.room_no='{room_no}'"
        
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def getCalendar(self, start_date_string, end_date_string):
        sql = f"SELECT * FROM calendar WHERE date<='{end_date_string}' AND date>='{start_date_string}'"
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
            
    def __del__(self):
        self.cur.close()
        self.conn.close()
        print("資料庫已關閉!!")


if __name__=="__main__": 
    mydb = Mydb()
    payment_dict = {
        "pid": "A1639495093", 
        "name" :"王艾旻"
    }
    
    mydb.updatePayment(payment_dict, "administrator")
    del mydb

