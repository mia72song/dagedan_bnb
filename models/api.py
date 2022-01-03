from datetime import datetime, date, timedelta
import sys
sys.path.append("..")

from models.db import Mydb

class Apidb(Mydb):
    '''Calendar'''
    def getCalendar(self, start_date_string, end_date_string):
        sql = f"SELECT * FROM calendar WHERE Date BETWEEN '{start_date_string}' AND '{end_date_string}'"
        self.cur.execute(sql)
        return self.cur.fetchall()

    '''Room'''
    def getRoomInfoByType(self, room_type=None, num_of_guests=1):
        sql = f"""
            SELECT type, name, accommodate, images, description, 
            rate_weekday, rate_holiday, single_discount 
            FROM room_types WHERE is_del=0 AND accommodate>={int(num_of_guests)}
        """
        if room_type:
            sql += f" AND type='{room_type.capitalize()}'"
        
        self.cur.execute(sql)
        return self.cur.fetchall()

    def getAvailableRoomNos(self, room_type, date):
        sql = f"""
            SELECT room_no FROM rooms 
            WHERE is_available=1 AND RoomType='{room_type}' 
            AND room_no NOT IN(SELECT RoomNo FROM booking WHERE Date='{date}')
        """
        self.cur.execute(sql)
        return self.cur.fetchall()

    '''Order'''
    def getOrderById(self, oid):
        sql = f"SELECT * FROM orders WHERE oid={oid}"
        self.cur.execute(sql)
        return self.cur.fetchone()

    def createOrder(self, check_in_date, check_out_date, nights, num_of_guests, amount, phone, arrival_datetime, booking=[], update_user="guest"):
        oid = int(datetime.timestamp(datetime.now()))
        deadline = date.today()+timedelta(days=1)
        sql_o = f"""
            INSERT INTO orders 
            (check_in_date, check_out_date, nights, num_of_guests, amount, phone, oid, update_user, arrival_datetime, payment_deadline) 
            VALUES 
            ('{check_in_date}','{check_out_date}',{nights},{num_of_guests},{amount},'{phone}',{oid}, '{update_user}', '{arrival_datetime}', '{deadline}')
        """
        self.cur.execute(sql_o)
        self.conn.commit()
        for b in booking:
            booking_list = b.split("_")
            sql_b = f"""
                INSERT INTO booking (Date, RoomNo, OrderId) 
                VALUES ('{booking_list[0]}','{booking_list[1]}',{oid})
            """
            self.cur.execute(sql_b)
            self.conn.commit()
        print(f"編號：{oid}訂單已建立")
        return oid

    '''Guest'''
    def __phoneExist(self, phone):
        sql = f"SELECT gid from guests WHERE phone='{phone}'"
        self.cur.execute(sql)
        return self.cur.fetchone()

    def createGuest(self, name, gender, phone, email, update_user="guest"):
        if self.__phoneExist(phone):
            gid = self.__phoneExist(phone)[0]
            print(f"電話：{phone} 已存在於住客編號：{gid} 資料中")
        else:
            sql = f"""
                INSERT INTO guests (name, gender, phone, email, update_user) 
                VALUES ('{name}','{gender}','{phone}','{email}','{update_user}')
            """
            self.cur.execute(sql)
            self.conn.commit()
            print("新住客資料已建立")