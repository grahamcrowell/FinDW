import numpy as np
import pyFin.StockPrice

ohlc_vol_a = np.dtype(
    [('date', 'datetime64[D]')
        ,('open_price', np.float64)
        ,('high_price', np.float64)
        ,('low_price', np.float64)
        ,('close_price', np.float64)
        ,('volume', np.int64)
        ,('adjusted_close_price', np.float64)])

time_series_dtype = np.dtype(
    [('date', 'datetime64[D]')
        ,('value', np.float64)])

class FinTimeSeries(object):
    """abstract base class for time series: list of pairs (ie table with 2 columns) = [ dates, values ]"""
    def __init__(self, label, data, **kwargs):
        self._label = label
        if isinstance(data, pyFin.StockPrice.StockPrice):
            print('stock price')
            self._data = data.__getattribute__(default_OHLC_Vol_AdjC)
        elif isinstance(data, np.ndarray):
            if data.dtype == ohlc_vol_a:
                print('ohlc_vol_a => open_price')
                self._data = np.asarray([data['date'],data['open_price']], dtype=time_series_dtype)
                print(self._data.shape)
                print(self._data)
            elif data.dtype == time_series_dtype:
                print('time_series_dtype')
                self._data = data
            else:
                """Wrapper around Date, Open, High, Low, Close, Volume, Adj Close dataset"""
                print('np.ndarray')
                raise NotImplementedError('only StockPrice and FinTimeSeries implemented')
        else:
            raise NotImplementedError('only StockPrice and FinTimeSeries implemented')
        return super().__init__(**kwargs)

    def sma(self, length):
        """simple moving average"""
        print(self['value'])
        ret = np.cumsum(self._data['value'], dtype=np.float64)
        ret[length:] = ret[length:] - ret[:-length]
        ret_ = ret[length - 1:] / length
        dt = self._data['date'][:(len(ret_)-1)]
        return FinTimeSeries('{}_sma{}'.format(self._label, length), np.asarray([dt, ret_], dtype=time_series_dtype))

    def ema(self, length):
        """exponential moving average"""
        return FinTimeSeries('{}+ema{}'.format(self._label, length), self._data)
    
    def volitility(self, length):
            """volitility"""
            return FinTimeSeries('{}vol{}'.format(self._label, length), self._data)

    def __lt__(self, rhs):
        """self < rhs; wrapper around numpy.less; return piecewise comparison"""
        #rhs._data = np.array(rhs)
        return FinTimeSeries(self._label,np.less( self._data, rhs._data))

    def __str__(self):
        """to string; describe object/instance"""
        return self._label + '(len={})'.format(self._data.shape)

    def __repr__(self):
        """to string describe class"""
        return self._label + '(len={})'.format(self._data.shape)

    #def __getattribute__(self, name):
    #    """operator. <attribute_name> """
    #    return self._data[name]

    def __getitem__(self, index):
        """operator[ <column_name> ] """
        return self._data[index]
