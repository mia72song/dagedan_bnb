import sys
sys.path.append("..")
from models.rooms import RoomDB

class BookingDB(RoomDB):
    def closeBookingOnCalendar(self, date):
        sql = f"UPDATE calendar SET is_closed=1 WHERE date='{date}'"
        self.cur.execute(sql)
        self.conn.commit()
        print(f"{date}已全天關房")

    def getBookedCalendar(self, start_date_string, end_date_string):
        sql = f"""
            SELECT c.date, c.weekday, c.is_holiday, b.RoomNo AS room_no, c.is_closed
            from calendar AS c
            LEFT JOIN booking AS b ON b.Date=c.date
            WHERE c.date BETWEEN '{start_date_string}' AND '{end_date_string}'
            ORDER BY date, room_no
        """
        self.cur.execute(sql)
        return self.cur.fetchall()

    def getBookedCalendarByRoomAccommodate(self, start_date_string, end_date_string, num_of_guests=2):
        sql = f"""
            SELECT c.date, c.weekday, c.is_holiday, r.room_no, c.is_closed
            from calendar AS c
            LEFT JOIN booking AS b ON b.Date=c.date
            LEFT JOIN rooms AS r ON r.room_no=b.RoomNo
            LEFT JOIN room_types AS rt ON rt.type=r.RoomType
            WHERE c.date BETWEEN '{start_date_string}' AND '{end_date_string}'
            AND (rt.accommodate={num_of_guests} OR rt.accommodate IS NULL)
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
            WHERE c.date BETWEEN '{start_date_string}' AND '{end_date_string}'
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
    data_dict = {}
    booked = mydb.getBookingCalendarByRoomAccommodate("2021-12-28", "2022-01-04", 2)
    
    print(booked)