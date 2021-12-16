from datetime import datetime

import sys
sys.path.append("..")
from models.db import Mydb
from constants import DATE_FORMATTER

class BookingDB(Mydb):
    def getBookingByDateToFront(self, start_date_string, end_date_string, filter_none=True):
        cols = [
            "date", "weekday", "is_holiday", "room_no", 
            "room_name", "is_available" , "room_type", 
            "accommodate", "rate_weekday", "rate_holiday", "single_discount"
        ]
        
        filter_string = "INNER"        
        if not filter_none : filter_string = "LEFT"

        sql = f'''
            SELECT c.date AS date, c.weekday, c.is_holiday, b.room_no AS room_no, 
            r.name, r.is_available, r.room_type,
            rt.accommodate, rt.rate_weekday, rt.rate_holiday, rt.single_discount
            from calendar AS c
            {filter_string} JOIN booking AS b ON c.date=b.date
            {filter_string} JOIN rooms AS r ON b.room_no=r.room_no
            {filter_string} JOIN room_type AS rt ON r.room_type=rt.type
            WHERE c.date<='{end_date_string}' AND c.date>='{start_date_string}'
            ORDER BY date, room_no
        '''
        self.cur.execute(sql)
        results = self.cur.fetchall()
        
        if results:
            data_list = []
            for r in results:
                data_dict = dict(zip(cols, r))
                data_dict["date"] = datetime.strftime(data_dict["date"], DATE_FORMATTER)
                data_dict["rate_weekday"] = float(data_dict["rate_weekday"])
                data_dict["rate_holiday"] = float(data_dict["rate_holiday"])
                data_list.append(data_dict)
            return data_list
        else:
            return None

    def getBookingByDateToAdmin(self, start_date_string, end_date_string):
        cols = [
            "date", "room_no", "order_id", "price", "booker_name", "booker_gender", "booker_phone"
        ]
        sql = f"""
            SELECT b.date, b.room_no, b.order_id, b.price, g.last_name, g.gender, g.phone FROM booking AS b
            INNER JOIN orders AS o ON o.order_id=b.order_id
            INNER JOIN guests AS g ON g.guest_id=o.guest_id
            WHERE b.date<='{end_date_string}' AND b.date>='{start_date_string}'
            ORDER BY date, room_no
        """
        self.cur.execute(sql)
        results = self.cur.fetchall()
        if results:
            data_list = []
            for r in results:
                data_dict = dict(zip(cols, r))
                data_dict["date"] = datetime.strftime(data_dict["date"], DATE_FORMATTER)
                data_dict["price"] = float(data_dict["price"])
                data_list.append(data_dict)
            return data_list
        else:
            return None

    def getBookingByOrderId(self, order_id):
        cols = ["date", "room_no", "room_name", "room_type", "price"]
        sql = f'''
            SELECT b.date, b.room_no, r.name, r.room_type, b.price FROM booking AS b 
            INNER JOIN rooms AS r ON r.room_no=b.room_no
            INNER JOIN room_type AS rt ON rt.type=r.room_type
            WHERE order_id={order_id} ORDER BY date
        '''
        self.cur.execute(sql)
        results = self.cur.fetchall()
        if results:
            data_list = []
            for r in results:
                data_dict = dict(zip(cols, r))
                data_dict["date"] = datetime.strftime(data_dict["date"], DATE_FORMATTER)
                data_dict["price"] = float(data_dict["price"])
                data_list.append(data_dict)
            return data_list
        else:
            return None

if __name__=="__main__":
    mydb = BookingDB()
    data = mydb.getBookingByDateToAdmin("2021-12-28", "2022-01-02")
    print(data)