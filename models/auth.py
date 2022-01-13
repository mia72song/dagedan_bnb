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
            UPDATE orders SET status='CANCEL', update_user='system' 
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
            check_in_date, check_out_date, nights, num_of_guests, amount, 
            g.name, g.gender, g.phone, PaymentId, payment_deadline, status 
            FROM orders AS o
            INNER JOIN guests AS g ON g.phone=o.Phone
        """
        if status.upper()!="ALL":
            sql += f"WHERE status='{status.upper()}'"

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

    def updateOrderStatus(self, oid, status, current_user):
        # status："NEW", "PAID" ,"CANCEL"
        sql_o = f"UPDATE orders SET status='{status.upper()}', update_user='{current_user}' WHERE oid={oid}"
        self.cur.execute(sql_o)
        self.conn.commit()
        sql_b = f"DELETE FROM booking WHERE OrderId={oid}"
        self.cur.execute(sql_b)
        self.conn.commit()
        print(f"訂單編號：{oid}已取消")
    
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
    def __paymentIdExist(self, order_id):
        sql = f"SELECT * FROM orders WHERE oid={order_id} AND PaymentId IS NOT NULL"
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data

    def createPayment(self, current_user, oid, bank, account_no, name, amount, transfer_date):
        #是則該筆訂單沒有付款資料，表示未付款過
        data = self.__paymentIdExist(oid)
        if not data: 
            pid = "A" + str(int(datetime.now().timestamp()))
            sql_p = f"""
                INSERT INTO payment_atm 
                (id, bank, account_no, name, amount, transfer_date, update_user) 
                VALUES 
                ('{pid}','{bank}','{account_no}','{name}',{amount},'{transfer_date}','{current_user}')
            """
            sql_o = f"""
                UPDATE orders 
                SET PaymentId='{pid}', update_user='{current_user}', status="PAID"
                WHERE oid={oid} AND PaymentId IS NULL
            """
            self.cur.execute(sql_p)
            self.cur.execute(sql_o)
            self.conn.commit()
            msg = "ok"
        else:
            pid = data[9]
            msg = f"訂單編號：{oid}已有付款資料"
        
        return pid, msg

    def updatePayment(self, current_user, pid, bank=None, account_no=None, name=None, amount=None, transfer_date=None):
        data_string = ""
        if bank:
            data_string += f" bank='{bank}',"
        if account_no:
            data_string += f" account_no='{account_no}',"
        if name:
            data_string += f" name='{name}',"
        if amount:
            data_string += f" amount={amount},"
        if transfer_date:
            data_string += f" transfer_date='{transfer_date}',"
        
        if data_string!="":
            sql = f"""
                UPDATE payment_atm SET{data_string} update_user="{current_user}" 
                WHERE id="{pid}"
            """
            self.cur.execute(sql)
            self.conn.commit()
            print(f"付款編號：{pid} 資料已修改")
            msg = "ok"
        else:
            msg = f"付款編號：{pid} 未修改任何資料!!"
        
        return msg

    def getPaymentById(self, pid):
        sql = f"SELECT * FROM payment_atm WHERE id='{pid}'"
        self.cur.execute(sql)
        return self.cur.fetchone()

if __name__=="__main__":
    mydb = Authdb()
    mydb.updatePayment('mia72song', 'A1641305569', name='宋先生', amount=2112)
