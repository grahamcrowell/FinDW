import pyFin
from pyFin import *
from pyFin.StockPrice import *
#pyFin.StockPrice.StockPrice('CAT')

s = StockPrice('MSFT')
print(s)


print(s._data.dtype.names)

all_dates = s['date']
all_open = s['open_price']
all_high = s['high_price']
print(all_dates)


simple_moving_average_FinTimeSeries10 = s.sma(10)
simple_moving_average_FinTimeSeries50 = s.sma(50)

cross_points = simple_moving_average_FinTimeSeries10 < simple_moving_average_FinTimeSeries50

