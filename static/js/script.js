function fetchLiveData() {
    const symbol = document.getElementById('stock-symbol').value;
    fetch(`/live-data?symbol=${symbol}`)
        .then(response => response.text())
        .then(data => {
            document.getElementById('stock-data').innerHTML = data;
        })
        .catch(error => {
            console.error('Error fetching live data:', error);
        });
}
