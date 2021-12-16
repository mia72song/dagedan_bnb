from models.db import Mydb

class OrderDB(Mydb):
    def getOrderById(self, order_id):
        sql = f"""
            SELECT o.order_id,  o.create_datetime, 
            g.last_name, g.gender, g.phone,
            o.check_in_date, o.check_out_date, o.nights, o.guests,
            o.amount, o.status,
            o.add_on_order_id, payment_id
            FROM orders AS o
            INNER JOIN guests AS g ON o.guest_id=g.guest_id 
            WHERE order_id={order_id}
        """
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data

    def getOrdersByDataType(self, search_list=[]):
        '''
        search_list = [data_type, keyword]
        None則，調用所有訂單
        '''
        sql = f"""
            SELECT o.order_id,  o.create_datetime, 
            g.last_name, g.gender, g.phone AS phone,
            o.check_in_date, o.check_out_date, o.nights, o.guests,
            o.amount, o.status,
            o.add_on_order_id, payment_id
            FROM orders AS o
            INNER JOIN guests AS g ON o.guest_id=g.guest_id
        """
        if search_list:
            sql += f" WHERE {search_list[0]}='{search_list[1]}'"

        # 訂單建立時間 由近到遠
        sql += f" ORDER BY o.create_datetime DESC"
        
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data