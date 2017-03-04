import requests
import os
import time
import collections
from datetime import date
#from pyFin._internals.tools import * 
import pyFin._internals.tools as tools
import numpy as np


#fin_dtype = np.dtype([('date', 'datetime64[D]'),('open_price', np.float64),('high_price', np.float64),('low_price', np.float64),('close_price', np.float64),('volume', np.int64),('adjusted_close_price', np.float64)])
price_dict_keys = ['date','open_price','high_price','low_price','close_price','volume','adjusted_close_price']
price_dict_value_np_dtypes = [np.dtype('datetime64[D]'),np.dtype(np.float64),np.dtype(np.float64),np.dtype(np.float64),np.dtype(np.float64),np.dtype(np.int64),np.dtype(np.float64)]

def yahoo_price_url(symbol, start_date, end_date=None):
    """returns string of internet address from which price data is downloaded"""
    if end_date is None:
        end_date = date.today()
    price_param = {'symbol': symbol, 'start_day': start_date.day, 'start_month': start_date.month - 1, 'start_year': start_date.year, 'end_day': end_date.day, 'end_month': end_date.month - 1, 'end_year': end_date.year}
    # 'http://real-chart.finance.yahoo.com/table.csv?s={symbol}&d={start_month}&e={start_day}&f={start_year}&g=d&a={end_month}&b={end_day}&c={end_year}&ignore=.csv'.format(**price_param)
    url = 'http://chart.finance.yahoo.com/table.csv?s={symbol}&d={end_month}&e={end_day}&f={end_year}&g=d&a={start_month}&b={start_day}&c={start_year}&ignore=.csv'.format(
        **price_param)
    return url


def yahoo_price_path(symbol, start_date, end_date=None):
    """returns local file path where csv file of price data will be saved"""
    if end_date is None:
        end_date = date.today()
    return os.path.join(tools.price_loading, tools.make_price_filename(symbol, start_date, end_date))


PriceDownloadParam = collections.namedtuple(
    'PriceDownloadParam', ['symbol', 'start_date', 'end_date'])


def download(price_download_param):
    url = yahoo_price_url(price_download_param.symbol,
                          price_download_param.start_date, price_download_param.end_date)
    inpath = yahoo_price_path(price_download_param.symbol,
                              price_download_param.start_date, price_download_param.end_date)
    req = requests.get(url)
    sql = "INSERT INTO FinDW.dbo.StockPrice (Date,OpenPrice,HighPrice,LowPrice,ClosePrice,Volume,AdjClosePrice) VALUES ('%s',%s,%s,%s,%s,%s,%s)"
    data_in = None
    past_header_line = False
    with open(inpath, 'w') as fout:
        for line in req.iter_lines():
            line_str = line.decode("utf-8")
            fout.write(line_str + '\n')
            if past_header_line:
                tkns = line_str.split(',')
                for i in range(len(tkns)):
                    data_in[i].append(tkns[i])
                #tkns[0] = tkns[0].replace('-','')
                data_in.append(tuple(tkns))
            else:
                data_in = [list() for i in range(len(price_dict_keys))]
                past_header_line = True
    #print(data_in)
    #print(len(data_in))
    
    #if(False):

    #    conn = tools.get_sql_server_connection()
    #    cur = conn.cursor()
    #    cur.executemany(sql,data_in)
    #    conn.commit()
    if os.path.exists(inpath):
        pass
        # print('saved {}'.format(inpath))
    else:
        print('\n\n\t* * *\nNOT saved {}'.format(inpath))
    time.sleep(0.05)
    # convert list of lists to dict of numpy arrays
    out = {}
    for i in range(len(price_dict_keys)):
        key = price_dict_keys[i]
        out[key] = np.asarray(data_in[i], dtype=price_dict_value_np_dtypes[i])
    return out

if __name__ == '__main__':
    symbol = 'CAT'
    start_date = date(year=1900, month=1, day=1)
    caterpillar_test = PriceDownloadParam(symbol, start_date, None)
    download(caterpillar_test)
