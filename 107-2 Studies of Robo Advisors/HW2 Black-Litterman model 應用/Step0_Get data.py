from pandas_datareader import data
import pandas as pd

startTime = '2008-01-01'
endTime = '2017-12-31'

d = ['AGG', 'EMB', 'EWT', 'IVV', 'JNK', 'PFF', 'TLT', 'VGK', 'VNQ', 'VPL', 'VWO']
df1 = data.DataReader(d, 'yahoo', startTime, endTime)['Adj Close']
df1.to_csv('/Users/Kang/Desktop/ETF 2008_2017.csv')
