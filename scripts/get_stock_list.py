import requests


print("开始测试东方财富沪深京A股股票池")


url = "https://push2.eastmoney.com/api/qt/clist/get"


params = {
    "pn": 1,
    "pz": 20,
    "po": 1,
    "np": 1,
    "fltt": 2,
    "invt": 2,
    "fid": "f3",
    "fs": "b:MK0002",
    "fields": "f12,f14"
}


headers = {
    "User-Agent": "Mozilla/5.0"
}


response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=15
)


print("状态码：", response.status_code)
print("返回长度：", len(response.text))


if response.status_code != 200:
    raise Exception("接口请求失败")


result = response.json()


if not result.get("data"):
    raise Exception("接口没有返回 data")


data = result["data"]


print("东方财富返回的股票总数：", data.get("total"))


diff = data.get("diff", {})


print("本次测试返回：", len(diff), "只")


for key, stock in list(diff.items())[:10]:
    print(
        stock.get("f12"),
        stock.get("f14")
    )


print("股票池接口测试完成")
