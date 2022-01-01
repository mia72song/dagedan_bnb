from datetime import datetime
import sys
sys.path.append("..")

from models.db import Mydb

class Orders(Mydb):
    def getOrderById(self, order_id):
        sql = f"""
            SELECT o.order_id,  o.create_datetime, 
            g.last_name, g.gender, g.phone,
            o.check_in_date, o.check_out_date, o.nights, o.num_of_guests,
            o.amount, o.status,
            o.with_AddOnServices, PaymentId
            FROM orders AS o
            INNER JOIN guests AS g ON o.GuestId=g.guest_id 
            WHERE order_id={order_id}
        """
        self.cur.execute(sql)
        return self.cur.fetchone()

    def getOrdersByDataType(self, search_list=[]):
        """
        search_list = [col_name, value]
        None則，調用所有訂單
        """
        sql = f"""
            SELECT o.order_id,  o.create_datetime, 
            g.last_name, g.gender, g.phone AS phone,
            o.check_in_date, o.check_out_date, o.nights, o.num_of_guests,
            o.amount, o.status,
            o.with_AddOnServices, PaymentId
            FROM orders AS o
            INNER JOIN guests AS g ON o.GuestId=g.guest_id
        """
        if search_list:
            sql += f" WHERE {search_list[0]}='{search_list[1]}'"

        # 訂單建立時間 由近到遠
        sql += f" ORDER BY o.create_datetime DESC"
        
        self.cur.execute(sql)
        return self.cur.fetchall()

    def createOrder(self, check_in_date, check_out_date, nights, num_of_guests, amount, phone, arrival_datetime, booking=[], update_user="guest"):
        oid = int(datetime.timestamp(datetime.now()))
        sql_o = f"""
            INSERT INTO orders 
            (check_in_date, check_out_date, nights, num_of_guests, amount, phone, oid, update_user, arrival_datetime) 
            VALUES 
            ('{check_in_date}','{check_out_date}',{nights},{num_of_guests},{amount},'{phone}',{oid}, '{update_user}', '{arrival_datetime}')
        """
        self.cur.execute(sql_o)
        self.conn.commit()
        for b in booking:
            booking_list = b.split("_")
            sql_b = f"""
                INSERT INTO booking (Date, RoomNo, OrderId) 
                VALUES ('{booking_list[0]}','{booking_list[1]}',{oid})
            """
            self.cur.execute(sql_b)
            self.conn.commit()
        print(f"編號：{oid}訂單已建立")

if __name__=="__main__":
    from datetime import datetime
    oid = int(datetime.timestamp(datetime.now()))
    print(oid)