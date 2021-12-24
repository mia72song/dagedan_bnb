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

    def getRoomNos(self, room_type=None, num_of_guests=None):
        sql = f"""
            SELECT room_no FROM rooms AS r 
            INNER JOIN room_types AS rt ON rt.type=r.RoomType 
            WHERE is_available=1
        """
        if room_type:
            sql += f" AND RoomType='{room_type.capitalize()}'"

        if num_of_guests:
            sql += f" AND rt.accommodate={int(num_of_guests)}"

        sql += " ORDER BY room_no"

        self.cur.execute(sql)
        return self.cur.fetchall()

    def getRoomTypes(self, room_type=None, num_of_guests=None):
        sql = f"""
            SELECT type, name, accommodate, images, description, 
            rate_weekday, rate_holiday, single_discount 
            FROM room_types WHERE is_del=0
        """
        if room_type:
            sql += f" AND type='{room_type.capitalize()}'"

        if num_of_guests:
            sql += f" AND accommodate={int(num_of_guests)}"
        
        self.cur.execute(sql)
        return self.cur.fetchall()
    
if __name__=="__main__":
    mydb = RoomDB()

    data = mydb.getRoomNos(room_type="Twin")
    print(data)