import requests


print("开始测试股票接口")


url = "https://push2.eastmoney.com/api/qt/clist/get"


params = {

    "pn": 1,
    "pz": 10,
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


print("状态码:")
print(response.status_code)


print("返回长度:")
print(len(response.text))


print("返回前500字符:")
print(response.text[:500])
