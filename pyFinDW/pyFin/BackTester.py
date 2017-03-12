from enum import Enum


class StockUniverse(object):
    """contains all stocks available to BackTester.
    This will store FinTimeSeries objects for all stocks.
    """

    def __init__(self, start_date, end_date):
        self.__start_date = start_date
        self.__end_date = end_date

    def get_available_stocks(self, date):
        """returns collection of FinTimeSeries objects
        that are available for purchase by a BackTester
        on the given date"""
        raise NotImplemented


class Recommendation(Enum):
    """simple flag indicating a BUY or SELL Recommendation"""
    SELL = -1
    BUY = 1


class Strategy(object):
    def __init__(self):
        pass

    def get_recommendation(self, time_series):
        """recieves a FinTimeSeries object containing stock price data.
        returns recommdation from point of view of last day in time series"""
        return Recommendation.BUY
        raise NotImplemented


class BackTester(object):
    """main back testing engine"""

    def __init__(self, strategy, stock_universe):
        self.__strategy = strategy
        self.__stock_universe = stock_universe
        self.__portfolio_total_weighting = 100.0
        self.__strategy = strategy

    def begin(self):
        pass

    def rate_of_return(self):
        """returns the profitability of strategy"""
        pass
        raise NotImplemented
