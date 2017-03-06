import numpy as np
import numbers

ohlc_vol_a = np.dtype(
    [('date', 'datetime64[D]'), ('open_price', np.float64), ('high_price', np.float64), ('low_price', np.float64), ('close_price', np.float64), ('volume', np.int64), ('adjusted_close_price', np.float64)])

time_series_dtype = np.dtype(
    [('date', 'datetime64[D]'), ('value', np.float64)])


class FinTimeSeries(object):
    """class for time series: list of pairs (ie table with 2 columns) = [ dates, values ]"""

    def __init__(self, label, date_arr, value_arr, **kwargs):
        print('init FinTimeSeries({}, len={})'.format(label, len(date_arr)))
        self.__label = label
        self.__date_arr = date_arr
        self.__value_arr = value_arr
        assert len(self.__date_arr) == len(self.__value_arr)
        # return super().__init__(**kwargs)

    def GetDates(self):
        return self.__date_arr

    def GetValues(self):
        return self.__value_arr

    def sma(self, length):
        """simple moving average"""
        ret = np.cumsum(self.__value_arr, dtype=np.float64)
        ret[length:] = ret[length:] - ret[:-length]
        ret_ = ret[length - 1:] / length
        dt = self.__date_arr[:len(ret_)]
        return FinTimeSeries('{}_sma{}'.format(self.__label, length), dt, ret_)

    def ema(self, length):
        """exponential moving average"""
        return FinTimeSeries('{}+ema{}'.format(self.__label, length), self.__value_arr)

    def volitility(self, length):
        """ volitility """
        return FinTimeSeries('{}vol{}'.format(self.__label, length), self.__value_arr)

    def __lt__(self, rhs):
        """self < rhs; wrapper around numpy.less; return piecewise comparison"""
        if isinstance(rhs, FinTimeSeries):
            return np.less(self.__value_arr, rhs.GetValues())
        elif isinstance(rhs, numbers.Number):
            return np.less(self.__value_arr, rhs)

    def __gt__(self, rhs):
        """self < rhs; wrapper around numpy.less; return piecewise comparison"""
        if isinstance(rhs, np.ndarray):
            return np.greater(self.__value_arr, rhs.GetValues())
        elif isinstance(rhs, numbers.Number):
            return np.greater(self.__value_arr, rhs)

    def __str__(self):
        """to string; describe object/instance"""
        return 'FinTimeSeries ({} shape={})'.format(self.__label, self.__value_arr.shape)

    def __repr__(self):
        """to string describe class"""
        return self.__label + '(len={})'.format(self.__value_arr.shape)

    def __len__(self):
        """overload the len (ie. length) function"""
        assert len(self.__date_arr) == len(self.__value_arr)
        return len(self.__date_arr)

    def cross_indexes(self, rhs):
        assert isinstance(rhs, FinTimeSeries)
        """relax this constraint later"""
        assert len(self) == len(rhs)
        """relax this constraint later"""
        assert self.__date_arr == rhs.GetDates()

    # def __getattribute__(self, name):
    #    """operator. <attribute_name> """
    #    return self.__value_arr[name]

    def __getitem__(self, index):
        """operator[ <column_name> ] """
        return FinTimeSeries(self.__label, self.__date_arr[index], self.__value_arr[index])
