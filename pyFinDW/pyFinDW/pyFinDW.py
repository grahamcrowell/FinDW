import pyFin
from pyFin import *
from pyFin.StockPrice import *


s = StockPrice('MSFT')

date_column = s['date']
print(len(date_column))
print(s['open_price'])
print(s['high_price'])
# ma is object of the FinTimeSeries class
ma = s.sma(10)
# all FinTimeSeries class objects have 'date' and 'value' member variables
# they are accessed by via index operator (like a dict)
dts = ma['date']
vals = ma['value']
# dts and val are numpy arrays
# loop over elements

for dt in dts:
	print(dt)

for val in vals:
	print(val)

# todo: validate that s.sma(10) really simple moving average with lag of 10
