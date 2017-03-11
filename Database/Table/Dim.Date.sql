USE FinDW
GO


IF OBJECT_ID('Dim.Date') IS NOT NULL
BEGIN
	PRINT 'drop Dim.Date'
	DROP TABLE Dim.Date;
END
GO

BEGIN
PRINT 'create Dim.Date'
CREATE TABLE Dim.Date(
	DateID int NOT NULL 
	--,Date AS CONVERT(date, CAST(DateID AS varchar(10)), 112)
	,Date date NULL
	,Year AS YEAR(Date) 
	,Month AS MONTH(Date)
	,Day AS DAY(Date)
	,mdy AS CAST(FORMAT(Date, 'M/d/yyyy') AS varchar(12))
	,isTradeDate bit NULL
	,CONSTRAINT PK_Date PRIMARY KEY CLUSTERED (DateID ASC)
	);
END
GO