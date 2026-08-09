import json
import requests


print("开始获取A股股票列表")


url = "https://push2.eastmoney.com/api/qt/clist/get"


params = {

    "pn": 1,

    "pz": 6000,

    "fs": "m:0+t:6,m:1+t:2",

    "fields": "f12,f14"

}


headers = {

    "User-Agent": "Mozilla/5.0"

}


response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=10
)



result = response.json()



items = result["data"]["diff"]



stocks = []



for key, item in items.items():

    stocks.append({

        "code": item["f12"],

        "name": item["f14"]

    })




with open(
    "data/all_stocks.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        stocks,
        f,
        ensure_ascii=False,
        indent=2
    )



print("股票池数量:", len(stocks))

print("股票池更新完成")
