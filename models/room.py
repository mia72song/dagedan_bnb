import sys
sys.path.append("..")

from models.db import Mydb

class Rooms(Mydb):
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

    def getCalendar(self, start_date_string, end_date_string):
        sql = f"SELECT * FROM calendar WHERE Date BETWEEN '{start_date_string}' AND '{end_date_string}'"
        self.cur.execute(sql)
        return self.cur.fetchall()
