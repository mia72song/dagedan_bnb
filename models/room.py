from models.db import Mydb

class RoomDB(Mydb):
    def getRooms(self, type=None, room_no=None):
        sql = f"""SELECT r.room_no, r.name, r.room_type, 
            rt.accommodate, rt.rate_weekday, rt.rate_holiday, rt.single_discount,
            rt.discribe, rt.images
            FROM rooms AS r
            INNER JOIN room_type AS rt ON rt.type=r.room_type
            WHERE r.is_available=1"""

        if type:
            sql += f" AND r.room_type='{type}'"
        
        if room_no:
            sql += f" AND r.room_no='{room_no}'"
        
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

if __name__=="__main__":
    mydb = RoomDB()
    data = mydb.getRooms()
    print(data)