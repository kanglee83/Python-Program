import pandas as pd

df1 = pd.read_csv('/Users/Kang/Desktop/HW1/Betterment.csv')
df2 = pd.read_csv('/Users/Kang/Desktop/HW1/WiseBanyan.csv')
df3 = pd.read_csv('/Users/Kang/Desktop/HW1/Charles_Schwab.csv')
df4 = pd.read_csv('/Users/Kang/Desktop/HW1/Ellevest.csv')

df1.set_index("Date", inplace=True)
df2.set_index("Date", inplace=True)
df3.set_index("Date", inplace=True)
df4.set_index("Date", inplace=True)
