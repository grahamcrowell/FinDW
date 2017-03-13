import requests
import pyodbc
import datetime



   
class PriceDataDownloadRequest(object):
    def __init__(self, symbol, stock_id, start_date, end_date=None):
        self.symbol = symbol
        self.stock_id = stock_id
        self.start_date = start_date
        self.end_date = end_date
        if self.end_date is None:
            self.end_date = date.today()
        self.rows = None
    
    def yahoo_price_url(self):
        """returns string of internet address from which price data is downloaded"""
        price_param = {'symbol': self.symbol, 'start_day': self.start_date.day, 'start_month': self.start_date.month - 1, 'start_year': self.start_date.year, 'end_day': self.end_date.day, 'end_month': self.end_date.month - 1, 'end_year': self.end_date.year}
        # 'http://real-chart.finance.yahoo.com/table.csv?s={self.symbol}&d={start_month}&e={start_day}&f={start_year}&g=d&a={end_month}&b={end_day}&c={end_year}&ignore=.csv'.format(**price_param)
        url = 'http://chart.finance.yahoo.com/table.csv?s={symbol}&d={end_month}&e={end_day}&f={end_year}&g=d&a={start_month}&b={start_day}&c={start_year}&ignore=.csv'.format(
            **price_param)
        return url

    def sql(self):
        if self.rows is None:
            return None
        cmd = """
        INSERT INTO FinDW.Fact.StockPrice
            (DateID, StockID, OpenPrice, HighPrice, LowPrice, ClosePrice, Volume, AdjClosePrice)
            VALUES (?,{},?,?,?,?,?,?)
        """
        cmd = cmd.format(self.stock_id)
        server_name = 'localhost'
        database_name = 'FinDW'
        driver_name = 'ODBC Driver 13 for SQL Server'

        pyodbc_connection_string = 'DRIVER={{{}}};SERVER={};Trusted_Connection=Yes;'.format(driver_name,server_name)
        conn = pyodbc.connect(pyodbc_connection_string)
        if database_name is not None:
            pyodbc_connection_string+='DATABASE={};'.format(database_name)

       
        if len(self.rows) > 0:
            con = pyodbc.connect(pyodbc_connection_string)
            cur = con.cursor()
            try:
                cur.executemany(cmd, self.rows)
                cur.commit()
            except:
                print(self.rows)
        return cmd

    def begin(self):
        self.rows = []
        past_header_line = False
        req = requests.get(self.yahoo_price_url())
        if req.status_code == 404:
            print('stock price data not found for: {}'.format(self.symbol))
            return None
        else:
            for line in req.iter_lines():
                line_str = line.decode("utf-8")
                if past_header_line:
                    tkns = line_str.split(',')
                    tkns[0] = str.join('',tkns[0].split('-'))
                    self.rows.append(tuple(tkns))
                else:
                    # date_in is a list of lists
                    # data_in = [list() for i in range(len(price_dict_keys))]
                    past_header_line = True
            print('price data: {} records'.format(len(self.rows)))
# check if symbol valid
# check if dates valid
# check if db has data
# no:
#   refresh price data for symbol
#       determine 
# yes: 
#   query data store
#   return filled panadas/xarray data structure

if __name__ == '__main__':
    symbol = 'CAT'


    server_name = 'localhost'
    database_name = 'FinDW'
    driver_name = 'ODBC Driver 13 for SQL Server'

    pyodbc_connection_string = 'DRIVER={{{}}};SERVER={};Trusted_Connection=Yes;'.format(driver_name,server_name)
    if database_name is not None:
        pyodbc_connection_string+='DATABASE={};'.format(database_name)

    con = pyodbc.connect(pyodbc_connection_string)

    sql = 'SELECT * FROM [FinDW].[Etl].[vwMostRecentStockPrice]'

    cur = con.cursor()
    cur.execute(sql)

    for row in cur:
        start_date = row[0]
        end_date = row[1]
        symbol = row[2]
        stock_id = row[3]
        print('downloading and uploading:\n\t{} ({} to {})'.format(symbol, start_date, end_date))
        downloader = PriceDataDownloadRequest(symbol, stock_id, start_date, end_date)
        rows = downloader.begin()
        downloader.sql()

        