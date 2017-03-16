from _internals.tools import *

sql = """
SELECT 
	stk.Symbol
	,dt.Date
	,prc.AdjClosePrice
FROM Fact.StockPrice aS prc
JOIN Dim.Stock AS stk
ON prc.StockID = stk.StockID
JOIN Dim.Date AS dt
ON prc.DateID = dt.DateID
WHERE stk.Symbol = 'CAT'
"""

con = get_database_connection()
cur = con.cursor()
cur.execute(sql)



con.close()