import sys
sys.path.append("..")

sql = f"""
    SELECT r.room_no, rt.name, r.RoomType, 
    rt.accommodate, rt.rate_weekday, rt.rate_holiday, rt.single_discount, 
    rt.description, rt.images, r.is_available FROM rooms AS r
    INNER JOIN room_types AS rt ON rt.type=r.RoomType
"""

from models.db import Mydb
class RoomDB(Mydb):
    def getRooms(self, sql=sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def getAvailableRooms(self, sql=sql):
        sql += f"WHERE is_available=1"
        self.cur.execute(sql)
        return self.cur.fetchall()

    def getRoomsByAccommodate(self, num_of_guests, sql=sql, available=True):            
        sql += f"WHERE rt.accommodate='{num_of_guests}'"
        if available:
            sql += f" AND is_available=1"
        self.cur.execute(sql)
        return self.cur.fetchall()

    def getAvailableRoomNosByRoomType(self, RoomType):
        sql = f"SELECT room_no FROM rooms WHERE is_available=1 AND RoomType='{RoomType}'"
        self.cur.execute(sql)
        return self.cur.fetchall()

    def getRoomTypes(self, type=None):
        sql = f"""
            SELECT type, name, accommodate, images, description, 
            rate_weekday, rate_holiday, single_discount 
            FROM room_types WHERE is_del=0
        """
        if type:
            sql += f" AND type='{type.capitalize()}'"
        self.cur.execute(sql)
        return self.cur.fetchall()
    
if __name__=="__main__":
    mydb = RoomDB()
    data = mydb.getRoomTypes("TWIN")
    print(data)