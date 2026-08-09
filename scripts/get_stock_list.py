import akshare as ak
import json


print("开始获取A股股票列表")


df = ak.stock_info_a_code_name()


stocks = []


for _, row in df.iterrows():

    stocks.append({

        "code": row["code"],

        "name": row["name"]

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


print("股票数量:", len(stocks))

print("股票列表生成完成")

print("股票池生成完成")
