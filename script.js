Promise.all([

fetch("data/portfolio.json")
.then(response => response.json()),


fetch("data/market.json")
.then(response => response.json())


])


.then(([portfolioData, marketData]) => {


const portfolio =
document.getElementById("portfolio");


portfolio.innerHTML = "";



portfolioData.stocks.forEach(stock => {


const market =
marketData[stock.code];



const profit =
((market.price - stock.cost)
* stock.shares).toFixed(2);



const rate =
(((market.price-stock.cost)
/stock.cost)*100)
.toFixed(2);




const div =
document.createElement("div");



div.innerHTML = `


<p>

<strong>${stock.name}</strong>

</p>


<p>

股票代码：
${stock.code}

</p>


<p>

成本价：
${stock.cost}

</p>


<p>

当前价格：
${market.price}

</p>


<p>

今日涨跌：
${market.change}%

</p>



<p>

持仓盈亏：
${profit} 元

</p>



<p>

收益率：
${rate}%

</p>


<hr>


`;



portfolio.appendChild(div);



});


});





// 股票排名


fetch("data/ranking.json")


.then(response => response.json())


.then(rankingData => {



const ranking =
document.getElementById("ranking");



ranking.innerHTML="";



rankingData
.slice(0,5)
.forEach(stock=>{


const div =
document.createElement("div");



div.innerHTML=`


<p>

<strong>
${stock.name}
</strong>

</p>


<p>

代码：
${stock.code}

</p>


<p>

当前价格：
${stock.price}

</p>


<p>

今日涨跌：
${stock.change}%

</p>


<p>

评分：
${stock.score}

</p>


<hr>


`;



ranking.appendChild(div);



});



});
