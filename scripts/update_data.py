import json

print("股票助手自动更新程序启动")


with open("data/all_stocks.json", "r", encoding="utf-8") as f:
    stocks = json.load(f)


print("股票池数量：", len(stocks))


for stock in stocks:
    print(
        stock["code"],
        stock["name"]
    )
