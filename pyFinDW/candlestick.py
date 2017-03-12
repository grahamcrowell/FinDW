import pyFin
from pyFin import *
from pyFin.StockPrice import *

import matplotlib.pyplot as plt
import matplotlib.finance
import numpy as np


# http://matplotlib.org/api/finance_api.html#matplotlib.finance.candlestick2_ochl
stockPriceBuilder = StockPriceBuilder('MSFT')

matplotlib.finance.candlestick2_ochl(ax, opens, closes, highs, lows, width=4, colorup='k', colordown='r', alpha=0.75)