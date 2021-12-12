from db import Mydb
import pymysql

# 中華民國政府行政機關辦公日曆表(csv檔)：https://data.gov.tw/dataset/14718
csv_file_mane = "111年中華民國政府行政機關辦公日曆表.csv"

if __name__=="__main__": 
    try:
        mydb = Mydb()
        mydb.updateCalendar(csv_file_mane)
        print(f"{csv_file_mane}已更新入資料庫")
    except pymysql.err.IntegrityError:
        print(f"Woop!!!{csv_file_mane}已存在資料庫中")
    except Exception as e:
        print(f"其他資料庫錯誤：", e)
    finally:
        del mydb