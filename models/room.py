import sys
sys.path.append("..")

from models.db import Mydb

class Rooms(Mydb):
    def getRoomTypes(self, num_of_guests=1):
        sql = f"SELECT type FROM room_types WHERE is_del=0 AND accommodate>={int(num_of_guests)}"
        self.cur.execute(sql)
        return self.cur.fetchall()

    def getRoomInfoByType(self, room_type=None):
        sql = f"""
            SELECT type, name, accommodate, images, description, 
            rate_weekday, rate_holiday, single_discount 
            FROM room_types WHERE is_del=0
        """
        if room_type:
            sql += f" AND type='{room_type.capitalize()}'"
        
        self.cur.execute(sql)
        return self.cur.fetchall()