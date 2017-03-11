USE FinDW
GO

IF(OBJECT_ID('Fact.vwStockPrice','V') IS NOT NULL)
BEGIN
	PRINT 'drop VIEW Fact.vwStockPrice';
	DROP VIEW Fact.vwStockPrice;
END
GO

CREATE VIEW Fact.vwStockPrice
AS 
SELECT 
	DateID
	,OpenPrice
	,HighPrice
	,LowPrice
	,ClosePrice
	,Volume
	,AdjClosePrice
FROM dbo.StockPrice;