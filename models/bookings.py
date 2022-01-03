import sys
sys.path.append("..")

from models.db import Mydb

class Bookings(Mydb):
    def getBookingByOrderId(self, oid):
        sql = f"""
            SELECT b.Date, rt.name, b.RoomNo, b.OrderId FROM booking AS b
            INNER JOIN rooms AS r ON r.room_no=b.RoomNo
            INNER JOIN room_types AS rt ON rt.type=r.RoomType
            WHERE OrderId={oid}
        """
        self.cur.execute(sql)
        return self.cur.fetchall()

    def getBookingByDate(self, date):
        pass

if __name__=="__main__":
    mydb = Bookings()
    data = mydb.getBookingByOrderId(1641136864)
    print(data)