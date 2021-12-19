from werkzeug.security import generate_password_hash, check_password_hash

from models.db import Mydb

class UserDB(Mydb):
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

if __name__=="__main__":
    userdb = UserDB()
    result = userdb.getUser("mia72song", "721015")
    print(result)
    del userdb