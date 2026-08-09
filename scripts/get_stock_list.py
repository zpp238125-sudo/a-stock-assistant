import requests

print("开始测试东方财富A股接口")


url = "https://push2.eastmoney.com/api/qt/clist/get"


params = {
    "pn": 1,
    "pz": 20,
    "po": 1,
    "np": 1,
    "fltt": 2,
    "invt": 2,
    "fid": "f3",

    "fs": "m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23",

    "fields": "f12,f14,f2,f3"
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


print("状态码：", response.status_code)

print("返回长度：", len(response.text))

print("返回前500字符：")

print(response.text[:500])
