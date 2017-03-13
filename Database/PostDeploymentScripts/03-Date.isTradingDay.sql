USE FinDW
GO

UPDATE Dim.Date 
SET isTradeDate = 1
FROM Dim.Date AS dt
GO

UPDATE Dim.Date 
SET isTradeDate = 0
FROM Dim.Date AS dt
WHERE DATEPART(weekday, date) IN (1,7)
GO

;WITH most_recent_trading_day AS (
	SELECT MAX(Date) AS MostRecentTradingDay
	FROM Dim.Date AS dt
	WHERE 1=1
	AND dt.Date <= CAST(GETDATE() AS date)
	AND dt.isTradeDate = 1
)
SELECT LastUpdateDate, MostRecentTradingDay, Symbol
FROM most_recent_trading_day AS mr
CROSS JOIN Etl.vwMostRecentStockPrice AS stk
WHERE 1=1
AND stk.LastUpdateDate < mr.MostRecentTradingDay
