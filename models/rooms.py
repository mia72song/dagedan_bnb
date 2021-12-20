import sys
sys.path.append("..")

sql = f"""
    SELECT r.room_no, r.name, r.RoomType AS room_type, 
    rt.accommodate, rt.rate_weekday, rt.rate_holiday, rt.single_discount, 
    rt.discribe, rt.images, r.is_available FROM rooms AS r
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

    def getRoomsByType(self, type, sql=sql, available=True):
        sql += f"WHERE RoomType='{type}'"
        if available:
            sql += f" AND is_available=1"
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def getRoomsByAccommodate(self, num_of_guests, sql=sql, available=True):       
        sql += f"WHERE rt.accommodate='{num_of_guests}'"
        if available:
            sql += f" AND is_available=1"
        self.cur.execute(sql)
        return self.cur.fetchall()

if __name__=="__main__":
    mydb = RoomDB()
    data = mydb.getAvailableRooms()
    print(data)