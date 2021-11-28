from datetime import datetime, timedelta
import json
import os 

def datetimeToSting(datetime_class):
    date_string = str(datetime_class.year)
    if datetime_class.month<10:
        date_string += "0"+str(datetime_class.month)
    else:
        date_string += str(datetime_class.month)

    if datetime_class.day<10:
        date_string += "0"+str(datetime_class.day)
    else:
        date_string += str(datetime_class.day)
    return date_string

def getSevenDays(datetime_class=None):
    json_file_name = "tw_calendar.json"
    seven_days = []
    if not datetime_class:
        datetime_class = datetime.today()    
    
    if not os.path.exists(json_file_name):
        json_file_name = "model/tw_calendar.json"

    with open(json_file_name, "r", encoding="utf-8") as f:
        calendar_dict = json.load(f)
        # print(calendar_dict[date_string])
        for n in range(0, 7) :
            data = {}
            if n!=0:
                one_day = timedelta(days=1)
                datetime_class += one_day
            date_string = datetimeToSting(datetime_class)
            data["date"] = date_string
            data = {**data, **calendar_dict[date_string]}
            seven_days.append(data)
    
    return seven_days