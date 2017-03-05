import pyFin
from pyFin import *
from pyFin.StockPrice import *

# single stock example
stockPriceBuilder = StockPriceBuilder('MSFT')
print(stockPriceBuilder)
stockPrice = stockPriceBuilder.GetStockPrice()
print(stockPrice)
adjCloseTS = stockPrice.GetAdjCloseTS()
print(adjCloseTS)
print(adjCloseTS.GetDates()[0])
adjCloseTSSMA10 = adjCloseTS.sma(10)[0:-40]
print(adjCloseTSSMA10)
print(adjCloseTSSMA10.GetDates()[0])
adjCloseTSSMA50 = adjCloseTS.sma(50)
print(adjCloseTSSMA50)
print(adjCloseTSSMA50.GetDates()[0])
print(adjCloseTSSMA50.GetDates())

print('-----------------------------------------------')




# figure out sma crosses
# array of TRUEs and FALSEs.  element of short_lt_long_bool_idx is TRUE when adjCloseTSSMA10 < adjCloseTSSMA50
short_lt_long_bool_idx = adjCloseTSSMA10 < adjCloseTSSMA50
# cross points are when adjacent values of short_lt_long_bool_idx aren't equal
cross_pt_idxs = []
prev = short_lt_long_bool_idx[0]
for i in range(1,len(a)-1):
    if short_lt_long_bool_idx[i] != prev:
        cross_pt_idxs.append(i)
        prev = short_lt_long_bool_idx[i]

# print out cross points 
for idx in cross_pt_idxs:
    print('on {}\n\tthe adjCloseTSSMA10 was {}'.format(adjCloseTSSMA10.GetDates()[idx-1], adjCloseTSSMA10.GetValues()[idx-1]))
    print('\tthe adjCloseTSSMA50 was {}'.format(adjCloseTSSMA50.GetValues()[idx-1]))
    print('the next day...')
    print('\tthe adjCloseTSSMA10 was {}'.format(adjCloseTSSMA10.GetValues()[idx]))
    print('\tthe adjCloseTSSMA50 was {}'.format(adjCloseTSSMA50.GetValues()[idx]))


# same thing with list of symbols (later we get all symbols from a sql query to our db
#stock_symbol_list = ['MSFT','CAT','APPL','ORCL']
#for stock_symbol in stock_symbol_list:
#    print('current stock in loop: {}'.format(stock_symbol))
#    stockPriceBuilder = StockPriceBuilder(stock_symbol)
#    print(stockPriceBuilder)
#    stockPrice = stockPriceBuilder.GetStockPrice()
#    print(stockPrice)
#    adjCloseTS = stockPrice.GetAdjCloseTS()
#    print(adjCloseTS)
#    adjCloseTSSMA = adjCloseTS.sma(10)
#    print(adjCloseTSSMA)

## todo: validate with unit test that sma(10) really simple moving average with lag of 10
## todo: implement detection of cross points of 2 FinTimeSeries objects
## todo: ema and volitilty
## todo: simple matplotlib graph
## todo: cloud sql db

