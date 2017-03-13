import pandas as pd
import pyodbc
import pyFin._internals.download_csv_price as download


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
    print(row)
    print(row[0])
    print(row[1])
    print(row[2])
    param = 