import json
import requests
import time


print("开始生成A股股票池")


url = "https://push2.eastmoney.com/api/qt/clist/get"


headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://quote.eastmoney.com/"
}


stocks = []


for page in range(1, 60):


    print("获取第", page, "页")


    params = {

        "pn": page,

        "pz": 100,

        "po": 1,

        "np": 1,

        "fltt": 2,

        "invt": 2,

        "fid": "f3",

        "fs": "m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23",

        "fields": "f12,f14"

    }


    try:

        response = requests.get(

            url,

            params=params,

            headers=headers,

            timeout=15

        )


        result = response.json()


        diff = result["data"]["diff"]


        if not diff:

            break



        for item in diff:

            stocks.append({

                "code": item["f12"],

                "name": item["f14"]

            })


        print(
            "当前数量:",
            len(stocks)
        )


        time.sleep(1)



    except Exception as e:

        print(
            "第",
            page,
            "页失败:",
            e
        )

        time.sleep(5)

        continue




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
    "最终股票数量:",
    len(stocks)
)

print("股票池生成完成")
