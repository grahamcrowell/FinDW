USE FinDW
GO

IF(OBJECT_ID('Etl.vwMostRecentStockPrice','V') IS NOT NULL)
BEGIN
	PRINT 'drop VIEW Etl.vwMostRecentStockPrice';
	DROP VIEW Etl.vwMostRecentStockPrice;
END
GO

CREATE VIEW Etl.vwMostRecentStockPrice
AS 
-- returns date of most recent price data stored in database
-- used to determine which stocks have out of date price data
WITH most_recent_trading_day AS (
	SELECT MAX(Date) AS MostRecentTradingDay
	FROM Dim.Date AS dt
	WHERE 1=1
	AND dt.Date < CAST(GETDATE() AS date)
	AND dt.isTradeDate = 1
), MostRecentStockPrice AS (
    SELECT ISNULL(dbo.ufnIDToDate(MAX(DateID)),0) AS LastUpdateDate
        ,stk.Symbol
        ,stk.StockID
    FROM Dim.Stock AS stk
    LEFT JOIN Fact.StockPrice AS prc
    ON stk.StockID = prc.StockID
    WHERE stk.StockName != 'Invalid'
    GROUP BY stk.Symbol, stk.StockID
)
SELECT CAST(LastUpdateDate AS date) AS LastUpdateDate, MostRecentTradingDay, Symbol, StockID
FROM most_recent_trading_day AS mr
CROSS JOIN MostRecentStockPrice AS stk
WHERE 1=1
AND stk.LastUpdateDate < mr.MostRecentTradingDay

GO