USE FinDW
GO

IF(OBJECT_ID('Fact.StockPrice','U') IS NOT NULL)
BEGIN
	PRINT 'drop table Fact.StockPrice';
	DROP TABLE Fact.StockPrice;
END

CREATE TABLE Fact.StockPrice
(
	--Date,Open,High,Low,Close,Volume,Adj Close
	--2017-02-27,95.480003,97.519997,95.120003,97.440002,5434400,97.440002
	DateID int
	,StockID int
	,OpenPrice numeric(12,6)
	,HighPrice numeric(12,6)
	,LowPrice numeric(12,6)
	,ClosePrice numeric(12,6)
	,Volume bigint
	,AdjClosePrice numeric(12,6)
    ,CONSTRAINT [PK_StockPrice] PRIMARY KEY (DateID, StockID)
);