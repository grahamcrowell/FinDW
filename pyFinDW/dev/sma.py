import pandas as pd
import numpy as n
import datetime
import pandas_datareader.data as web


def strategy_sma(high,low):
    sma1 = joined.rolling(window=high, min_periods=1).mean()
    sma2 = joined.rolling(window=low, min_periods=1).mean()
    #sma1 = sma1.dropna(how='all')
    #sma2 = sma2.dropna(how='all')
    return sma1
    return sma2

def findcrosses(symbol):
    #table = pd.merge(sma1[symbol],sma2[symbol],how='inner',on='dates')
    prevsma1 = sma1[symbol].shift(1)
    prevsma2 = sma2[symbol].shift(1)
    buycross = sma1[symbol] <= sma2[symbol] & prevsma1 >= prevsma2
    sellcross = sma1[symbol] >= sma2[symbol] & prevsma1 <= prevsma2
