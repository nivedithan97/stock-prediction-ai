# stock_scheduler.py

import yfinance as yf
import pandas as pd
from datetime import datetime
import pandas_market_calendars as mcal
import pytz

# ======= CONFIG =======
fav_stocks = ['NVDA', 'MSTR', 'MRK', 'AVGO']
output_file = 'hourly_stock_report.xlsx'
sgt = pytz.timezone("Asia/Singapore")
# ======================

def is_trading_day(date: datetime) -> bool:
    """Check if date is a valid US trading day (NYSE calendar)."""
    nyse = mcal.get_calendar('XNYS')
    schedule = nyse.schedule(start_date=date.strftime("%Y-%m-%d"),
                             end_date=date.strftime("%Y-%m-%d"))
    return not schedule.empty

def fetch_hourly_data():
    today = datetime.today()

    if not is_trading_day(today):
        print(f"{today.date()} is not a trading day. Skipping...")
        return

    with pd.ExcelWriter(output_file) as writer:
        for stock in fav_stocks:
            print(f"Fetching hourly data for {stock}...")

            data = yf.download(stock, period="1d", interval="1h", auto_adjust=True)

            if data.empty:
                print(f"No data found for {stock}, skipping...")
                continue

            # Handle timezone properly
            if data.index.tz is None:
                data.index = data.index.tz_localize("UTC").tz_convert(sgt)
            else:
                data.index = data.index.tz_convert(sgt)

            # Keep only regular U.S. trading hours in SGT (21:30–04:00 next day)
            start = datetime.strptime("21:30", "%H:%M").time()
            end = datetime.strptime("04:00", "%H:%M").time()
            mask = (data.index.time >= start) | (data.index.time <= end)
            data = data[mask]

            if data.empty:
                print(f"No trading-hours data for {stock}, skipping sheet...")
                continue

            # Remove timezone info for Excel compatibility
            data.index = data.index.tz_localize(None)

            data.to_excel(writer, sheet_name=stock)

    print(f"Hourly stock report saved to {output_file}")

if __name__ == "__main__":
    fetch_hourly_data()
