USE FinDW
GO

IF(OBJECT_ID('TimeSeries.uspGetAvailableAt','P') IS NOT NULL)
BEGIN
	PRINT 'drop PROC TimeSeries.uspGetAvailableAt';
	DROP PROC TimeSeries.uspGetAvailableAt;
END
GO

CREATE PROC TimeSeries.uspGetAvailableAt
AS 
BEGIN
	SELECT 
		DateID
		,OpenPrice
		,HighPrice
		,LowPrice
		,ClosePrice
		,Volume
		,AdjClosePrice
	FROM dbo.StockPrice;
END