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
WITH MostRecentStockPrice AS (
    SELECT ISNULL(MAX(DateID),0) AS LastUpdateDateID
        ,stk.Symbol
    FROM Dim.Stock AS stk
    LEFT JOIN Fact.StockPrice AS prc
    ON stk.StockID = prc.StockID
    WHERE stk.StockName != 'Invalid'
    GROUP BY stk.Symbol
)
SELECT *
FROM MostRecentStockPrice;

GO