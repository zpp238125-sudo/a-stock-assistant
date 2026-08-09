import json
import requests
import time


print("开始获取A股股票列表")


url = "https://push2.eastmoney.com/api/qt/clist/get"


headers = {
    "User-Agent": "Mozilla/5.0"
}


stocks = []


page_size = 100



for page in range(1, 40):


    print("正在获取第", page, "页")


    success = False



    for retry in range(3):

        try:


            params = {

                "pn": page,

                "pz": page_size,

                "fs": "m:0+t:6,m:1+t:2",

                "fields": "f12,f14"

            }



            response = requests.get(

                url,

                params=params,

                headers=headers,

                timeout=10

            )



            if not response.text:

                raise Exception("返回为空")



            result = response.json()


            success = True

            break



        except Exception as e:


            print(
                "第",
                page,
                "页失败，重试",
                retry+1
            )


            time.sleep(2)



    if not success:

        print(
            "第",
            page,
            "页跳过"
        )

        continue



    data = result.get("data")



    if not data:

        break



    diff = data.get("diff")



    if not diff:

        break



    for key,item in diff.items():

        stocks.append({

            "code": item["f12"],

            "name": item["f14"]

        })



    print(
        "已获取:",
        len(stocks)
    )



    time.sleep(1)




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
    "股票池最终数量:",
    len(stocks)
)


print("股票池更新完成")
