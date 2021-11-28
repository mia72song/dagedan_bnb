import csv
import json
import os

# 日曆JSON檔
json_file_name = "tw_calendar.json" 

def updateTwCalendarJson(json_file_name, csv_file_mane):
    calendar_dict = {}
    
    if os.path.exists(json_file_name):
        with open("tw_calendar.json", "r", encoding='utf8') as f:
            calendar_dict = json.load(fp=f)
            # print(type(calendar_dict))#<class 'dict'>

    calendar_dict = csvFileToDict(csv_file_mane, calendar_dict)

    with open(json_file_name, "w", encoding='utf8') as f:
        json.dump(calendar_dict, f, ensure_ascii=False)
        print("json檔已寫入")

def csvFileToDict(csv_file_mane, dict_name):
    '''dict 格式：
    dict_name = {
        'yyyymmdd':{
            "is_holiday":bool值,
            "note":假日名or補班
            },
        'yyyymmdd':{
            "is_holiday":bool值,
            "note":假日名or補班
            }
        }
    '''
    with open(csv_file_mane, "r") as f:
        data = csv.DictReader(f)
        for row in data:
            if row['是否放假']==2:
                dict_name[row['西元日期']] = {"is_holiday":True, "note":row['備註']}
            else:
                dict_name[row['西元日期']] = {"is_holiday":False, "note":row['備註']}

    return dict_name

# 中華民國政府行政機關辦公日曆表(csv檔)：https://data.gov.tw/dataset/14718
lastest_csv = "111年中華民國政府行政機關辦公日曆表.csv"

if __name__=="__main__":
    updateTwCalendarJson(json_file_name, lastest_csv)