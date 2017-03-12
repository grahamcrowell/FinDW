import pandas
import pyodbc

server_name = 'localhost'
database_name = 'FinDW'
driver_name = 'ODBC Driver 13 for SQL Server'

pyodbc_connection_string = 'DRIVER={{{}}};SERVER={};Trusted_Connection=Yes;'.format(driver_name,server_name)
if database_name is not None:
    pyodbc_connection_string+='DATABASE={};'.format(database_name)

con = pyodbc.connect(pyodbc_connection_string)

sql = 'SELECT * FROM [FinDW].[Etl].[vwMostRecentStockPrice]'
pandas_data_frame = pandas.read_sql(sql, con)

print(pandas_data_frame)
print(type(pandas_data_frame))

xarray = pandas_data_frame.to_xarray()
print(xarray)
print(type(xarray))
