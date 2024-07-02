# import yfinance as yf
# import requests
# from bs4 import BeautifulSoup
#
# def fetch_stock_data(ticker):
#     stock = yf.Ticker(ticker)
#     return stock.history(period="1d")
#
# def fetch_news_data(query):
#     url = f'https://news.google.com/search?q={query}'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     headlines = [a.text for a in soup.find_all('a', class_='DY5T1d')]
#     return headlines
import requests
import pandas as pd

ALPHA_VANTAGE_API_KEY = 'A023YS5YCVHJ92EH'

def fetch_live_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame.from_dict(data['Time Series (5min)'], orient='index')
    df = df.astype(float)
    return df

# Example usage
if __name__ == "__main__":
    symbol = 'AAPL'
    live_data = fetch_live_stock_data(symbol)
    print(live_data.head())
