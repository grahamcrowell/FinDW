import datetime
from enum import Enum
import pandas as pd
import numpy as np
import pandas_datareader.data as web


start = datetime.datetime(2016,1,1)
end = datetime.datetime(2017,1,1)

# get data
df1 = web.DataReader('TSLA','yahoo',start,end)
df2 = web.DataReader('AAPL','yahoo',start,end)
# turn into data frame
dfA=pd.DataFrame({'date':list(df1.index),'open':df1.Open})
dfB=pd.DataFrame({'date':list(df2.index),'open':df2.Open})
# merge into single data frame
joined = pd.merge(dfA,dfB,how='outer',on='date')


