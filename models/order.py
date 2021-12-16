from datetime import datetime

from models.db import Mydb
from constants import DATE_FORMATTER, DATETIME_FORMATTER

# 將由db取得的訂單資料，整理成dict格式
def orderFormatter(result):
    cols = [
            "order_id", "create_datetime", "booker_name", "booker_gender", "booker_phone",
            "check_in_date", "check_out_date", "nights", "guests", "amount", "order_status",
            "add_on_order_id", "payment_id"
        ]
    data_dict = dict(zip(cols, result))
    data_dict["create_datetime"] = datetime.strftime(data_dict["create_datetime"], DATETIME_FORMATTER)
    data_dict["check_in_date"] = datetime.strftime(data_dict["check_in_date"], DATE_FORMATTER)
    data_dict["check_out_date"] = datetime.strftime(data_dict["check_out_date"], DATE_FORMATTER)
    data_dict["amount"] = float(data_dict["amount"])
    return data_dict

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
        result = self.cur.fetchone()
        if result:
            return orderFormatter(result)
        else:
            return None

    def getOrdersByDataType(self, search_list=[]):
        '''
        search_list = [col_name, value]
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
        results = self.cur.fetchall()
        if results:
            data_list = []
            for r in results:
                data_list.append(orderFormatter(r))
            return data_list
        else:
            return None

if __name__=="__main__":
    mydb = OrderDB()
    data = mydb.getOrdersByDataType()
    print(data)