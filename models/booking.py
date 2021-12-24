from models.room import Rooms

class Bookings(Rooms):
    def getAvailableRoomNos(self, room_type, date):
        sql = f"""
            SELECT room_no FROM rooms 
            WHERE is_available=1 AND RoomType='{room_type}' 
            AND room_no NOT IN(SELECT RoomNo FROM booking WHERE Date='{date}')
        """
        self.cur.execute(sql)
        return self.cur.fetchall()

    def getCalendar(self, start_date_string, end_date_string):
        sql = f"SELECT * FROM calendar WHERE Date BETWEEN '{start_date_string}' AND '{end_date_string}'"
        self.cur.execute(sql)
        return self.cur.fetchall()
