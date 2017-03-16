import datetime
from enum import Enum
import pandas as pd
import xarray as xr
import numpy as np
import pandas_datareader.data as web


# start = datetime.datetime(2016,1,1)
# end = datetime.datetime(2017,1,1)

# df1 = web.DataReader('TSLA','yahoo',start,end)

# df2 = web.DataReader('AAPL','yahoo',start,end)


# # df1.to_csv('tsla.csv')

# # df2.to_csv('aapl.csv')

# print(df2.head())

df1 = pd.read_csv('tsla.csv',parse_dates = True,index_col = 0)

df2 = pd.read_csv('aapl.csv',parse_dates = True,index_col = 0)

TSLA = df1[['Adj Close','High']]

AAPL = df2[['Adj Close','High']]

# x1 = xarray.Dataset({'Dates':df1[Date]})

# print(x1)

a = xr.DataArray(TSLA)
b = xr.DataArray(AAPL)

print(a)
print('++++++++++++++++++++++++++++')
print(b)
print('++++++++++++++++++++++++++++')

c = xr.concat([a,b],dim='Stock')



print(c)

# c = xr.concat(a,b)


# b = ds.to_dataframe()

# print(b.index.values)

# print(b.head(5))