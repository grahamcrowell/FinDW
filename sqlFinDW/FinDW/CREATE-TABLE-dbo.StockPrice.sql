USE FinDW
GO

IF(OBJECT_ID('dbo.StockPrice','U') IS NOT NULL)
BEGIN
	PRINT 'drop table dbo.StockPrice';
	DROP TABLE dbo.StockPrice;
END

CREATE TABLE dbo.StockPrice
(
	--Date,Open,High,Low,Close,Volume,Adj Close
	--2017-02-27,95.480003,97.519997,95.120003,97.440002,5434400,97.440002
	DateID int
	,OpenPrice numeric(12,6)
	,HighPrice numeric(12,6)
	,LowPrice numeric(12,6)
	,ClosePrice numeric(12,6)
	,Volume bigint
	,AdjClosePrice numeric(12,6)
);