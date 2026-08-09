import json


print("股票分析模块启动")


with open("data/market.json", "r", encoding="utf-8") as f:
    market = json.load(f)


ranking = []


for code, stock in market.items():

    score = 0

    if stock["change"] > 0:
        score += 10

    if stock["change"] > 3:
        score += 10


    ranking.append({
        "code": code,
        "name": stock["name"],
        "price": stock["price"],
        "change": stock["change"],
        "score": score
    })


ranking.sort(
    key=lambda x:x["score"],
    reverse=True
)


with open("data/ranking.json", "w", encoding="utf-8") as f:
    json.dump(
        ranking,
        f,
        ensure_ascii=False,
        indent=2
    )


print("分析完成")
