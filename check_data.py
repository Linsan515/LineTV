import datetime
import re

#檢測資料值是否有缺漏或格式有誤
def validation(data_dic):
    
    pattern = re.compile(r'(.*)\.(.*)\.(.*)')
    keys = ["ad_network", "unit_id", "request", "imp", "revenue", "date", "app_name"]
    
    #若dict長度不足7，則表示資料有缺漏
    if len(data_dic) != 7:
        return 0
    
    for key, value in data_dic.items():
        #檢測key值是否在預設中
        if key not in keys:
            return 0
        #檢測資料值是否有缺漏
        if value == "" or value is None:
            return 0
        #檢測資料值格式是否正確
        if type(value) != str:
            return 0
    
    #檢測時間格式是否正確
    try:
        datetime.datetime.strptime(data_dic["date"], "%Y-%m-%d")
    except ValueError:
        return 0
    
    #檢測部分資料值是否為整數或小數
    if not data_dic["unit_id"].isnumeric():
        return 0
    elif not data_dic["request"].isnumeric():
        return 0
    elif not data_dic["imp"].isnumeric():
        return 0
    elif pattern.match(data_dic["revenue"]):
        return 0
    elif not data_dic["revenue"].replace(".","").isnumeric():
        return 0
    else:
        return 1
    
    