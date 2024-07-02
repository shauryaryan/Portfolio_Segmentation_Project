import yfinance as yf

def fetch_historical_data(ticker, period='5y'):
    stock = yf.Ticker(ticker)
    return stock.history(period=period)
