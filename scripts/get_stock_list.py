import json
import requests


print("开始获取A股股票列表")


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
    headers=headers
)



result = response.json()



print("接口返回成功")


print("返回结构：")

print(result.keys())



print("data内容：")

print(result.get("data"))



print("diff类型：")

print(type(result["data"]["diff"]))



print("第一条数据：")

print(result["data"]["diff"][0])



print("第一条数据类型：")

print(type(result["data"]["diff"][0]))
