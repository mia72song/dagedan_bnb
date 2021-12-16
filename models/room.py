import sys
sys.path.append("..")

from models.db import Mydb

class RoomDB(Mydb):
    def getRooms(self, type=None, number=None, available=True):
        cols = [
            "room_no", "name", "type", "accommodate", "rate_weekday", "rate_holiday", "single_discount", 
            "discribe", "images"
        ]
        sql = f"""SELECT r.room_no, r.name, r.room_type, 
            rt.accommodate, rt.rate_weekday, rt.rate_holiday, rt.single_discount,
            rt.discribe, rt.images FROM rooms AS r
            INNER JOIN room_type AS rt ON rt.type=r.room_type"""

        if available or type or number :
            sql += f" WHERE"
            if available:
                sql += f" r.is_available=1"

            if type:
                sql += f" AND r.room_type='{type}'"
            
            if number:
                sql += f" AND r.room_no='{number}'"
        
        self.cur.execute(sql)
        results = self.cur.fetchall()
        if results:
            data_list = []
            for r in results:
                data_dict = dict(zip(cols, r))
                data_dict["rate_weekday"] = float(data_dict["rate_weekday"])
                data_dict["rate_holiday"] = float(data_dict["rate_holiday"])
                data_list.append(data_dict)
            return data_list
        else:
            return None

if __name__=="__main__":
    mydb = RoomDB()
    data = mydb.getRooms(number="t001")
    print(data)