import json
import requests


print("开始获取行情")


with open("data/all_stocks.json", "r", encoding="utf-8") as f:
    stocks = json.load(f)


market = {}


for stock in stocks:

    code = stock["code"]

    if code.startswith("6"):
        symbol = "sh" + code
    else:
        symbol = "sz" + code


    url = f"https://qt.gtimg.cn/q={symbol}"


    try:
        response = requests.get(url)

        data = response.text


        parts = data.split("~")


        price = float(parts[3])
        change = float(parts[32])


        market[code] = {
            "name": stock["name"],
            "price": price,
            "change": change
        }


        print(stock["name"], price, change)


    except Exception as e:
        print(code, "获取失败", e)



with open("data/market.json", "w", encoding="utf-8") as f:
    json.dump(
        market,
        f,
        ensure_ascii=False,
        indent=2
    )


print("行情更新完成")
