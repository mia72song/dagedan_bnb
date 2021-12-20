import sys
sys.path.append("..")
from models.db import Mydb

class BookingDB(Mydb):
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
    '''
    data_dict = {
        date: {
            "weekday": "日",
            "is_holiday": bool, 
            "booked": []
        }
    }
    '''
    data_dict = {}
    booked = mydb.getBookedCalendar("2022-01-28", "2022-02-02")
    from datetime import datetime
    from constants import DATE_FORMATTER
    for b in booked:
        date = datetime.strftime(b[0], DATE_FORMATTER)
        booked = []  
        if date in data_dict:
            booked = data_dict[date]["booked"]
            booked.append(b[3])
            continue

        if b[3] : 
            booked.append(b[3])   

        data_dict[date] = {
            "weekday": b[1],
            "is_holiday": (b[2]==1),
            "booked": booked,
            "is_closed": (b[4]==1)
        }
    print(data_dict)