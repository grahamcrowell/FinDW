#import os
#import time
#import datetime
#import json
#import requests
#import pymssql
from datetime import date
#import download_csv_price
#import _internals.tools
#import pyFin.download_csv_price
#from pyFin import download_csv_price
#from _internals. import *
#from pyFin import _internals
import pyFin
import pyFin.FinTimeSeries
import pyFin._internals
import pyFin._internals.download_csv_price
from pyFin._internals.download_csv_price import *
#from pyFin._internals.download_csv_price import download_csv_price as download_csv_price

default_OHLC_Vol_AdjC = 'adjusted_close_price'


class StockPrice(pyFin.FinTimeSeries.FinTimeSeries):
    """Wrapper around Date, Open, High, Low, Close, Volume, Adj Close dataset"""
    def __init__(self, symbol):
        print('StockPrice({})'.format(symbol))
        self._symbol = symbol
        start_date = date(year=1900, month=1, day=1)
        download_job = PriceDownloadParam(symbol, start_date, None)
        downloaded_data = download(download_job)

        return super(StockPrice, self).__init__(symbol, downloaded_data)
   
    def __str__(self):
        return self._symbol

    #def __getitem__(self, index):
    #    if 

    #def __getattribute__(self, name):
        #return self._data[name]