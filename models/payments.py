from datetime import datetime
from models.db import Mydb

class PaymentDB(Mydb):
    def __orderIsNull(self, order_id, col_name):
        sql = f"SELECT * FROM orders WHERE order_id={order_id} AND {col_name} IS NULL"
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data

    def createPayment(self, payment_dict, current_user):
        """
        payment_dict = {
            'oid': int, 
            'bank': value,
            'account_no': value,
            'name': value,
            'amount': value,
            'transfer_date': value
        }
        """
        order_id = payment_dict["oid"]
        #是則該筆訂單沒有付款資料，表示未付款過
        data = self.__orderIsNull(order_id, "payment_id")
        if data: 
            pid = "A" + str(int(datetime.now().timestamp()))
            now = datetime.now()
            sql_p = f"""
                INSERT INTO payment_atm 
                (id, bank, account_no, name, amount, transfer_date, update_datetime, update_user) 
                VALUES 
                ("{pid}", "{payment_dict['bank']}", "{payment_dict['account_no']}", "{payment_dict['name']}", 
                "{payment_dict['amount']}", "{payment_dict['transfer_date']}", "{now}", "{current_user}")
            """
            sql_o = f"""
                UPDATE orders 
                SET payment_id="{pid}", update_datetime="{now}", update_user="{current_user}", status="PAID"
                WHERE order_id={order_id} AND payment_id IS NULL
            """
            self.cur.execute(sql_p)
            self.cur.execute(sql_o)
            self.conn.commit()
            message = "ok"
            return True, message
        else:
            message = f"訂單編號：{order_id}已有付款資料{data[11]}"
            return False, message

    def updatePayment(self, payment_dict, current_user):
        """
        payment_dict = {pid: value, key :value, ...}
        data_string = "data_dict[key]=data_dict[value],"
        """
        pid = payment_dict["pid"]
        data_string = ""
        for k, v in payment_dict.items():
            if k=="pid":
                continue
            data_string += f"{k}='{v}', "
        sql = f"""
            UPDATE payment_atm SET {data_string}
            update_datetime="{datetime.now()}", update_user="{current_user}" 
            WHERE id="{pid}"
        """
        self.cur.execute(sql)
        self.conn.commit()
        print(f"付款編號：{pid} 資料已修改")

    def getPaymentById(self, pid):
        sql = f"SELECT * FROM payment_atm WHERE id='{pid}'"
        self.cur.execute(sql)
        return self.cur.fetchone()
