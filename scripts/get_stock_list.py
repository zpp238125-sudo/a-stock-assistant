import json
import requests


print("开始生成A股股票池")


url = "https://push2.eastmoney.com/api/qt/clist/get"


params = {
    "pn": 1,
    "pz": 6000,
    "po": 1,
    "np": 1,
    "fltt": 2,
    "invt": 2,
    "fid": "f3",
    "fs": "m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23",
    "fields": "f12,f14"
}


headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://quote.eastmoney.com/"
}


response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=15
)


result = response.json()


items = result["data"]["diff"]


stocks = []


for item in items:

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


print(
    "股票池数量:",
    len(stocks)
)


print(
    "股票池生成完成"
)
