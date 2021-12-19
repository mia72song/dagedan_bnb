import sys
sys.path.append("..")
from models.db import Mydb

class BookingDB(Mydb):
    def getBookedByDate(self, start_date_string, end_date_string):
        sql = f"""
            SELECT c.date, c.is_holiday, b.RoomNo AS room_no 
            from calendar AS c
            LEFT JOIN booking AS b ON b.Date=c.date
            WHERE c.date<='{end_date_string}' AND c.date>='{start_date_string}'
            ORDER BY date, room_no
        """
        self.cur.execute(sql)
        return self.cur.fetchall()

    def getBookedByDateWithBookerInfo(self, start_date_string, end_date_string):
        sql = f"""
            SELECT b.Date, b.RoomNo, b.rate, b.OrderId, o.GuestId, 
            g.last_name, g.gender, g.phone 
            FROM booking AS b
            INNER JOIN orders AS o ON o.order_id=b.OrderId
            INNER JOIN guests AS g on g.guest_id =o.GuestId
            WHERE b.Date<='{end_date_string}' AND b.Date>='{start_date_string}'
            ORDER BY Date, RoomNo
        """
        self.cur.execute(sql)
        return self.cur.fetchall()

    def getBookedByOrderIdWithRoomInfo(self, oid):
        cols = ["date", "room_no", "room_name", "order_id"]
        sql = f"""
            SELECT b.Date, b.RoomNo, r.name, b.OrderId 
            FROM booking AS b
            INNER JOIN Rooms AS r ON r.room_no=b.RoomNo
            WHERE OrderId={oid}
        """
        self.cur.execute(sql)
        return self.cur.fetchall()

if __name__=="__main__":
    mydb = BookingDB()
    data = mydb.getBookedByOrderIdWithRoomInfo(2)
    print(data)