USE FinDW
GO

IF(OBJECT_ID('fact.StockPrice','V') IS NOT NULL)
BEGIN
	PRINT 'drop table fact.StockPrice';
	DROP TABLE fact.StockPrice;
END

CREATE VIEW fact.StockPrice
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