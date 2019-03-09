from pandas_datareader import data
import pandas as pd

df = pd.read_csv('/Users/Kang/Desktop/HW1/content.csv')
t = df.columns.tolist()

startTime = '2016-01-01'
endTime = '2019-03-05'

for i in range(len(t)):
    d = df[t[i]].dropna().tolist()
    df1 = data.DataReader(d, 'yahoo', startTime, endTime)['Adj Close']
    df1.to_csv('/Users/Kang/Desktop/' + t[i] + '.csv')
