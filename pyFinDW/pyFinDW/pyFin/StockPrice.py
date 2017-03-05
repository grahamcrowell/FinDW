from datetime import date
import pyFin
import pyFin.FinTimeSeries
import pyFin._internals
import pyFin._internals.download_csv_price
#from pyFin._internals.download_csv_price import *

default_OHLC_Vol_AdjC = 'adjusted_close_price'

class StockPriceBuilder(object):
    def __init__(self, symbol, start_date=None, end_date=None):
        print('init StockPriceBuilder({})'.format(symbol))
        self.__symbol = symbol
        if start_date == None:
            self.__start_date = date(1900,1,1)
        else:
            self.__start_date = start_date
        if end_date == None:
            self.__end_date = date.today()
        else:
            self.__end_date = end_date
        
    def GetStockPrice(self):
        """downloads prices data, initializes StockPrice object with data, then returns it
        TODO: add logic to check if data already exists (in database or local csv)"""
        tmp_param = pyFin._internals.download_csv_price.PriceDownloadParam(self.__symbol, self.__start_date, self.__end_date)
        data = pyFin._internals.download_csv_price.download(tmp_param)
        return StockPrice(self.__symbol, **data)

    def __str__(self):
        return 'StockPriceBuilder {}'.format(self.__symbol)

class StockPrice(object):
    """Composition of numpy arrays for Date, Open, High, Low, Close, Volume, Adj Close
    """
    def __init__(self, symbol, date_arr, open_arr, high_arr, low_arr, close_arr, volume_arr, adj_close_arr):
        print('init StockPrice({}, len={})'.format(symbol, len(date_arr)))
        self.__symbol = symbol
        self.__date_arr = date_arr
        self.__open_arr = open_arr
        self.__high_arr = high_arr
        self.__low_arr = low_arr
        self.__close_arr = close_arr
        self.__volume_arr = volume_arr
        self.__adj_close_arr = adj_close_arr
        assert len(self.__date_arr) == len(self.__open_arr) == len(self.__high_arr) == len(self.__low_arr) == len(self.__close_arr) == len(self.__volume_arr)

    def __str__(self):
        """python's to string"""
        return 'StockPrice ({})'.format(self.__symbol)

    def GetOpenTS(self):
        """returns FinTimeSeries object containing open """
        return pyFin.FinTimeSeries.FinTimeSeries('{}({})'.format(self.__symbol, 'open'),self.__date_arr,self.__open_arr)
    def GetHighTS(self):
        """returns FinTimeSeries object containing high """
        return pyFin.FinTimeSeries.FinTimeSeries('{}({})'.format(self.__symbol, 'high'),self.__date_arr,self.__high_arr)
    def GetLowTS(self):
        """returns FinTimeSeries object containing low """
        return pyFin.FinTimeSeries.FinTimeSeries('{}({})'.format(self.__symbol, 'low'),self.__date_arr,self.__low_arr)
    def GetCloseTS(self):
        """returns FinTimeSeries object containing close """
        return pyFin.FinTimeSeries.FinTimeSeries('{}({})'.format(self.__symbol, 'close'),self.__date_arr,self.__close_arr)
    def GetVolumeTS(self):
        """returns FinTimeSeries object containing volume """
        return pyFin.FinTimeSeries.FinTimeSeries('{}({})'.format(self.__symbol, 'volume'),self.__date_arr,self.__volume_arr)
    def GetAdjCloseTS(self):
        """returns numpy FinTimeSeries object containing adj_close """
        return pyFin.FinTimeSeries.FinTimeSeries('{}({})'.format(self.__symbol, 'adj_close'),self.__date_arr,self.__adj_close_arr)
    

    def GetDateArr(self):
        """returns numpy 1d array (dtype=datetime64[D]) of Date"""
        return self.__date_arr
    def GetOpenArr(self):
        """returns numpy 1d array (dtype=float64) of Open"""
        return self.__open_arr
    def GetHighArr(self):
        """returns numpy 1d array (dtype=float64) of High"""
        return self.__high_arr
    def GetLowArr(self):
        """returns numpy 1d array (dtype=float64) of Low"""
        return self.__low_arr
    def GetCloseArr(self):
        """returns numpy 1d array (dtype=float64) of Close"""
        return self.__close_arr
    def GetVolumeArr(self):
        """returns numpy 1d array (dtype=int64) of Volume"""
        return self.__volume_arr
    def GetAdjCloseArr(self):
        """returns numpy 1d array (dtype=float64) of AdjClose"""
        return self.__adj_close_arr

    #def ema(self, length):
    #    return super(StockPrice, self).ema(length)

    #def sma(self, length):
    #    return super(StockPrice, self).sma(length)

    #def volitility(self, length):
    #    return super(StockPrice, self).volitility(length)

    #def __getitem__(self, dict_key):
    #    """operator[ <column_name> ] """
    #    return self.__stock_price_data_dict[dict_key]
