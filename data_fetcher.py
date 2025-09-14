import yfinance as yf

# Fetch stock data for a given ticker and date range
def get_stock_data(ticker):
    stock = yf.Ticker(ticker) 
    df = stock.history(period="1d", interval="5m")
    high_price = round(df["High"].max(), 2)
    low_price = round(df["Low"].min(), 2)
    return high_price, low_price

# this will be modified eventually to fetch real news
def fetch_dummy_news(ticker):
    return [
        f"{ticker} reports strong earnings amid AI demand surge",
        f"Analysts warn {ticker} stock might be overvalued after rally",
        f"{ticker} announces new partnership with cloud provider",
        f"Market volatility impacts {ticker} investor sentiment"
    ]