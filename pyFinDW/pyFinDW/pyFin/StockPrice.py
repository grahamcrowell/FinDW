from datetime import date
import pyFin
import pyFin.FinTimeSeries
import pyFin._internals
import pyFin._internals.download_csv_price
from pyFin._internals.download_csv_price import *

default_OHLC_Vol_AdjC = 'adjusted_close_price'


class StockPrice(pyFin.FinTimeSeries.FinTimeSeries):
    """Wrapper around Date, Open, High, Low, Close, Volume, Adj Close dataset"""

    def __init__(self, symbol):
        print('StockPrice({})'.format(symbol))
        self._symbol = symbol
        start_date = date(year=1900, month=1, day=1)
        download_job = PriceDownloadParam(symbol, start_date, None)
        self.__stock_price_data_dict = download(download_job)
        return super(StockPrice, self).__init__(symbol, self.__stock_price_data_dict['date'], self.__stock_price_data_dict['adjusted_close_price'])

    def __str__(self):
        """python's to string"""
        return self._symbol

    def ema(self, length):
        return super(StockPrice, self).ema(length)

    def sma(self, length):
        return super(StockPrice, self).sma(length)

    def volitility(self, length):
        return super(StockPrice, self).volitility(length)

    def __getitem__(self, dict_key):
        """operator[ <column_name> ] """
        return self.__stock_price_data_dict[dict_key]
