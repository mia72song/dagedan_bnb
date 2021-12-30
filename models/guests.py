import sys
sys.path.append("..")

from models.db import Mydb

class Guests(Mydb):
    def guestPhoneExist(self, phone):
        sql = f"SELECT guest_id from guests WHERE phone='{phone}'"
        self.cur.execute(sql)
        return self.cur.fetchone()

    def createGuest(self, last_name, first_name, gender, phone, email, nationality, current_user):
        if self.guestPhoneExist(phone):
            gid = self.guestPhoneExist(phone)[0]
            print(f"編號{gid}住客資料已存在")
        else:
            pass


if __name__=="__main__":
    mydb = Guests()
    data = mydb.guestExist("0950400600")
    print(data)