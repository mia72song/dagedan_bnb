from models.db import Mydb

class BookingDB(Mydb):
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

    def getBookingListByOrderId(self, order_id):
        cols = ["date", "room_no", "room_name", "room_type"]
        sql = f'''
            SELECT b.date, b.room_no, r.name, r.room_type FROM booking AS b 
            INNER JOIN rooms AS r ON r.room_no=b.room_no
            INNER JOIN room_type AS rt ON rt.type=r.room_type
            WHERE order_id={order_id}
        '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data, cols