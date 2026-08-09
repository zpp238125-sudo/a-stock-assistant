import json
import requests


print("开始获取A股股票列表")


url = "https://qt.gtimg.cn/q=sh000001"


headers = {
    "User-Agent": "Mozilla/5.0"
}


response = requests.get(
    url,
    headers=headers
)


if response.status_code == 200:

    print("接口连接成功")


else:

    print("接口连接失败")



# 临时股票池测试

stocks = []


# 沪市股票示例
sh_codes = [
    "600597",
    "600737",
    "601985"
]


# 深市股票示例
sz_codes = [
    "002167"
]



for code in sh_codes:

    stocks.append(
        {
            "code": code,
            "name": ""
        }
    )



for code in sz_codes:

    stocks.append(
        {
            "code": code,
            "name": ""
        }
    )



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
    "股票池生成完成:",
    len(stocks)
)
