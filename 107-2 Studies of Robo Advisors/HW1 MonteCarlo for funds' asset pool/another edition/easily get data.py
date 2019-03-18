import pandas as pd
import datetime as dt
import pandas_datareader.data as web

database = pd.DataFrame()
tickers = ['AAPL', 'FB', 'GOOG', 'MSFT']

for i in tickers:
    tmp = web.DataReader(i, 'yahoo', '1/1/2010', dt.date.today())
    database[i] = tmp['Adj Close']

