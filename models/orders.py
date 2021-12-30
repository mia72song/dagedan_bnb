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
