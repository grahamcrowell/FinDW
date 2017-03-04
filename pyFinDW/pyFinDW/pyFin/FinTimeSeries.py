import numpy as np

ohlc_vol_a = np.dtype(
    [('date', 'datetime64[D]'), ('open_price', np.float64), ('high_price', np.float64), ('low_price', np.float64), ('close_price', np.float64), ('volume', np.int64), ('adjusted_close_price', np.float64)])

time_series_dtype = np.dtype(
    [('date', 'datetime64[D]'), ('value', np.float64)])


class FinTimeSeries(object):
    """abstract base class for time series: list of pairs (ie table with 2 columns) = [ dates, values ]"""

    def __init__(self, label, date_array, value_array, **kwargs):
        print('init FinTimeSeries({}, len={})'.format(label, len(date_array)))
        self.__label = label
        self.__date_array = date_array
        self.__value_array = value_array
        # if isinstance(data, pyFin.StockPrice.StockPrice):
        #     print('stock price')
        #     self.__value_array = data.__getattribute__(default_OHLC_Vol_AdjC)
        # elif isinstance(data, np.ndarray):
        #     if data.dtype == ohlc_vol_a:
        #         print('ohlc_vol_a => open_price')
        #         self.__value_array = np.asarray([data['date'],data['open_price']], dtype=time_series_dtype)
        #         print(self.__value_array.shape)
        #         print(self.__value_array)
        #     elif data.dtype == time_series_dtype:
        #         print('time_series_dtype')
        #         self.__value_array = data
        #     else:
        #         """Wrapper around Date, Open, High, Low, Close, Volume, Adj Close dataset"""
        #         print('np.ndarray')
        #         raise NotImplementedError('only StockPrice and FinTimeSeries implemented')
        # elif isinstance(data, dict):
        #     print('dict recieved by FinTimeSeries')
        #     self.__value_array = data
        # else:
        #     raise NotImplementedError('only StockPrice and FinTimeSeries implemented')
        return super().__init__(**kwargs)

    def sma(self, length):
        """simple moving average"""
        ret = np.cumsum(self.__value_array, dtype=np.float64)
        ret[length:] = ret[length:] - ret[:-length]
        ret_ = ret[length - 1:] / length
        dt = self.__date_array[:len(ret_)]
        return FinTimeSeries('{}_sma{}'.format(self.__label, length), dt, ret_)

    def ema(self, length):
        """exponential moving average"""
        return FinTimeSeries('{}+ema{}'.format(self.__label, length), self.__value_array)

    def volitility(self, length):
        """ volitility """
        return FinTimeSeries('{}vol{}'.format(self.__label, length), self.__value_array)

    def __lt__(self, rhs):
        """self < rhs; wrapper around numpy.less; return piecewise comparison"""
        return FinTimeSeries(self.__label, np.less(self.__value_array, rhs.__value_array))

    def __str__(self):
        """to string; describe object/instance"""
        return 'FinTimeSeries ({} shape={})'.format(self.__label, self.__value_array.shape)

    def __repr__(self):
        """to string describe class"""
        return self.__label + '(len={})'.format(self.__value_array.shape)

    # def __getattribute__(self, name):
    #    """operator. <attribute_name> """
    #    return self.__value_array[name]

    def __getitem__(self, index):
        if index == 'date':
            return self.__date_array
        elif index == 'value':
            return self.__value_array
        else:
            """operator[ <column_name> ] """
            return self.__value_array[index]
