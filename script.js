fetch("data/portfolio.json")
    .then(response => response.json())
    .then(data => {

        const portfolio = document.getElementById("portfolio");

        portfolio.innerHTML = "";

        data.stocks.forEach(stock => {

            const div = document.createElement("div");

            div.innerHTML = `
                <p>
                <strong>${stock.name}</strong>
                </p>

                <p>
                股票代码：${stock.code}
                </p>

                <p>
                成本价：${stock.cost}
                </p>

                <p>
                持股数量：${stock.shares}股
                </p>

                <hr>
            `;

            portfolio.appendChild(div);

        });

    });
