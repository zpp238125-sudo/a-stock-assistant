import json

with open("data/portfolio.json", "r", encoding="utf-8") as f:
    portfolio = json.load(f)


print("股票助手自动更新程序启动")

for stock in portfolio["stocks"]:
    print(stock["code"], stock["name"])
