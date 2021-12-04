from datetime import datetime

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