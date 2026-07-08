async function loadData() {
    const response = await fetch("http://127.0.0.1:8000/report");

    const data = await response.json();

    document.getElementById("risk-score").innerText =
        "Risk Score: " + data.risk_score;

    let html = "";

    for (let key in data.results) {
        html += `<p><b>${key}</b>: ${data.results[key]}</p>`;
    }

    document.getElementById("results").innerHTML = html;
}

loadData();