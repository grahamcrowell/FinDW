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
adjCloseTSSMA = adjCloseTS.sma(10)
print(adjCloseTSSMA)


# same thing with list of symbols (later we get all symbols from a sql query to our db
stock_symbol_list = ['MSFT','CAT','APPL','ORCL']
for stock_symbol in stock_symbol_list:
    print('current stock in loop: {}'.format(stock_symbol))
    stockPriceBuilder = StockPriceBuilder(stock_symbol)
    print(stockPriceBuilder)
    stockPrice = stockPriceBuilder.GetStockPrice()
    print(stockPrice)
    adjCloseTS = stockPrice.GetAdjCloseTS()
    print(adjCloseTS)
    adjCloseTSSMA = adjCloseTS.sma(10)
    print(adjCloseTSSMA)

# todo: validate with unit test that sma(10) really simple moving average with lag of 10
# todo: implement detection of cross points of 2 FinTimeSeries objects
# todo: ema and volitilty
# todo: simple matplotlib graph
# todo: cloud sql db

