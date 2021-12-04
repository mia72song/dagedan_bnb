from datetime import datetime

# 日期的字串格式：yyyy-mm-dd
dateFormatter = "%Y-%m-%d"

# 將由資料庫取得的預約日期，整理成dict格式
def bookingDateFormatter(result):
    cols = ["date", "room_no", "order_id", "weekday", "is_holiday", "note"]
    data_dict = dict(zip(cols, result))
    # date 轉字串
    data_dict["date"] = datetime.strftime(data_dict["date"], dateFormatter)
    # is_holiday 轉bool值
    is_holiday = result[-2]
    if is_holiday:
        data_dict["is_holiday"] = True
    else:
        data_dict["is_holiday"] = False
    
    return data_dict

# 將由資料庫取得的房間資訊，整理成dict格式
def roomFormatter(result):
    cols = ["room_no", "name", "type", "accommodate", "rate_weekday", "rate_holiday", "single_discount"]
    data_dict = dict(zip(cols, result))
    data_dict["rate_weekday"] = float(data_dict["rate_weekday"])
    data_dict["rate_holiday"] = float(data_dict["rate_holiday"])
    return data_dict