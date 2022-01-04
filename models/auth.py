from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date, timedelta
import sys
sys.path.append("..")

from models.db import Mydb
from constants import DATE_FORMATTER

class Authdb(Mydb):
    ''' User'''
    def getUser(self, username, password):
        sql = f"SELECT username, password, staff_name FROM users WHERE username='{username}' and is_del=0"
        self.cur.execute(sql)
        data = self.cur.fetchone()
        if data and check_password_hash(data[1], password):
            return data[0], data[2]
        else:
            return None

    """密碼加密儲存用
    def updatePassword(self, username, password):
        password_hash = generate_password_hash(password)
        sql = f"UPDATE users SET password='{password_hash}' WHERE username='{username}'"
        self.cur.execute(sql)
        self.conn.commit()
        print("密碼已更新")
    """
    '''Order'''
    def __updateStatus(self):
        today = date.today()
        date_string =  datetime.strftime(today, DATE_FORMATTER)
        sql = f"""
            UPDATE orders SET status='CANCEL' 
            WHERE PaymentId IS NULL AND status='NEW' AND payment_deadline<'{date_string}'
        """
        self.cur.execute(sql)
        self.conn.commit()

    def __cancelBooking(self):
        sql = f"DELETE FROM booking WHERE OrderId IN(SELECT oid FROM orders WHERE status='CANCEL')"
        self.cur.execute(sql)
        self.conn.commit()

    def getOrdersByStatus(self, status="ALL"):
        self.__updateStatus()
        self.__cancelBooking()
        sql = f"""
            SELECT oid, create_datetime, 
            check_in_date, check_in_date, nights, num_of_guests, amount, 
            g.name, g.gender, g.phone, PaymentId, status 
            FROM orders AS o
            INNER JOIN guests AS g ON g.phone=o.Phone
        """
        if status!="ALL":
            sql += f"WHERE status='{status}'"

        sql += "ORDER BY create_datetime DESC"

        self.cur.execute(sql)
        return self.cur.fetchall()

    def getOrdersByKeyword(self, data_type, keyword):
        # data_type: phone, check_in_date
        sql = f"""
            SELECT oid, create_datetime, 
            check_in_date, check_in_date, nights, num_of_guests, amount, 
            g.name, g.gender, g.phone, PaymentId, status 
            FROM orders AS o
            INNER JOIN guests AS g ON g.phone=o.Phone
        """
        if data_type.lower()=="phone":
            sql += f"WHERE g.phone='{keyword}'"
        else:
            sql += f"WHERE {data_type.lower()}='{keyword}'"

        sql += "ORDER BY create_datetime DESC"

        self.cur.execute(sql)
        return self.cur.fetchall()

    def getOrderById(self, oid):
        sql = f"""
            SELECT oid, create_datetime, 
            check_in_date, check_in_date, nights, num_of_guests, amount, 
            g.name, g.gender, g.phone, PaymentId, status 
            FROM orders AS o
            INNER JOIN guests AS g ON g.phone=o.Phone
            WHERE oid={oid}
        """
        self.cur.execute(sql)
        return self.cur.fetchall()

    def updateOrderStatus(self, oid, status):
        # status："NEW", "PAID" ,"CANCEL", "DELETE"
        sql = f"UPDATE orders SET status='{status.upper()}' WHERE oid={oid}"
        self.cur.execute(sql)
        self.conn.commit()
    
    '''Booking'''
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

    '''Payment'''
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

if __name__=="__main__":
    mydb = Authdb()
    data = mydb.getOrdersByStatus()
    print(data)