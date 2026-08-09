import akshare as ak
import json
import time


print("开始获取A股股票列表")


try:

    df = ak.stock_zh_a_spot_em()

except Exception as e:

    print("第一次获取失败，等待重试")

    time.sleep(5)

    df = ak.stock_zh_a_spot_em()



stocks = []


for _, row in df.iterrows():

    stocks.append({

        "code": str(row["代码"]),

        "name": row["名称"]

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
