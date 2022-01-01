import sys
sys.path.append("..")

from models.db import Mydb

class Guests(Mydb):
    def __phoneExist(self, phone):
        sql = f"SELECT gid from guests WHERE phone='{phone}'"
        self.cur.execute(sql)
        return self.cur.fetchone()

    def createGuest(self, name, gender, phone, email, update_user="guest"):
        if self.__phoneExist(phone):
            gid = self.__phoneExist(phone)[0]
            print(f"電話：{phone} 已存在於住客編號：{gid} 資料中")
        else:
            sql = f"""
                INSERT INTO guests (name, gender, phone, email, update_user) 
                VALUES ('{name}','{gender}','{phone}','{email}','{update_user}')
            """
            self.cur.execute(sql)
            self.conn.commit()
            print("新住客資料已建立")


if __name__=="__main__":
    mydb = Guests()
    mydb.createGuest("李鷗", "M", "0987654321", "leolee@gmail.com", "mia72song")
