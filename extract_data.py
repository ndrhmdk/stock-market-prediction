import os
import pandas as pd

def get_aapl_data():
    try:
        if os.path.exists('aapl.csv'):
            aapl = pd.read_csv('aapl.csv', index_col='Date', parse_dates=True)
            aapl.index = pd.to_datetime(aapl.index, utc=True)
            aapl.index = aapl.index.tz_localize(None)
            print("Loaded data from aapl.csv")
        else:
            import yfinance as yf
            starttime = '2005-01-01'
            endtime = '2025-01-01'
            aapl = yf.Ticker("AAPL").history(start=starttime, end=endtime)
            aapl.to_csv('aapl.csv')
            print("Downloaded data using yfinance and saved to CSV.")
        return aapl
    except Exception as e:
        print("Error occurred:", e)
        return None
