from db import Mydb

# 中華民國政府行政機關辦公日曆表(csv檔)：https://data.gov.tw/dataset/14718
lastest_csv = "111年中華民國政府行政機關辦公日曆表.csv"

if __name__=="__main__":
    mydb = Mydb()
    mydb.updateCalendar(lastest_csv)
    del mydb
