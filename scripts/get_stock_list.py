import json
import requests


print("开始获取A股股票列表")


url = "https://qt.gtimg.cn/q=sh000001"


# 测试接口连接
response = requests.get(url)

print("行情接口连接成功")


# 暂时先创建股票池文件
stocks = [

    {
        "code": "600597",
        "name": "光明乳业"
    },

    {
        "code": "600737",
        "name": "中粮糖业"
    },

    {
        "code": "601985",
        "name": "中国核电"
    },

    {
        "code": "002167",
        "name": "东方锆业"
    }

]


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


print("股票列表更新完成")
