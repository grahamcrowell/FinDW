# High Level Logical Flow:

1. Entry Point Class
    - collects/reads/encapsulates all the settings/configurations for a single BackTest instance
    - output: instance of Back Test Config Class
1. Back Test Config Class
    - Stores all the settings/parameters/configurations required by the Back Test Class
    - Start Date, End Date, Stock List,...?
1. Data Getter Class 
    - input: instance of Back Test Class
    - Use info from input to know what data is required then queries some data source (csv file, database, internet, whatever)
    - output: instance(s) Price Series Class
1. Price Series Class
    - Maybe just a Pandas array, maybe this isn't needed
1. Crystal Ball Class 
    - input: instance of Price Series Class
    - generates buy or don't buy signals for each stock for each day
    - output: instance(s) Buy Signal Series
1. Buy Signal Series 
    - Maybe just a Panada array, maybe this isn't needed
1. Balancer Class 
    - input: instance(s) Buy Signal Series
    - implements daily re-balancing of holdings according input
    - output: instance Portfolio Class
1. Portfolio Class
    - all sorts of analytics
        - overall return calculation
        - volatility
        - Sharpe Ratio
        - daily return calculations 

# Stock Trading Strategy Backtesting

# Back testing engine

1. sell every thing we bought yesterday at today's prices
    1. determine % change in stock price of all stocks bought yesterday
    1. determine % change of holding
        1. yesterdays allocation * % change of stock price
1. determine which stocks are a buy at today's prices
    1. for each stock crystal ball says whether or not to buy
1. determine today's allocation for the buys
    1. 1 / count of buys signals
1. hold stocks.  go to tomorrow.

